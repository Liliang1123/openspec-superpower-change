# Cross-CLI Skill Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Plan revision:** 11 (2026-07-11). This revision aligns the executable sync CLI,
the five forward-test IDs, and the final-verification template scope with the
current source diff, and covers first-time skill/managed-block installation.
Runtime/global writes, backup deletion, archive, and Git publication remain
separately authorized actions.

**Execution context:** Continue in the existing approved dirty `main` checkout
because moving or recreating the protected partial diff would violate the
handoff. Do not create a worktree, reset, clean, restore, stage, commit, or push.

**Goal:** Make Codex the authoritative workflow owner while safely synchronizing the two core skills and their shared governance rules to Codex, Antigravity CLI, and Grok CLI.

**Architecture:** The approved OpenSpec change `align-cross-cli-skill-governance` is the single design contract. The two repositories remain canonical skill sources; schema 4 binds external executor/reviewer identities, while a standalone standard-library validator verifies allowlisted runtime files and one versioned managed global-rule block without touching CLI-native overlays or sensitive configuration.

**Tech Stack:** Markdown Agent Skills, OpenSpec, Python 3 standard library, unittest, SHA-256, native CLI discovery/validation.

---

## Scope and files

### `openspec-superpower-change`

- Modify: `SKILL.md`
- Modify: `references/handoff-contract.md`
- Modify: `references/approved-implementation-workflow.md`
- Modify: `references/self-evolution-rule.md`
- Modify: `references/sync-checklist.md`
- Modify: `references/step-evidence-gate.md`
- Create: `references/cross-cli-sync.md`
- Create: `references/shared-global-governance.md`
- Create: `references/cross-cli-portable-manifest.json`
- Modify: `scripts/validate_core_gates.py`
- Create: `scripts/validate_cross_cli_sync.py`
- Modify: `templates/final-verification-template.md`
- Modify: `tests/test_workflow_rules.py`
- Create: `tests/test_cross_cli_sync.py`
- Modify: `README.md`, `README_cn.md`, `CHANGELOG.md`
- Create: `docs/design/2026-07-11-cross-cli-skill-governance.md`

### `codex-brief-antigravity-review`

- Modify: `SKILL.md`
- Modify: `references/handoff-contract.md`
- Modify: `references/brief-template.md`
- Modify: `references/report-template.md`
- Modify: `references/review-template.md`
- Modify: `references/timeout-audit-template.md`
- Modify: `references/agy-dispatch-template.md`
- Modify: `scripts/validate_templates.py`
- Modify: `tests/test_workflow_rules.py`
- Modify: `README.md`, `CHANGELOG.md`
- Create: `docs/design/2026-07-11-cross-cli-skill-governance.md`

### Runtime allowlist

- Managed skill roots only:
  - `~/.codex/skills/{openspec-superpower-change,codex-brief-antigravity-review}`
  - `~/.gemini/antigravity-cli/skills/{openspec-superpower-change,codex-brief-antigravity-review}`
  - `~/.grok/skills/{openspec-superpower-change,codex-brief-antigravity-review}`
- Managed rule blocks only:
  - `~/.codex/AGENTS.md`
  - `~/.gemini/GEMINI.md`
  - `~/.grok/AGENTS.md`
- Forbidden: auth/token/session/history/log/cache/settings/hooks/MCP/model/binary files.

## Task 1: Preserve approval, inventory, and rollback evidence

- [x] Record the exact OpenSpec approval in `proposal.md`.
- [x] Confirm both repositories are clean before proposal edits.
- [x] Confirm `active_schema3_count=0` in declared collaboration workspaces.
- [x] Back up source/runtime allowlisted files under `/private/tmp/cross-cli-skill-sync-major-20260711`; global-rule backups are mode `0600`.

## Task 2: RED — schema 4 identity binding

- [x] Add mirrored failing assertions/tests for:
  - schema version 4 required fields;
  - canonical identity enum and `decision_owner: codex`;
  - standard/strict distinct reviewer;
  - compact `not-applicable` reason pairing;
  - immutable identity fields;
  - Report/Review/final evidence identity and role binding;
  - impersonation, alias, self-review, and timeout-audit cases.
- [x] From `/Users/elvis/file/develop/opensource/openspec-superpower-change`, run:

  ```bash
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_workflow_rules -v
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s ../codex-brief-antigravity-review/tests -p 'test_workflow_rules.py' -v
  ```

  Expected RED: new schema-4 tests fail because current contracts still publish
  `schema_version: 3` and lack agent identity/role fields. Save output to the
  temporary evidence root without adding logs to either repository.

