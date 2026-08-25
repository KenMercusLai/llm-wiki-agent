from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import validate_publish


class ValidatePublishTest(unittest.TestCase):
    @staticmethod
    def _git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args], cwd=repo, text=True, capture_output=True, check=True
        )

    def _repository(self, *, legacy_blank_eof: bool = False) -> tuple[tempfile.TemporaryDirectory, Path]:
        temp = tempfile.TemporaryDirectory()
        repo = Path(temp.name)
        self._git(repo, "init")
        self._git(repo, "config", "user.name", "Test")
        self._git(repo, "config", "user.email", "test@example.invalid")
        wiki = repo / "wiki"
        wiki.mkdir()
        ending = "\n\n" if legacy_blank_eof else "\n"
        (wiki / "Existing.md").write_text(f"existing{ending}", encoding="utf-8")
        self._git(repo, "add", "wiki/Existing.md")
        self._git(repo, "commit", "-m", "baseline")
        return temp, repo

    def test_changed_whitespace_rejects_unstaged_blank_line_at_eof(self):
        temp, repo = self._repository()
        self.addCleanup(temp.cleanup)
        (repo / "wiki" / "New.md").write_text("new\n\n", encoding="utf-8")

        result = validate_publish.validate_changed_whitespace(repo)

        self.assertEqual(1, result)

    def test_changed_whitespace_rejects_staged_blank_line_at_eof(self):
        temp, repo = self._repository()
        self.addCleanup(temp.cleanup)
        (repo / "wiki" / "New.md").write_text("new\n\n", encoding="utf-8")
        self._git(repo, "add", "wiki/New.md")

        result = validate_publish.validate_changed_whitespace(repo)

        self.assertEqual(1, result)

    def test_changed_whitespace_rejects_staged_blank_line_hidden_by_clean_worktree(self):
        temp, repo = self._repository()
        self.addCleanup(temp.cleanup)
        existing = repo / "wiki" / "Existing.md"
        existing.write_text("existing\n\n", encoding="utf-8")
        self._git(repo, "add", "wiki/Existing.md")
        existing.write_text("existing\n", encoding="utf-8")

        result = validate_publish.validate_changed_whitespace(repo)

        self.assertEqual(1, result)

    @mock.patch("tools.validate_publish._git")
    def test_changed_whitespace_fails_if_untracked_file_disappears(self, git):
        clean = subprocess.CompletedProcess([], 0, b"", b"")
        untracked = subprocess.CompletedProcess([], 0, b"wiki/Gone.md\0", b"")
        missing = subprocess.CompletedProcess([], 1, b"", b"error: file disappeared\n")
        git.side_effect = [clean, clean, untracked, missing]

        result = validate_publish.validate_changed_whitespace(Path("/repo"))

        self.assertEqual(1, result)

    def test_changed_whitespace_ignores_unchanged_legacy_blank_line(self):
        temp, repo = self._repository(legacy_blank_eof=True)
        self.addCleanup(temp.cleanup)

        result = validate_publish.validate_changed_whitespace(repo)

        self.assertEqual(0, result)

    @mock.patch("tools.validate_publish.synthesis.validate_repository")
    @mock.patch("tools.validate_publish.validate_identities.main", return_value=1)
    def test_stops_after_identity_failure(self, identity_main, synthesis_validate):
        self.assertEqual(1, validate_publish.main([]))
        synthesis_validate.assert_not_called()

    @mock.patch("tools.validate_publish.synthesis.validate_repository")
    @mock.patch("tools.validate_publish.validate_changed_whitespace", return_value=1)
    @mock.patch("tools.validate_publish.validate_identities.main", return_value=0)
    def test_stops_after_whitespace_failure(
        self, identity_main, whitespace_validate, synthesis_validate
    ):
        self.assertEqual(1, validate_publish.main([]))
        identity_main.assert_called_once()
        whitespace_validate.assert_called_once()
        synthesis_validate.assert_not_called()

    @mock.patch("tools.validate_publish.synthesis.validate_repository", return_value={"topic_count": 8})
    @mock.patch("tools.validate_publish.validate_identities.main", return_value=0)
    def test_runs_identity_and_synthesis_checks(self, identity_main, synthesis_validate):
        self.assertEqual(0, validate_publish.main([]))
        synthesis_validate.assert_called_once()

    @mock.patch("tools.validate_publish.synthesis.validate_repository", side_effect=ValueError("bad manifest"))
    @mock.patch("tools.validate_publish.validate_identities.main", return_value=0)
    def test_synthesis_failure_is_fail_closed(self, identity_main, synthesis_validate):
        self.assertEqual(1, validate_publish.main([]))


if __name__ == "__main__":
    unittest.main()
