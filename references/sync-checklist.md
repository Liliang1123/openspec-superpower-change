# Sync Checklist

Use this checklist whenever `openspec-superpower-change` changes in either the local runtime skill or the open-source project.

## Scope

This checklist applies to:

- Patch self-evolution when the change should be shared across local/open-source copies;
- all Minor self-evolution changes;
- all Major self-evolution changes after OpenSpec approval;
- any change touching `SKILL.md`, `references/`, `scripts/`, `templates/`, or examples.

## Required paths

Set these for the current checkout instead of hardcoding a user's home path:

```bash
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
OPENSPEC_SKILL_SOURCE="${OPENSPEC_SKILL_SOURCE:-$PWD}"
BRIEF_SKILL_SOURCE="${BRIEF_SKILL_SOURCE:-$(dirname "$PWD")/codex-brief-antigravity-review}"
```

## Pre-change checklist

1. Confirm the change level: Patch, Minor, or Major.
2. If Major, stop and require OpenSpec approval before implementation.
3. Confirm the intended source of truth for this change: local runtime, open-source project, or both.
4. Create timestamped temporary structured backups before editing both affected trees.
5. Check the open-source repo is clean before editing:

```bash
git -C "$OPENSPEC_SKILL_SOURCE" status -sb
```

## Sync checklist

1. Apply the change to the intended primary tree.
2. Apply the same logical change to the secondary tree unless explicitly out of scope.
3. Compare key files when both trees should stay aligned:
   - `SKILL.md`
   - `references/handoff-contract.md`
   - `references/superpowers-adapter.md`
   - `references/self-evolution-rule.md`
   - `references/step-evidence-gate.md`
   - `references/sync-checklist.md`
   - `scripts/validate_core_gates.py`
   - companion Brief `SKILL.md`, evidence templates, Handoff Contract, and
     `scripts/validate_templates.py`
4. Do not force byte-for-byte equality when local runtime needs stricter execution details than the open-source project.
5. Do require logical equality for:
   - Non-negotiables;
   - OpenSpec approval boundary;
   - Superpowers planning boundary;
   - Step Evidence Gate signoff boundary;
   - Self-Evolution Patch/Minor/Major classification;
   - backup, validation, forward-test, and no-push-without-approval rules.

## Validation checklist

Run for both local and open-source copies when present:

```bash
"${PYTHON_BIN:-python3}" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" "$CODEX_HOME/skills/openspec-superpower-change"
PYTHONDONTWRITEBYTECODE=1 python3 "$CODEX_HOME/skills/openspec-superpower-change/scripts/validate_core_gates.py" "$CODEX_HOME/skills/openspec-superpower-change"
"${PYTHON_BIN:-python3}" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" "$OPENSPEC_SKILL_SOURCE"
PYTHONDONTWRITEBYTECODE=1 python3 "$OPENSPEC_SKILL_SOURCE/scripts/validate_core_gates.py" "$OPENSPEC_SKILL_SOURCE"
"${PYTHON_BIN:-python3}" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" "$CODEX_HOME/skills/codex-brief-antigravity-review"
PYTHONDONTWRITEBYTECODE=1 python3 "$CODEX_HOME/skills/codex-brief-antigravity-review/scripts/validate_templates.py" "$CODEX_HOME/skills/codex-brief-antigravity-review"
"${PYTHON_BIN:-python3}" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" "$BRIEF_SKILL_SOURCE"
PYTHONDONTWRITEBYTECODE=1 python3 "$BRIEF_SKILL_SOURCE/scripts/validate_templates.py" "$BRIEF_SKILL_SOURCE"
```

Set `PYTHON_BIN` to an interpreter with PyYAML. Run both repositories'
standard-library `unittest` suites with default `python3` to exercise fallback behavior.

## Forward-test checklist

Run forward-tests when:

- the change is Minor and affects routing, examples, references, scripts, or validation behavior;
- the change is Major after approval;
- reviewers explicitly request it.

Minimum scenarios:

1. Review-only should not modify files.
2. Direct bugfix should not require OpenSpec and must verify.
3. OpenSpec-required new behavior should stop before implementation.
4. Major self-evolution weakening request must require OpenSpec and refuse direct implementation.
5. Minor self-evolution in a temporary copy should backup, edit, validate, and report.

## Backup cleanup checklist

After validation and required forward-tests pass:

1. Remove temporary structured backups created for the update.
2. Remove `.bak.*` files from the runtime skill and open-source working trees.
3. Remove discoverable `*.backup*` skill directories from `$CODEX_HOME/skills/`.
4. Keep a temporary backup only when validation fails, rollback is pending, or the
   user explicitly asks to retain it.
5. Treat the open-source git history as the long-term version history; do not
   keep parallel backup histories in skill discovery paths.

## Git checklist for open-source sync

1. Review diff:

```bash
git -C "$OPENSPEC_SKILL_SOURCE" diff --stat
git -C "$OPENSPEC_SKILL_SOURCE" diff
```

2. Commit with a clear message.
3. Push only after explicit user approval.
4. Report commit hash and validation results.

## Report checklist

Every sync report must include:

- change level;
- source of truth;
- temporary backup paths and cleanup result;
- changed files in local runtime skill;
- changed files in open-source project;
- validation commands and results;
- forward-test result when run;
- residual risks;
- rollback path.
