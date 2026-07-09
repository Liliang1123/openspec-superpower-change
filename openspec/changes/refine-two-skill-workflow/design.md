# Design: Refine the two-skill workflow boundary and closure loop

## Context

The current skills already separate routing from external execution in principle, but their trigger descriptions overlap and the external governor has no standalone lightweight path. The shared contract expresses batch counts but not review attempts, blockers, or final handback. Superpowers and OpenSpec can also create duplicate design/approval artifacts when their ownership is not stated explicitly.

## Goals / Non-Goals

### Goals

- Make the primary skill decision deterministic.
- Preserve lightweight prompt/review work without governance artifacts.
- Make review and correction mandatory before completion.
- Keep one canonical external collaboration state.
- Test the rules without adding dependencies or frameworks.

### Non-Goals

- Merge the two skills.
- Replace OpenSpec, Superpowers, or project `AGENTS.md`.
- Require external agents or Handoff artifacts for inline/compact work.
- Add a generic workflow engine or persistent runtime service.

## Decisions

### 1. Deterministic routing priority

1. Any request to modify, fix, implement, dispatch, or change behavior enters `openspec-superpower-change`.
2. Existing valid Handoff plus external execution/report/batch review enters the brief skill's handed-off path.
3. Prompt/brief/checklist generation or read-only diff/artifact review enters the brief skill's standalone path.
4. Review of architecture, OpenSpec necessity, implementation authorization, or completion evidence enters the change gate.

“Review and fix” is implementation, not standalone review.

### 2. No duplicate approval artifacts

OpenSpec owns what/why/acceptance and the approval record. Superpowers brainstorming may clarify alternatives before or while drafting the proposal, but its outcome is written into the OpenSpec design rather than a duplicate design artifact. After approval, `writing-plans` owns implementation steps; OpenSpec `tasks.md` remains a contract checklist and does not replace the plan.

### 3. Profile-aware review

- `compact`: focused validation plus inline diff/self-review; no separate review artifact unless requested.
- `standard`: a distinct review pass is mandatory.
- `strict`: an independent review pass and all real acceptance layers are mandatory.

Any review finding restarts correction, verification, and review. No unresolved finding can be carried into a completion claim.

### 4. Canonical external state and lifecycle

Only `docs/agent-collab/<change-id>/status.md` owns the machine-readable marker block. Briefs and reports reference the status path and record a fingerprint; they do not embed competing state copies.

Lifecycle:

```text
ready-for-brief -> ready-for-execution -> ready-for-review
ready-for-review + FAIL -> needs-fix -> next attempt on same batch
ready-for-review + BLOCKED -> blocked -> resume same batch when condition is met
ready-for-review + PASS (non-final) -> next batch ready-for-brief
ready-for-review + PASS (final) -> awaiting-final-verification
router final verification + final review PASS -> complete
```

The contract records `lifecycle_state`, `attempt`, `last_review_result`, `final_review_result`, `blocker_owner`, `resume_condition`, and `final_verification`. Attempt-specific Brief/Report/Review paths preserve audit history.

### 5. Source/runtime synchronization

Open-source repositories are the source of truth. Runtime copies receive the same logical skill, references, templates, validators, and metadata after source validation. Runtime-only discovery files are not copied back into source.

## Risks / Trade-offs

| Risk | Mitigation |
|---|---|
| Schema version 2 requires status migration | Document the required fields and fail closed with a clear `BLOCKED` result. |
| More state fields could make compact work heavy | The contract exists only for external handed-off execution, never for standalone or inline compact work. |
| Mandatory review could duplicate verification | Define review as scope/contract/diff assessment; reuse verification evidence while still rerunning critical checks by profile. |
| Runtime/source drift | Add parity tests and run validation on all four copies before cleanup. |

## Rollback

Restore both source and runtime trees from `/private/tmp/two-codex-skills-self-evolution-20260710-064702/`, or revert the new repository commits after push. Temporary backups remain until all validations, pushes, and final checks pass.
