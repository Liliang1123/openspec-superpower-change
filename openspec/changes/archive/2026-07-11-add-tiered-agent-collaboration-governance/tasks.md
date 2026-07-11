## 1. Approval and baseline

- [x] 1.1 Strictly validate this Change and record explicit approval of the exact
  change-id `add-tiered-agent-collaboration-governance` and scoped contract.
- [x] 1.2 Inventory active schema-4 Handoffs, current runtime parity, dirty Git
  state, and existing permission/decision artifacts without reading secret values.
- [x] 1.3 Block schema-5 deployment until every active schema-4 Handoff reaches
  its existing terminal state; do not rewrite or silently migrate it.
- [x] 1.4 After approval and immediately before implementation, create a new
  timestamped structured backup outside every Skill discovery root.

## 2. RED forward-tests

- [x] 2.1 Add failing capability-routing tests for High/Medium/Low authority,
  escalation, forbidden decisions, and same-product multi-instance separation.
- [x] 2.2 Add failing three-layer authorization and Confirmation Lease tests for
  reuse, invalidation, production approval, archive, promotion, and Git boundaries.
- [x] 2.3 Add failing decision-source and Learning Candidate tests, including
  single-correction non-promotion and repeated high-severity proposal-only behavior.
- [x] 2.4 Add failing external-execution and High Review tests for manual
  copy/paste Briefs, actual diff inspection, wiring trace, claim-to-mechanism
  checks, and independent adversarial probes.
- [x] 2.5 Preserve reproducible RED evidence outside the repositories; failures
  must reflect missing behavior rather than missing test IDs or imports.

## 3. Router Skill implementation

- [x] 3.1 Add `references/agent-capability-routing.md` with stable profiles,
  authority ceilings, escalation rules, and model-name prohibition.
- [x] 3.2 Add `references/confirmation-lease.md` with the three authorization
  layers, lease fields, reuse matrix, invalidation, and human-only gates.
- [x] 3.3 Add `references/learning-candidate-pipeline.md` with Candidate Card,
  scope classification, evidence threshold, conflict handling, and promotion gate.
- [x] 3.4 Upgrade new Handoff creation and core validation to schema 5 with
  product/instance/role separation, immutable owner/profile/provenance fields,
  and active-v4 drain enforcement.
- [x] 3.5 Update approved implementation, self-evolution, evidence, and sync
  guidance without weakening existing Non-negotiables.

## 4. Brief governor implementation

- [x] 4.1 Update Brief templates with profile, instance, partial-state audit,
  do-not-repeat scope, escalation, authorization, and Report contract fields.
- [x] 4.2 Update Report templates so executors report facts and cannot promote
  canonical state or final completion.
- [x] 4.3 Update Review templates to require actual diff, production wiring,
  claim-to-mechanism trace, critical reruns, and an independent probe.
- [x] 4.4 Govern manually copied state-changing standard/strict Briefs through
  the Handoff route while preserving lightweight standalone prompt work.
- [x] 4.5 Extend the companion validator and mirrored tests for schema 5,
  instance separation, profile authority, lease/provenance, and Review evidence.

## 5. Verification, pilot, synchronization, and closeout

- [x] 5.1 Run source quick validators, project validators, unittest suites,
  cross-skill compatibility tests, RED/GREEN forward-tests, sensitive audit,
  and diff Review; fix and Review every finding.
- [x] 5.2 Update README/changelog and both `docs/design` closeout records with
  document type and version log.
- [x] 5.3 After explicit runtime/global-write authorization, synchronize required
  Codex, Antigravity CLI, and Grok CLI targets one at a time and prove parity,
  installed validation, managed-block integrity, and discovery.
- [x] 5.4 Run two isolated pilots without changing OpenHarness acceptance: one
  compact mechanical slice and one strict cohesive implementation plus High
  adversarial Review; record confirmation reuse, scope drift, finding yield, and
  false-PASS catch.
- [x] 5.5 Reconcile tasks, obtain archive authorization, archive, run strict
  validation, and complete final diff/sensitive Review.
- [x] 5.6 Clean temporary backups only under separate explicit user authorization.
- [ ] 5.7 Keep Git staging, commit, push, merge, and publication under separate
  explicit user authorization.
