---
name: openspec-superpower-change
description: "Use when handling development changes, bugfixes, architecture or code review, OpenSpec proposals/approvals, implementation plans, task or step breakdowns, TDD/debugging, external-agent handoff, skill/workflow routing, or completion verification; also trigger on 变更评审、实施计划、任务拆解、外部 Agent 协作."
---

# OpenSpec + Superpowers Change Gate

Project-level AI development change gate. It decides whether work is review-only,
discovery, OpenSpec proposal, approved implementation, direct change, or
self-evolution; then routes to the right contract, implementation discipline,
evidence, and completion verification.

## Mandatory Entry Gate

Before any file modification, state-changing command, implementation, or
proposal artifact creation, complete Gate 0:

1. Mode: Review-only / Discovery First / OpenSpec proposal / Approved
   implementation / Direct Change / Self-Evolution.
2. References read and why sufficient.
3. OpenSpec decision: yes / no / uncertain, with reason.
4. Required Superpowers sub-skills.
5. Risk level, next action, and whether user confirmation is required.

Inspection-only reads are allowed before Gate 0 only to classify the request.
If the user interrupts due to process concerns, stop and run the interrupted /
dirty diff audit from `references/step-evidence-gate.md`.

## Router Role

`openspec-superpower-change` owns request classification, OpenSpec approval
routing, risk/evidence profile selection, batch profile selection, Handoff
Contract creation, and final verification-before-completion. After external
execution starts, `codex-brief-antigravity-review` owns Brief, Report, Review,
and batch promotion mechanics.

## Reference Read Matrix

Read `SKILL.md` first, then the matching references:

| Task | Required references |
|---|---|
| Review-only / plan review | `references/request-modes.md`, `references/response-patterns.md` |
| Implementation / bugfix | `references/request-modes.md`, `references/openspec-decision-rule.md`, `references/step-evidence-gate.md` |
| Direct Change candidate | `references/direct-change-rule.md`, `references/step-evidence-gate.md` |
| Runtime / tool / workflow change | `references/openspec-decision-rule.md`, `references/proposal-workflow.md`, `references/approved-implementation-workflow.md`, `references/step-evidence-gate.md` |
| External-agent execution | `references/approved-implementation-workflow.md`, `references/handoff-contract.md` |
| Skill self-evolution | `references/self-evolution-rule.md`, `references/step-evidence-gate.md` |
| Sync runtime/open-source copies | `references/sync-checklist.md` |

## OpenSpec Boundary

OpenSpec is required for new functionality, architecture or pattern changes,
public/operator-visible behavior, security, migrations, API/schema/data
lifecycle changes, broad refactors, agent runtime control flow, request routing,
skill routing, workflow lifecycle, or skill workflow changes.

OpenSpec may be skipped only for localized restoration of already-defined
behavior, small config-only changes, typo/comment/formatting updates, docs-only
updates without contract impact, or tests for already-defined behavior. Direct
Change is forbidden for workflow/routing/security/cross-module runtime changes
unless an approved contract already covers the behavior.

Do not implement OpenSpec-required work before approval.

## Approved Implementation

Approved implementation requires a Superpowers implementation plan unless the
user explicitly forbids it. Use TDD for behavior changes, systematic debugging
for unexplained failures, Step Evidence Gate for gated steps, and verification
before any completion claim.

For external-agent execution, create one Handoff Contract before handoff. The
contract is the single shared state; missing, duplicated, stale, contradictory,
or unparsable contracts are BLOCKED and return to this router or the user.

## Evidence Profiles

- `compact`: low-risk docs, formatting, config, tests for existing behavior, or
  local restoration. Focused verification; no large plan by default.
- `standard`: default. Each batch runs `step_critical`; review reruns critical
  plus one independent behavior check; `final_critical` runs once at the final
  batch unless later code changes invalidate it.
- `strict`: security, auth, permission, public API/schema, persistence,
  migration, deletion/recovery, deployment/rollback, cross-tenant boundaries.
  Real migration/API/business-chain evidence cannot be replaced with mocks or
  unit tests.

## Batch Profiles

- `single`: one complete low-risk behavior slice.
- `cohesive`: default for tightly related multi-file work; usually 2-3 batches.
- `staged`: independent approval, deployment, rollback, migration, security, or
  external-dependency boundaries.

Never split solely by file, helper, schema/runtime/test layer, or diff size when
that sacrifices an end-to-end runnable business slice.

## Self-Evolution

Use Self-Evolution for changes to this skill, its references, examples,
templates, validation, trigger scope, routing, evidence gates, completion rules,
or runtime/open-source sync.

Major self-evolution requires an approved contract before implementation,
structured backup, validation, forward-test, rollback path, and final report.

## Non-Recursive Skill Self-Evolution

For global personal skill edits, short-circuit only unrelated business-project
OpenSpec recursion. Do not short-circuit user approval, structured backup,
self-evolution gate, RED/GREEN forward-test, validation, or rollback. If the
skill source itself is being changed as an OpenSpec-managed product repository,
require OpenSpec approval.

## Superpowers Mapping

| Scenario | Required Superpowers |
|---|---|
| Bug / unexpected behavior | `superpowers:systematic-debugging` |
| Feature, bugfix, test, refactor, approved behavior | `superpowers:test-driven-development` |
| Multi-step implementation plan | `superpowers:writing-plans` |
| Completion/fixed/passing/ready claim | `superpowers:verification-before-completion` |
| Editing this or another skill | `superpowers:writing-skills` |
| Substantial implementation before handoff | `superpowers:requesting-code-review` |

## Non-Negotiables

- Do not let `CONTEXT.md` replace OpenSpec proposal artifacts.
- Do not let OpenSpec `tasks.md` replace a Superpowers implementation plan.
- Do not use Superpowers planning to bypass OpenSpec approval.
- Do not implement OpenSpec-required work before approval.
- Do not move to the next gated step until Step Evidence Gate passes.
- Do not claim completion without verification evidence.
- Do not compress official artifacts so much that evidence, risks, or decisions
  become unauditable.
- Self-evolution cannot weaken approval gates, evidence gates, verification
  requirements, or user-control boundaries.
- Never run `git add`, `git commit`, `git reset`, or `git clean` unless the
  user explicitly commands it.
- Do not push without explicit user approval.
