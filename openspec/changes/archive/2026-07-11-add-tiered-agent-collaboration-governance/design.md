# Design: Tiered agent collaboration governance

## Context

Codex remains the control plane, while Codex, Antigravity CLI, or Grok CLI
instances may execute or independently Review a bounded batch. Product identity
alone is insufficient when two Codex windows have different roles and
capabilities. Existing permission handling also needs to distinguish what the
platform can execute from what the approved workflow allows and what only the
user may authorize as a business decision.

## Goals / Non-Goals

### Goals

- Route work by stable capability profile and bounded decision authority.
- Make product, instance, role, and decision owner independently auditable.
- Reduce repeated confirmations without weakening production or user control.
- Turn corrections into governed learning candidates rather than automatic
  global mutations.
- Increase the defect yield of High Review beyond replaying executor commands.
- Preserve lightweight behavior for compact and non-state-changing work.

### Non-Goals

- Select a concrete model for the user.
- Build a scheduler, daemon, agent marketplace, or third orchestration layer.
- Give an executor permission to promote its own result.
- Change OpenHarness product code or pilot acceptance in this Change.

## Considered Approaches

### 1. Encode concrete model names in global rules

This is simple but becomes stale as models change and incorrectly turns model
metadata into authority. Rejected.

### 2. Add a third enterprise-agent governance Skill

This centralizes wording but duplicates the existing router and Brief governor,
creating trigger and ownership conflicts. Rejected.

### 3. Extend the two existing Skills with typed references and validators

Selected. `openspec-superpower-change` owns capability routing, authorization,
decision provenance, learning candidates, final Review, and completion.
`codex-brief-antigravity-review` consumes those decisions in Brief/Report/Review
attempts without reclassifying risk or authority.

## Decisions

### 1. Stable capability profiles

- `control-plane-high`: architecture, OpenSpec, security, migration, ambiguous
  debugging, Preflight, evidence audit, independent probes, promotion, archive,
  and completion.
- `cohesive-medium`: approved multi-file implementation slices with no open
  architecture or authorization decision.
- `mechanical-low`: deterministic one-to-two-file edits, generated changes,
  focused tests, command execution, or evidence collection.

Profiles are recommendations and authority ceilings, not model names. Low or
Medium escalates `BLOCKED` on unexpected failure, ambiguity, security fields,
forbidden files, scope expansion, production credentials, or approval changes.

### 2. Schema-5 instance and role identity

New contracts separate:

- `agent_product`: stable enum such as `codex`, `antigravity-cli`, or `grok-cli`;
- `agent_instance_id`: non-sensitive identifier unique within the contract;
- `agent_role`: `control-plane`, `executor`, or `independent-reviewer`;
- `control_plane_owner`: exactly the authoritative Codex instance;
- `executor_profile` and `reviewer_profile`;
- `decision_source` and Confirmation Lease reference.

The executor and independent reviewer must be different instances for
standard/strict work, even when they use the same product. Model strings may be
optional observational metadata but never influence authorization.

Schema 5 is not an in-place migration. Before deployment, inventory all active
schema-4 statuses. Any active v4 contract blocks the switch until it reaches its
existing terminal state. Historical complete v4 evidence remains immutable.

### 3. Three authorization layers

1. Tool/platform authorization: sandbox, prefix, network, or CLI permission.
2. Scope/workflow authorization: approved OpenSpec, Plan, Brief, allowlist, and
   current artifact revision.
3. Business/production authorization: real credentials, paid or real endpoints,
   production writes, migration, deletion, release, archive, promotion,
   destructive Git, external messages, and equivalent user-owned decisions.

A lower layer cannot satisfy a higher layer. The workflow does not repeat a
chat confirmation for an already resolved platform permission, but it always
stops for a newly required business/production decision.

### 4. Confirmation Lease

A lease binds a decision ID, artifact revision/SHA-256, approved scope/action,
risk, decision source, owner, and invalidation conditions. Unchanged read-only
inspection, tests, diff checks, and same-finding fix/verify/Review loops reuse
the lease. Scope, acceptance, risk, production impact, credentials, external
side effects, destructive Git, contradictory evidence, or user correction
invalidate it.

Compact work records the lease inline. Standard/strict external work stores a
typed canonical reference validated with the Handoff evidence chain.

### 5. Decision provenance and Learning Candidate Pipeline

Every material decision records one of the allowed sources. A correction first
creates a Candidate Card containing the symptom, prior assumption, correction
or evidence, generalized invariant, severity, scope classification, target
artifact, baseline scenario, and duplicate/conflict assessment.

- task-local candidates update the current Plan/Brief/Review;
- project-local candidates update project governance or documentation;
- global candidates require two independent reproductions or one high-severity
  security/integrity/false-PASS event before a new Self-Evolution proposal;
- mechanical invariants prefer validators and tests over duplicated prose.

Candidate generation may be automatic. Skill modification never is.

### 6. Governed external execution and High Review

Manually copied state-changing standard/strict Briefs use the same Handoff-backed
contract as tool-dispatched work. The executor reports facts and cannot edit
canonical state or claim authoritative completion.

High Review must:

1. inspect actual files and the complete diff;
2. trace copy/transform/wiring paths and claim-to-mechanism support;
3. rerun `step_critical` or `final_critical` where applicable;
4. add at least one independent adversarial or real business-chain probe;
5. return `PASS`, `FAIL`, or `BLOCKED`, with every finding entering a fresh
   fix/verify/Review loop.

### 7. Process weight and source/runtime synchronization

Compact remains inline and concise when risk genuinely qualifies. Standard
requires cohesive slices and distinct Review. Strict requires real evidence for
security, authorization, public contracts, persistence, migration, deployment,
or recovery.

Portable changes to either Skill or the managed governance block trigger the
existing Codex -> Antigravity CLI -> Grok CLI synchronization gate. Required
target drift or discovery failure remains `BLOCKED`.

## Validation Strategy

RED/GREEN forward-tests cover:

1. already-authorized safe commands do not cause duplicate chat confirmation;
2. platform permission cannot authorize production deletion;
3. AI-proposed/user-approved decisions retain their provenance;
4. Low ambiguity escalates instead of designing;
5. High Review catches copy-field loss despite executor PASS;
6. an adversarial bounded input catches behavior missed by green unit tests;
7. Review traces workload/metadata claims to actual mechanisms;
8. same-product instances cannot self-review;
9. one low-risk correction creates only a candidate;
10. repeated high-severity false PASS may propose but cannot implement a Skill
    change without approval.

Both source repositories run quick validation, project validators, unittest,
cross-skill compatibility tests, sensitive audit, and final diff Review. Every
required runtime then passes parity, installed validators, discovery, and final
Review.

## Rollback

Before implementation, create a new timestamped structured backup outside Skill
discovery roots. Each implementation slice and runtime target is independently
reversible. A failed target restores only that target and stops later targets.
Temporary backups are removed after user-approved publication or local closeout.