## Task 3: GREEN — schema 4 contract and templates

- [x] Update both byte-identical Handoff contracts to schema 4.
- [x] Update both validator cores with the same identity/role rules while preserving repository-specific layout checks.
- [x] Update Brief, Report, Review, timeout, and dispatch templates plus final
  verification rules in `references/approved-implementation-workflow.md` and the
  shared Handoff evidence-role contract; update `references/step-evidence-gate.md`
  to state that Handoff schema 4 extends the separately versioned evidence
  schema-1 manifest with required identity fields. Do not create an unused template.
- [x] From the OpenSpec repository, run until GREEN:

  ```bash
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_workflow_rules -v
  (cd ../codex-brief-antigravity-review && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v)
  ```

  Expected GREEN: both workflow suites report `OK` with zero failures.

## Task 4: RED — cross-CLI synchronization safety

- [x] Create `tests/test_cross_cli_sync.py` with failing cases for:
  - portable allowlist and sensitive denylist;
  - absolute/traversal/backslash/URL/NUL paths;
  - symlink escape and non-regular files;
  - manifest/hash/missing/extra drift;
  - marker count/version/invariant/body hash/outside-byte protection;
  - first-time managed-block insertion with byte-identical native content;
  - required/blocked/strict `not-applicable` state;
  - `0600` backups, non-disclosing diagnostics, atomic rollback, and cleanup;
  - first-time skill installation and rollback that removes only files/directories
    created by the failed transaction;
  - Grok discovered paths and deterministic Antigravity validation inputs.
- [x] Create only an importable interface scaffold in
  `scripts/validate_cross_cli_sync.py`; its behavior functions raise
  `NotImplementedError`. Then run the five forward-test IDs individually:

  ```bash
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
    tests.test_cross_cli_sync.CrossCliForwardTests.test_premature_completion_is_blocked_until_all_required_targets_pass \
    tests.test_cross_cli_sync.CrossCliForwardTests.test_auxiliary_self_approval_cannot_complete_sync \
    tests.test_cross_cli_sync.CrossCliForwardTests.test_missing_grok_sync_blocks_completion \
    tests.test_cross_cli_sync.CrossCliForwardTests.test_stale_antigravity_files_block_completion \
    tests.test_cross_cli_sync.CrossCliForwardTests.test_credential_copying_is_rejected -v \
    > /private/tmp/cross-cli-skill-sync-major-20260711/forward-tests-red.log 2>&1
  ```

  Expected RED: all five named scenarios are discovered and fail independently
  because their behavior is not implemented; no failure may be only an import or
  missing-test error. Then run the remaining focused suite and preserve its RED
  failure list.

## Task 5: GREEN — synchronization validator and governance core

- [x] Add stable invariants `CCG-001` through `CCG-008` in `references/shared-global-governance.md`.
- [x] Implement `scripts/validate_cross_cli_sync.py` using only the standard
  library. Its executable CLI contract is `plan`, `apply`, `verify`,
  `verify-all`, `verify-discovery`, and `audit`; `verify-discovery` and `audit`
  support the exact arguments used below, including `--consume` and
  `--report-paths-only`. Keep the existing library helpers importable for
  focused tests.
- [x] Keep apply behavior explicit, allowlisted, atomic, rollback-capable, and non-disclosing.
- [x] Support both update and first installation. Existing files are secure-backed
  up before atomic replacement. Missing Grok skill files are created only below
  the validated target root through transaction-owned staging; rollback removes
  only transaction-created files and then empty transaction-created directories.
  Never follow or replace symlinks and never delete a pre-existing path.
- [x] For a global rule file with zero managed markers, insert exactly one
  canonical versioned block while preserving every original byte as an unchanged
  prefix (adding only the minimum line separator before the new block). Existing
  files with one valid pair use bounded replacement; duplicate, partial,
  mismatched, or nested markers fail without writing.
- [x] Add `references/cross-cli-sync.md` plus a path-free portable manifest and link them from entry, self-evolution, execution, and sync guidance.
- [x] Run the focused suite until it reports `OK`, then run:

  ```bash
  export PYTHON_BIN="${PYTHON_BIN:-/opt/anaconda3/envs/qagent-3.12.11/bin/python}"
  export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
  "$PYTHON_BIN" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" .
  PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
  (cd ../codex-brief-antigravity-review && \
    "$PYTHON_BIN" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" . && \
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_templates.py . && \
    PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v)
  ```

  Expected: both quick validators are valid, both project validators PASS, and
  both unittest suites report `OK`.

