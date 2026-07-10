# Change: Harden skill evidence and closure semantics

## Why

The previous workflow revision established deterministic ownership and a mandatory
verify/review/fix loop, but adversarial review found that completion can still be
represented by status strings without linked evidence. Empty critical commands,
blank blocker details, and an atomic final-gate update can also bypass the intent
of the closure rules. Trigger metadata and Superpowers defaults still leave a few
ambiguous routing, duplicate-design, and Git-authorization paths.

## What Changes

- Upgrade the external Handoff Contract to schema version 3 and bind attempt,
  batch Review, final verification, and final Review states to hashed artifact
  references whose manifests identify role, result, batch, attempt, and source
  canonical fingerprint.
- Reject blank critical commands, stop conditions, blocker fields, mutable fields
  mislabeled as readonly, and booleans used as positive integers.
- Persist final verification before final Review, then allow completion only from
  that evidenced intermediate state.
- Require an executable Plan/Brief Preflight Review before implementation or
  external dispatch, without duplicating design approval or post-implementation
  Review.
- Narrow the brief skill's implicit trigger so review-and-fix, workflow edits, and
  final completion decisions enter the change gate.
- Define the project-specific Superpowers adapter for OpenSpec design artifacts,
  plan granularity, worktree/main consent, and Git authorization.
- Add OpenSpec task reconciliation, archive, and post-archive validation to the
  completion lifecycle.
- Replace substring-only coverage with adversarial state tests, stronger routing
  assertions, and standalone-safe cross-repository parity tests.

## Impact

- Affected spec: `skill-workflow-governance`.
- Affected projects: both open-source skill repositories and both installed
  runtime copies.
- Compatibility: existing external status files must migrate from schema 2 to 3.
- Risk profile: `standard` Major Self-Evolution; no application runtime, security,
  persistence, or public API implementation changes.

## Approval Record

On 2026-07-10 the user reviewed the GPT-5.6 findings and explicitly instructed:
“按你建议推进实施”. This proposal is a direct formalization of that numbered
scope. Any expansion beyond it requires a new approval decision.
