---
name: summarize
description: >
  Summarize documents into AI-agent-friendly markdown. Use when the user asks to
  summarize a document, create a reference summary, convert documentation to markdown,
  or prepare documents for AI consumption. Also use when the user says things like
  "summarize this doc", "create a reference from this", "make this AI-friendly",
  or needs to turn any document into a scannable, structured markdown summary.
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

## How to Use

1. Identify the source document(s) the user wants summarized
2. If the user has not specified an output path, ask where to save the summary
3. Dispatch the `summarizer` agent with the source and output path
4. The agent handles reading, analyzing, formatting, and saving

## Output Conventions

- Summaries use hierarchical markdown headings for navigation
- Tables for structured data, bullet points for lists, numbered lists for processes
- Code blocks for technical patterns (JQL, regex, API calls, etc.)
- Technical details (URLs, identifiers, field names) are preserved exactly
- Each summary includes a Source section noting the origin document and date
