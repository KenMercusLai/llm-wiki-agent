#!/usr/bin/env python3
"""Validate opt-in synthesis-first Concept and Entity page contracts."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCHEMA = "synthesis-v1"
SECTION_CONTRACTS = {
    "concept": (
        "Definition",
        "Current Synthesis",
        "Key Claims",
        "Evidence",
        "Counterevidence & Qualifications",
        "What Changed",
        "Related Concepts",
    ),
    "entity": (
        "Overview",
        "Current Profile",
        "Key Characteristics",
        "Evidence",
        "Qualifications",
        "What Changed",
        "Relationships",
    ),
}
CORE_SECTION = {"concept": "Key Claims", "entity": "Key Characteristics"}
RELATION_SECTION = {"concept": "Related Concepts", "entity": "Relationships"}
H2_RE = re.compile(r"(?m)^## ([^\n]+?)\s*$")
SOURCE_APPEND_RE = re.compile(
    r"(?im)^(?:\[\[[^\]\n]+\]\]|the(?:\s+\[[^\]\n]+\]|\s+[^\n]{1,80})?\s+source|source\s+[^\n]{1,80})\s+adds\b"
)
RELATION_RE = re.compile(r"^\s*-\s+.*\[\[[^\]\n]+\]\].*\s+-\s+\S")


def split_front_matter(text: str) -> tuple[list[str], str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return [], text
    try:
        end = lines.index("---", 1)
    except ValueError:
        return [], text
    return lines[1:end], "\n".join(lines[end + 1 :])


def front_matter_value(lines: list[str], key: str) -> str:
    prefix = f"{key}:"
    for raw_line in lines:
        if raw_line.startswith(prefix):
            return raw_line.split(":", 1)[1].strip().strip("\"'")
    return ""


def front_matter_list(lines: list[str], key: str) -> tuple[str, ...]:
    values: list[str] = []
    active = False
    for line in lines:
        if line == f"{key}:":
            active = True
            continue
        if not active:
            continue
        if line.startswith("  - "):
            values.append(line[4:].strip().strip("\"'"))
            continue
        break
    return tuple(values)


def sections(body: str) -> tuple[list[str], dict[str, str]]:
    matches = list(H2_RE.finditer(body))
    names = [match.group(1).strip() for match in matches]
    content = {
        name: body[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(body)].strip()
        for index, (name, match) in enumerate(zip(names, matches))
    }
    return names, content


def top_level_bullets(content: str) -> list[str]:
    return [
        line
        for line in content.splitlines()
        if re.match(r"^(?:- |\d+\. )", line)
    ]


def validate_page(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(text)
    if front_matter_value(front_matter, "knowledge_schema") != SCHEMA:
        return []

    errors: list[str] = []
    page_type = front_matter_value(front_matter, "type")
    relative = path.as_posix()
    if page_type not in SECTION_CONTRACTS:
        return [f"{relative}: knowledge_schema {SCHEMA} is only valid for concept or entity pages"]

    expected = list(SECTION_CONTRACTS[page_type])
    names, content_by_name = sections(body)
    if names != expected:
        errors.append(
            f"{relative}: expected exact ordered H2 sections {expected!r}; found {names!r}"
        )
        return errors + _source_append_errors(relative, body)

    for name in expected:
        if not content_by_name[name]:
            errors.append(f"{relative}: section {name!r} must not be empty")

    core = CORE_SECTION[page_type]
    core_count = len(top_level_bullets(content_by_name[core]))
    if not 3 <= core_count <= 7:
        errors.append(
            f"{relative}: {core} must contain 3-7 top-level bullets; found {core_count}"
        )

    changed_count = len(top_level_bullets(content_by_name["What Changed"]))
    if changed_count > 5:
        errors.append(
            f"{relative}: What Changed must contain at most 5 top-level bullets; found {changed_count}"
        )

    source_keys = set(front_matter_list(front_matter, "sources"))
    evidence_bullets = top_level_bullets(content_by_name["Evidence"])
    if not evidence_bullets:
        errors.append(f"{relative}: Evidence must contain claim-grouped bullets")
    for bullet in evidence_bullets:
        links = set(re.findall(r"\[\[([^\]|#]+)", bullet))
        if not links.intersection(source_keys):
            errors.append(
                f"{relative}: each Evidence bullet must cite at least one source note from front matter: {bullet}"
            )

    relationship = RELATION_SECTION[page_type]
    relationship_bullets = top_level_bullets(content_by_name[relationship])
    if not relationship_bullets:
        errors.append(f"{relative}: {relationship} must contain semantic relationship bullets")
    for bullet in relationship_bullets:
        if not RELATION_RE.match(bullet):
            errors.append(
                f"{relative}: {relationship} bullet must contain a wikilink and semantic relationship after ' - ': {bullet}"
            )

    errors.extend(_source_append_errors(relative, body))
    return errors


def _source_append_errors(relative: str, body: str) -> list[str]:
    append_lines = SOURCE_APPEND_RE.findall(body)
    if not append_lines:
        return []
    return [
        f"{relative}: source-by-source append prose is not allowed; found {len(append_lines)} source-led additions"
    ]


def validate_wiki(wiki_dir: Path) -> list[str]:
    if not wiki_dir.is_dir():
        return [f"Wiki directory does not exist: {wiki_dir}"]
    errors: list[str] = []
    available_sources = {
        path.stem for path in (wiki_dir / "sources").glob("*.md")
    }
    for path in sorted(wiki_dir.glob("*/*.md")):
        if path.name.startswith("_"):
            continue
        page_errors = validate_page(path)
        errors.extend(page_errors)
        if path.parent.name not in {"concepts", "entities"}:
            continue
        text = path.read_text(encoding="utf-8")
        front_matter, _body = split_front_matter(text)
        if front_matter_value(front_matter, "knowledge_schema") != SCHEMA:
            continue
        relative = path.relative_to(wiki_dir).as_posix()
        for source_key in front_matter_list(front_matter, "sources"):
            if source_key not in available_sources:
                errors.append(
                    f"{relative}: missing source note from canonical wiki/sources: {source_key}"
                )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiki-dir", type=Path, default=Path("wiki"))
    args = parser.parse_args(argv)
    errors = validate_wiki(args.wiki_dir)
    if errors:
        print(f"Knowledge page validation failed: {len(errors)} error(s)", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print(f"Knowledge pages conform to {SCHEMA}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
