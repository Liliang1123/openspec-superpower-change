# Project Learning Gate Forward-Test Evidence

## Method

- Baseline: structured pre-change snapshot at
  `/private/tmp/context-learning-gate-self-evolution-20260715-175013/feature-router/`.
- Candidate: current feature worktree after GREEN source implementation.
- Isolation: each scenario reads only its declared reference/fixture and requires
  the baseline to miss the complete contract (`RED`) while the candidate must
  contain and validate the complete contract (`GREEN`).
- Constraint: no new subagent was spawned because the active collaboration rule
  forbids spawning without an explicit subagent request. Independent High Review
  remains a separate required gate; these fixtures do not impersonate it.

## Results

| Scenario | Baseline | Current |
|---|---|---|
| Clear localized task skips grill ceremony | RED | GREEN |
| Ambiguous domain language uses grill or complete fallback | RED | GREEN |
| Human correction plus independent Review triggers promotion | RED | GREEN |
| Single low-risk task-local correction remains non-blocking | RED | GREEN |
| Explicit archive/distill request always runs the audit | RED | GREEN |
| Qagent-shaped lesson separates semantics, engineering invariant, and regression | RED | GREEN |
| Ignored canonical context cannot satisfy durability | RED | GREEN |
| Chat-only archive and prose-only enforcement are rejected | RED | GREEN |

Summary: `forward_scenarios=8 pass=8`, command exit 0.

The durable focused unittest for the automatic/explicit triggers also passed on
the same source revision. No private qagent code, conversation transcript,
customer data, credential, token, or native CLI configuration was copied into
the fixture or evidence.

## Interpretation

The forward evidence proves the new source contract is absent from the preserved
baseline and present in the candidate across both lean and full routes. It does
not by itself prove final completion: full validation, independent Review,
runtime synchronization, Project Learning Closeout, and fresh final verification
remain pending.
