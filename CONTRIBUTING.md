# Contributing

Thanks for improving `pushback`.

The goal is not to make Codex negative. The goal is to make Codex more honest when agreement would be misleading.

## Good Changes

- Add sharper rules for common failure modes.
- Improve examples with realistic prompts.
- Reduce vague wording.
- Make the skill easier to install or validate.
- Improve compatibility with Codex skill conventions.

## Avoid

- Making the skill rude or performatively contrarian.
- Adding large essays to `SKILL.md`; runtime instructions should stay compact.
- Adding objections that are not tied to evidence, risk, or decision quality.
- Mixing open-source project docs into the skill folder itself.

## Validate Before Opening a PR

Run:

```bash
python tests/validate_skill.py .
```

If you have local Codex skill creator tools:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\pushback"
```
