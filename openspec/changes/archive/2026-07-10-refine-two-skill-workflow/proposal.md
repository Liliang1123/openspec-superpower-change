# Change: Refine the two-skill workflow boundary and closure loop

## Why

`openspec-superpower-change` and `codex-brief-antigravity-review` currently overlap on task breakdown, code review, and external-agent coordination. The brief skill also requires a Handoff Contract even for standalone prompt writing or read-only diff review. Their shared state cannot represent repair attempts, recovery from `BLOCKED`, or the handback from a final external batch to final verification. These gaps make lightweight work too heavy and allow verified-but-unreviewed work to appear complete.

## What Changes

- Make `openspec-superpower-change` the only entry gate for state-changing development work, OpenSpec decisions, Superpowers routing, evidence profiles, and final completion.
- Give `codex-brief-antigravity-review` two explicit paths:
  - standalone lightweight prompt/brief/checklist generation and read-only review, without Handoff or OpenSpec;
  - Handoff-backed external execution governance, without re-deciding approval or risk.
- Define one canonical Handoff Contract in `status.md` with lifecycle, attempt, review result, blocker recovery, and final-verification state.
- Require `Implement -> Verify -> Review -> Fix` loops. `FAIL` and `BLOCKED` remain on the same batch; final batch `PASS` returns to the router and is not task completion.
- Avoid duplicate OpenSpec and Superpowers artifacts: OpenSpec owns the approved change contract; Superpowers owns implementation discipline after approval.
- Add standard-library regression tests for routing, state transitions, validator fallback parsing, and cross-skill schema parity.
- Synchronize the open-source repositories and installed runtime skill copies after validation.

## Impact

- Affected specs: `skill-workflow-governance`.
- Affected projects: `openspec-superpower-change`, `codex-brief-antigravity-review`, and their installed runtime copies.
- Affected artifacts: both `SKILL.md` files, routing/workflow references, Handoff Contract, Brief/Report/Review templates, metadata, validators, tests, README/AGENTS guidance, and design documentation.
- Compatibility: existing external workflows must migrate their canonical status block to schema version 2; standalone read-only usage becomes lighter.
- Risk profile: `standard` Major self-evolution. No security, persistence, or public API runtime change is involved.

## Approval Record

The user explicitly requested complete implementation, local validation, separate commits, and push on 2026-07-10. That direct instruction is the implementation and publication approval for this scoped contract. Any scope expansion still requires a new decision.
