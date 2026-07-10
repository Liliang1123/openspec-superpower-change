## 1. Contract and baseline

- [x] 1.1 Record Gate 0, user approval, clean Git state, and structured backup.
- [x] 1.2 Reconcile and archive the completed previous OpenSpec change.
- [x] 1.3 Capture adversarial RED cases for empty evidence, blank blockers,
  flags-only completion, and non-persistable final-gate progress.
- [x] 1.4 Validate this OpenSpec change with strict mode.

## 2. Tests first

- [x] 2.1 Add schema-3 tests for evidence fields and sequential final gates.
- [x] 2.2 Add negative tests for blank commands/blockers, bool integers, unsafe
  artifact paths, and readonly-field supersets.
- [x] 2.3 Add routing/Superpowers adapter and Plan/Brief Preflight assertions.
- [x] 2.4 Make cross-repository parity tests safe for standalone clones.

## 3. Implementation

- [x] 3.1 Upgrade the shared Handoff Contract and both validators.
- [x] 3.2 Update Brief/Report/Review fingerprints and pre-dispatch Review rules.
- [x] 3.3 Tighten both skill triggers, Direct Change wording, Self-Evolution
  approval, and Superpowers execution mapping.
- [x] 3.4 Add OpenSpec task reconciliation/archive completion rules.
- [x] 3.5 Update README, changelog, and project design documentation.

## 4. Verification and publication

- [x] 4.1 Run both validators, both unittest suites, and `quick_validate.py` on
  source and runtime copies.
- [x] 4.2 Run adversarial RED-to-GREEN cases and fresh routing forward-tests.
- [x] 4.3 Complete independent routing, integration, and closure Reviews; fix and
  re-review every actionable finding.
- [ ] 4.4 Reconcile this task list, archive the change, and validate OpenSpec after
  archive.
- [x] 4.5 Check final diffs, sensitive information, temporary files, and scope.
- [ ] 4.6 Commit and push each repository separately, then remove the temporary
  backup only after all publication checks pass.
