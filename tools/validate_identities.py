#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_WIKI_DIR = REPO_ROOT / "wiki"
PUBLIC_SECTIONS = ("entities", "concepts", "sources")


class WikiIdentityValidationError(ValueError):
    """The canonical wiki layout is missing or invalid."""


@dataclass(frozen=True)
class IdentityCollisions:
    exact: dict[str, list[Path]]
    casefolded: dict[tuple[str, str], list[Path]]
    public_routes: dict[str, list[Path]]


def canonical_pages(wiki_dir: Path) -> list[Path]:
    if not wiki_dir.is_dir():
        raise WikiIdentityValidationError(f"Wiki directory does not exist: {wiki_dir}")

    missing_sections = [section for section in PUBLIC_SECTIONS if not (wiki_dir / section).is_dir()]
    if missing_sections:
        raise WikiIdentityValidationError(
            "Missing public wiki section directories: " + ", ".join(missing_sections)
        )

    pages: list[Path] = []
    for section in PUBLIC_SECTIONS:
        section_dir = wiki_dir / section
        pages.extend(
            path
            for path in sorted(section_dir.glob("*.md"))
            if not path.name.startswith("_")
        )

    if not pages:
        raise WikiIdentityValidationError(f"Wiki directory contains no canonical pages: {wiki_dir}")

    return pages


def public_route(path: Path, wiki_dir: Path) -> str:
    section = path.relative_to(wiki_dir).parts[0]
    return f"/wiki/{section}/{quote(path.stem.lower(), safe='')}/"


def find_identity_collisions(wiki_dir: Path = DEFAULT_WIKI_DIR) -> IdentityCollisions:
    by_exact_key: dict[str, list[Path]] = defaultdict(list)
    by_casefolded_key: dict[tuple[str, str], list[Path]] = defaultdict(list)
    by_public_route: dict[str, list[Path]] = defaultdict(list)

    for path in canonical_pages(wiki_dir):
        section = path.relative_to(wiki_dir).parts[0]
        by_exact_key[path.stem].append(path)
        by_casefolded_key[(section, path.stem.casefold())].append(path)
        by_public_route[public_route(path, wiki_dir)].append(path)

    return IdentityCollisions(
        exact={key: paths for key, paths in by_exact_key.items() if len(paths) > 1},
        casefolded={key: paths for key, paths in by_casefolded_key.items() if len(paths) > 1},
        public_routes={route: paths for route, paths in by_public_route.items() if len(paths) > 1},
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Fail when canonical wiki pages collide by case-insensitive key or public route."
    )
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR)
    args = parser.parse_args(argv)

    try:
        collisions = find_identity_collisions(args.wiki_dir)
    except WikiIdentityValidationError as exc:
        print(f"Wiki identity validation error: {exc}", file=sys.stderr)
        return 2
    if not collisions.exact and not collisions.casefolded and not collisions.public_routes:
        print("Wiki identities are unique.")
        return 0

    if collisions.exact:
        print(f"Exact wiki key collisions: {len(collisions.exact)}", file=sys.stderr)
        for key, paths in collisions.exact.items():
            print(f"  {key}", file=sys.stderr)
            for path in paths:
                print(f"    {path.relative_to(args.wiki_dir).as_posix()}", file=sys.stderr)

    if collisions.casefolded:
        print(
            f"Case-insensitive wiki key collisions: {len(collisions.casefolded)}",
            file=sys.stderr,
        )
        for paths in collisions.casefolded.values():
            for path in paths:
                print(f"  {path.relative_to(args.wiki_dir).as_posix()}", file=sys.stderr)

    if collisions.public_routes:
        print(f"Public wiki route collisions: {len(collisions.public_routes)}", file=sys.stderr)
        for route, paths in collisions.public_routes.items():
            print(f"  {route}", file=sys.stderr)
            for path in paths:
                print(f"    {path.relative_to(args.wiki_dir).as_posix()}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
