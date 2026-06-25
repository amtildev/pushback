# Prompt Examples

Use these examples as starting points when you want Codex to challenge your thinking instead of agreeing too quickly.

## Product Judgment

```text
Use $pushback to evaluate this idea. I want to build a browser extension that rewrites every webpage in my writing style. Is this actually worth building?
```

Expected behavior:

- give a viability verdict
- name the likely adoption or distribution problem
- suggest the smallest useful validation step
- state what evidence would change the verdict

## Code Change

```text
Use $pushback before implementing this. I want to replace our current auth flow with a custom token system.
```

Expected behavior:

- inspect the current auth code first
- separate feasibility from advisability
- identify security and maintenance risks
- recommend a safer path if the premise is weak

## Risky Operation

```text
Use $pushback. I want to delete these old database rows in production because they look unused.
```

Expected behavior:

- pause before destructive action
- ask for explicit confirmation only after stating concrete risk
- prefer read-only inspection and backup verification first

## Factual Claim

```text
Use $pushback. I heard this API is deprecated, so we should migrate today.
```

Expected behavior:

- verify current facts before accepting the claim
- distinguish source evidence from inference
- explain whether immediate migration is justified

## Planning

```text
Use $pushback to review this launch plan and tell me what will probably fail.
```

Expected behavior:

- lead with the weakest assumption
- identify the opportunity cost
- propose a smaller test or sharper success condition
