# Tasks: add-notification-preferences-endpoint

## 1. Proposal and contract

- [x] 1.1 Inspect existing root specs and active changes.
- [x] 1.2 Draft proposal, design, tasks, and the
  `notification-preferences-api` spec delta.
- [x] 1.3 Run strict OpenSpec validation and correct every finding.
- [ ] 1.4 Present the exact change-id and record explicit approval before
  implementation.

## 2. Post-approval planning and Preflight

- [ ] 2.1 After approval, refresh Gate 0 for strict authenticated public-API
  implementation and create a Superpowers implementation plan.
- [ ] 2.2 Preflight Review the current plan against every requirement and
  scenario before changing application code.

## 3. TDD implementation

- [ ] 3.1 Add failing endpoint tests for bearer-auth protection and all four
  successful Boolean combinations.
- [ ] 3.2 Add failing validation tests proving a non-Boolean `email` or `push`
  returns HTTP `400` without type coercion.
- [ ] 3.3 Implement only `POST /notifications/preferences` using the existing
  bearer-auth boundary and make the focused tests pass.
- [ ] 3.4 Verify that the successful response echoes only the accepted `email`
  and `push` Boolean fields required by this change.
- [ ] 3.5 Verify that no compatibility alias or migration is introduced.

## 4. Verification and Review

- [ ] 4.1 Run the focused endpoint tests and repository-wide official checks.
- [ ] 4.2 Run a distinct High Review over the complete diff, auth wiring,
  validation behavior, response contract, route registration, and migration
  scope.
- [ ] 4.3 Fix every actionable finding, re-run verification, and repeat Review
  until PASS.
- [ ] 4.4 Persist fresh final verification and final Review evidence, reconcile
  tasks, and archive the OpenSpec change only when repository policy permits.
