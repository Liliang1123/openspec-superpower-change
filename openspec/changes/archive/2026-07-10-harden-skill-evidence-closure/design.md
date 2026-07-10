# Design: Harden skill evidence and closure semantics

## Context

The two skills now have correct high-level ownership, but their validators still
accept several structurally valid yet semantically empty contracts. The solution
must close those bypasses without turning inline compact work into a Handoff-heavy
workflow.

## Goals / Non-Goals

### Goals

- Make external completion evidence-addressable and mechanically non-empty.
- Preserve the existing lightweight inline path.
- Make final verification and final Review separately auditable.
- Remove remaining trigger and Superpowers integration ambiguity.
- Close OpenSpec changes rather than leaving completed work active indefinitely.

### Non-Goals

- Add a workflow service, database, generic engine, or third-party dependency.
- Require Handoff artifacts for standalone or inline compact work.
- Cryptographically sign evidence or replace repository access controls.
- Duplicate OpenSpec design approval with a second Superpowers design artifact.

## Decisions

### 1. Schema version 3 evidence binding

Add four mutable evidence fields to canonical status:

- `attempt_report_artifact`: current attempt Report/Abort/timeout evidence;
- `last_review_artifact`: batch Review, timeout audit, or blocking Review path;
- `final_verification_artifact`: a manifest containing commands, results, and raw
  evidence paths once final verification has run;
- `final_review_artifact`: final Review path once it has run.

Every external profile has at least one non-blank `step_critical` and
`final_critical` command. Each required artifact reference contains a safe
project-relative path and SHA-256. The optional runtime status-validation mode
checks that referenced files exist, are non-empty, remain inside an explicit
artifact root after symlink resolution, and match their hashes. Each file also
contains a schema-1 manifest for role, result, change, batch, attempt, and the
earlier canonical revision/SHA-256 it evidences. Role rules are state-sensitive:
Preflight and timeout evidence are BLOCKED-only and cannot satisfy batch PASS.

### 2. Sequential final gates

The final external batch enters `awaiting-final-verification` with both final
results pending. A same-state revision records `final_verification: pass` and its
artifacts before final Review. Only that evidenced revision may transition to
`complete` with final Review PASS and a Review artifact. FAIL returns to
`needs-fix`; BLOCKED records an artifact, owner, reason, and resume condition.
Runtime completion validation requires the actual previous canonical status and
checks the final Review manifest against its revision and SHA-256. Proposed and
previous snapshots remain outside the project so canonical marker uniqueness is
not weakened.

### 3. Contract integrity

- Positive integers explicitly reject booleans.
- All command, blocker, strategy, and stop-condition strings must be non-blank.
- `readonly_fields` must exactly equal the validator's immutable field set.
- Brief/Report/Review fingerprints include the canonical contract SHA-256 and
  transition-validation evidence so external edits cannot be hidden by a partial
  field table.

### 4. Preflight Review without duplicate approval

After plan self-review, and before code execution or external dispatch, run one
Preflight Review of the current artifact revision. It checks contract/spec
coverage, placeholders, allowed files, exact commands, evidence profile, rollback,
stop conditions, and Git authorization. Findings revise the same artifact and
restart Preflight Review. It does not re-approve design and does not replace the
post-implementation Review.

Preflight has only `PASS` and `BLOCKED`: any actionable finding is BLOCKED.
`FAIL` is reserved for executed behavior or post-implementation Review. This
keeps the schema's blocking tuple and its evidence result unambiguous.

### 5. Superpowers adapter

When OpenSpec is required, brainstorming still explores intent and alternatives,
but its design output and user-review gate map to the same OpenSpec proposal,
design, change-id, and approval. No second `docs/superpowers/specs/` artifact is
created for the same decision. A Superpowers plan never grants Git permission;
unauthorized `git add`, `commit`, or `push` steps are removed or marked blocked.
Step Evidence remains business-slice based even when plan tasks contain TDD
micro-steps.

### 6. Completion and archive

Before claiming an OpenSpec-backed task closed, reconcile `tasks.md`, perform
fresh final verification and Review, write the locally required design/closeout
record, archive the change when repository completion semantics allow it, and run
strict validation after archive. If deployment or release is still required,
keep the change active and report its owner/condition instead of calling it closed.

## Risks / Trade-offs

| Risk | Mitigation |
|---|---|
| Schema migration adds fields | Limit schema 3 to external Handoff state; inline work is unchanged. |
| Artifact paths can become stale | Validate paths at final closure and invalidate evidence after implementation changes. |
| Preflight duplicates design review | Scope it to executability and rerun only after artifact revision changes. |
| Stronger triggers become too narrow | Keep ordinary standalone prompt/diff Review keywords while adding explicit exclusions. |
| Cross-repo tests fail in isolated clones | Skip only parity integration checks when the sibling repo is absent; local invariants remain mandatory. |
| Previous-status validates only one history edge | Trust the live canonical prior state plus retained transition outputs/repository history; append-only journals or signatures are explicitly outside this lightweight change. |

## Rollback

Restore both source and runtime skill trees from
`/private/tmp/two-codex-skills-v2-self-evolution-20260710-182410/`. After a
successful publish and cleanup, use the two repository commits for long-term
rollback.
