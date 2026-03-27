# Summarizer Refresh/Update Feature Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable the doc-tools summarizer to re-read source documents and update existing reference markdown files when content has meaningfully changed.

**Architecture:** Single skill, single agent. The existing `summarizer` agent gets an "Update Mode" section that defines the scan-compare-update workflow. Mode is inferred from context (directory of existing summaries = update mode). Existing reference files migrate to YAML frontmatter for structured source tracking.

**Tech Stack:** Markdown, YAML frontmatter, Claude Code agent/skill system

---

### Task 1: Migrate scrum-guide-summary.md to YAML Frontmatter

**Files:**
- Modify: `plugins/ansible-agile-coach/skills/ansible-product-owner/references/scrum-guide-summary.md`

- [ ] **Step 1: Add YAML frontmatter and remove inline source line**

Replace the current file header (lines 1-4):

```markdown
# 2020 Scrum Guide — Coaching Reference

Summary of the 2020 Scrum Guide by Ken Schwaber and Jeff Sutherland.
Source: `2020-Scrum-Guide-US.pdf` — Google Drive file ID: `1Gq3jc2mXmgfXn3FTu_64Zv7kuUfxR0oB`
```

With:

```markdown
---
source_type: gdrive
source_id: "1Gq3jc2mXmgfXn3FTu_64Zv7kuUfxR0oB"
source_name: "2020-Scrum-Guide-US.pdf"
last_summarized: 2026-03-03
---

# 2020 Scrum Guide — Coaching Reference

Summary of the 2020 Scrum Guide by Ken Schwaber and Jeff Sutherland.
```

- [ ] **Step 2: Add a `## Source` footer section**

This file currently has no `## Source` footer. Add one at the end of the file (after line 157):

```markdown

## Source

This summary was generated from Google Drive file "2020-Scrum-Guide-US.pdf" (ID: `1Gq3jc2mXmgfXn3FTu_64Zv7kuUfxR0oB`) on 2026-03-03.
```

- [ ] **Step 3: Verify the file parses correctly**

Run: `head -10 plugins/ansible-agile-coach/skills/ansible-product-owner/references/scrum-guide-summary.md`

Expected: YAML frontmatter block followed by the `# 2020 Scrum Guide` heading.

- [ ] **Step 4: Commit**

```bash
git add plugins/ansible-agile-coach/skills/ansible-product-owner/references/scrum-guide-summary.md
git commit -m "feat: migrate scrum-guide-summary.md to YAML frontmatter"
```

---

### Task 2: Migrate pichler-agile-product-management-summary.md to YAML Frontmatter

**Files:**
- Modify: `plugins/ansible-agile-coach/skills/ansible-product-owner/references/pichler-agile-product-management-summary.md`

- [ ] **Step 1: Add YAML frontmatter and remove inline source line**

Replace the current file header (lines 1-3):

```markdown
# Pichler: Agile Product Management with Scrum -- Coaching Reference

Source: Roman Pichler, *Agile Product Management with Scrum: Creating Products that Customers Love* (Addison-Wesley, 2010). Google Drive file ID: `1LSdQ2VpNj_uZB1ylEiUGVbRVEyvIRwRH`
```

With:

```markdown
---
source_type: gdrive
source_id: "1LSdQ2VpNj_uZB1ylEiUGVbRVEyvIRwRH"
source_name: "Agile Product Management with Scrum"
last_summarized: 2026-03-03
---

# Pichler: Agile Product Management with Scrum -- Coaching Reference
```

- [ ] **Step 2: Update the existing `## Source` footer**

Replace the current footer (line 385-388):

```markdown
## Source

This summary was generated from the extracted text of "Agile Product Management with Scrum" by Roman Pichler (Addison-Wesley, 2010) on 2026-03-03. Content is organized by coaching use cases for AI agent consumption.
```

With:

```markdown
## Source

This summary was generated from Google Drive file "Agile Product Management with Scrum" (ID: `1LSdQ2VpNj_uZB1ylEiUGVbRVEyvIRwRH`) on 2026-03-03. Content is organized by coaching use cases for AI agent consumption.
```

- [ ] **Step 3: Verify the file parses correctly**

Run: `head -10 plugins/ansible-agile-coach/skills/ansible-product-owner/references/pichler-agile-product-management-summary.md`

Expected: YAML frontmatter block followed by the `# Pichler:` heading.

- [ ] **Step 4: Commit**

```bash
git add plugins/ansible-agile-coach/skills/ansible-product-owner/references/pichler-agile-product-management-summary.md
git commit -m "feat: migrate pichler-agile-product-management-summary.md to YAML frontmatter"
```

---

