# Sync Checklist

Use this checklist whenever `openspec-superpower-change` changes in either the local runtime skill or the open-source project.

## Scope

This checklist applies to:

- Patch self-evolution when the change should be shared across local/open-source copies;
- all Minor self-evolution changes;
- all Major self-evolution changes after OpenSpec approval;
- any change touching `SKILL.md`, `references/`, `scripts/`, `templates/`, or examples.

## Required paths

- Local runtime skill: `/Users/elvis/.codex/skills/openspec-superpower-change`
- Open-source project: `/Users/elvis/file/develop/opensource/openspec-superpower-change`

## Pre-change checklist

1. Confirm the change level: Patch, Minor, or Major.
2. If Major, stop and require OpenSpec approval before implementation.
3. Confirm the intended source of truth for this change: local runtime, open-source project, or both.
4. Create timestamped backups before editing both affected trees.
5. Check the open-source repo is clean before editing:

```bash
git -C /Users/elvis/file/develop/opensource/openspec-superpower-change status -sb
```

## Sync checklist

1. Apply the change to the intended primary tree.
2. Apply the same logical change to the secondary tree unless explicitly out of scope.
3. Compare key files when both trees should stay aligned:
   - `SKILL.md`
   - `references/self-evolution-rule.md`
   - `references/step-evidence-gate.md`
   - `references/sync-checklist.md`
   - `scripts/validate_core_gates.py`
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
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.codex/skills/openspec-superpower-change
python3 /Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/.codex/skills/openspec-superpower-change
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/file/develop/opensource/openspec-superpower-change
python3 /Users/elvis/file/develop/opensource/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/file/develop/opensource/openspec-superpower-change
```

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

## Git checklist for open-source sync

1. Review diff:

```bash
git -C /Users/elvis/file/develop/opensource/openspec-superpower-change diff --stat
git -C /Users/elvis/file/develop/opensource/openspec-superpower-change diff
```

2. Commit with a clear message.
3. Push only after explicit user approval.
4. Report commit hash and validation results.

## Report checklist

Every sync report must include:

- change level;
- source of truth;
- backup paths;
- changed files in local runtime skill;
- changed files in open-source project;
- validation commands and results;
- forward-test result when run;
- residual risks;
- rollback path.
