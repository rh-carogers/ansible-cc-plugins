# Ansible Agent Plugins

A marketplace of reusable skills for Ansible teams. The repository provides a portable
Agent Plugins package that can be discovered by Claude and Codex.

## Available plugins

| Plugin | Description | Version |
| --- | --- | --- |
| `ansible-agile-coach` | Agile coaching and product ownership guidance for Ansible teams | 1.2.0 |
| `ansible-jira-expert` | Jira workflow guidance and MCP-backed issue search, analysis, and management | 1.1.3 |
| `daily-brief` | Daily briefing dashboard from calendar, email, Slack, Jira, and community sources | 1.0.1 |
| `doc-tools` | Summarize documents into structured, AI-agent-friendly Markdown | 1.1.1 |

## Marketplace manifests

- Claude marketplace: `.claude-plugin/marketplace.json`
- Codex marketplace: `.agents/plugins/marketplace.json`

The portable plugin manifests are at the root of each plugin directory. Shared skills are
the canonical behavior for both clients; no client-specific agents or MCP configuration is
bundled in the portable packages.

## Installation

Claude can add this repository as a marketplace and install the plugins with its normal
marketplace workflow:

```bash
claude plugin marketplace add git@github.com:rh-carogers/ansible-cc-plugins.git
claude plugin install <plugin-name>@ansible-cc-plugins --scope user
```

Codex uses the local marketplace manifest at `.agents/plugins/marketplace.json` through its
plugin installation flow.

## External MCP dependencies

The Jira plugin requires an externally configured MCP server named `mcp-atlassian` for
every user. Configure it through the hosting agent's private MCP settings. The plugin does
not include credentials or an environment file.

See the upstream [MCP Atlassian installation](https://github.com/sooperset/mcp-atlassian/blob/main/docs/installation.mdx)
and [authentication](https://github.com/sooperset/mcp-atlassian/blob/main/docs/authentication.mdx)
documentation, plus the [Codex MCP configuration guide](https://learn.chatgpt.com/docs/extend/mcp)
when using Codex.

The daily brief also uses configured Google Workspace and Slack MCP servers. See the
plugin's README for links to those upstream projects.

## Portability

See [PORTABILITY.md](PORTABILITY.md) for the migration report, retained legacy behavior,
external setup requirements, and validation results.
