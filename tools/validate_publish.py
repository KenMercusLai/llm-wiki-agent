#!/usr/bin/env python3
"""Fail-closed publish validation for canonical identities and derived synthesis."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from tools import synthesis, validate_identities


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, check=False
    )


def validate_changed_whitespace(root: Path) -> int:
    """Mirror the downstream publisher's Git whitespace gate for changed Wiki files."""
    for args in (
        ("diff", "--cached", "--check", "HEAD", "--", "wiki"),
        ("diff", "--check", "--", "wiki"),
    ):
        changed = _git(root, *args)
        if changed.returncode:
            sys.stderr.buffer.write(changed.stdout + changed.stderr)
            return 1

    untracked = _git(
        root,
        "ls-files",
        "--others",
        "--exclude-standard",
        "-z",
        "--",
        "wiki",
    )
    if untracked.returncode:
        sys.stderr.buffer.write(untracked.stdout + untracked.stderr)
        return 1

    for raw_path in filter(None, untracked.stdout.split(b"\0")):
        path = raw_path.decode("utf-8", errors="surrogateescape")
        check = _git(root, "diff", "--no-index", "--check", "/dev/null", path)
        if check.stdout or check.stderr or check.returncode not in (0, 1):
            sys.stderr.buffer.write(check.stdout + check.stderr)
            return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)

    identity_status = validate_identities.main(["--wiki-dir", str(args.root / "wiki")])
    if identity_status:
        return identity_status
    whitespace_status = validate_changed_whitespace(args.root)
    if whitespace_status:
        return whitespace_status
    try:
        report = synthesis.validate_repository(args.root)
    except (OSError, ValueError) as error:
        print(f"Derived synthesis validation failed: {error}", file=sys.stderr)
        return 1
    print(f"Derived synthesis is valid: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
