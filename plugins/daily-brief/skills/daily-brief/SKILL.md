---
name: daily-brief
description: Generate a daily briefing from configured calendar, email, Slack, Jira, team demo, and community sources, then write a triaged Markdown dashboard.
---

# Daily Brief

Generate a concise morning briefing from the configured sources. Keep collection work in
focused subagents whenever the client supports them so the main context is reserved for
triage, deduplication, and dashboard writing. If subagents are unavailable, perform the
same collection steps directly.

## Required setup

Copy `config.example.yaml` from the installed plugin to `daily-brief.yaml` in the project
or vault being scanned. Do not assume a client-specific configuration directory.

The configuration file is `daily-brief.yaml` in the current working directory. If it is
missing, stop and tell the user to copy the example file and fill in the values.

The Google Workspace and Slack MCP servers are required for the default brief. The
`mcp-atlassian` server is required whenever the configuration contains a `jira` section.
MCP servers are configured outside this plugin; discover their available capabilities
instead of relying on generated client-specific tool names.

Supported configuration values:

- `team.members`: team members with `name` and `slack_display_name`.
- `team.roster_file`: optional YAML roster. Prefer a top-level `members` list, then
  `teams[0].members`.
- `slack.team_channels`: channel objects with `id` and `name`.
- `slack.org_channels`: channel objects with `id` and `name`.
- `slack.demos_channel`: one channel object with `id` and `name`.
- `jira.backlog_filter_id`: saved Jira filter ID.
- `jira.escalation_label`: label used to flag escalations.
- `forum.enabled`, `forum.url`, and `forum.tag`: optional community forum source.
- `timezone`: IANA timezone, defaulting to `America/New_York`.
- `output.dashboard_path`: Markdown output path, defaulting to `Dashboards/daily-brief.md`.
- `output.state_path`: state path, defaulting to `Dashboards/snapshots/daily-brief-state.json`.

When the configuration includes Jira, every Jira collection task must use the externally
configured server named `mcp-atlassian`.

## Step 1: Load identity and time context

Read and parse `daily-brief.yaml`. Treat missing optional sections as disabled sources.

Use the configured Slack MCP identity capability to discover the user's display name,
user ID, and workspace URL. Use these values in searches and dashboard links; never use
hardcoded user names or workspace URLs.

Use the configured Jira MCP server to discover the Jira instance URL from a response or
from its configured `JIRA_URL`. Use that base URL for issue links.

Run `scripts/compute-lookback.sh` from this skill directory with the configured state path
and timezone:

```text
bash scripts/compute-lookback.sh "<output.state_path>" "<timezone>"
```

Use the script's JSON output directly. It provides:

- `today` for calendar queries;
- `prev_biz_day` and `cutoff_unix` for Slack and Jira queries;
- current timestamps for the dashboard header and state file;
- `demos_lookback_unix` and `demos_lookback_iso` for team demos;
- the configured timezone and abbreviation.

Do not manually calculate dates or day-of-week values. Email scanning has no time cutoff;
scan all unread inbox messages.

## Step 2: Collect source data in parallel

Dispatch one focused subagent per applicable collection task, in parallel. Give each
worker only the context and source access it needs. Every worker must return compact,
structured data and must not triage, deduplicate, or write the final dashboard.

Always run:

1. Unread email through the Google Workspace Gmail search and message-metadata capabilities.
2. Slack direct messages and mentions through the Slack search capabilities.
3. Today's calendar through the Google Workspace calendar capability.

Run these conditionally:

4. Slack team channels, if `slack.team_channels` is non-empty.
5. Slack organization channels, if `slack.org_channels` is non-empty.
6. Jira backlog, if the `jira` section exists.
7. Team demos, if `slack.demos_channel` and `team.members` exist.
8. Community forum, if `forum.enabled` is true.

Split team and organization channel lists into groups of no more than three channels. Fetch
channels sequentially inside each worker so messages cannot be attributed to the wrong
channel. Run the groups in parallel.

### Email worker

Search unread messages in the inbox, follow pagination, fetch metadata in batches, and
return one line per message:

```text
URGENCY | SENDER_NAME | SUBJECT | DATE | REASON
```

Classify as `IMMEDIATE`, `RESPONSE_NEEDED`, or `FYI`. Treat direct requests, deadlines,
expense alerts, and action-oriented calendar changes as immediate. Treat direct human
mail, future calendar changes, and invitations as needing response. Treat mailing lists,
automated notifications, canceled events, and newsletters as FYI. Sort by urgency, then
date descending. Return the unread count.

### Slack direct-message and mention worker

Search both direct messages and mentions since the previous business-day cutoff. Deduplicate
overlapping results, remove messages authored by the user, and remove bot-only messages
with no human reply. Return:

```text
AUTHOR | TIMESTAMP | MESSAGE_SNIPPET | MENTIONS_USER: yes/no
```

Do not triage this feed; the parent agent handles that.

### Slack channel workers

Fetch each assigned channel's history since the cutoff, including threads. Exclude messages
authored by the user and bot-only messages without human replies. Preserve channel identity
for every message and return:

