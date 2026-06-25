# Pushback

Stop your coding agent from nodding along.

`pushback` is a Codex skill that makes an agent challenge weak assumptions before agreeing. It is for moments when the default "helpful assistant" behavior is too agreeable: product ideas, architecture decisions, risky shell commands, live changes, pricing calls, launches, and any plan that needs a real counterparty.

## The Problem

LLMs are often tuned to be helpful, polite, and cooperative. That is useful until the assistant starts validating a bad premise, skipping the hard question, or saying "great idea" before inspecting the evidence.

This skill gives Codex a compact operating protocol:

- state a verdict instead of flattering the premise
- surface hidden assumptions
- name concrete risks
- separate "I can do this" from "this is a good idea"
- offer a better path when the request is weak
- slow down before destructive, expensive, or public actions

It does not make the assistant hostile. It makes disagreement useful.

## Install

Clone or download this repo, then copy the skill folder into your Codex skills directory.

PowerShell:

```powershell
Copy-Item -Recurse -Force .\skills\pushback "$env:USERPROFILE\.codex\skills\pushback"
```

Bash:

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/pushback ~/.codex/skills/pushback
```

If you use a Codex skill installer that supports GitHub paths, point it at:

```text
skills/pushback
```

## Use

Invoke it directly in a Codex prompt:

```text
Use $pushback to sanity-check this plan before implementing it.
```

```text
Use $pushback. Be direct: what is weak about this product idea?
```

```text
Use $pushback before touching production. Inspect first, then tell me the risk.
```

## What Changes

Without the skill:

```text
This sounds like a strong direction. I can implement it.
```

With the skill:

```text
Partly. The implementation is possible, but the premise is weak because the current repo has no evidence that users need this flow. The smallest useful test is to instrument the existing path before adding a new one.
```

## Good Use Cases

- Product and startup idea evaluation
- Technical architecture review
- Code-change sanity checks
- Security-sensitive or destructive operations
- Pricing, launch, or monetization decisions
- Debugging plans where the first theory may be wrong
- Any prompt where you want the assistant to say "no" when needed

## Not For

- Forcing the agent to be rude
- Generating objections for their own sake
- Bypassing model safety behavior
- Replacing real domain experts for legal, medical, financial, or security decisions

## Project Layout

```text
pushback/
  skills/pushback/
    SKILL.md
    agents/openai.yaml
  examples/
    prompts.md
  tests/
    validate_skill.py
```

## Validate

Run the project validator:

```bash
python tests/validate_skill.py .
```

If you have the Codex skill creator tools locally, you can also run:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\pushback"
```

## Contributing

Good contributions make the skill more truth-seeking without making it abrasive. Improve specific decision rules, add realistic examples, or tighten wording that causes false pushback.

## License

MIT. See [LICENSE](LICENSE).
