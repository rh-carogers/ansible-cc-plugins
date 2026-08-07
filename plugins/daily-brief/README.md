# daily-brief

Daily briefing dashboard from calendar, email, Slack, Jira, and community sources. Scans your inbox, Slack channels, calendar, Jira backlog, team demos, and an optional community forum, then produces a triaged dashboard with items categorized as Immediate Action, Needs Response, or FYI.

## Prerequisites

This plugin requires three MCP servers to be configured in your Claude Code environment:

| MCP Server | Purpose | Setup |
|------------|---------|-------|
| [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | Calendar events, Gmail search | See repo README for auth setup |
| [slack-mcp](https://github.com/redhat-community-ai-tools/slack-mcp) | Channel history, message search, user identity | See repo README for token setup |
| [mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | Jira issue search | See repo README for credentials |

The Google Workspace and Slack MCP servers are required. The Jira MCP server is only needed if you configure the `jira` section in your config.

## Installation

```bash
claude plugin install daily-brief@ansible-cc-plugins --scope user
```

## Configuration

Copy the example config to your project directory:

```bash
cp ~/.claude/plugins/cache/*/daily-brief/config.example.yaml .claude/daily-brief.yaml
```

Edit `.claude/daily-brief.yaml` with your values. See `config.example.yaml` for detailed comments on each section.

### Required sections

None — every section is optional. The plugin gracefully skips any data source whose config section is missing. At minimum, you'll want `output` (to control where the dashboard is written) and at least one data source.

### Data sources

| Config section                         | What it scans                | Required MCP             |
| -------------------------------------- | ---------------------------- | ------------------------ |
| _(always runs)_                        | Unread Gmail                 | Google Workspace         |
| _(always runs)_                        | Today's calendar             | Google Workspace         |
| _(always runs)_                        | Slack DMs and @mentions      | Slack                    |
| `slack.team_channels`                  | Listed team Slack channels   | Slack                    |
| `slack.org_channels`                   | Listed org Slack channels    | Slack                    |
| `slack.demos_channel` + `team.members` | Demos posted by team members | Slack                    |
| `jira`                                 | New Jira backlog items       | mcp-atlassian            |
| `forum`                                | Community forum activity     | _(none — uses WebFetch)_ |

### Team roster

Define team members inline or point to an external YAML file:

```yaml
team:
  # Inline
  members:
    - name: "Jane Smith"
      slack_display_name: "Jane Smith"

  # Or external file
  roster_file: /path/to/roster.yaml
```

The external file can have either a top-level `members` list or a `teams[0].members` list, each with `name` and `slack_display_name` fields per entry.

## Usage

```
/daily-brief
```

The plugin writes a Markdown dashboard to the configured `output.dashboard_path` and displays it in the conversation.

## Output

The dashboard includes:

- Today's meeting schedule
- Team demos since last brief
- Community forum activity (if enabled)
- New Jira backlog items (if configured)
- Triaged items: Immediate Action, Needs Response, FYI