### Task 3: Migrate cohn-user-stories-applied-summary.md to YAML Frontmatter

**Files:**
- Modify: `plugins/ansible-agile-coach/skills/ansible-product-owner/references/cohn-user-stories-applied-summary.md`

- [ ] **Step 1: Add YAML frontmatter and remove inline source line**

Replace the current file header (lines 1-5):

```markdown
# User Stories Applied (Mike Cohn) -- AI Product Owner Coaching Reference

A coaching-optimized summary of "User Stories Applied: For Agile Software Development" (Addison-Wesley, 2004). Organized by coaching use case, not chapter order. All content derived from the source text.

Source: `User-Stories-Applied-Mike-Cohn.pdf` — Google Drive file ID: `17L9r6ZSy6VbKNcTw0haQRrWXBkNnSdb9`
```

With:

```markdown
---
source_type: gdrive
source_id: "17L9r6ZSy6VbKNcTw0haQRrWXBkNnSdb9"
source_name: "User-Stories-Applied-Mike-Cohn.pdf"
last_summarized: 2026-03-03
---

# User Stories Applied (Mike Cohn) -- AI Product Owner Coaching Reference

A coaching-optimized summary of "User Stories Applied: For Agile Software Development" (Addison-Wesley, 2004). Organized by coaching use case, not chapter order. All content derived from the source text.
```

- [ ] **Step 2: Update the existing trailing source line**

Replace the current trailing source line (line 384):

```markdown
Source: "User Stories Applied: For Agile Software Development" by Mike Cohn (Addison-Wesley, 2004). Local file: `/Users/carogers/git-checkouts/manager-toolkit/.claude/skills/ansible-product-owner/references/User-Stories-Applied-Mike-Cohn.pdf`. Summary created 2026-03-03.
```

With a proper `## Source` section:

```markdown
## Source

This summary was generated from Google Drive file "User-Stories-Applied-Mike-Cohn.pdf" (ID: `17L9r6ZSy6VbKNcTw0haQRrWXBkNnSdb9`) on 2026-03-03.
```

- [ ] **Step 3: Verify the file parses correctly**

Run: `head -10 plugins/ansible-agile-coach/skills/ansible-product-owner/references/cohn-user-stories-applied-summary.md`

Expected: YAML frontmatter block followed by the `# User Stories Applied` heading.

- [ ] **Step 4: Commit**

```bash
git add plugins/ansible-agile-coach/skills/ansible-product-owner/references/cohn-user-stories-applied-summary.md
git commit -m "feat: migrate cohn-user-stories-applied-summary.md to YAML frontmatter"
```

---

### Task 4: Add Update Mode to the Summarizer Agent

**Files:**
- Modify: `plugins/doc-tools/agents/summarizer.md`

- [ ] **Step 1: Add the Frontmatter Schema section**

After the `## Preservation Rules` section (after line 107), add:

````markdown

## Reference File Frontmatter Schema

When creating new summaries, include this YAML frontmatter at the top of the output file:

```yaml
---
source_type: gdrive          # gdrive | local_file | url | manual
source_id: "file-id-here"   # Google Drive file ID, file path, URL, or null
source_name: "filename.pdf"  # human-readable source name, or null
last_summarized: 2026-03-27  # date the summary was created or last updated
---
```

- `source_type: gdrive` — source is a Google Drive file, read via MCP gdrive tool
- `source_type: local_file` — source is a local file, read via Read tool
- `source_type: url` — source is a URL, fetch via WebFetch
- `source_type: manual` — no external source; file was created manually

Set `last_summarized` to today's date when creating or updating a summary.
````

- [ ] **Step 2: Add the Update Mode Workflow section**

After the new Frontmatter Schema section, add:

````markdown

## Update Mode (Refresh Existing Summaries)

When the user asks to "update", "refresh", or "re-summarize" existing reference files — or points you at a directory of existing markdown summaries — follow this workflow instead of the standard create workflow.

### Mode Detection

- User points at a **source document** + output path → use the standard create workflow above
- User points at a **directory of existing markdown summaries** → use this update workflow
- User says "update", "refresh", or "re-summarize" → use this update workflow

### Update Workflow

1. **Scan** — Use Glob to find all `.md` files in the target directory
2. **Parse frontmatter** — For each file, read the YAML frontmatter and extract `source_type`, `source_id`, `source_name`, `last_summarized`
3. **Triage** each file:
   - `source_type: manual` → skip, record as "skipped (manual)"
   - `source_type: gdrive` → read source document via MCP gdrive tool using `source_id`
   - `source_type: local_file` → read source document via Read tool using `source_id`
   - `source_type: url` → fetch source document via WebFetch using `source_id`
   - If the source is inaccessible → record as "error" with details
