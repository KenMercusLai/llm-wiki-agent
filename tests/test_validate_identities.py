from __future__ import annotations

import tempfile
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path

from tools.validate_identities import WikiIdentityValidationError, find_identity_collisions, main


class WikiIdentityValidationTest(unittest.TestCase):
    def test_rejects_case_insensitive_keys_and_public_routes(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki"
            entities = wiki / "entities"
            concepts = wiki / "concepts"
            sources = wiki / "sources"
            entities.mkdir(parents=True)
            concepts.mkdir(parents=True)
            sources.mkdir(parents=True)
            (entities / "ZhuHai.md").write_text("# Zhu Hai\n", encoding="utf-8")
            (entities / "Zhuhai.md").write_text("# Zhuhai\n", encoding="utf-8")
            (concepts / "ZhuHai.md").write_text("# Separate section\n", encoding="utf-8")

            collisions = find_identity_collisions(wiki)

            self.assertEqual(
                sorted(path.name for path in collisions.casefolded[("entities", "zhuhai")]),
                ["ZhuHai.md", "Zhuhai.md"],
            )
            self.assertEqual(
                sorted(path.name for path in collisions.public_routes["/wiki/entities/zhuhai/"]),
                ["ZhuHai.md", "Zhuhai.md"],
            )
            self.assertNotIn(("concepts", "zhuhai"), collisions.casefolded)

    def test_accepts_semantically_disambiguated_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki"
            entities = wiki / "entities"
            concepts = wiki / "concepts"
            sources = wiki / "sources"
            entities.mkdir(parents=True)
            concepts.mkdir(parents=True)
            sources.mkdir(parents=True)
            (entities / "ZhuHaiWeiRetainer.md").write_text("# Zhu Hai\n", encoding="utf-8")
            (entities / "Zhuhai.md").write_text("# Zhuhai\n", encoding="utf-8")

            collisions = find_identity_collisions(wiki)

            self.assertEqual(collisions.casefolded, {})
            self.assertEqual(collisions.public_routes, {})

    def test_rejects_missing_wiki_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing"

            with self.assertRaisesRegex(WikiIdentityValidationError, "Wiki directory does not exist"):
                find_identity_collisions(missing)

    def test_rejects_missing_public_section(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki"
            (wiki / "entities").mkdir(parents=True)
            (wiki / "concepts").mkdir(parents=True)

            with self.assertRaisesRegex(WikiIdentityValidationError, "sources"):
                find_identity_collisions(wiki)

    def test_cli_returns_two_when_wiki_root_is_invalid(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing"
            stderr = StringIO()

            with redirect_stderr(stderr):
                returncode = main(["--wiki-dir", str(missing)])

            self.assertEqual(returncode, 2)
            self.assertIn("Wiki directory does not exist", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
