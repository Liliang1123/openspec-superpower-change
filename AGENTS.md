# AGENTS.md

## Project positioning

`openspec-superpower-change` is a project-level AI development change gate, not an ordinary SDD workflow.

## Required behavior for agents

- Read `SKILL.md` before changing this project.
- Before completion after correction/Review history, or when asked to archive and
  distill a session, read `docs/engineering-invariants.md` and
  `references/project-learning-closeout.md`.
- Use Self-Evolution mode when modifying this skill itself.
- Create a backup before self-evolution changes.
- Treat trigger scope, OpenSpec boundaries, Superpowers boundaries, Step Evidence Gate signoff conditions, and completion-claim rules as Major self-evolution. Major changes require OpenSpec approval before implementation.
- Do not weaken Non-negotiables.
- Do not push without explicit user approval.

## Validation

Run before completion:

```bash
"${PYTHON_BIN:-python3}" "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

`quick_validate.py` requires PyYAML; choose `PYTHON_BIN` from an environment that provides it. Project validators and tests must also pass with the dependency-free fallback.

## Sync

Read `references/sync-checklist.md` before syncing changes between the local runtime skill and this open-source project.
