from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import _utils, synthesis


OVERVIEW = """---
title: \"Overview\"
last_updated: 2026-08-23
---

# Overview

Automatic latest-addition prose.

## Current Synthesis

AI systems reshape work and institutions through [[Automation]] and [[Governance]].

Markets allocate capital under uncertainty through [[Investing]].

A broad observation with [[Culture]] but no configured lexical signal.

## Open Questions

- What remains unresolved?
"""

CONFIG = {
    "version": 1,
    "global_compaction": {"max_ingests": 25, "max_age_hours": 24, "max_chars": 25000},
    "topics": [
        {"id": "ai-and-work", "title": "AI and Work", "terms": ["ai", "automation", "work"]},
        {"id": "governance", "title": "Governance", "terms": ["governance", "institutions"]},
        {"id": "markets", "title": "Markets", "terms": ["markets", "investing", "capital"]},
        {"id": "cross-domain", "title": "Cross-domain", "terms": []},
    ],
}


class SynthesisTest(unittest.TestCase):
    def make_repo(self) -> Path:
        root = Path(self.temp.name)
        (root / "wiki").mkdir()
        (root / "wiki" / "overview.md").write_text(OVERVIEW, encoding="utf-8")
        (root / "config").mkdir()
        (root / "config" / "synthesis-topics.json").write_text(
            json.dumps(CONFIG), encoding="utf-8"
        )
        for section in ("concepts", "entities", "sources"):
            directory = root / "wiki" / section
            directory.mkdir()
        for name in ("Automation", "Governance", "Investing", "Culture"):
            (root / "wiki" / "concepts" / f"{name}.md").write_text(
                f"# {name}\n", encoding="utf-8"
            )
        return root

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = self.make_repo()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_generated_synthesis_is_excluded_from_canonical_wiki_scans(self):
        generated = self.root / "wiki" / "_generated" / "synthesis" / "topics" / "ai.md"
        generated.parent.mkdir(parents=True)
        generated.write_text("generated", encoding="utf-8")
        canonical = self.root / "wiki" / "concepts" / "Canonical.md"
        canonical.write_text("canonical", encoding="utf-8")

        with mock.patch.object(_utils, "WIKI_DIR", self.root / "wiki"):
            pages = _utils.all_wiki_pages()

        self.assertIn(canonical, pages)
        self.assertNotIn(generated, pages)

    def test_extracts_only_current_synthesis_into_complete_ledger(self):
        plan = synthesis.build_plan(self.root, now="2026-08-23T00:00:00Z")

        self.assertEqual(3, len(plan["paragraphs"]))
        self.assertTrue(all(item["primary_topic"] for item in plan["paragraphs"]))
        self.assertEqual(
            {item["id"] for item in plan["paragraphs"]},
            set(plan["coverage"]["assigned_paragraph_ids"]),
        )
        self.assertNotIn("Automatic latest-addition prose", json.dumps(plan))
        self.assertNotIn("What remains unresolved", json.dumps(plan))

    def test_topic_scoring_uses_word_boundaries_for_short_ascii_terms(self):
        config = synthesis.load_config(self.root)
        primary, secondary, _scores = synthesis.assign_topics("Retail statements create markets evidence.", config)
        topic_ids = [primary, *secondary]
        self.assertNotIn("ai-and-work", topic_ids)
        self.assertEqual("markets", topic_ids[0])

    def test_camel_case_wikilinks_contribute_auditable_topic_signals(self):
        config = synthesis.load_config(self.root)
        # Fixture topics do not include science; use the exact CamelCase boundary behavior on AI/work.
        primary, secondary, scores = synthesis.assign_topics("A source extends [[AutomationAtWork]].", config)
        self.assertEqual("ai-and-work", primary)
        self.assertGreater(scores["ai-and-work"], 0)

    def test_assigns_primary_and_secondary_topics_with_cross_domain_fallback(self):
        plan = synthesis.build_plan(self.root, now="2026-08-23T00:00:00Z")
        paragraphs = plan["paragraphs"]

        self.assertEqual("ai-and-work", paragraphs[0]["primary_topic"])
        self.assertIn("governance", paragraphs[0]["secondary_topics"])
        self.assertEqual("markets", paragraphs[1]["primary_topic"])
        self.assertEqual("cross-domain", paragraphs[2]["primary_topic"])

    def test_plan_writes_full_bounded_inputs_only_for_dirty_topics(self):
        plan = synthesis.plan_repository(self.root, now="2026-08-23T00:00:00Z")
        stage = self.root / ".synthesis-staging"

        self.assertEqual(set(plan["dirty_topics"]), {p.stem for p in (stage / "inputs").glob("*.json")})
        first = json.loads((stage / "inputs" / "ai-and-work.json").read_text())
        self.assertEqual("ai-and-work", first["topic_id"])
        self.assertEqual(1, len(first["paragraphs"]))
        self.assertIn("AI systems reshape work", first["paragraphs"][0]["text"])

    def test_topic_claims_fail_closed_when_support_is_not_in_topic_input(self):
        synthesis.plan_repository(self.root, now="2026-08-23T00:00:00Z")
        claims = self.root / ".synthesis-staging" / "claims"
        claims.mkdir()
        (claims / "ai-and-work.json").write_text(
            json.dumps(
                {
                    "topic_id": "ai-and-work",
                    "summary": "Summary.",
                    "claims": [
                        {
                            "id": "work-change",
                            "status": "supported",
                            "statement": "Claim.",
                            "supporting_wikilinks": ["InventedPage"],
                            "qualifications": [],
                            "global_candidate": True,
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(synthesis.SynthesisError, "not present in topic input"):
            synthesis.load_topic_claims(self.root, "ai-and-work")

    def test_material_candidate_change_requires_one_global_output(self):
        plan = synthesis.plan_repository(self.root, now="2026-08-23T00:00:00Z")
        self.write_valid_claims(plan)

        global_plan = synthesis.prepare_global(self.root, now="2026-08-23T00:00:00Z")

        self.assertTrue(global_plan["global_due"])
        self.assertIn("material-candidate-change", global_plan["reasons"])
        self.assertTrue((self.stage / "global-input.json").exists())

    def test_global_input_states_the_summary_length_contract(self):
        plan = synthesis.plan_repository(self.root, now="2026-08-23T00:00:00Z")
        self.write_valid_claims(plan)

        synthesis.prepare_global(self.root, now="2026-08-23T00:00:00Z")

        global_input = json.loads((self.stage / "global-input.json").read_text())
        self.assertIn("summary of at most 180 characters", global_input["instructions"])

    def test_dirty_topic_requires_new_staged_claims(self):
        plan = synthesis.plan_repository(self.root, now="2026-08-23T00:00:00Z")

        with self.assertRaisesRegex(synthesis.SynthesisError, "Dirty topic .* has no staged claims"):
            synthesis.prepare_global(self.root, now="2026-08-23T00:00:00Z")

        self.assertTrue(plan["dirty_topics"])

    def complete_first_render(self) -> dict:
        plan = synthesis.plan_repository(self.root, now="2026-08-23T00:00:00Z")
        self.write_valid_claims(plan)
        global_plan = synthesis.prepare_global(self.root, now="2026-08-23T00:00:00Z")
        self.assertTrue(global_plan["global_due"])
        self.write_valid_global()
        synthesis.render_repository(self.root, now="2026-08-23T00:00:00Z")
        return plan

    def test_only_dirty_topic_changes_and_global_snapshot_waits_for_gate(self):
        first_plan = self.complete_first_render()
        topic_dir = self.root / "wiki" / "_generated" / "synthesis" / "topics"
        before_topics = {path.stem: path.read_bytes() for path in topic_dir.glob("*.md")}
        current_path = self.root / "wiki" / "_generated" / "synthesis" / "current.md"
        before_current = current_path.read_bytes()

        paragraph = next(item for item in first_plan["paragraphs"] if not item["secondary_topics"])
        topic_id = paragraph["primary_topic"]
        overview_path = self.root / "wiki" / "overview.md"
        overview = overview_path.read_text(encoding="utf-8")
        overview_path.write_text(
            overview.replace(paragraph["text"], paragraph["text"] + " Additional context.", 1),
            encoding="utf-8",
        )
        sources = self.root / "wiki" / "sources"
        (sources / "new-episode.md").write_text(
            "---\ntype: source\nsource_file: /episodes/new.md\n---\n# New episode\n",
            encoding="utf-8",
        )

        second_plan = synthesis.plan_repository(self.root, now="2026-08-23T01:00:00Z")
        self.assertEqual([topic_id], second_plan["dirty_topics"])
        self.write_valid_claims(second_plan)
        global_plan = synthesis.prepare_global(self.root, now="2026-08-23T01:00:00Z")
        self.assertFalse(global_plan["global_due"])
        result = synthesis.render_repository(self.root, now="2026-08-23T01:00:00Z")

        self.assertFalse(result["global_compacted"])
        self.assertEqual(before_current, current_path.read_bytes())
        after_topics = {path.stem: path.read_bytes() for path in topic_dir.glob("*.md")}
        self.assertNotEqual(before_topics[topic_id], after_topics[topic_id])
        for clean_topic in set(before_topics) - {topic_id}:
            self.assertEqual(before_topics[clean_topic], after_topics[clean_topic])
        manifest = json.loads((self.root / "wiki" / "_generated" / "synthesis" / "manifest.json").read_text())
        self.assertEqual({"episode_count": 1, "source_count": 1}, manifest["corpus"])
        self.assertEqual({"episode_count": 0, "source_count": 0}, manifest["global"]["corpus"])
        synthesis.validate_repository(self.root)

    def test_render_is_atomic_valid_and_second_identical_run_is_noop(self):
        sources = self.root / "wiki" / "sources"
        (sources / "episode-one.md").write_text(
            '---\ntype: source\nsource_file: "/episodes/one.md"\n---\n# One\n', encoding="utf-8"
        )
        (sources / "episode-two.md").write_text(
            '---\ntype: source\nsource_file: "/episodes/two.md"\n---\n# Two\n', encoding="utf-8"
        )
        plan = synthesis.plan_repository(self.root, now="2026-08-23T00:00:00Z")
        self.write_valid_claims(plan)
        synthesis.prepare_global(self.root, now="2026-08-23T00:00:00Z")
        self.write_valid_global()

        first = synthesis.render_repository(self.root, now="2026-08-23T00:00:00Z")
        manifest_path = self.root / "wiki" / "_generated" / "synthesis" / "manifest.json"
        first_manifest = manifest_path.read_bytes()
        current = (manifest_path.parent / "current.md").read_text(encoding="utf-8")
        synthesis.validate_repository(self.root)

        second_plan = synthesis.plan_repository(self.root, now="2026-08-23T00:00:00Z")

        self.assertTrue(first["global_compacted"])
        self.assertIn("## Executive Summary", current)
        self.assertIn("episode_count: 2", current)
        self.assertIn("source_count: 2", current)
        self.assertEqual({"episode_count": 2, "source_count": 2}, json.loads(first_manifest)["corpus"])
        self.assertEqual([], second_plan["dirty_topics"])
        self.assertEqual(first_manifest, manifest_path.read_bytes())

    def test_invalid_candidate_never_replaces_published_output(self):
        self.complete_first_render()
        output = self.root / "wiki" / "_generated" / "synthesis"
        before = {path.relative_to(output): path.read_bytes() for path in output.rglob("*") if path.is_file()}
        synthesis.plan_repository(self.root, now="2026-08-23T01:00:00Z", force_global=True)
        synthesis.prepare_global(self.root, now="2026-08-23T01:00:00Z")
        self.write_valid_global()
        global_path = self.stage / "global.json"
        payload = json.loads(global_path.read_text())
        first_topic = next(iter(payload["domain_summaries"]))
        payload["domain_summaries"][first_topic] = "## Open Questions\nInvalid embedded section."
        global_path.write_text(json.dumps(payload), encoding="utf-8")

        with self.assertRaisesRegex(synthesis.SynthesisError, "independently published section"):
            synthesis.render_repository(self.root, now="2026-08-23T01:00:00Z")

        after = {path.relative_to(output): path.read_bytes() for path in output.rglob("*") if path.is_file()}
        self.assertEqual(before, after)

    def test_overlong_global_summary_never_replaces_published_output(self):
        self.complete_first_render()
        output = self.root / "wiki" / "_generated" / "synthesis"
        before = {path.relative_to(output): path.read_bytes() for path in output.rglob("*") if path.is_file()}
        synthesis.plan_repository(self.root, now="2026-08-23T01:00:00Z", force_global=True)
        synthesis.prepare_global(self.root, now="2026-08-23T01:00:00Z")
        self.write_valid_global()
        global_path = self.stage / "global.json"
        payload = json.loads(global_path.read_text())
        payload["summary"] = "x" * 181
        global_path.write_text(json.dumps(payload), encoding="utf-8")

        with self.assertRaisesRegex(synthesis.SynthesisError, "summary exceeds 180 characters"):
            synthesis.render_repository(self.root, now="2026-08-23T01:00:00Z")

        after = {path.relative_to(output): path.read_bytes() for path in output.rglob("*") if path.is_file()}
        self.assertEqual(before, after)

    def test_validation_rejects_tampered_or_missing_topic_components(self):
        self.complete_first_render()
        output = self.root / "wiki" / "_generated" / "synthesis"
        claims_file = next((output / "claims").glob("*.json"))
        original = claims_file.read_text(encoding="utf-8")
        payload = json.loads(original)
        payload["summary"] += " Tampered."
        claims_file.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(synthesis.SynthesisError, "claims digest differs"):
            synthesis.validate_repository(self.root)

        claims_file.write_text(original, encoding="utf-8")
        topic_file = next((output / "topics").glob("*.md"))
        topic_file.unlink()
        with self.assertRaisesRegex(synthesis.SynthesisError, "do not exactly match"):
            synthesis.validate_repository(self.root)

    def test_release_validation_rejects_overlong_published_summary(self):
        self.complete_first_render()
        output = self.root / "wiki" / "_generated" / "synthesis"
        current_path = output / "current.md"
        current = current_path.read_text(encoding="utf-8")
        current = current.replace(
            'summary: "A compact cross-source knowledge map."',
            f"summary: {json.dumps('x' * 181)}",
        )
        current_path.write_text(current, encoding="utf-8")
        manifest_path = output / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["global"]["output_digest"] = synthesis.digest_text(current)
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        with self.assertRaisesRegex(synthesis.SynthesisError, "summary exceeds 180 characters"):
            synthesis.validate_repository(self.root)

    def test_release_validation_ignores_body_summary_when_frontmatter_summary_is_missing(self):
        self.complete_first_render()
        output = self.root / "wiki" / "_generated" / "synthesis"
        current_path = output / "current.md"
        current = current_path.read_text(encoding="utf-8")
        current = current.replace('summary: "A compact cross-source knowledge map."\n', "", 1)
        current += '\nsummary: "A body line is not metadata."\n'
        current_path.write_text(current, encoding="utf-8")
        manifest_path = output / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["global"]["output_digest"] = synthesis.digest_text(current)
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        with self.assertRaisesRegex(synthesis.SynthesisError, "missing its summary"):
            synthesis.validate_repository(self.root)

    def test_release_validation_rejects_duplicate_frontmatter_summaries(self):
        self.complete_first_render()
        output = self.root / "wiki" / "_generated" / "synthesis"
        current_path = output / "current.md"
        current = current_path.read_text(encoding="utf-8")
        current = current.replace(
            'summary: "A compact cross-source knowledge map."',
            'summary: "First summary."\nsummary: "A compact cross-source knowledge map."',
            1,
        )
        current_path.write_text(current, encoding="utf-8")
        manifest_path = output / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["global"]["output_digest"] = synthesis.digest_text(current)
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        with self.assertRaisesRegex(synthesis.SynthesisError, "exactly one summary"):
            synthesis.validate_repository(self.root)

    def test_release_validation_rejects_yaml_equivalent_duplicate_summary_keys(self):
        self.complete_first_render()
        output = self.root / "wiki" / "_generated" / "synthesis"
        current_path = output / "current.md"
        manifest_path = output / "manifest.json"
        original_current = current_path.read_text(encoding="utf-8")
        original_manifest = manifest_path.read_text(encoding="utf-8")
        for duplicate in ('summary : "Second summary."', '"summary": "Second summary."', "summary:"):
            with self.subTest(duplicate=duplicate):
                current = original_current.replace(
                    'summary: "A compact cross-source knowledge map."',
                    f'summary: "A compact cross-source knowledge map."\n{duplicate}',
                    1,
                )
                current_path.write_text(current, encoding="utf-8")
                manifest = json.loads(original_manifest)
                manifest["global"]["output_digest"] = synthesis.digest_text(current)
                manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

                with self.assertRaisesRegex(synthesis.SynthesisError, "exactly one summary"):
                    synthesis.validate_repository(self.root)

        current_path.write_text(original_current, encoding="utf-8")
        manifest_path.write_text(original_manifest, encoding="utf-8")

    def test_release_validation_rejects_noncanonical_yaml_summary_keys(self):
        self.complete_first_render()
        output = self.root / "wiki" / "_generated" / "synthesis"
        current_path = output / "current.md"
        manifest_path = output / "manifest.json"
        original_current = current_path.read_text(encoding="utf-8")
        original_manifest = manifest_path.read_text(encoding="utf-8")
        for duplicate in ('!!str summary: "Second summary."', r'"\x73ummary": "Second summary."'):
            with self.subTest(duplicate=duplicate):
                current = original_current.replace(
                    'summary: "A compact cross-source knowledge map."',
                    f'summary: "A compact cross-source knowledge map."\n{duplicate}',
                    1,
                )
                current_path.write_text(current, encoding="utf-8")
                manifest = json.loads(original_manifest)
                manifest["global"]["output_digest"] = synthesis.digest_text(current)
                manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

                with self.assertRaisesRegex(synthesis.SynthesisError, "frontmatter is not canonical"):
                    synthesis.validate_repository(self.root)

        current_path.write_text(original_current, encoding="utf-8")
        manifest_path.write_text(original_manifest, encoding="utf-8")

    def test_stable_candidate_id_with_changed_content_triggers_global_gate(self):
        first_plan = self.complete_first_render()
        paragraph = next(item for item in first_plan["paragraphs"] if not item["secondary_topics"])
        overview_path = self.root / "wiki" / "overview.md"
        overview = overview_path.read_text(encoding="utf-8")
        overview_path.write_text(
            overview.replace(paragraph["text"], paragraph["text"] + " Material revision.", 1),
            encoding="utf-8",
        )
        plan = synthesis.plan_repository(self.root, now="2026-08-23T01:00:00Z")
        self.write_valid_claims(plan)
        claims_path = self.stage / "claims" / f"{paragraph['primary_topic']}.json"
        payload = json.loads(claims_path.read_text())
        if payload["claims"]:
            payload["claims"][0]["statement"] += " Revised conclusion."
        else:
            payload["summary"] += " Revised conclusion."
        claims_path.write_text(json.dumps(payload), encoding="utf-8")

        global_plan = synthesis.prepare_global(self.root, now="2026-08-23T01:00:00Z")

        self.assertTrue(global_plan["global_due"])
        self.assertIn("material-candidate-change", global_plan["reasons"])

    @property
    def stage(self) -> Path:
        return self.root / ".synthesis-staging"

    def write_valid_claims(self, plan: dict) -> None:
        claims_dir = self.stage / "claims"
        claims_dir.mkdir(parents=True, exist_ok=True)
        for topic_id in plan["dirty_topics"]:
            bundle = json.loads((self.stage / "inputs" / f"{topic_id}.json").read_text())
            links = sorted({link for paragraph in bundle["paragraphs"] for link in paragraph["wikilinks"]})
            payload = {
                "topic_id": topic_id,
                "summary": f"Current state for {topic_id}.",
                "claims": [],
            }
            if links:
                payload["claims"].append(
                    {
                        "id": f"{topic_id}-claim",
                        "status": "supported",
                        "statement": f"A supported finding for [[{links[0]}]].",
                        "supporting_wikilinks": [links[0]],
                        "qualifications": [],
                        "global_candidate": True,
                    }
                )
            (claims_dir / f"{topic_id}.json").write_text(json.dumps(payload), encoding="utf-8")

    def write_valid_global(self) -> None:
        global_input = json.loads((self.stage / "global-input.json").read_text())
        candidates = global_input["global_candidates"]
        payload = {
            "summary": "A compact cross-source knowledge map.",
            "executive_claim_ids": [item["qualified_id"] for item in candidates[:8]],
            "domain_summaries": {
                topic["topic_id"]: topic["summary"] for topic in global_input["topics"]
            },
        }
        (self.stage / "global.json").write_text(json.dumps(payload), encoding="utf-8")


class CheckedInSynthesisTest(unittest.TestCase):
    def test_checked_in_generated_synthesis_passes_release_validation(self):
        root = Path(__file__).resolve().parents[1]
        result = synthesis.validate_repository(root)
        self.assertGreater(result["paragraph_count"], 0)
        self.assertGreater(result["topic_count"], 0)


if __name__ == "__main__":
    unittest.main()
