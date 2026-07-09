# Project Context

## Purpose

`openspec-superpower-change` is the single change-control entry gate for AI-assisted development. It coordinates project `AGENTS.md`, OpenSpec contracts, Superpowers execution discipline, evidence gates, external-agent collaboration, and completion verification.

## Conventions

- Keep `SKILL.md` concise and route detail to `references/`.
- Treat trigger scope, OpenSpec/Superpowers boundaries, evidence signoff, and completion rules as Major self-evolution.
- Preserve a lightweight path for non-behavioral work.
- Do not weaken approval, review, verification, backup, rollback, or user-control boundaries.
- Use Python standard-library tests where possible and do not add runtime dependencies for validation.

## Validation

- Run `quick_validate.py` with a Python interpreter that provides PyYAML.
- Run `scripts/validate_core_gates.py` and the repository `unittest` suite.
- For Major self-evolution, run routing and lifecycle forward-tests before completion.
