# Learning Candidate Card: Dual-Parser Fixtures

```yaml
status: promoted
event_kind: correction
severity: medium
scope: project-local
promotion_trigger: explicit-archive-distill
symptom: A schema-4 inventory fixture passed the fallback parser but failed PyYAML after cherry-pick to main.
prior_assumption: Passing the dependency-free test run implied the fenced YAML fixture was valid for every supported parser.
correction_or_evidence: The fixture must be standard YAML and the affected suite must run through both PyYAML and fallback paths.
generalized_invariant: Shared YAML fixtures require dual-parser validation; fallback-only PASS cannot establish parity.
independent_reproductions: Homebrew fallback PASS; Anaconda PyYAML failure on the byte-identical fixture
independence_rationale: Two independently resolved interpreters exercised different supported parser implementations against the same committed bytes.
duplicate_or_conflict_result: no conflict; adds the parser-parity invariant to existing project validation guidance
target_artifacts: docs/engineering-invariants.md; tests/test_workflow_rules.py; docs/design/2026-07-15-publication-validation-correction.md
mechanical_enforcement: required
mechanical_enforcement_reason: The corrected standard-YAML fixture is executed by the same deterministic inventory test under both interpreters.
verification: focused 1/1 and full 128/128 suites passed with both Homebrew fallback and Anaconda PyYAML
review_result: pass
decision_owner: codex
decision_provenance: evidence-discovered during explicitly requested archive-and-distill publication closeout
```

## Non-sensitive provenance

- `tests/test_workflow_rules.py` —
  `ca29762996b90fd56d0fd8ff6d5bfee92050c73ae29e386681baebb0a4e48573`
- `docs/engineering-invariants.md` —
  `a144f6d34cc4a59a4b0148b1bbcdc7c3f2ec209e22196e9112687e98f03c2446`
- `docs/design/2026-07-15-publication-validation-correction.md` —
  `948cb165d8de4f07ccca6b17e2009264e5eb39be76c5e0bdd3bc79b4b9ca1f56`

No transcript, private prompt, credential, token, customer data, or private
source content is stored in this Candidate Card.
