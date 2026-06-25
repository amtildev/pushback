<div align="center">
  <img src="assets/banner.svg" alt="Pushback: truth-seeking mode for coding agents" width="100%">

  <p>
    <a href="https://github.com/AhmedAmtil-coder/pushback/actions/workflows/validate.yml"><img alt="Validation" src="https://img.shields.io/github/actions/workflow/status/AhmedAmtil-coder/pushback/validate.yml?branch=main&label=validation"></a>
    <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/AhmedAmtil-coder/pushback"></a>
    <img alt="Codex skill" src="https://img.shields.io/badge/Codex-skill-69E0B5">
    <img alt="Invoke with $pushback" src="https://img.shields.io/badge/invoke-%24pushback-E8C547">
  </p>

  <p><strong>Truth-seeking mode for coding agents.</strong></p>
  <p>Make Codex challenge weak assumptions before it agrees, edits, deletes, buys, ships, or publishes.</p>
</div>

## Why Pushback Exists

LLMs are tuned to be helpful, polite, and cooperative. That is useful until the assistant validates a bad premise, skips the hard question, or says "great idea" before checking the evidence.

`pushback` gives Codex a compact counterparty protocol:

| Instead of this | Pushback does this |
|---|---|
| "Sounds good, I will implement it." | Separates feasibility from judgment. |
| "Great idea." | Tests the hidden assumption first. |
| "I can do that." | Names the risk before action. |
| "Here is the plan." | Offers the smaller, safer, sharper path. |

> [!TIP]
> Use `$pushback` when agreement would be cheap but being wrong would be expensive.

## Install

Clone or download this repo, then copy the skill folder into your Codex skills directory.

```powershell
Copy-Item -Recurse -Force .\skills\pushback "$env:USERPROFILE\.codex\skills\pushback"
```

On macOS or Linux:

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/pushback ~/.codex/skills/pushback
```

If your Codex skill installer supports GitHub paths, point it at:

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

| Default assistant | With Pushback |
|---|---|
| "This sounds like a strong direction. I can implement it." | "Partly. The implementation is possible, but the premise is weak because the repo has no evidence users need this flow. The smallest useful test is to instrument the existing path before adding a new one." |

## Good Use Cases

| Area | What Pushback should catch |
|---|---|
| Product ideas | Distribution gaps, fake urgency, weak demand signals |
| Architecture | Complexity, lock-in, migration risk, maintainability cost |
| Code changes | Edge cases, regressions, missing tests, pattern drift |
| Risky operations | Destructive commands, live systems, secrets, recurring billing |
| Launch plans | Unclear audience, weak proof, vague success criteria |

## Not For

- Making the agent rude
- Generating objections for their own sake
- Bypassing model safety behavior
- Replacing real domain experts for legal, medical, financial, or security decisions

## Project Layout

```text
pushback/
  assets/
    banner.svg
    mark.svg
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