## Task 6: Documentation and Pre-runtime Review

- [x] Update both Skill entry documents, READMEs, changelogs, and `docs/design` records without changing unrelated formatting.
- [x] Confirm repository-only docs do not trigger runtime sync.
- [x] Run a distinct diff Review for scope, identity binding, secret boundaries, and lifecycle consistency.
- [x] Fix every finding and rerun validation/Review.

## Task 7: Runtime synchronization

- [x] Set paths from the OpenSpec repository and generate a plan:

  ```bash
  export OPEN_REPO="$PWD"
  export BRIEF_REPO="$(dirname "$PWD")/codex-brief-antigravity-review"
  export SYNC_MANIFEST="$OPEN_REPO/references/cross-cli-portable-manifest.json"
  export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
  export ANTIGRAVITY_CLI_HOME="${ANTIGRAVITY_CLI_HOME:-$HOME/.gemini/antigravity-cli}"
  export GROK_HOME="${GROK_HOME:-$HOME/.grok}"
  python3 scripts/validate_cross_cli_sync.py plan \
    --manifest "$SYNC_MANIFEST" --openspec-source "$OPEN_REPO" --brief-source "$BRIEF_REPO" \
    --codex-skills-root "$CODEX_HOME/skills" --codex-rule-file "$CODEX_HOME/AGENTS.md" \
    --antigravity-skills-root "$ANTIGRAVITY_CLI_HOME/skills" --antigravity-rule-file "$HOME/.gemini/GEMINI.md" \
    --grok-skills-root "$GROK_HOME/skills" --grok-rule-file "$GROK_HOME/AGENTS.md" \
    --output /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json
  ```

  Expected: exit 0; plan contains only allowlisted paths, source hashes, required
  targets, managed-rule marker changes, and no file contents or credential values.
- [x] Stop before the first `apply` and obtain explicit user authorization for
  the Codex, Antigravity CLI, and Grok CLI runtime/global-rule writes. The
  source-only tests and reviewed plan do not grant that authorization.
- [x] Review `sync-plan.json` by keys/paths only, snapshot every target into the
  existing `0600` backup root, then apply one target at a time:

  ```bash
  python3 scripts/validate_cross_cli_sync.py apply --target codex --plan /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json --backup-root /private/tmp/cross-cli-skill-sync-major-20260711/runtime
  python3 scripts/validate_cross_cli_sync.py verify --target codex --plan /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json
  python3 scripts/validate_cross_cli_sync.py apply --target antigravity-cli --plan /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json --backup-root /private/tmp/cross-cli-skill-sync-major-20260711/runtime
  python3 scripts/validate_cross_cli_sync.py verify --target antigravity-cli --plan /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json
  python3 scripts/validate_cross_cli_sync.py apply --target grok-cli --plan /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json --backup-root /private/tmp/cross-cli-skill-sync-major-20260711/runtime
  python3 scripts/validate_cross_cli_sync.py verify --target grok-cli --plan /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json
  ```

  If a target is restored after a failed installed-validator check, its next
  correction attempt uses a new attempt-specific backup subdirectory such as
  `/private/tmp/cross-cli-skill-sync-major-20260711/runtime/retry-02`; never mix
  retry backups into the failed attempt's backup directory.

  Expected after each pair: apply and verify exit 0. On any apply failure, the
  script atomically restores that target from its backup, verifies restoration,
  and stops before the next target.
- [x] After Antigravity replacement and validation PASS, verify each path is
  contained under its skills root, is a real directory rather than a symlink,
  then remove only these inventoried obsolete discovery paths:

  ```text
  $ANTIGRAVITY_CLI_HOME/skills/openspec-superpower-change.backup-20260623-095800
  $ANTIGRAVITY_CLI_HOME/skills/openspec-superpower-change.backup-review-hardening-20260623-135444
  $ANTIGRAVITY_CLI_HOME/skills/openspec-superpower-change.backup-self-evolution-20260623-133723
  $ANTIGRAVITY_CLI_HOME/skills/openspec-superpower-change.backup-stability-20260623-165522
  ```

  Deletion requires a dry-run inventory artifact and the user's destructive-action
  authorization; otherwise leave them as an explicit blocker rather than widening
  the deletion pattern.
