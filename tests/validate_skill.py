from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str, errors: list[str]) -> dict[str, str]:
    match = re.match(r"^---\r?\n(?P<body>.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not match:
        fail(errors, "SKILL.md must start with YAML frontmatter delimited by ---")
        return {}

    result: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(errors, f"Invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    skill_dir = root / "skills" / "pushback"
    skill_md = skill_dir / "SKILL.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"

    errors: list[str] = []

    if not skill_md.exists():
        fail(errors, f"Missing {skill_md}")
    if not openai_yaml.exists():
        fail(errors, f"Missing {openai_yaml}")
    if not (root / "README.md").exists():
        fail(errors, "Missing README.md")
    if not (root / "LICENSE").exists():
        fail(errors, "Missing LICENSE")
    if not (root / "assets" / "banner.svg").exists():
        fail(errors, "Missing assets/banner.svg")
    if not (root / "assets" / "mark.svg").exists():
        fail(errors, "Missing assets/mark.svg")
    if not (root / "assets" / "social-card.svg").exists():
        fail(errors, "Missing assets/social-card.svg")
    if not (root / "prompts" / "universal.md").exists():
        fail(errors, "Missing prompts/universal.md")
    if not (root / "demo" / "before-after.md").exists():
        fail(errors, "Missing demo/before-after.md")
    if not (root / "launch" / "social-posts.md").exists():
        fail(errors, "Missing launch/social-posts.md")
    if not (root / "launch" / "submission-targets.md").exists():
        fail(errors, "Missing launch/submission-targets.md")

    required_adapter_files = [
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        ".hermes.md",
        ".cursorrules",
        ".windsurfrules",
        "CONVENTIONS.md",
        "SOUL.md",
        ".cursor/rules/pushback.mdc",
        ".clinerules/pushback.md",
        ".roo/rules/pushback.md",
        ".kilo/rules/pushback.md",
        "kilo.jsonc",
        ".github/copilot-instructions.md",
        "rules/pushback.md",
        "scripts/install.py",
        "docs/agent-support.md",
    ]
    for relative_path in required_adapter_files:
        if not (root / relative_path).exists():
            fail(errors, f"Missing adapter file: {relative_path}")

    if skill_md.exists():
        text = skill_md.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text, errors)
        if frontmatter.get("name") != "pushback":
            fail(errors, "Frontmatter name must be pushback")
        description = frontmatter.get("description", "")
        if len(description) < 140:
            fail(errors, "Frontmatter description should be specific enough to trigger correctly")
        required_phrases = [
            "reflexive agreement",
            "$pushback",
            "push back",
            "test assumptions",
        ]
        for phrase in required_phrases:
            if phrase not in text:
                fail(errors, f"SKILL.md missing required phrase: {phrase}")
        if "TODO" in text:
            fail(errors, "SKILL.md still contains TODO")
        if len(text.splitlines()) > 180:
            fail(errors, "SKILL.md is getting too long for a compact runtime skill")

    if openai_yaml.exists():
        ui_text = openai_yaml.read_text(encoding="utf-8")
        if "$pushback" not in ui_text:
            fail(errors, "agents/openai.yaml default_prompt should mention $pushback")
        if "Challenge weak assumptions" not in ui_text:
            fail(errors, "agents/openai.yaml should keep the current short_description positioning")

    readme = root / "README.md"
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        if "assets/banner.svg" not in readme_text:
            fail(errors, "README.md should display the visual banner")
        if "github/actions/workflow/status" not in readme_text:
            fail(errors, "README.md should show the validation badge")
        if "prompts/universal.md" not in readme_text:
            fail(errors, "README.md should link the universal prompt")
        if "Your AI assistant agrees too much" not in readme_text:
            fail(errors, "README.md should lead with the shareable hook")
        if "docs/agent-support.md" not in readme_text:
            fail(errors, "README.md should link agent support docs")
        for agent_name in ["Claude Code", "Cursor", "Gemini CLI", "GitHub Copilot", "Cline", "Roo Code", "Kilo Code", "Hermes", "OpenCode", "OpenClaw"]:
            if agent_name not in readme_text:
                fail(errors, f"README.md missing agent mention: {agent_name}")

    universal_prompt = root / "prompts" / "universal.md"
    if universal_prompt.exists():
        prompt_text = universal_prompt.read_text(encoding="utf-8")
        for phrase in ["Pushback mode", "Separate \"this can be done\" from \"this should be done\"", "Do not be rude"]:
            if phrase not in prompt_text:
                fail(errors, f"Universal prompt missing phrase: {phrase}")

    canonical_rule = root / "rules" / "pushback.md"
    if canonical_rule.exists():
        rule_text = canonical_rule.read_text(encoding="utf-8")
        for phrase in ["Pushback Mode", "truth-seeking", "Pause before destructive commands"]:
            if phrase not in rule_text:
                fail(errors, f"Canonical rule missing phrase: {phrase}")

    for relative_path in required_adapter_files:
        if relative_path.endswith((".md", ".mdc", ".md")) and (root / relative_path).exists():
            text = (root / relative_path).read_text(encoding="utf-8")
            if "Pushback" not in text:
                fail(errors, f"Adapter should mention Pushback: {relative_path}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: pushback project looks ready to publish")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
