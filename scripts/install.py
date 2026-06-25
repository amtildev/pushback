from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

AGENT_FILES: dict[str, list[str]] = {
    "agents-md": ["AGENTS.md", "rules/pushback.md"],
    "codex": ["AGENTS.md", "rules/pushback.md"],
    "opencode": ["AGENTS.md", "rules/pushback.md"],
    "hermes": [".hermes.md", "AGENTS.md", "rules/pushback.md"],
    "openclaw": ["AGENTS.md", "SOUL.md", "rules/pushback.md"],
    "claude": ["CLAUDE.md", "rules/pushback.md"],
    "cursor": [".cursor/rules/pushback.mdc", ".cursorrules", "rules/pushback.md"],
    "gemini": ["GEMINI.md", "rules/pushback.md"],
    "copilot": [".github/copilot-instructions.md", "rules/pushback.md"],
    "cline": [".clinerules/pushback.md", "AGENTS.md", "rules/pushback.md"],
    "roo": [".roo/rules/pushback.md", "AGENTS.md", "rules/pushback.md"],
    "kilo": ["kilo.jsonc", ".kilo/rules/pushback.md", "rules/pushback.md"],
    "kiloclaw": ["kilo.jsonc", ".kilo/rules/pushback.md", "AGENTS.md", "SOUL.md", "rules/pushback.md"],
    "windsurf": [".windsurfrules", "rules/pushback.md"],
    "aider": ["CONVENTIONS.md", "rules/pushback.md"],
}


def selected_files(agent_names: list[str]) -> list[str]:
    names = [name.lower() for name in agent_names]
    if "all" in names:
        names = sorted(AGENT_FILES)

    unknown = [name for name in names if name not in AGENT_FILES]
    if unknown:
        options = ", ".join(["all", *sorted(AGENT_FILES)])
        raise SystemExit(f"Unknown agent(s): {', '.join(unknown)}. Options: {options}")

    files: list[str] = []
    for name in names:
        for file_name in AGENT_FILES[name]:
            if file_name not in files:
                files.append(file_name)
    return files


def copy_file(relative_path: str, target: Path, force: bool) -> str:
    source = ROOT / relative_path
    destination = target / relative_path

    if not source.exists():
        raise FileNotFoundError(f"Missing source template: {source}")

    if destination.exists():
        if destination.read_bytes() == source.read_bytes():
            return f"same  {relative_path}"
        if not force:
            return f"skip  {relative_path} (exists; rerun with --force to overwrite)"

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    return f"write {relative_path}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Install Pushback rule files into an AI-agent project.")
    parser.add_argument("--target", default=".", help="Target project directory. Defaults to the current directory.")
    parser.add_argument(
        "--agents",
        nargs="+",
        default=["all"],
        help="Agents to install for. Use all, or names like claude cursor gemini copilot cline roo kilo hermes openclaw.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--list", action="store_true", help="List supported agent names and exit.")
    args = parser.parse_args()

    if args.list:
        print("all")
        for name in sorted(AGENT_FILES):
            print(name)
        return 0

    target = Path(args.target).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)

    files = selected_files(args.agents)
    print(f"Installing Pushback into {target}")
    for file_name in files:
        print(copy_file(file_name, target, args.force))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
