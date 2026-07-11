## 1. Approval and baseline

- [x] 1.1 Strictly validate this OpenSpec change and record explicit user
  approval of `align-cross-cli-skill-governance`.
- [x] 1.2 Inventory clean Git state, the three runtime roots, global-rule files,
  installed skill revisions, and CLI discovery capabilities without reading or
  copying credential values; also inventory active schema-3 canonical statuses
  and block schema-4 deployment until every one reaches the existing v3
  `complete` terminal state.
- [x] 1.3 Create structured temporary backups of both repositories and the
  allowlisted runtime files before implementation; global-rule backups use mode
  `0600`, their contents are never printed, and successful closeout removes them.
- [x] 1.4 Capture RED forward-tests for premature completion, auxiliary
  self-approval, missing target sync, stale files, and denied secret categories.

## 2. Tests first

- [x] 2.1 Add failing workflow-rule tests for Codex primary ownership and
  schema-4 auxiliary executor/independent-reviewer identity binding, including
  same-agent self-review, impersonation, and evidence role mismatch.
- [x] 2.2 Add failing tests for the post-optimization three-runtime sync gate and
  required/`not-applicable` target states.
- [x] 2.3 Add failing tests for portable-file parity, semantic global-rule
  invariants, marker-bounded replacement, path/symlink containment, regular-file
  enforcement, `0600` rule backups, non-disclosing diagnostics, cleanup, and
  sensitive-category denial.
- [x] 2.4 Run the new tests and preserve the expected RED evidence.

## 3. Implementation

- [x] 3.1 Add a concise cross-agent synchronization reference and link it from
  `SKILL.md`, Self-Evolution, external execution, and sync guidance.
- [x] 3.2 Extend the source/runtime sync validator using only the Python standard
  library and path/manifest arguments; do not hardcode private credentials or
  machine-specific secrets.
- [x] 3.3 Upgrade the shared Handoff, templates, evidence manifest, and both
  validators to schema 4 with concrete executor/reviewer identities and Codex
  decision ownership.
- [x] 3.4 Update the companion Brief skill to accept auxiliary implementation and
  independent Review evidence while keeping Codex authoritative.
- [x] 3.5 Update both repositories' tests, README/changelog, and project design
  documentation with the role and sync boundary.
- [x] 3.6 Produce a current-revision executable implementation plan and pass
  Preflight Review before runtime synchronization.

## 4. Runtime synchronization and verification

- [x] 4.1 Synchronize and validate both skills in Codex runtime.
- [x] 4.2 Synchronize and validate both skills in Antigravity CLI runtime without
  touching auth, sessions, settings, hooks, models, or caches.
- [x] 4.3 Synchronize and validate both skills in Grok CLI runtime, then prove
  discovery with `grok inspect --json`.
- [x] 4.4 Align the shared governance invariant block in Codex, Antigravity, and
  Grok global rules while preserving each CLI's native overlay.
- [x] 4.5 Run all source/runtime validators, unittest suites, RED/GREEN
  forward-tests, parity checks, sensitive-information audits, backup-mode checks,
  non-disclosing diagnostic checks, and successful-backup cleanup checks.
- [x] 4.6 Obtain profile/declared-role-appropriate Review: compact may use Codex
  inline Review; standard/strict external work always separates executor and
  reviewer identities, preferring the other auxiliary CLI and otherwise using a
  Codex Review pass. If no distinct reviewer is available, block rather than
  downgrade. Fix every actionable finding, rerun verification, and complete final
  Codex Review.

## 5. Closeout and publication

- [x] 5.1 Reconcile this task list and update the approved design closeout record
  under `docs/design` with document type and version log.
- [x] 5.2 Archive the OpenSpec change and run strict validation after archive.
- [x] 5.3 Review both Git diffs for unrelated changes, temporary files, backups,
  credentials, tokens, and private configuration.
- [x] 5.4 Resolve the publication gate under explicit user control: the user
  selected local closeout without `git add`/commit/push, and explicitly
  authorized removal of the temporary backup root after Final Review PASS.
