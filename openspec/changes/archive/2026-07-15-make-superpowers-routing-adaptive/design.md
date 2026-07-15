# Design: make-superpowers-routing-adaptive

## Context

`openspec-superpower-change` currently maps brainstorming to ambiguous creative
alternatives and already provides compact evidence paths. The installed
Superpowers metadata is broader: creation or behavior modification can activate
brainstorming before the router has applied its phase-specific decision. A RED
simulation of a `/notifications/preferences` OpenSpec request therefore entered
question-by-question brainstorming even though the immediate deliverable was an
unapproved proposal, not implementation.

The companion skill behaved proportionately in the same simulation: an explicit
read-only Review used Standalone Lightweight, created no Handoff, and did not
claim completion. Its route needs clarification and a concrete OpenSpec-artifact
checklist, not a replacement workflow.

## Goals / Non-Goals

### Goals

- Make sub-skill activation deterministic from phase, unresolved material
  decisions, and implementation risk.
- Let sufficiently specified proposal-only work produce one reviewable OpenSpec
  contract without a duplicate design dialogue.
- Preserve mandatory discovery when a decision changes security, compatibility,
  data lifecycle, scope, or testable acceptance.
- Keep standalone OpenSpec Review concise and valuable without auto-chaining it
  after every generated change.
- Retain all approval, evidence, Review, verification, rollback, sync, and
  user-control boundaries.

### Non-Goals

- Disable or uninstall the Superpowers skill family.
- Route by GPT/model/vendor/version name.
- Replace OpenSpec approval with plan mode or model confidence.
- Remove TDD, Preflight, independent Review, final verification, Handoff, or
  completion gates from the implementation paths where they currently apply.
- Change Handoff schema 5, evidence manifests, capability profiles, or the
  semantics of existing managed global-rule invariants. One new routing-
  precedence invariant is in scope.

## Decisions

### 1. Separate task phase from implementation risk

Gate 0 selects the current phase first:

1. `proposal-only`;
2. `approved-implementation`;
3. `direct-change`;
4. `standalone-review`;
5. `handed-off-execution`.

The evidence profile still describes implementation/acceptance risk. A future
public API implementation remains `strict`; its proposal-only draft does not
automatically load implementation planning, TDD, or code Review.

### 2. Selective brainstorming, intact HARD-GATE

Proposal-only work inspects existing specs, conventions, and active changes
before asking the user. It may record an explicit bounded assumption only when
the assumption is reversible at approval time, visible in the proposal/design,
and does not decide security, compatibility, destructive migration, data
lifecycle, production authority, or testable acceptance on the user's behalf.

Brainstorming is required when a material unresolved choice remains after that
inspection. Invoking it keeps its existing HARD-GATE; its accepted decisions are
written into the one OpenSpec design/spec delta. The optimization is selective
invocation, not partial compliance after invocation.

### 3. Change-gate precedence and Gate 0 `none`

The managed cross-CLI governance block gains a stable invariant requiring
governed state-changing work to enter `openspec-superpower-change` phase
classification before broad Superpowers metadata selects a sub-skill. This rule
is needed because router-body wording alone is loaded too late to prevent eager
metadata triggering.

When Gate 0 records that no Superpowers sub-skill applies to proposal drafting,
generic words such as create, add, modify, or design cannot reactivate one by
themselves. A later phase transition reruns Gate 0 and can select planning, TDD,
debugging, Review, or verification normally. The portable manifest increments
the managed-rule version and adds the new invariant ID without changing the
declared portable file set.

This rule is based on task facts rather than model identity. Model metadata may
inform capability assignment but never grants approval or removes a gate.

### 4. Standalone Review is request-scoped and brief by default

`codex-brief-antigravity-review` runs Standalone Lightweight only for the
current explicit wording/read-only-review request. Producing OpenSpec artifacts
does not implicitly require a second skill invocation.

For an explicit OpenSpec artifact Review, the default checklist is:

- proposal scope, motivation, impact, and non-goals;
- spec requirements, normative scenarios, and observable acceptance;
- design decisions, alternatives, risks, migration, and rollback;
- task traceability to each accepted requirement and validation gate;
- cross-artifact naming, scope, and compatibility consistency.

The response remains findings-first: scope/evidence, actionable findings,
verdict, and next action. It omits governance narration unless the narration
changes the result or next action. A valid Handoff still selects the complete
handed-off lifecycle with no reduction.

### 5. Preserve implementation and completion discipline

After approval, multi-slice, strict, or external implementation continues to
use the existing executable plan and Preflight boundary. Behavior changes still
use TDD; standard/strict work still needs distinct High Review; final completion
still needs fresh verification, Review PASS, task reconciliation, archive rules,
and required runtime synchronization.

### 6. Prove routing behavior before portable edits

Implementation starts with failing contract tests in both repositories. GREEN
forward-tests use fresh isolated agents and raw scenario prompts so they do not
receive the expected answer. The required scenarios distinguish a fully
specified proposal, a materially ambiguous proposal, approved strict
implementation, explicit standalone Review, and no-review-request behavior.

## Risks / Trade-offs

| Risk | Mitigation |
|---|---|
| A proposal hides an important assumption to avoid questions | Bound assumptions by reversibility and forbid them for security, compatibility, data lifecycle, production authority, or untestable acceptance |
| Broad upstream skill metadata still causes eager activation | Add managed global precedence plus router/adapter/tests; Gate 0 records `none` explicitly |
| Brief output becomes short but shallow | Keep the five-part OpenSpec checklist and omit narration, not inspected evidence or findings |
| Source and runtime copies diverge | Use the portable manifest plan/apply/verify-all sequence for all required targets |
| “Strong model” becomes an authorization shortcut | Forbid model-name routing and retain existing capability/evidence/approval boundaries |

## Migration / Rollback

No persisted Handoff or evidence schema migrates. Existing active schema-4
contracts finish under schema 4 and schema-5 contracts remain unchanged. The
managed governance block version increments atomically on all required targets;
native CLI rules outside the marker block remain byte-identical.

Before portable edits, retain the structured backup at
`/private/tmp/adaptive-superpowers-self-evolution-20260715-103712/`. Apply and
verify source repositories first, then each declared runtime target atomically.
If a target fails, restore that target, verify restoration, stop later target
application, and report `BLOCKED`. After successful closeout, remove temporary
backups; repository history remains the long-term rollback mechanism.
