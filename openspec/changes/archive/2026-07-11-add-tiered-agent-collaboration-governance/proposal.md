# Change: Add tiered agent collaboration governance

## Why

The current schema-4 workflow distinguishes Codex, Antigravity CLI, and Grok
CLI as products, but it cannot distinguish multiple agent instances of the same
product or bind their capability profile, decision authority, and execution
role. Platform command permission, approved workflow scope, and real business
or production approval also remain easy to conflate. These gaps can cause an
executor result to be mistaken for a control-plane decision, repeat already
valid confirmations, or let a single task correction overfit global Skill rules.

## What Changes

- Introduce stable capability profiles `control-plane-high`,
  `cohesive-medium`, and `mechanical-low` without binding authority to a model
  name.
- Upgrade newly created external Handoffs to schema 5, separating
  `agent_product`, `agent_instance_id`, and `agent_role`, and binding immutable
  control-plane, executor, and independent-reviewer assignments.
- Separate tool/platform authorization, scope/workflow authorization, and
  business/production authorization; platform permission never substitutes for
  OpenSpec, production, promotion, archive, release, or Git approval.
- Add profile-weighted Confirmation Leases that reuse unchanged approvals and
  expire on material scope, risk, evidence, production, or user-decision changes.
- Record decision provenance as `ai-proposed/user-approved`,
  `user-originated`, `user-corrected`, `evidence-discovered`, `deferred`, or
  `revoked`.
- Add a Learning Candidate Pipeline that captures corrections and evidence but
  cannot automatically edit a global Skill. Promotion requires generalization,
  approval, TDD, forward-tests, Review, and runtime synchronization.
- Govern manually copied external Briefs when they perform state-changing
  standard/strict work; copy/paste does not downgrade them to standalone mode.
- Require High control-plane Review to inspect the actual diff and production
  wiring, rerun critical evidence, trace claims to mechanisms, and add an
  independent adversarial or business-chain probe.
- Preserve compact/standard/strict process weighting and add a schema-4 drain
  gate before schema-5 deployment.

## Impact

- Affected spec: `skill-workflow-governance`.
- Affected source repositories: `openspec-superpower-change` and
  `codex-brief-antigravity-review`.
- Expected new references: capability routing, Confirmation Lease, and Learning
  Candidate Pipeline guidance; existing two Skill entry points remain the only
  workflow owners.
- Affected runtime surfaces after implementation approval: required Codex,
  Antigravity CLI, and Grok CLI Skill copies and the versioned managed
  governance block.
- Compatibility: active schema-4 Handoffs finish under schema 4; schema 5 is a
  hard switch only for newly created contracts after the active-v4 drain gate.
- Risk profile: strict Major Self-Evolution because identity, authorization,
  external execution, evidence acceptance, and completion semantics change.

## Non-Goals

- Hardcode model names, vendors, or transient model tiers as security identity
  or decision authority.
- Add a third top-level orchestration Skill.
- Let Low or Medium executors change OpenSpec scope, risk, production authority,
  canonical state, or final completion.
- Treat sandbox/prefix permission as business approval.
- Automatically rewrite a Skill after one user correction.
- Modify the OpenHarness repository or its acceptance criteria as part of this
  change.

## Approval Status

Approved for implementation. On 2026-07-11 the user explicitly approved the
exact change-id and scoped contract with: “批准实施
add-tiered-agent-collaboration-governance”. Any expansion beyond this contract
requires a new approval decision.
