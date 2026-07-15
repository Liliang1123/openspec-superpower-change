# Project Learning Gate Review Corrections

Date: 2026-07-15

## Review result before correction

Independent High Review returned `FAIL` with two findings:

1. explicit archive-and-distill requests were not discoverable from the
   `SKILL.md` frontmatter description;
2. the core validator searched concatenated learning artifacts, so required
   closeout rules could be relocated into the Candidate Card template without
   failing validation.

## RED evidence

Focused command:

```bash
python3 -m unittest \
  tests.test_workflow_rules.WorkflowRulesTest.test_description_routes_explicit_archive_and_distill_requests \
  tests.test_workflow_rules.WorkflowRulesTest.test_project_learning_validator_binds_rules_to_owned_artifacts -v
```

Observed before correction: one assertion failure for the missing frontmatter
trigger and one error because the artifact-specific validator did not exist.

## Correction

- Added `archive and distill`, `Project Learning Closeout`, and `归档并蒸馏` to
  the `SKILL.md` frontmatter description.
- Added `validate_project_learning_gate()` in the router-specific validator
  section, outside the byte-identical shared validator core.
- Bound entry/final routing to `SKILL.md` and the approved workflow, closeout
  triggers/order/blocking/safety to `project-learning-closeout.md`, and fixed
  Candidate Card fields/enforcement/safety to its template.
- Added negative relocation probes for both closeout and template artifacts.

## GREEN evidence

The focused tests pass and `validate_core_gates.py` rejects the prior relocation
bypass. The complete source matrix then passed:

- skill quick validation;
- core gate validation;
- 127 unit tests with the companion feature worktree present;
- strict OpenSpec validation, 2/2;
- `git diff --check`;
- path-only sensitive audit, 0 categories.

Runtime synchronization remains intentionally pending until the corrected
revision receives a fresh independent High Review `PASS`.
