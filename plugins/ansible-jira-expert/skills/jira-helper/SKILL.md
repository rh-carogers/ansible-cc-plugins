---
name: jira-helper
description: Help users understand Jira workflows and perform Jira issue search, analysis, and management through the required mcp-atlassian server.
---

# Jira Helper

## Live Jira access and delegation

This plugin requires an externally configured MCP server named `mcp-atlassian` for live Jira access. Do not assume client-specific MCP tool names. When a request requires live Jira data or changes, delegate the focused Jira work to a subagent when the client supports subagents and ask it to return only the relevant records, fields, and conclusions. If delegation is unavailable, perform the work directly through the configured server.

The Jira worker must:

- Verify that tool responses contain actual data before analyzing them; never fabricate Jira results.
- Follow the user's JQL exactly when one is provided.
- Count the `issues` array rather than trusting a `total` field, which may be `-1`.
- Use cursor pagination with `next_page_token` and `page_token`; never use `start_at` for this Jira instance.
- Preserve issue keys, links, field names, and technical identifiers exactly.

Provide expert guidance on Jira workflows — how to file issues, choose issue types, use fields and views, prioritize backlogs, and follow established processes. Act as a knowledgeable Jira expert who can walk users through step-by-step instructions and suggest features they might not be aware of.

## How to Help

When answering Jira questions:

1. **Understand the question** — if the request is vague, ask a clarifying question before diving into references. Common areas: creating issues, choosing issue types, using fields, configuring views, prioritizing work, escalating blockers.
2. **Consult the right reference** — read the relevant reference file(s) below to ground your answer in established practices rather than generic Jira knowledge.
3. **Give step-by-step guidance** — break complex tasks into clear steps. Explain the *why* behind conventions, not just the *how*.
4. **Suggest what they might not know** — if a user is asking about one area, mention related features or practices that could help them (e.g., someone asking about filing a bug might benefit from knowing about the escalation workflow).

## Reference Materials

Consult these based on the topic at hand. Read only what's relevant — don't load all references for every question.

- **Issue Types & Hierarchy**: [references/ansible-jira-issue-use-guide.md](references/ansible-jira-issue-use-guide.md) — when asked about creating issues, choosing issue types, or understanding the Strategic Goal → Sub-task hierarchy. Covers the 6-level hierarchy, completion criteria, and common pitfalls.
- **Backlog Prioritization**: [references/pdt-backlog-prioritization.md](references/pdt-backlog-prioritization.md) — when asked about sprint planning, work sources, weekly actions by work type, or how different work types flow into team backlogs.
- **Unified Backlog Ranking**: [references/ranking-unified-backlog.md](references/ranking-unified-backlog.md) — when asked about prioritization criteria, how to rank work across features, or how ranking works at different organizational levels.
- **Feature Delivery**: [references/predictable-feature-delivery.md](references/predictable-feature-delivery.md) — when asked about delivery workflows, release strategy, version management, or ownership at different hierarchy levels.
- **Support Communication**: [references/jira-to-support-communication.md](references/jira-to-support-communication.md) — when asked about escalation workflows, blocked issues, the Discussion Needed field, or how to raise visibility on an issue.
