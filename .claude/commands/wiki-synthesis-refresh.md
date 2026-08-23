Refresh downstream synthesis artifacts after the normal ingest has finished updating `wiki/overview.md`.

Usage: `/wiki-synthesis-refresh`

Hard boundary: `wiki/overview.md` is automatic canonical output. This workflow reads it and must never rewrite it.

1. Run `python3 -m tools.synthesis plan`.
2. Read `.synthesis-staging/plan.json`.
3. For every ID in `dirty_topics`, read the complete bounded input at `.synthesis-staging/inputs/<topic-id>.json` and write `.synthesis-staging/claims/<topic-id>.json`:

```json
{
  "topic_id": "controlled-topic-id",
  "summary": "A concise current-state synthesis using every supplied paragraph.",
  "claims": [
    {
      "id": "stable-kebab-case-claim-id",
      "status": "supported",
      "statement": "A current finding with a grounded [[WikiLink]].",
      "supporting_wikilinks": ["WikiLink"],
      "qualifications": ["A limitation, counterexample, conflict, or source-scope boundary."],
      "global_candidate": true
    }
  ]
}
```

Rules:
- Use every paragraph in the topic input, not only the newest one.
- Merge repetition and update an existing stable claim instead of appending a near-duplicate.
- Preserve or narrow existing claim IDs when the same proposition remains.
- Every supporting wikilink must occur in that topic's input bundle.
- Allowed statuses: `supported`, `qualified`, `contested`, `source-scoped`.
- Mark only claims useful in the short global map as `global_candidate`.

4. Run `python3 -m tools.synthesis prepare-global`.
5. If `global_due` is true, read `.synthesis-staging/global-input.json` and write `.synthesis-staging/global.json`:

```json
{
  "summary": "One short description suitable for the Podcast Atlas landing card.",
  "executive_claim_ids": ["topic-id:claim-id"],
  "domain_summaries": {
    "topic-id": "A concise current synthesis for this complete topic."
  }
}
```

Select one to eight existing `global_candidates`. `domain_summaries` must contain every active topic exactly once. Do not add Update History, Open Questions, processing logs, or claims absent from the topic inputs.

6. Run `python3 -m tools.synthesis render`.
7. Run `python3 -m tools.synthesis validate` and stop on any error.
8. Commit the canonical ingest changes and all validated `wiki/_generated/synthesis/` artifacts together. The renderer writes `manifest.json` last; never edit generated Markdown manually.
