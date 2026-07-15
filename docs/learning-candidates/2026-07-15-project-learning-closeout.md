# Learning Candidate Card: Project Learning Closeout

```yaml
status: promoted
event_kind: review-finding
severity: high
scope: project-local
promotion_trigger: explicit-archive-distill
symptom: A fresh session could miss mandatory project learning, and misplaced rules could still pass validation.
prior_assumption: Rules in loaded prose plus concatenated keyword checks were sufficient to guarantee closeout behavior.
correction_or_evidence: Frontmatter routing and artifact-owned negative validation are both required.
generalized_invariant: Mandatory workflow paths must be entry-discoverable, artifact-bound, and mechanically regression-tested.
independent_reproductions: user correction; independent High Review frontmatter probe; independent High Review relocation probe
independence_rationale: The user identified the missing project-learning lifecycle, while a distinct reviewer independently demonstrated two concrete bypasses against the implemented revision.
duplicate_or_conflict_result: no conflicting project invariant; promoted as the canonical local rule
target_artifacts: AGENTS.md; docs/engineering-invariants.md; SKILL.md; references/project-learning-closeout.md; scripts/validate_core_gates.py; tests/test_workflow_rules.py
mechanical_enforcement: required
mechanical_enforcement_reason: Deterministic tests reject absent frontmatter triggers and closeout/template responsibility relocation.
verification: focused correction tests, core validator, 127-test source suite, strict OpenSpec validation, and cross-CLI verify-all passed
review_result: pass
decision_owner: codex
decision_provenance: ai-proposed/user-approved plus explicit user archive-and-distill instruction
```

## Non-sensitive provenance

- `openspec/changes/add-project-learning-gate/design.md` —
  `eda1a6f7aa1502f634cd4712d3a5d3ba782675db1e1f4b667c316984bd0a4f9b`
- `docs/design/2026-07-15-project-learning-gate-review-corrections.md` —
  `b405f02506d807fc92ea1ed893c58c3819030caa9175d52645e98b52acbb1345`
- `tests/test_workflow_rules.py` —
  `e62d25f69f294a55aa18c04e5fd8cf955fd166cf7c79bbbf165b7538beee2852`
- `scripts/validate_core_gates.py` —
  `257fa35564753330f389358e40e94df265826b41659ef183dbafae5cf11b9e55`

No chat transcript, private prompt, credential, token, customer data, or private
source file is stored in this Candidate Card.
