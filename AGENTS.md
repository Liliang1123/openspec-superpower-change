# AGENTS.md

## Project positioning

`openspec-superpower-change` is a project-level AI development change gate, not an ordinary SDD workflow.

## Required behavior for agents

- Read `SKILL.md` before changing this project.
- Use Self-Evolution mode when modifying this skill itself.
- Create a backup before self-evolution changes.
- Treat trigger scope, OpenSpec boundaries, Superpowers boundaries, Step Evidence Gate signoff conditions, and completion-claim rules as Major self-evolution. Major changes require OpenSpec approval before implementation.
- Do not weaken Non-negotiables.
- Do not push without explicit user approval.

## Validation

Run before completion:

```bash
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 scripts/validate_core_gates.py .
```

## Sync

Read `references/sync-checklist.md` before syncing changes between the local runtime skill and this open-source project.