4. **Re-summarize** — Generate a new summary from the source document using the same Output Format, Formatting Guidelines, and Quality Criteria as create mode
5. **Compare** — Read the existing summary body (below frontmatter) and compare it against the newly generated summary. Use your judgment to assess whether the source has **materially changed**:
   - **Meaningful changes**: new sections added, content removed, facts or details updated, structural reorganization
   - **NOT meaningful**: minor wording differences that are just LLM rephrasing noise, whitespace changes, slightly different bullet ordering with identical content
6. **Write or skip**:
   - If meaningful changes exist → overwrite the file with the new summary, update `last_summarized` to today's date in the frontmatter, and record as "updated"
   - If no meaningful changes → do not write the file, record as "no changes"

### Update Report

After processing all files, return a report in this format:

```
## Refresh Results

### Updated
- **filename.md** — Updated `last_summarized` to YYYY-MM-DD
  - [Brief description of what changed in the source]
  - [Another change if applicable]

### No Changes
- **filename.md** — Source unchanged since YYYY-MM-DD

### Skipped
- **filename.md** — Manual source, no external document to refresh

### Errors
- **filename.md** — [Error description, e.g., "Could not access Google Drive file ID `...` (permission denied)"]
```

Categorize every file into exactly one of these four sections. Omit empty sections.
For updated files, include a brief description of what materially changed in the source document.
````

- [ ] **Step 3: Update the Output Format section to include frontmatter**

Replace the existing Output Format section (lines 67-87):

````markdown
## Output Format

Structure every summary as follows:

```markdown
# [Document Name] - Summary

[Brief intro paragraph explaining the document's purpose]

## [Key Section 1]

[Content with appropriate formatting]

## [Key Section 2]

[Content with appropriate formatting]

## Source

This summary was generated from [source type] "[Document Name]" (ID/Path: [identifier]) on YYYY-MM-DD.
```
````

With:

````markdown
## Output Format

Structure every summary as follows:

```markdown
---
source_type: [gdrive | local_file | url | manual]
source_id: "[identifier]"
source_name: "[human-readable name]"
last_summarized: YYYY-MM-DD
---

# [Document Name] - Summary

[Brief intro paragraph explaining the document's purpose]

## [Key Section 1]

[Content with appropriate formatting]

## [Key Section 2]

[Content with appropriate formatting]

## Source

This summary was generated from [source type] "[Document Name]" (ID/Path: [identifier]) on YYYY-MM-DD.
```
````

- [ ] **Step 4: Add an update-mode example to the agent description**

In the YAML frontmatter `description` field (lines 3-41), add a new example after the existing examples:

```markdown
  <example>
  Context: User wants to refresh existing reference summaries
  user: "Update the reference files in the ansible-product-owner skill"
  assistant: "I'll use the summarizer agent to scan the reference files, re-read their source documents, and update any summaries where the source has meaningfully changed."
  <commentary>
  The user is pointing at a directory of existing summaries with frontmatter — this triggers update mode.
  </commentary>
  </example>
```

- [ ] **Step 5: Verify the agent file is well-formed**

Run: `head -50 plugins/doc-tools/agents/summarizer.md`

Expected: YAML frontmatter with examples (including the new update example), followed by the `# Document Summarizer Agent` heading.

Run: `grep -c "## " plugins/doc-tools/agents/summarizer.md`

Expected: a count showing all section headings including the new ones (Reference File Frontmatter Schema, Update Mode, Mode Detection, Update Workflow, Update Report).

- [ ] **Step 6: Commit**

```bash
git add plugins/doc-tools/agents/summarizer.md
git commit -m "feat: add update mode and frontmatter schema to summarizer agent"
```

---

### Task 5: Update the Summarize Skill Triggers

**Files:**
- Modify: `plugins/doc-tools/skills/summarize/SKILL.md`

- [ ] **Step 1: Expand the skill description to trigger on update/refresh phrases**

Replace the current `description` field in the YAML frontmatter (lines 3-8):

```yaml
description: >
  Summarize documents into AI-agent-friendly markdown. Use when the user asks to
  summarize a document, create a reference summary, convert documentation to markdown,
  or prepare documents for AI consumption. Also use when the user says things like
  "summarize this doc", "create a reference from this", "make this AI-friendly",
  or needs to turn any document into a scannable, structured markdown summary.
```

With:

```yaml
description: >
  Summarize documents into AI-agent-friendly markdown, or update existing summaries
  from their source documents. Use when the user asks to summarize a document, create
  a reference summary, convert documentation to markdown, prepare documents for AI
  consumption, update reference files, refresh summaries, or re-summarize existing
  references. Also use when the user says things like "summarize this doc", "create a
  reference from this", "make this AI-friendly", "update the reference files",
  "refresh the summaries", or "re-summarize the references".
```

