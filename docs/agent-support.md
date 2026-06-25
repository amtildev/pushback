# Agent Support

Pushback is a multi-agent rule pack. The Codex skill remains available, but the repo now includes direct adapters for other coding agents and editors.

## Fast Install

Install every supported adapter into another project:

```bash
python scripts/install.py --target /path/to/project --agents all
```

Install only selected agents:

```bash
python scripts/install.py --target /path/to/project --agents claude cursor gemini copilot
```

Use `--force` to overwrite existing instruction files.

## Supported Agents And Files

| Agent or tool | Files provided | Notes |
|---|---|---|
| Codex | `AGENTS.md`, `skills/pushback/` | Use `AGENTS.md` for project rules or install the Codex skill for `$pushback`. |
| AGENTS.md-compatible agents | `AGENTS.md` | Works with agents that read the AGENTS.md standard. |
| OpenCode | `AGENTS.md` | OpenCode documents `AGENTS.md` as its custom instruction file. |
| Hermes Agent | `.hermes.md`, `AGENTS.md`, `rules/pushback.md` | Hermes loads `.hermes.md` first, then AGENTS-style context files. |
| OpenClaw-style agents | `AGENTS.md`, `SOUL.md`, `rules/pushback.md` | `AGENTS.md` is the project rule layer; `SOUL.md` is included for personality-style setups. |
| Claude Code | `CLAUDE.md`, `rules/pushback.md` | Project-level Claude memory file. |
| Cursor | `.cursor/rules/pushback.mdc`, `.cursorrules`, `rules/pushback.md` | Provides both current MDC project rule and legacy `.cursorrules`. |
| Gemini CLI | `GEMINI.md`, `rules/pushback.md` | Gemini context file. |
| GitHub Copilot | `.github/copilot-instructions.md`, `rules/pushback.md` | Repository custom instructions for Copilot Chat and coding agent surfaces. |
| Cline | `.clinerules/pushback.md`, `AGENTS.md`, `rules/pushback.md` | Cline reads `.clinerules/` and also supports `AGENTS.md`. |
| Roo Code | `.roo/rules/pushback.md`, `AGENTS.md`, `rules/pushback.md` | Roo reads `.roo/rules/` and also supports `AGENTS.md`. |
| Kilo Code / KiloClaw | `kilo.jsonc`, `.kilo/rules/pushback.md`, `rules/pushback.md` | `kilo.jsonc` points Kilo at the rule file. |
| Windsurf | `.windsurfrules`, `rules/pushback.md` | Workspace rules for Cascade/Windsurf-style agents. |
| Aider | `CONVENTIONS.md`, `rules/pushback.md` | Load with `/read CONVENTIONS.md` or `aider --read CONVENTIONS.md`. |

## Compatibility Notes

- Prefer `AGENTS.md` when you want one file that many agents can read.
- Prefer tool-specific files when a tool has a strong native convention, such as `CLAUDE.md`, `GEMINI.md`, or `.cursor/rules/*.mdc`.
- If a tool is not listed, use [prompts/universal.md](../prompts/universal.md) as a system prompt, project rule, or custom instruction.
- These files are guidance, not a hard sandbox. Keep destructive actions behind explicit confirmation and use read-only inspection first.

## Reference Docs

- Codex and `AGENTS.md`: https://developers.openai.com/codex/guides/agents-md
- AGENTS.md standard: https://agents.md/
- Claude Code memory: https://docs.anthropic.com/en/docs/claude-code/memory
- Cursor rules: https://cursor.com/docs/rules
- Gemini CLI context files: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- Hermes context files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files
- Cline rules: https://docs.cline.bot/customization/cline-rules
- Roo Code custom instructions: https://roocodeinc.github.io/Roo-Code/features/custom-instructions/
- Kilo custom rules: https://kilo.ai/docs/customize/custom-rules
- GitHub Copilot custom instructions: https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- Aider conventions: https://aider.chat/docs/usage/conventions.html
