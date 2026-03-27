---
name: summarize
description: >
  Summarize documents into AI-agent-friendly markdown, or update existing summaries
  from their source documents. Use when the user asks to summarize a document, create
  a reference summary, convert documentation to markdown, prepare documents for AI
  consumption, update reference files, refresh summaries, or re-summarize existing
  references. Also use when the user says things like "summarize this doc", "create a
  reference from this", "make this AI-friendly", "update the reference files",
  "refresh the summaries", or "re-summarize the references".
context: fork
agent: summarizer
---

## What This Skill Does

This skill orchestrates document summarization by dispatching the `summarizer` agent.
When activated, invoke the doc-summarizer agent to handle the full workflow of reading,
analyzing, and formatting documents into AI-agent-friendly markdown.

## When to Use

- User asks to summarize a document from any source (local files, Google Drive, etc.)
- User needs to create reference documentation for a skill or project
- User wants to convert existing documentation into a more scannable format
- User mentions needing AI-friendly or agent-friendly documentation
- User asks to update, refresh, or re-summarize existing reference files

## How to Use

1. Identify whether this is a **create** (new summary) or **update** (refresh existing summaries) request
2. For create: identify the source document(s) and output path (ask if not specified)
3. For update: identify the directory of existing summary files to refresh
4. Dispatch the `summarizer` agent — it detects the mode and handles the full workflow

## Output Conventions

- Summaries include YAML frontmatter with source tracking metadata (source_type, source_id, source_name, last_summarized)
- Summaries use hierarchical markdown headings for navigation
- Tables for structured data, bullet points for lists, numbered lists for processes
- Code blocks for technical patterns (JQL, regex, API calls, etc.)
- Technical details (URLs, identifiers, field names) are preserved exactly
