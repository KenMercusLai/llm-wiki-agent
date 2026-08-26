Ingest a source document into the LLM Wiki.

Usage: /wiki-ingest $ARGUMENTS

$ARGUMENTS should be the path to a file in raw/, e.g. `raw/articles/my-article.md`

Follow the Ingest Workflow defined in CLAUDE.md exactly:
1. Read the source file at the given path
2. Read wiki/index.md and wiki/overview.md for current context
3. Write wiki/sources/<slug>.md (source page format per CLAUDE.md)
4. Update wiki/index.md — add the new entry under Sources
5. Update wiki/overview.md — revise synthesis if warranted
6. Create/update entity pages (wiki/entities/) for key people, companies, projects. Read the complete existing `sources` set first and use the `knowledge_schema: synthesis-v1` Entity contract from CLAUDE.md.
7. Create/update concept pages (wiki/concepts/) for key ideas and frameworks. Read the complete existing `sources` set first and use the `knowledge_schema: synthesis-v1` Concept contract from CLAUDE.md.
8. Flag any contradictions with existing wiki content
9. Append to wiki/log.md: ## [today's date] ingest | <Title>
10. Follow `.claude/commands/wiki-synthesis-refresh.md` to refresh the downstream generated synthesis. This downstream step reads but never rewrites the automatic `wiki/overview.md`.
11. Run `python3 -m tools.validate_publish` as the fail-closed post-ingest validation.

After completing all writes, summarize: what was added, which canonical and generated pages were created or updated, whether global compaction ran, and any contradictions found.
