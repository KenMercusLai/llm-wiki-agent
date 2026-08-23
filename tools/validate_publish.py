#!/usr/bin/env python3
"""Fail-closed publish validation for canonical identities and derived synthesis."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tools import synthesis, validate_identities


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)

    identity_status = validate_identities.main(["--wiki-dir", str(args.root / "wiki")])
    if identity_status:
        return identity_status
    try:
        report = synthesis.validate_repository(args.root)
    except (OSError, ValueError) as error:
        print(f"Derived synthesis validation failed: {error}", file=sys.stderr)
        return 1
    print(f"Derived synthesis is valid: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
