# Tasks: add-governed-caveman-lite

## 1. Proposal and approval

- [x] 1.1 Capture current-rule baseline behavior with a fresh read-only agent.
- [x] 1.2 Create proposal, design, tasks, and governance spec delta.
- [x] 1.3 Run strict OpenSpec validation and correct every finding.
- [x] 1.4 Review the proposal for scope, trigger, governance, validation, sync,
  and rollback completeness.
- [x] 1.5 Present the exact change-id and record explicit approval of this scoped
  contract.

## 2. RED evidence and implementation plan

- [x] 2.1 Create timestamped structured source/runtime backups outside skill
  discovery roots.
- [x] 2.2 Write and Preflight Review the Superpowers implementation plan.
- [x] 2.3 Add a failing contract test for the canonical enable/disable phrases,
  lite semantics, conversation lifecycle, fallback, protected surfaces, and
  latest-explicit-mode precedence after a prior Caveman instruction.
- [x] 2.4 Run the focused test and preserve the expected RED result.

## 3. GREEN source implementation

- [x] 3.1 Add the minimal built-in `governed-caveman-lite` profile to `SKILL.md`.
- [x] 3.2 Update response patterns and bilingual usage documentation.
- [x] 3.3 Add artifact-owned validator checks and focused negative fixtures.
- [x] 3.4 Confirm portable manifest membership and generate required path/hash
  sync evidence for the changed files.
- [x] 3.5 Run focused GREEN tests and refactor without changing behavior.

## 4. Source validation and Review

- [x] 4.1 Run `quick_validate.py` with PyYAML.
- [x] 4.2 Run `validate_core_gates.py` and the full unittest suite with the
  dependency-free interpreter.
- [x] 4.3 Run isolated forward-tests for activation, protected artifacts,
  disable behavior, latest-explicit-mode precedence after a prior Caveman
  instruction, missing external Caveman, and unchanged default behavior.
- [x] 4.4 Run complete-diff Review; fix every actionable finding and repeat
  verification and Review until PASS.

## 5. Runtime synchronization

- [x] 5.1 Inventory active external contracts and required runtime targets.
- [x] 5.2 Generate and Review the path/hash-only sync plan.
- [x] 5.3 Apply and verify Codex, Antigravity CLI, and Grok CLI one target at a
  time; restore and stop on failure.
- [x] 5.4 Run verify-all, discovery checks, and final cross-target Review.

## 6. Closeout

- [x] 6.1 Run Project Learning Closeout for any qualifying correction history.
- [x] 6.2 Run fresh final project/runtime validation and final Review.
- [x] 6.3 Reconcile tasks, archive the OpenSpec change when repository semantics
  permit, and run strict post-archive validation.
- [x] 6.4 Remove temporary backups after all rollback decisions resolve and
  report evidence, residual risks, and publication status.