- [x] Prove Grok discovery without model usage:

  ```bash
  umask 077
  : > /private/tmp/cross-cli-skill-sync-major-20260711/grok-inspect.json
  chmod 600 /private/tmp/cross-cli-skill-sync-major-20260711/grok-inspect.json
  "$GROK_HOME/bin/grok" inspect --json > /private/tmp/cross-cli-skill-sync-major-20260711/grok-inspect.json
  stat -f '%Sp' /private/tmp/cross-cli-skill-sync-major-20260711/grok-inspect.json
  python3 scripts/validate_cross_cli_sync.py verify-discovery --target grok-cli \
    --inspect-json /private/tmp/cross-cli-skill-sync-major-20260711/grok-inspect.json \
    --plan /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json --consume
  ```

  Expected: mode output is `-rw-------`; the validator reads only required skill
  path fields, never prints the JSON, confirms both `$GROK_HOME/skills/` paths,
  exits 0, and removes the consumed inspect artifact.
- [x] Each target `apply` above updates both allowlisted skill files and exactly
  one managed governance block. Verify all target manifests, blocks, and installed
  skill validators with:

  ```bash
  python3 scripts/validate_cross_cli_sync.py verify-all \
    --plan /private/tmp/cross-cli-skill-sync-major-20260711/sync-plan.json
  export PYTHON_BIN="${PYTHON_BIN:-/opt/anaconda3/envs/qagent-3.12.11/bin/python}"
  for root in "$CODEX_HOME/skills" "$ANTIGRAVITY_CLI_HOME/skills" "$GROK_HOME/skills"; do
    "$PYTHON_BIN" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" "$root/openspec-superpower-change"
    PYTHONDONTWRITEBYTECODE=1 python3 "$root/openspec-superpower-change/scripts/validate_core_gates.py" "$root/openspec-superpower-change"
    "$PYTHON_BIN" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" "$root/codex-brief-antigravity-review"
    PYTHONDONTWRITEBYTECODE=1 python3 "$root/codex-brief-antigravity-review/scripts/validate_templates.py" "$root/codex-brief-antigravity-review"
  done
  ```

  Expected: `verify-all` reports all three targets and managed blocks PASS; all
  twelve installed-skill validator commands exit 0.

## Task 8: Final verification and closeout

- [x] Run five isolated workflow forward-tests and persist path-only evidence:

  ```bash
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
    tests.test_cross_cli_sync.CrossCliForwardTests -v \
    > /private/tmp/cross-cli-skill-sync-major-20260711/forward-tests.log 2>&1
  ```

  Expected GREEN: premature completion, auxiliary self-approval, missing target,
  stale runtime, and denied secret-category scenarios all PASS. Reconcile this
  evidence with OpenSpec tasks 1.4, 4.5, and 5.1.
- [x] Run full final verification from the OpenSpec repository:

  ```bash
  export PYTHON_BIN="${PYTHON_BIN:-/opt/anaconda3/envs/qagent-3.12.11/bin/python}"
  export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
  "$PYTHON_BIN" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" .
  PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
  (cd ../codex-brief-antigravity-review && \
    "$PYTHON_BIN" "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" . && \
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_templates.py . && \
    PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v)
  openspec validate align-cross-cli-skill-governance --strict
  git diff --check
  git -C ../codex-brief-antigravity-review diff --check
  python3 scripts/validate_cross_cli_sync.py audit \
    --openspec-source "$PWD" --brief-source "$(dirname "$PWD")/codex-brief-antigravity-review" \
    --report-paths-only
  ```

  Expected: all commands exit 0. Sensitive audit emits only path/category and
  prints `0 sensitive categories found`; it must never print matching values.
- [x] Reconcile all completed `tasks.md` items and write the final `docs/design`
  closeout before archive; leave no unexplained open task.
- [x] Stop and obtain explicit user authorization immediately before archive.
- [x] Archive and validate with exact commands:

  ```bash
  openspec archive align-cross-cli-skill-governance --yes
  openspec validate --all --strict --no-interactive
  ```

  Expected: the change moves under `openspec/changes/archive/`, the main spec is
  updated, and all specs/remaining changes report valid.
- [x] After archive, rerun `git diff --check`, both Git status/diff reviews, the
  path/category-only sensitive audit, and then run the true final independent
  Review over the complete two-repository diff. `FAIL/BLOCKED` returns to fix,
  strict validation, relevant tests/audit, and Review again. Do not commit or
  push without explicit user authorization for those Git actions.
- [x] After successful publication or user-approved local closeout, inventory
  temporary backups and obtain explicit user authorization before removing
  them; then report rollback commits/paths.
