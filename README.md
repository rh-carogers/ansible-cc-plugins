# Ansible Claude Code Plugins

A Claude Code marketplace of reusable plugins for Ansible teams.

## Available Plugins

| Plugin              | Description                                                            | Version |
| ------------------- | ---------------------------------------------------------------------- | ------- |
| ansible-agile-coach | Agile coaching and product ownership guidance for Ansible teams        | 1.2.0   |
| ansible-jira-expert | Jira specialist agent for searching, managing, and analyzing issues    | 1.1.0   |
| doc-tools           | General-purpose document summarization into AI-agent-friendly markdown | 1.1.1   |

## Installation

```bash
claude plugin marketplace add git@github.com:rh-carogers/ansible-cc-plugins.git
claude plugin install <plugin-name>@ansible-cc-plugins --scope user
```