- [ ] **Step 2: Add update mode to the "When to Use" section**

Replace the current "When to Use" section (lines 19-24):

```markdown
## When to Use

- User asks to summarize a document from any source (local files, Google Drive, etc.)
- User needs to create reference documentation for a skill or project
- User wants to convert existing documentation into a more scannable format
- User mentions needing AI-friendly or agent-friendly documentation
```

With:

```markdown
## When to Use

- User asks to summarize a document from any source (local files, Google Drive, etc.)
- User needs to create reference documentation for a skill or project
- User wants to convert existing documentation into a more scannable format
- User mentions needing AI-friendly or agent-friendly documentation
- User asks to update, refresh, or re-summarize existing reference files
```

- [ ] **Step 3: Add update mode to the "How to Use" section**

Replace the current "How to Use" section (lines 26-31):

```markdown
## How to Use

1. Identify the source document(s) the user wants summarized
2. If the user has not specified an output path, ask where to save the summary
3. Dispatch the `summarizer` agent with the source and output path
4. The agent handles reading, analyzing, formatting, and saving
```

With:

```markdown
## How to Use

1. Identify whether this is a **create** (new summary) or **update** (refresh existing summaries) request
2. For create: identify the source document(s) and output path (ask if not specified)
3. For update: identify the directory of existing summary files to refresh
4. Dispatch the `summarizer` agent — it detects the mode and handles the full workflow
```

- [ ] **Step 4: Add frontmatter note to "Output Conventions"**

Replace the current "Output Conventions" section (lines 33-39):

```markdown
## Output Conventions

- Summaries use hierarchical markdown headings for navigation
- Tables for structured data, bullet points for lists, numbered lists for processes
- Code blocks for technical patterns (JQL, regex, API calls, etc.)
- Technical details (URLs, identifiers, field names) are preserved exactly
- Each summary includes a Source section noting the origin document and date
```

With:

```markdown
## Output Conventions

- Summaries include YAML frontmatter with source tracking metadata (source_type, source_id, source_name, last_summarized)
- Summaries use hierarchical markdown headings for navigation
- Tables for structured data, bullet points for lists, numbered lists for processes
- Code blocks for technical patterns (JQL, regex, API calls, etc.)
- Technical details (URLs, identifiers, field names) are preserved exactly
- Each summary includes a Source section noting the origin document and date
```

- [ ] **Step 5: Verify the skill file**

Run: `cat plugins/doc-tools/skills/summarize/SKILL.md`

Expected: Updated description with refresh/update triggers, new "When to Use" bullet, updated "How to Use" steps, and frontmatter note in "Output Conventions".

- [ ] **Step 6: Commit**

```bash
git add plugins/doc-tools/skills/summarize/SKILL.md
git commit -m "feat: expand summarize skill triggers for update/refresh mode"
```

---

### Task 6: Final Verification

- [ ] **Step 1: Verify all three reference files have valid frontmatter**

Run for each file:
```bash
head -7 plugins/ansible-agile-coach/skills/ansible-product-owner/references/scrum-guide-summary.md
head -7 plugins/ansible-agile-coach/skills/ansible-product-owner/references/pichler-agile-product-management-summary.md
head -7 plugins/ansible-agile-coach/skills/ansible-product-owner/references/cohn-user-stories-applied-summary.md
```

Expected: Each file starts with `---`, has `source_type: gdrive`, `source_id:`, `source_name:`, `last_summarized: 2026-03-03`, and closes with `---`.

- [ ] **Step 2: Verify no inline source lines remain in reference files**

Run: `grep -n "^Source:" plugins/ansible-agile-coach/skills/ansible-product-owner/references/*.md`

Expected: No matches (all inline `Source:` lines have been removed or moved into `## Source` footer sections).

- [ ] **Step 3: Verify the agent file contains all new sections**

Run: `grep "^## " plugins/doc-tools/agents/summarizer.md`

Expected output includes these headings:
```
## Your Core Responsibilities
## Workflow
## Output Format
## Formatting Guidelines
## Preservation Rules
## Reference File Frontmatter Schema
## Update Mode (Refresh Existing Summaries)
## Quality Criteria
## Edge Cases
## Response
```

- [ ] **Step 4: Verify the skill description includes update triggers**

Run: `grep -c "update\|refresh\|re-summarize" plugins/doc-tools/skills/summarize/SKILL.md`

Expected: 6 or more matches across the description, When to Use, and How to Use sections.
