# Knowledge Page Schema

## `synthesis-v1`

`synthesis-v1` is the synthesis-first contract for Concept and Entity pages. It is opt-in so the corpus can migrate incrementally; any Concept or Entity that is created or updated must adopt it.

### Front matter

A structured page retains the existing canonical metadata and adds:

```yaml
knowledge_schema: synthesis-v1
```

The `sources` list remains the complete, ordered provenance inventory. Do not remove, reorder, or replace existing source keys during a structural migration. `last_updated` records the latest source-backed change.

### Concept body

Use these H2 sections, exactly and in order:

1. `Definition`
2. `Current Synthesis`
3. `Key Claims`
4. `Evidence`
5. `Counterevidence & Qualifications`
6. `What Changed`
7. `Related Concepts`

### Entity body

Use these H2 sections, exactly and in order:

1. `Overview`
2. `Current Profile`
3. `Key Characteristics`
4. `Evidence`
5. `Qualifications`
6. `What Changed`
7. `Relationships`

### Invariants

- `Key Claims` or `Key Characteristics` contains 3-7 top-level items.
- `Evidence` is grouped by claim or characteristic, not by source arrival order.
- Every Evidence group cites at least one source-note wikilink present in front matter.
- Counterevidence and qualifications stay explicit; disagreement is not flattened away.
- `What Changed` contains at most five material synthesis changes. It is not an ingest log.
- Related-page bullets use `- [[Page]] - semantic relationship`.
- Source-led append prose and legacy `Connections` sections are forbidden.
- A structural rewrite uses the complete bounded source set before changing the synthesis.

### Publication

Canonical Markdown does not duplicate the complete source inventory in the body. Podcast Atlas derives the public coverage line and collapsed `Sources` section from front matter plus Source Note-to-Episode mappings. The projection fails closed when a source note, episode, or Show mapping is missing.

### Validation

Run:

```bash
python3 -m tools.validate_knowledge_pages
python3 -m tools.validate_publish --root .
```
