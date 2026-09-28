---
name: summarize
description: Summarize documents into structured Markdown for AI agents and human readers, or refresh existing summaries from their source documents.
---

## What This Skill Does

When a client supports subagents, delegate the focused reading and extraction work to a
document-summarization subagent so the main context stays concise. Give the worker the
source, requested output path, and output conventions below. If subagents are unavailable,
follow the same workflow directly.

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
4. Delegate the reading, analysis, and formatting work when possible; otherwise complete it directly.

## Output Conventions

- Summaries include YAML frontmatter with source tracking metadata (source_type, source_id, source_name, last_summarized)
- Summaries use hierarchical markdown headings for navigation
- Tables for structured data, bullet points for lists, numbered lists for processes
- Code blocks for technical patterns (JQL, regex, API calls, etc.)
- Technical details (URLs, identifiers, field names) are preserved exactly
