# Portability migration report

## Scope

This repository was migrated from a Claude Code marketplace to a portable Agent Plugins
package while retaining a Claude marketplace manifest for existing users.

The migration followed the [Agent Plugin migration skill](https://github.com/agentplugins/agent-plugins-example/blob/main/skills/migrate-agent-plugin/SKILL.md)
and the [Agent Plugins specification](https://agent-plugins.org/specification).

## Artifact mapping

| Source artifact | Portable result |
| --- | --- |
| Claude marketplace manifest | Retained at `.claude-plugin/marketplace.json` |
| Codex marketplace | Added at `.agents/plugins/marketplace.json` |
| Claude plugin manifests | Retained under each `.claude-plugin/` directory |
| Portable plugin manifests | Added as root `plugin.json` files |
| Claude skills | Normalized as shared Agent Skills under `skills/` |
| Claude MCP configuration | Removed from the Jira plugin |
| Claude agent definitions | Removed from the plugin package after their role guidance was moved into shared skills |

## External MCP dependency

The Jira plugin requires an externally configured MCP server named `mcp-atlassian` for
every user. No credentials, `.env` file, or MCP configuration is shipped in this
repository.

Use the upstream [installation](https://github.com/sooperset/mcp-atlassian/blob/main/docs/installation.mdx)
and [authentication](https://github.com/sooperset/mcp-atlassian/blob/main/docs/authentication.mdx)
documentation. Codex users can also consult the [Codex MCP configuration guide](https://learn.chatgpt.com/docs/extend/mcp).

## Subagents

The portable skills describe focused delegation by role without naming a client-specific
agent or generated tool identifier. Claude and Codex use their native subagent mechanisms.
The shared skills also contain the worker rules needed to complete the task directly when
delegation is unavailable.

## Validation

Run the dependency-free structural validator from the repository root:

```bash
python3 scripts/validate-portability.py
```

The validator checks both marketplace manifests, all portable plugin manifests, skill
metadata limits, removal of bundled credentials and MCP files, and absence of
client-specific orchestration markers in shared skills.

Current structural result: PASS on 2026-09-28.

User-reported Codex smoke test result: PASS on 2026-09-28.

Manual smoke tests remain necessary in both Claude and Codex with the required external
MCP servers configured. In particular, verify Jira access, daily-brief source collection,
document summarization delegation, and direct-execution fallbacks.
