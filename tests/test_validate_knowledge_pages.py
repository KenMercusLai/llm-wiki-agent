from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools import validate_knowledge_pages


CONCEPT_BODY = """# Example Concept

## Definition
A stable definition.

## Current Synthesis
A current synthesis.

## Key Claims
- Claim one.
- Claim two.
- Claim three.

## Evidence
### Claim one
- [[source-one]] supports the first claim.

## Counterevidence & Qualifications
- The claim is bounded.

## What Changed
- Added a qualification after [[source-two]].

## Related Concepts
- [[RelatedConcept]] - narrows the concept boundary.
"""

ENTITY_BODY = """# Example Entity

## Overview
A stable overview.

## Current Profile
A current profile.

## Key Characteristics
- Characteristic one.
- Characteristic two.
- Characteristic three.

## Evidence
### Characteristic one
- [[source-one]] supports the profile.

## Qualifications
- The corpus is incomplete.

## What Changed
- Added a new branch after [[source-two]].

## Relationships
- [[RelatedEntity]] - hosts the relevant discussion.
"""


def page(page_type: str, body: str, *, schema: bool = True) -> str:
    schema_line = "knowledge_schema: synthesis-v1\n" if schema else ""
    return (
        "---\n"
        'title: "Example"\n'
        f"type: {page_type}\n"
        "tags: [example]\n"
        "sources:\n"
        "  - source-one\n"
        "  - source-two\n"
        f"{schema_line}"
        "last_updated: 2026-08-26\n"
        "---\n\n"
        f"{body}"
    )


def write_source_fixtures(wiki: Path) -> None:
    sources = wiki / "sources"
    sources.mkdir(parents=True, exist_ok=True)
    for key in ("source-one", "source-two"):
        (sources / f"{key}.md").write_text(
            f"---\ntitle: {key}\ntype: source\n---\n",
            encoding="utf-8",
        )


class ValidateKnowledgePagesTest(unittest.TestCase):
    def validate(self, relative: str, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            wiki = Path(directory) / "wiki"
            write_source_fixtures(wiki)
            path = wiki / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            return validate_knowledge_pages.validate_wiki(wiki)

    def test_accepts_valid_concept_and_entity_contracts(self):
        with tempfile.TemporaryDirectory() as directory:
            wiki = Path(directory) / "wiki"
            write_source_fixtures(wiki)
            (wiki / "concepts").mkdir(parents=True)
            (wiki / "entities").mkdir(parents=True)
            (wiki / "concepts" / "Concept.md").write_text(
                page("concept", CONCEPT_BODY), encoding="utf-8"
            )
            (wiki / "entities" / "Entity.md").write_text(
                page("entity", ENTITY_BODY), encoding="utf-8"
            )
            self.assertEqual([], validate_knowledge_pages.validate_wiki(wiki))

    def test_ignores_legacy_pages_without_schema_marker(self):
        legacy = page("concept", "# Example\n\n## Connections\n- [[Thing]]\n", schema=False)
        self.assertEqual([], self.validate("concepts/Legacy.md", legacy))

    def test_requires_exact_ordered_sections(self):
        invalid = CONCEPT_BODY.replace(
            "## Definition\nA stable definition.\n\n## Current Synthesis",
            "## Current Synthesis\nA current synthesis.\n\n## Definition",
        )
        errors = self.validate("concepts/Concept.md", page("concept", invalid))
        self.assertTrue(any("ordered H2 sections" in error for error in errors), errors)

    def test_requires_three_to_seven_core_bullets(self):
        too_few = CONCEPT_BODY.replace("- Claim three.\n", "")
        errors = self.validate("concepts/Concept.md", page("concept", too_few))
        self.assertTrue(any("3-7 top-level bullets" in error for error in errors), errors)

    def test_requires_each_evidence_group_to_cite_a_front_matter_source(self):
        uncited = CONCEPT_BODY.replace("[[source-one]]", "[[RelatedConcept]]")
        errors = self.validate("concepts/Concept.md", page("concept", uncited))
        self.assertTrue(any("each Evidence bullet" in error for error in errors), errors)

    def test_rejects_missing_canonical_source_note(self):
        missing = page("concept", CONCEPT_BODY).replace("source-two", "missing-source")
        errors = self.validate("concepts/Concept.md", missing)
        self.assertTrue(any("missing source note" in error for error in errors), errors)

    def test_limits_what_changed_to_five_bullets(self):
        changes = "".join(f"- Change {index}.\n" for index in range(6))
        invalid = CONCEPT_BODY.replace(
            "- Added a qualification after [[source-two]].\n", changes
        )
        errors = self.validate("concepts/Concept.md", page("concept", invalid))
        self.assertTrue(any("at most 5 top-level bullets" in error for error in errors), errors)

    def test_rejects_legacy_connections_and_source_append_logs(self):
        invalid = CONCEPT_BODY + (
            "\n## Connections\n- [[Thing]]\n"
            "\n[[source-one]] adds one angle.\n"
            "[[source-two]] adds another angle.\n"
        )
        errors = self.validate("concepts/Concept.md", page("concept", invalid))
        self.assertTrue(any("ordered H2 sections" in error for error in errors), errors)
        self.assertTrue(any("source-by-source append" in error for error in errors), errors)

    def test_relationships_require_wikilink_and_semantic_explanation(self):
        invalid = ENTITY_BODY.replace(
            "- [[RelatedEntity]] - hosts the relevant discussion.",
            "- [[RelatedEntity]]",
        )
        errors = self.validate("entities/Entity.md", page("entity", invalid))
        self.assertTrue(any("semantic relationship" in error for error in errors), errors)

    def test_rejects_schema_on_wrong_page_type(self):
        errors = self.validate("sources/Source.md", page("source", CONCEPT_BODY))
        self.assertTrue(any("only valid for concept or entity" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
