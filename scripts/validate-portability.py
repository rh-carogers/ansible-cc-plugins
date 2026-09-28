#!/usr/bin/env python3
"""Validate the repository's portable Agent Plugins structure."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PLUGIN_NAMES = {
    "ansible-agile-coach",
    "ansible-jira-expert",
    "daily-brief",
    "doc-tools",
}
CLIENT_MARKERS = (
    "mcp__",
    "subagent_type",
    "user-invocable",
    ".claude",
    "CLAUDE_PLUGIN_ROOT",
    "Agent tool",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text())
    except FileNotFoundError:
        fail(f"missing JSON file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"JSON root is not an object: {path.relative_to(ROOT)}")
    return value


def check_marketplace(path: Path, codex: bool) -> None:
    data = load_json(path)
    plugins = data.get("plugins")
    if not isinstance(plugins, list):
        fail(f"{path.relative_to(ROOT)} has no plugins list")

    names = set()
    for entry in plugins:
        if not isinstance(entry, dict):
            fail(f"non-object marketplace entry in {path.relative_to(ROOT)}")
        name = entry.get("name")
        names.add(name)
        if codex:
            source = entry.get("source")
            if not isinstance(source, dict) or source.get("source") != "local":
                fail(f"Codex entry {name!r} does not use a local source")
            if source.get("path") != f"./plugins/{name}":
                fail(f"Codex entry {name!r} has an unexpected source path")
        else:
            if entry.get("source") != f"./plugins/{name}":
                fail(f"Claude entry {name!r} has an unexpected source path")
    if names != PLUGIN_NAMES:
        fail(f"{path.relative_to(ROOT)} lists {sorted(names)}, expected {sorted(PLUGIN_NAMES)}")


def parse_frontmatter(path: Path) -> tuple[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        fail(f"skill has no YAML frontmatter: {path.relative_to(ROOT)}")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        fail(f"skill frontmatter is not closed: {path.relative_to(ROOT)}")
    frontmatter = parts[0][4:]

    lines = frontmatter.splitlines()
    name = next((line.split(":", 1)[1].strip() for line in lines if line.startswith("name:")), "")
    if not name:
        fail(f"skill has no name: {path.relative_to(ROOT)}")

    description_index = next((i for i, line in enumerate(lines) if line.startswith("description:")), None)
    if description_index is None:
        fail(f"skill has no description: {path.relative_to(ROOT)}")
    first = lines[description_index].split(":", 1)[1].strip()
    description_lines = [] if first in {"|", ">", "|-", ">-", "|+", ">+"} else [first]
    if not description_lines:
        for line in lines[description_index + 1 :]:
            if line and not line[0].isspace():
                break
            description_lines.append(line.strip())
    description = " ".join(part for part in description_lines if part)
    if len(description) > 1024:
        fail(f"skill description exceeds 1024 characters: {path.relative_to(ROOT)}")
    return name, description


def check_skills() -> None:
    for skill_path in sorted(ROOT.glob("plugins/*/skills/*/SKILL.md")):
        expected_name = skill_path.parent.name
        name, _ = parse_frontmatter(skill_path)
        if name != expected_name:
            fail(f"skill name {name!r} does not match directory {expected_name!r}")
        text = skill_path.read_text()
        for marker in CLIENT_MARKERS:
            if marker in text:
                fail(f"shared skill {skill_path.relative_to(ROOT)} contains client marker {marker!r}")


def check_plugins() -> None:
    for name in sorted(PLUGIN_NAMES):
        path = ROOT / "plugins" / name / "plugin.json"
        data = load_json(path)
        if data.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            fail(f"{path.relative_to(ROOT)} has the wrong Agent Plugins schema")
        if data.get("name") != name:
            fail(f"{path.relative_to(ROOT)} has the wrong plugin name")
        if not data.get("description"):
            fail(f"{path.relative_to(ROOT)} has no description")
        if "mcpServers" in data or "skills" in data or "agents" in data:
            fail(f"{path.relative_to(ROOT)} contains a non-portable component field")

        plugin_dir = path.parent
        if (plugin_dir / ".mcp.json").exists():
            fail(f"bundled Claude MCP configuration remains in {plugin_dir.relative_to(ROOT)}")
        if (plugin_dir / "agents").exists():
            fail(f"client-specific agents directory remains in {plugin_dir.relative_to(ROOT)}")


def main() -> int:
    check_marketplace(ROOT / ".claude-plugin/marketplace.json", codex=False)
    check_marketplace(ROOT / ".agents/plugins/marketplace.json", codex=True)
    check_plugins()
    check_skills()

    tracked = __import__("subprocess").run(
        ["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.splitlines()
    for filename in tracked:
        if not (ROOT / filename).exists():
            continue
        if filename.endswith(".env") or filename.endswith(".env.atlassian"):
            fail(f"tracked environment file found: {filename}")
        if re.search(r"(^|/)\.mcp\.json$", filename):
            fail(f"tracked MCP configuration found: {filename}")

    print("PASS: portable Agent Plugins structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
