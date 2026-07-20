# Change: Streamline workflow prompt contracts

## Why

The adaptive two-skill workflow now preserves approval, evidence, Review,
learning, and cross-runtime completion gates, but the combined prompt stack
still has three bounded architecture problems:

1. installed Superpowers branch-finishing guidance contradicts itself about
   whether Option 2 removes or preserves its worktree;
2. whole-task completion is defined across several workflow artifacts instead
   of one canonical result contract;
3. the Companion places lightweight Review and full Handoff governance in one
   Skill body without measured evidence that every supported runtime can avoid
   loading the inactive route.

Textual precedence currently mitigates Superpowers routing and Git-default
collisions, but those mitigations need explicit forward-tests. Previous
byte-count estimates do not prove actual prompt load or token savings. This
change therefore performs a measured, targeted redesign rather than weakening
governance or assuming model instability.

## What Changes

- Correct `superpowers:finishing-a-development-branch` so Option 2 consistently
  preserves its worktree and automatic cleanup applies only to Options 1 and 4.
- Establish one Router-owned canonical Completion Contract containing the
  whole-task success, stop, evidence, learning, reconciliation, sync, and final
  Review conditions. Other artifacts retain route-specific evidence but refer
  to the canonical whole-task decision.
- Make the Companion a thin mutually-exclusive route entry. Move Handoff-only
  lifecycle detail behind the Handoff route; split it into a separate Skill only
  if measured supported-runtime loading evidence shows references cannot provide
  route isolation.
- Add prompt-collision forward-tests covering phase-aware Superpowers selection,
  material-choice brainstorming, unauthorized Git steps, and preservation of a
  selected sub-skill's complete HARD-GATE.
- Replace byte-count token claims with reproducible runtime-load evidence and,
  only for known exact prompt text, tokenizer measurements with documented
  method and uncertainty.

## Non-Goals

- Do not redesign Project Learning Closeout, Learning Candidate thresholds,
  `CONTEXT.md` responsibility, `grill-with-docs`, or caveman/cavecrew semantics.
- Do not weaken OpenSpec approval, TDD, Preflight, independent Review, evidence,
  Git authority, final verification, runtime synchronization, or user control.
- Do not change Handoff schema 5, evidence manifests, capability profiles,
  Confirmation Leases, or external batch state transitions.
- Do not route workflow weight by model or vendor name.
- Do not install `shadcn/improve` or add a third workflow governor.

## Impact

- Affected spec: `skill-workflow-governance`.
- Affected source repositories: `openspec-superpower-change` and
  `codex-brief-antigravity-review`.
- Separately scoped dependency: the installed/source-managed
  `superpowers:finishing-a-development-branch` contract and regression fixture.
- Candidate Router files: `SKILL.md`, a new canonical completion reference,
  navigation/response/evidence references, validators, tests, README files, and
  changelog.
- Candidate Companion files: `SKILL.md`, a Handoff-only route reference or
  evidence-supported split Skill, validators, tests, README files, and changelog.
- Runtime targets: every declared required Codex, Antigravity CLI, and Grok CLI
  target when portable files or shared governance change.
- Compatibility: existing approval, Handoff, evidence, learning, and completion
  outcomes remain at least as strict. Existing active contracts are not migrated.
- Risk: Major Self-Evolution because completion ownership, Skill route loading,
  Superpowers interaction, and portable runtime layout may change.

## Bounded Decisions Pending Measurement

- If a supported runtime demonstrably loads Companion references only when
  selected, use one thin Companion Skill plus route-specific references.
- If a supported runtime always injects the complete activated Skill body and
  cannot isolate the inactive Handoff contract, use two mutually exclusive
  Companion Skill entrypoints with unchanged authority boundaries.
- A runtime whose loading cannot be observed is recorded `UNKNOWN`; file bytes
  alone do not select the split branch.

## Approval Status

- User authorized creation of a Major Self-Evolution proposal on 2026-07-17.
- Independent proposal Review PASS on 2026-07-17:
  `docs/design/reviews/2026-07-17-streamline-workflow-prompt-contracts-proposal-review.md`
- Change-id and scoped contract approved for implementation on 2026-07-17.
- [x] This exact change-id and scoped contract are approved for implementation.
