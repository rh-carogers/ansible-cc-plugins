# ansible-jira-expert

Jira specialist agent for searching, managing, and analyzing issues.

## Components

- **Agent: jira-operator** — Searches, creates, updates, and summarizes Jira issues
- **Skill: jira-helper** — Expert guidance on Jira workflows, issue types, backlog prioritization, and escalation processes

## Prerequisites

Create `~/.env.atlassian` with your Jira credentials. See [mcp-atlassian docs](https://github.com/sooperset/mcp-atlassian) for the required format.

## Installation

```bash
claude plugin install ansible-jira-expert@ansible-cc-plugins --scope user
```
