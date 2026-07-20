# Learning Candidate Card: External CLI Debug Trace Hygiene

```yaml
status: promoted
event_kind: security
severity: high
scope: project-local
promotion_trigger: high-severity
symptom: A private external-CLI debug trace used for route-load evidence contained runtime authentication material and was unsafe to quote or retain as durable evidence.
prior_assumption: A trace stored in a private temporary directory with mode 0600 was sufficiently safe to inspect, quote, or retain until ordinary cleanup.
correction_or_evidence: File permissions are containment, not redaction; raw CLI traces remain sensitive temporary evidence and durable records must retain only sanitized metadata.
generalized_invariant: Never quote, echo, or durably promote raw external-CLI debug traces; keep them mode 0600 only while required, persist sanitized path/hash/result metadata, and remove the raw trace after final gates.
independent_reproductions: one observed high-severity security event during the Grok route-load forward test
independence_rationale: The high-severity security trigger requires one established event rather than two independent low-risk corrections.
duplicate_or_conflict_result: Complements the existing sensitive-data, temporary-file, and cleanup rules without changing their authority or the approved workflow scope.
target_artifacts: docs/engineering-invariants.md; tests/test_workflow_rules.py
mechanical_enforcement: required
mechanical_enforcement_reason: A deterministic repository test pins the handling rule and rejects raw debug-log or debug-JSONL artifacts in durable documentation, OpenSpec, and reference roots.
verification: focused regression RED observed; focused GREEN passed under Python 3.11.7 and 3.14.2; independent learning Review PASS
review_result: pass
decision_owner: codex
decision_provenance: evidence-discovered during approved implementation closeout and promoted by the high-severity Project Learning threshold
```

## Non-sensitive provenance

- `docs/design/evidence/2026-07-20-prompt-collision-and-route-load-forward-tests.md` —
  `5f15ef4eb828cbfab7a0df60687c5ace465b95bf66e1702f7b53702f00d3cece`
- `docs/design/evidence/2026-07-20-runtime-sync-results.md` —
  `a8cc0c505dd8258182a9170748b06f7a72fca2666502808de71b024543a56358`

No raw trace, transcript, private prompt, credential, token, customer data, or
private source content is stored in this Candidate Card.
