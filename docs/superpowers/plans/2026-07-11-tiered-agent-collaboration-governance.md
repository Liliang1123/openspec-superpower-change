# Tiered Agent Collaboration Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:executing-plans` to implement this plan task-by-task. Do not use
> delegated agents for this run because the user explicitly requested no agent
> delegation.

**Plan revision:** 2 (2026-07-11). This revision confines the schema-4 drain
gate to schema-5 runtime deployment, defines evidence schema 2 for new schema-5
contracts while preserving historical schema-1 evidence, and makes both pilots
synthetic validator fixtures so they do not delegate agents. This is the
current-revision plan for the approved OpenSpec Change `add-tiered-agent-collaboration-governance`.

**Decision provenance:** `ai-proposed/user-approved`. The user explicitly
approved the exact Change with “批准实施 add-tiered-agent-collaboration-governance”.
That approval covers source implementation within the approved contract; it does
not authorize runtime/global-rule writes, archive, backup deletion, Git staging,
commit, push, or merge.

**Execution context:** Implement only in these isolated worktrees:

- Router: `/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/tiered-agent-governance`
- Brief governor: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/tiered-agent-governance`

Do not reset, clean, restore, overwrite, stage, or reconstruct either original
`main` checkout. Do not modify `/Users/elvis/file/develop/opensource/openharness`.

**Goal:** Add stable capability routing, schema-5 agent-instance identity,
layered authorization, Confirmation Leases, governed learning candidates, and
High independent Review while retaining the existing two-Skill ownership model
and evidence-based completion boundary.

**Architecture:** `openspec-superpower-change` remains the control plane and
canonical decision owner. `codex-brief-antigravity-review` remains the Brief,
Report, and Review governor. Schema 5 separates product, instance, role, profile,
owner, and provenance; active schema-4 contracts drain under schema 4. Portable
source and managed governance changes continue through the existing transactional
Codex -> Antigravity CLI -> Grok CLI synchronization gate.

**Tech Stack:** Markdown Agent Skills, OpenSpec, Python 3 standard library,
`unittest`, SHA-256 evidence references, existing cross-CLI sync validator.

---

## Scope and files

### `openspec-superpower-change`

- Modify: `SKILL.md`
- Create: `references/agent-capability-routing.md`
- Create: `references/confirmation-lease.md`
- Create: `references/learning-candidate-pipeline.md`
- Modify: `references/handoff-contract.md`
- Modify: `references/approved-implementation-workflow.md`
- Modify: `references/self-evolution-rule.md`
- Modify: `references/step-evidence-gate.md`
- Modify: `references/superpowers-adapter.md`
- Modify: `references/sync-checklist.md`
- Modify: `references/shared-global-governance.md`
- Modify: `references/cross-cli-portable-manifest.json`
- Modify: `scripts/validate_core_gates.py`
- Modify: `tests/test_workflow_rules.py`
- Modify: `README.md`, `README_cn.md`, `CHANGELOG.md`
- Create: `docs/design/2026-07-11-tiered-agent-collaboration-governance.md`
- Modify: `openspec/changes/add-tiered-agent-collaboration-governance/tasks.md`

### `codex-brief-antigravity-review`

- Modify: `SKILL.md`
- Modify: `references/handoff-contract.md` byte-identically with the router copy
- Modify: `references/brief-template.md`
- Modify: `references/report-template.md`
- Modify: `references/review-template.md`
- Modify: `references/timeout-audit-template.md`
- Modify: `references/agy-dispatch-template.md`
- Modify: `scripts/validate_templates.py` while preserving the shared validator core
- Modify: `tests/test_workflow_rules.py`
- Modify: `agents/openai.yaml` only if route wording must match the implemented route
- Modify: `README.md`, `README_cn.md`, `CHANGELOG.md`
- Create: `docs/design/2026-07-11-tiered-agent-collaboration-governance.md`

### Explicit non-scope

- No concrete model names or vendor tiers as authority.
- No third top-level orchestration Skill.
- No OpenHarness changes or acceptance changes.
- No credentials, tokens, sessions, logs, caches, hooks, MCP secrets, model
  settings, binaries, or native CLI configuration outside the managed block.
- No runtime/global write, archive, backup deletion, or Git publication without
  the separately required explicit authorization.

## Task 1: Preserve approval, baseline, inventory, and rollback evidence

- [ ] 1.1 Strictly validate the approved Change and retain the exit result.
- [ ] 1.2 Record both worktree branch/status snapshots and baseline validators.
- [ ] 1.3 Inventory known `docs/agent-collab/*/status.md` files by path and only
  the non-sensitive fields `schema_version`, `change_id`, `lifecycle_state`, and
  `contract_revision`.
- [ ] 1.4 Record the baseline active-v4 result without blocking source/test
  implementation. Require `active_schema4_count=0` immediately before runtime
  schema-5 deployment; the drain gate does not rewrite historical evidence.
- [ ] 1.5 Create a timestamped structured backup under
  `/private/tmp/tiered-agent-collaboration-major-20260711-*` before the first
  implementation edit. Back up both source worktrees and the current runtime
  allowlist; global-rule backups use mode `0600`. Do not delete it without
  separate user authorization.

## Task 2: RED — capability routing, authorization, and learning

- [ ] 2.1 In `tests/test_workflow_rules.py`, add mirrored failing tests with these
  stable scenario IDs:
  - `test_tiered_01_platform_permission_reuses_safe_command_lease`
  - `test_tiered_02_platform_permission_cannot_authorize_production_deletion`
  - `test_tiered_03_ai_proposed_user_approved_provenance_is_preserved`
  - `test_tiered_04_mechanical_low_ambiguity_blocks_instead_of_designing`
  - `test_tiered_09_single_correction_creates_candidate_without_promotion`
  - `test_tiered_10_high_severity_candidate_is_proposal_only_without_approval`
- [ ] 2.2 Tests must assert validator/reference/template behavior rather than only
  prose presence. A RED failure may not be an import error or missing test ID.
- [ ] 2.3 Run each named test independently in both repositories and preserve the
  expected failure output outside the repositories.

## Task 3: RED — schema 5 and High Review

- [ ] 3.1 Add mirrored failing tests:
  - `test_tiered_05_high_review_detects_copy_field_loss_after_executor_pass`
  - `test_tiered_06_high_review_requires_independent_adversarial_probe`
  - `test_tiered_07_high_review_traces_claim_to_runtime_mechanism`
  - `test_tiered_08_same_product_instances_cannot_self_review`
- [ ] 3.2 Add focused schema-5 contract tests for immutable
  `agent_product`, `agent_instance_id`, `agent_role`, `control_plane_owner`,
  `executor_profile`, `reviewer_profile`, `decision_source`, and lease reference.
- [ ] 3.3 Add negative cases for wrong instance/role/profile, model metadata as
  authority, active-v4 drain bypass, invalid provenance, stale/revoked lease,
  manual-copy downgrade, and executor completion promotion.
- [ ] 3.4 Preserve reproducible RED evidence outside both repositories.

## Task 4: GREEN — router contracts and deterministic validators

- [ ] 4.1 Create `references/agent-capability-routing.md` with
  `control-plane-high`, `cohesive-medium`, and `mechanical-low`, their authority
  ceilings, escalation conditions, and model-name prohibition.
- [ ] 4.2 Create `references/confirmation-lease.md` with three authorization
  layers, typed lease fields, reuse matrix, invalidation rules, provenance link,
  and human-only business/production gates.
- [ ] 4.3 Create `references/learning-candidate-pipeline.md` with Candidate Card,
  local/project/global scope, conflict/duplicate handling, evidence thresholds,
  validator-first mechanical invariants, and proposal-only promotion.
- [ ] 4.4 Upgrade new contracts in both byte-identical Handoff references to
  schema 5. New schema-5 evidence uses `evidence_schema_version: 2` and binds
  `agent_product`, `agent_instance_id`, `agent_role`, and `capability_profile`
  to the immutable canonical assignment. Historical schema-4 contracts and
  schema-1 evidence remain immutable and are validated only by their existing
  workflow. Hard-block runtime deployment when a known active v4 canonical
  status exists.
- [ ] 4.5 Extend both validator cores with deterministic schema-5 field,
  immutability, assignment, instance separation, profile authority, provenance,
  lease, manual-Handoff, and drain checks. Do not read or print secret values.
- [ ] 4.6 Update router entry, approved workflow, evidence gate, Superpowers
  adapter, self-evolution, and sync guidance without weakening Non-Negotiables.
- [ ] 4.7 Run focused suites until GREEN and verify shared Handoff/validator-core
  parity from an explicit companion path rather than relying on sibling checkout
  discovery.

## Task 5: GREEN — Brief, Report, Review, and dispatch governance

- [ ] 5.1 Update Brief/dispatch templates with assigned product, instance, role,
  profile, owner, lease/provenance, partial-state audit, do-not-repeat scope,
  allowed files, stop/escalation rules, and canonical Report path.
- [ ] 5.2 Update Report templates so executors report facts, commands, diffs,
  wiring observations, and blockers but cannot mutate canonical state, broaden
  approval, promote evidence, or claim authoritative completion.
- [ ] 5.3 Update Review/timeout templates to require actual files and complete
  diff inspection, copy/transform/wiring trace, critical reruns, claim-to-mechanism
  support, and at least one independent adversarial or real business-chain probe.
- [ ] 5.4 Keep standalone non-state-changing wording lightweight. Route manually
  copied state-changing standard/strict Briefs through the schema-5 Handoff
  lifecycle; transport does not downgrade governance.
- [ ] 5.5 Update `SKILL.md`, `agents/openai.yaml` when needed, companion validator,
  and mirrored tests. Ensure executor and reviewer instance IDs differ even when
  `agent_product` is equal.

## Task 6: Portable governance, documentation, and source verification

- [ ] 6.1 Add stable managed-governance invariants for profile authority,
  three-layer authorization, instance separation, learning-candidate promotion,
  and High Review. Increment managed-rule version and manifest invariant list.
- [ ] 6.2 Add the three new router references to the portable manifest; do not add
  repository-only docs, tests, OpenSpec files, or evidence logs.
- [ ] 6.3 Update both READMEs and changelogs. Create both `docs/design` records
  with headers `文档类型` and `日志及版本`, core design, implementation result,
  evidence, rollback, unresolved gates, and TODOs.
- [ ] 6.4 Reconcile OpenSpec tasks only after their evidence exists.
- [ ] 6.5 Run:

  ```bash
  /opt/anaconda3/bin/python "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" .
  PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
  ```

  and the equivalent companion commands with `scripts/validate_templates.py`.
- [ ] 6.6 Run all ten stable forward-test IDs, cross-skill compatibility tests,
  `git diff --check`, manifest audit, and a sensitive filename/content-pattern
  audit that reports paths/findings but never secret values.
- [ ] 6.7 Perform a distinct current-diff Review. Every finding follows
  fix -> verify -> fresh Review until PASS.

## Task 7: Isolated pilots and schema-5 deployment decision

- [ ] 7.1 Using synthetic validator evidence rather than delegated agents, pilot
  a compact mechanical fixture outside OpenHarness and confirm no
  unnecessary canonical lease artifact or duplicate confirmation is created.
- [ ] 7.2 Using synthetic validator evidence rather than delegated agents, pilot
  a strict cohesive fixture with separate executor/reviewer instance
  IDs, one deliberate copy/wiring defect, and High adversarial Review. Confirm
  the defect is caught despite executor PASS and cannot be promoted.
- [ ] 7.3 Record confirmation reuse, scope drift, finding yield, false-PASS catch,
  and rollback outcome outside production/runtime roots.
- [ ] 7.4 Repeat the active schema-4 inventory. Any active v4 status makes runtime
  schema-5 deployment `BLOCKED`; never rewrite, migrate, ignore, or abandon it.

## Task 8: Runtime synchronization — explicit stop gate

- [ ] 8.1 Generate and Review a path/hash-only cross-CLI plan using the existing
  sync CLI and the two worktree sources. This read-only planning step does not
  authorize apply.
- [ ] 8.2 Stop and obtain explicit runtime/global-write authorization.
- [ ] 8.3 Only after authorization, apply and verify one target at a time in order:
  Codex -> Antigravity CLI -> Grok CLI. A failed target restores only that target
  and blocks all later targets.
- [ ] 8.4 Verify installed quick/project validators, portable parity, managed-block
  version/body hash/outside-byte preservation, deterministic Antigravity closure,
  and `grok inspect --json` discovery.
- [ ] 8.5 Run final runtime diff/sensitive audit and High Review; findings re-enter
  fix -> verify -> Review.

## Task 9: Closeout — separately authorized actions

- [ ] 9.1 Reconcile all completed task checkboxes and retain evidence references.
- [ ] 9.2 Obtain explicit archive authorization, then archive the Change and run
  strict validation against the archive/current specs.
- [ ] 9.3 Obtain explicit backup-deletion authorization before deleting any
  structured backup or temporary evidence root.
- [ ] 9.4 Obtain separate current-task authorization before `git add` or commit.
  Obtain explicit approval again for push or merge. Never infer publication from
  implementation approval.
- [ ] 9.5 Final completion requires source/runtime verification PASS, full diff and
  sensitive audit, Final Review PASS, task/archive reconciliation, and no
  unresolved blocker.

## Preflight Review checklist

Before Task 1.5 and any implementation edit, Review this exact revision for:

- approved scope and non-goals;
- exact file list and ownership boundaries;
- TDD RED credibility and stable test IDs;
- schema-4 drain semantics and historical compatibility;
- three authorization layers and separate stop gates;
- executor/reviewer instance separation and decision-owner authority;
- evidence/validator feasibility without secret disclosure;
- runtime sync, rollback, archive, backup, and Git authorization boundaries.

Result must be `PASS` or `BLOCKED`. Any finding requires revising this plan and
Reviewing the new revision; an older PASS cannot authorize a newer plan.
