---
name: openspec-superpower-change
description: Project-level AI development change gate and governance orchestrator. Use when handling development tasks, bugfixes, direct code changes, regression fixes, OpenSpec proposal or approval, architecture/design review, multi-step planning, TDD, systematic debugging, Superpowers execution, Step Evidence Gate, or verification-before-completion. It decides when to use grill-with-docs for domain clarification, OpenSpec for approved change contracts, and Superpowers for implementation discipline.
---

# OpenSpec + Superpowers Change Gate

Use this skill as the default entry gate for development change work. It is not ordinary SDD. It orchestrates domain clarification, approved change contracts, disciplined implementation, and verification evidence.

## Core responsibility

- Read local project instructions before changing anything.
- Classify the request mode before acting.
- Use `grill-with-docs` when domain language, boundaries, or design choices are unclear.
- Use OpenSpec when a change needs an approved contract.
- Use Superpowers when approved or non-trivial work needs planning, TDD, debugging, implementation, review, or verification.
- Use Step Evidence Gate before moving across gated implementation steps.
- Provide verification evidence before any completion claim.


## Mandatory Entry Gate

Before any file modification, state-changing command, implementation work, or proposal artifact creation, the agent MUST complete Gate 0. Reading files and non-mutating inspection are allowed before Gate 0 only to classify the request and choose references.

Gate 0 requires:

1. State active mode: Review-only / Discovery First / OpenSpec proposal / Approved implementation / Direct Change / Self-Evolution.
2. List references read from this skill and why they are sufficient.
3. State whether OpenSpec is required: yes / no / uncertain, with a one-line reason.
4. State required Superpowers sub-skills for the task.
5. State risk level, next action, and whether user confirmation is required before changing state.

Direct Change is forbidden until an explicit gate says otherwise when the task touches agent runtime, tool exposure, cache strategy, request routing, skill routing, workflow behavior, security or sandbox boundaries, public/user-visible/operator-visible behavior, cross-module behavior, or multi-file runtime behavior.

If the user interrupts due to process concerns, stop implementation immediately and run an interrupted / dirty diff audit before continuing.

## Reference Read Matrix

Read the current `SKILL.md` first, then read the references below before the matching action. Do not treat this matrix as optional progressive disclosure.

| Task type | Required references |
|---|---|
| Any implementation or bugfix | `references/request-modes.md`, `references/openspec-decision-rule.md`, `references/step-evidence-gate.md` |
| Direct Change candidate | `references/direct-change-rule.md`, `references/step-evidence-gate.md` |
| Bugfix / regression fix | `references/request-modes.md`, `references/direct-change-rule.md`, `references/step-evidence-gate.md` |
| Runtime / tool / cache / workflow change | `references/openspec-decision-rule.md`, `references/proposal-workflow.md`, `references/approved-implementation-workflow.md`, `references/step-evidence-gate.md` |
| Skill self-evolution | `references/self-evolution-rule.md`, `references/step-evidence-gate.md` |
| Review-only / plan review | `references/request-modes.md`, `references/response-patterns.md` |
| Sync between runtime and open-source copies | `references/sync-checklist.md` |

## Superpowers Required Mapping

When the matching scenario occurs, the listed Superpowers are REQUIRED unless the user explicitly forbids their use; if forbidden, state the risk and choose the safest reduced path.

| Scenario | Required Superpowers |
|---|---|
| Bug / unexpected behavior | `superpowers:systematic-debugging` |
| Implementing a bugfix, feature, test, or approved behavior | `superpowers:test-driven-development` |
| Multi-step implementation plan | `superpowers:writing-plans` |
| Claiming completion, fixed, passing, or ready | `superpowers:verification-before-completion` |
| Editing this skill or another skill | `superpowers:writing-skills` |
| Larger implementation before merge/PR | `superpowers:requesting-code-review` |

## Request modes

1. **Review-only**: assess, critique, summarize, improve, or generate a prompt. Do not modify files. State whether future implementation would require OpenSpec.
2. **Discovery First**: clarify domain terms, boundaries, lifecycle, actors, or design trade-offs before deciding the change contract.
3. **OpenSpec proposal**: create or update proposal artifacts for new capabilities, behavior changes, architecture, security, migration, API/schema, data lifecycle, deployment/recovery, operator-visible behavior, or skill workflow changes.
4. **Approved implementation**: after proposal approval, create a Superpowers implementation plan and execute with TDD/debugging, evidence gates, and verification.
5. **Direct Change**: localized bug fixes restoring intended behavior, typo/comment/formatting updates, tests for existing behavior, docs-only updates without contract impact, or low-risk config changes.
6. **Self-Evolution**: improve this skill itself only with backup, scope classification, validation, and forward-test; use OpenSpec for major workflow or gate changes.

## Change paths

- **Lightweight path**: low-risk direct changes; no OpenSpec artifacts; scoped evidence and targeted verification.
- **Standard path**: already-approved or existing-contract work; Superpowers plan for multi-step work; compact Step Evidence Gate; verification-before-completion.
- **Strict path**: high-risk or contract-changing work; OpenSpec proposal and approval first; then Superpowers plan; then Step Evidence Gate and formal verification.

## Non-negotiables

- Do not let `CONTEXT.md` replace OpenSpec proposal artifacts.
- Do not let OpenSpec `tasks.md` replace a Superpowers implementation plan.
- Do not use Superpowers planning to bypass OpenSpec approval.
- Do not implement OpenSpec-required work before approval.
- Do not move to the next gated step until the current evidence gate passes.
- Do not claim completion without verification evidence.
- Do not compress official artifacts so much that evidence, risks, or decisions become unauditable.
- Self-evolution cannot weaken approval gates, evidence gates, verification requirements, or user-control boundaries.

## Required artifacts for OpenSpec-backed work

- OpenSpec artifacts: `openspec/changes/<change-id>/proposal.md`, `tasks.md`, optional `design.md`, and spec deltas.
- Superpowers implementation plan: `docs/superpowers/plans/YYYY-MM-DD-<change-id>.md`.
- Step Evidence Gate signoff notes for gated implementation steps.
- Verification evidence before completion.

## Reference guide

Read only the references needed for the current request:

- `references/workflow-overview.md`: overall routing, artifacts, and governance boundaries.
- `references/local-instruction-checkpoint.md`: root `AGENTS.md`, `openspec/AGENTS.md`, specs, active changes, and `CONTEXT.md` checks.
- `references/request-modes.md`: detailed rules for review-only, discovery, proposal, approved implementation, and direct change.
- `references/openspec-decision-rule.md`: when OpenSpec is required or can be skipped.
- `references/proposal-workflow.md`: proposal artifact creation and validation workflow.
- `references/approved-implementation-workflow.md`: Superpowers implementation planning and execution workflow.
- `references/direct-change-rule.md`: low-risk direct change workflow.
- `references/step-evidence-gate.md`: compact and full evidence templates and signoff rules.
- `references/response-patterns.md`: response patterns for each request mode.
- `references/fablecodex-caveman-review.md`: FableCodex and caveman-style boundaries.
- `references/self-evolution-rule.md`: controlled self-evolution rules for modifying this skill itself.
- `references/sync-checklist.md`: local/open-source synchronization checklist and validation gates.
