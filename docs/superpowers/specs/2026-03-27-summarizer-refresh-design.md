# Summarizer Refresh/Update Feature — Design Spec

## Overview

Extend the existing `doc-tools` summarizer skill and agent to support re-summarizing existing reference files. When pointed at a directory of markdown summaries with YAML frontmatter, the agent reads each file's source document, generates a new summary, compares for meaningful changes, and updates only files where the source has materially changed.

## YAML Frontmatter Schema

All reference markdown files use this frontmatter:

```yaml
---
source_type: gdrive          # gdrive | local_file | url | manual
source_id: "1Gq3jc2..."     # Google Drive file ID, file path, URL, or null
source_name: "filename.pdf"  # human-readable source name, or null
last_summarized: 2026-03-03  # date of last summarization, or null
---
```

- `source_type: manual` files are skipped during refresh (no external source to re-read).
- `source_type: gdrive` files are read via the MCP gdrive tool.
- `source_type: local_file` files are read via the Read tool.
- `source_type: url` files are fetched via WebFetch.

## Agent Update Mode Workflow

When the agent detects an update/refresh request (pointed at existing summaries rather than a new source document), it follows this flow:

1. **Scan** — Find all `.md` files in the target directory.
2. **Parse frontmatter** — Extract `source_type`, `source_id`, `source_name`, `last_summarized`.
3. **Triage** each file:
   - `source_type: manual` — skip, report as "skipped (manual)".
   - `source_type: gdrive` — read source via MCP gdrive tool.
   - `source_type: local_file` — read source via Read tool.
   - `source_type: url` — fetch source via WebFetch.
   - Source inaccessible — report as "error" with details.
4. **Re-summarize** — Generate a new summary from the source using the same formatting rules and quality criteria as create mode.
5. **Compare** — Read the existing summary and compare against the new one. Use judgment to assess whether the source has materially changed (new sections, removed content, updated details). Ignore minor wording variations that are just LLM rephrasing noise.
6. **Write or skip** — If meaningful changes exist, overwrite the file (preserving frontmatter with updated `last_summarized`). If no meaningful changes, skip and report "no changes."

## Mode Detection

The agent infers the mode from context:

- User points at a **source document** + output path — create mode (existing behavior).
- User points at a **directory of existing summaries** — update mode.
- User says "update" or "refresh" — update mode.

No routing logic needed. Single skill, single agent.

## Output Report

After processing all files, the agent produces a summary report:

```
## Refresh Results

### Updated
- **scrum-guide-summary.md** — Updated `last_summarized` to 2026-03-27
  - Added new section on "Scrum Values" expanded guidance
  - Removed deprecated "Development Team" terminology references

### No Changes
- **cohn-user-stories-applied-summary.md** — Source unchanged since 2026-03-03

### Skipped
- **manual-notes.md** — Manual source, no external document to refresh

### Errors
- **pichler-summary.md** — Could not access Google Drive file ID `1LSd...` (permission denied)
```

Each updated file gets a brief description of what changed in the source. Unchanged, skipped, and errored files get a one-line explanation.

## Skill Description Changes

The `summarize` SKILL.md description expands to trigger on update/refresh phrases:

- Add triggers: "update reference files", "refresh summaries", "re-summarize"
- Add "When to Use" bullet for updating existing reference files
- Add "How to Use" step for detecting update mode

## Migration of Existing Reference Files

The three existing files in `ansible-product-owner/references/` get migrated to frontmatter:

| File | source_type | source_id | source_name | last_summarized |
|------|-------------|-----------|-------------|-----------------|
| scrum-guide-summary.md | gdrive | `1Gq3jc2mXmgfXn3FTu_64Zv7kuUfxR0oB` | 2020-Scrum-Guide-US.pdf | 2026-03-03 |
| pichler-agile-product-management-summary.md | gdrive | `1LSdQ2VpNj_uZB1ylEiUGVbRVEyvIRwRH` | Agile Product Management with Scrum | 2026-03-03 |
| cohn-user-stories-applied-summary.md | gdrive | `17L9r6ZSy6VbKNcTw0haQRrWXBkNnSdb9` | User-Stories-Applied-Mike-Cohn.pdf | 2026-03-03 |

Inline `Source:` lines in the body are removed. Trailing source/date lines at the end of files are cleaned up into the standard `## Source` footer format.

## Files to Modify

1. **`plugins/doc-tools/agents/summarizer.md`** — Add Update Mode section, frontmatter schema docs, comparison logic, output report format
2. **`plugins/doc-tools/skills/summarize/SKILL.md`** — Expand description and trigger phrases for update/refresh
3. **`plugins/ansible-agile-coach/skills/ansible-product-owner/references/scrum-guide-summary.md`** — Add frontmatter, remove inline source
4. **`plugins/ansible-agile-coach/skills/ansible-product-owner/references/pichler-agile-product-management-summary.md`** — Add frontmatter, remove inline source
5. **`plugins/ansible-agile-coach/skills/ansible-product-owner/references/cohn-user-stories-applied-summary.md`** — Add frontmatter, remove inline source
