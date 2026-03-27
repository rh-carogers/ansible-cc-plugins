# Ansible Claude Code Plugins

A Claude Code marketplace of reusable plugins for Ansible teams.

## Available Plugins

| Plugin              | Description                                                            | Version |
| ------------------- | ---------------------------------------------------------------------- | ------- |
| ansible-agile-coach | Agile product ownership coaching and user story expertise              | 1.0.0   |
| doc-tools           | General-purpose document summarization into AI-agent-friendly markdown | 1.1.0   |

## Installation

```bash
claude plugin marketplace add git@github-ansible:rh-carogers/ansible-cc-plugins.git
claude plugin install <plugin-name>@ansible-cc-plugins --scope user
```