```text
CHANNEL_ID | CHANNEL_NAME:
- AUTHOR | CHANNEL_ID | TIMESTAMP | MESSAGE_SNIPPET | MENTIONS_USER: yes/no | IS_THREAD_REPLY: yes/no
```

Report channels with no activity and return the total message count.

### Calendar worker

Fetch today's primary-calendar events in the configured timezone. Exclude all-day events,
focus-time events, and events the user declined. Return events sorted by start time:

```text
START_TIME | END_TIME | DURATION_MIN | TITLE | RECURRING: yes/no | STATUS: accepted/tentative/needsAction
```

Flag overlaps and gaps of less than five minutes. Return `TOTAL_MEETINGS`.

### Jira worker

Use the required external `mcp-atlassian` server and the configured saved filter:

```text
filter=<jira.backlog_filter_id> AND created >= "<prev_biz_day> 17:00"
```

Extract issue key, type, priority, summary, reporter, labels, and created date. Sort by
priority and then creation date. Return:

```text
ISSUE_KEY | TYPE | PRIORITY | SUMMARY | REPORTER | LABELS | CREATED_DATE
TOTAL_NEW_ISSUES: <count>
```

If applicable, also return `ESCALATIONS` for the configured escalation label and
`HIGH_PRIORITY` for Critical or Blocker issues.

For this Jira instance, count the `issues` array rather than the unreliable `total` field.
Use sequential cursor pagination with `next_page_token` and `page_token`; never use
`start_at`. Verify actual tool data before reporting results.

### Team demos worker

Fetch the demos channel since `demos_lookback_unix`, keep only messages authored by the
configured team members, and return:

```text
AUTHOR | TIMESTAMP | MESSAGE_SNIPPET | URLS | THREAD_REPLIES
TOTAL_DEMOS: <count>
```

### Community forum worker

Fetch the configured tag endpoint, identify topics with new posts or new activity since
the previous-business-day cutoff, and fetch the new posts for each matching topic. Return
the topic URL, title, views, last poster, new-post count, and short snippets. Return
`TOPICS_WITH_ACTIVITY` and `NEW_TOPICS`.

## Step 3: Triage

After all workers return, classify each item into one tier:

### Immediate Action

- Email marked `IMMEDIATE`.
- Direct Slack requests or mentions requiring action.
- Urgent blockers, escalations, or deadline risks.
- Jira issues with the configured escalation label.

### Needs Response

- Email marked `RESPONSE_NEEDED`.
- Non-urgent Slack questions, review requests, or requests for an opinion.
- Future calendar changes.
- Jira issues with Critical or Blocker priority.

### FYI

- Email marked `FYI`.
- Informational Slack discussions and announcements.
- Automated reports and non-actionable activity.
- Jira backlog items not promoted to an action tier.

## Step 4: Deduplicate

Merge items about the same topic across email, Slack, Jira, calendar, demos, and the forum.
Match on Jira issue keys, calendar titles, or the same person and topic in the same time
window. Keep the highest urgency and list all relevant sources. Keep Jira issues in the
complete backlog table even when they also appear in triage.

## Step 5: Write the dashboard

Create parent directories and overwrite `output.dashboard_path`. Use this structure:

```markdown
# Daily Brief — [TODAY]

**Generated:** [CURRENT TIME] [TIMEZONE]
**Sources:** Calendar ([N]), Gmail ([N]), Slack ([N]), Jira ([N]), Demos ([N]), Forum ([N])
**Scanning since:** [PREVIOUS BUSINESS DAY] 5:00 PM [TIMEZONE]

> [!summary]
> [One or two sentences summarizing volume, tone, and top actions.]

---

## 📅 Today's Schedule

## 🎬 Team Demos

## 🗣 Community Forum

## 📋 New Backlog Items

## 🔴 Immediate Action

## 🟡 Needs Response

## 🔵 FYI
```

Dashboard rules:

- Use real Unicode emoji, not shortcode names.
- Include a summary callout between metadata and the first separator.
- Use tables for schedules and backlog items.
- Link Jira keys to `<Jira instance URL>/browse/<KEY>`.
- Link Slack channel names to `<Slack workspace URL>/archives/<CHANNEL_ID>`.
- Mark escalation-labeled issues with `⚠️` and Critical/Blocker issues with `🔺`.
- Include scheduling conflicts and back-to-back meetings below the schedule.
- Do not duplicate demos in the general Slack FYI section.
- Include source-specific citations such as a person and channel, not generic “Slack”.
- Keep each triage item to one or two sentences.
- Show an explicit no-items message for empty sections.

After writing the dashboard, write `output.state_path`:

```json
{
  "last_run_unix": 0,
  "last_run_iso": "<CURRENT_ISO_8601_TIMESTAMP>"
}
```

Replace `0` with the current Unix timestamp at dashboard-generation time.

## Step 6: Present the result

Display the generated dashboard contents directly in the conversation.

## Error handling

- If a source worker fails, note the specific source and continue with the others.
- If Jira fails, say `Jira scan failed — check the required mcp-atlassian server.`
- If the state file is unreadable, use a 24-hour demos fallback and note it.
- If all workers fail, write an error dashboard and tell the user to verify the configured
  MCP servers.

Schedule this workflow through the hosting client's scheduler or automation features.
