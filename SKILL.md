---
name: openspec-superpower-change
description: Project-level AI development change gate and governance orchestrator. Use for development tasks, bug fixes, direct code changes, architecture/design review, OpenSpec proposal or approval workflows, multi-step planning, TDD, systematic debugging, verification-before-completion, and evidence-gated AI coding. It decides when to use grill-with-docs for domain clarification, OpenSpec for approved change contracts, and Superpowers for implementation discipline.
---

# OpenSpec + Superpowers Change Gate

Use this skill as the default entry gate for development change work. It is not ordinary SDD. It orchestrates domain clarification, approved change contracts, implementation discipline, and verification evidence.

## Core responsibility

- Decide the request mode before acting.
- Read local project instructions before changing anything.
- Use OpenSpec when a change needs an approved contract.
- Use Superpowers when approved or non-trivial work needs planning, TDD, debugging, implementation, or verification.
- Use Step Evidence Gate before moving across gated implementation steps.
- Provide verification evidence before any completion claim.

## Request modes

1. **Review-only**: assess, critique, summarize, compare, or generate a prompt. Do not modify files. State whether implementation would require OpenSpec.
2. **Discovery First**: use when domain terms, boundaries, actors, states, lifecycle, or design trade-offs are unclear. Prefer `grill-with-docs` when available.
3. **OpenSpec proposal**: use for new capabilities, public behavior changes, architecture, API/schema, data lifecycle, security, migration, deployment, recovery, operator-visible behavior, or skill workflow changes.
4. **Approved implementation**: use after an OpenSpec proposal has been approved. Create a Superpowers implementation plan before code changes unless explicitly skipped by the user.
5. **Direct Change**: use for localized bug fixes restoring intended behavior, typo/comment/formatting updates, docs-only changes without contract impact, tests for existing behavior, or small low-risk config changes.

## Change paths

### Lightweight path

Use for low-risk direct changes. Do not create OpenSpec artifacts. Use scoped evidence and targeted verification.

### Standard path

Use for already-approved or existing-contract work. Use Superpowers planning for multi-step work, TDD or systematic debugging as applicable, compact evidence, and verification-before-completion.

### Strict path

Use for high-risk or contract-changing work. Create OpenSpec proposal artifacts, validate strictly, wait for approval, then create a Superpowers implementation plan and execute with Step Evidence Gate.

## Non-negotiables

- Do not use `CONTEXT.md` as a replacement for OpenSpec proposals.
- Do not use OpenSpec `tasks.md` as a replacement for a Superpowers implementation plan.
- Do not use Superpowers planning to bypass OpenSpec approval.
- Do not implement OpenSpec-required work before approval.
- Do not move to the next gated step until the current evidence gate passes.
- Do not claim completion without verification evidence.
- Do not compress official artifacts so much that evidence, risks, or decisions become unauditable.

## OpenSpec triggers

Create or update an OpenSpec change for new functionality, architecture or pattern changes, security model changes, migrations, public behavior changes, API/schema changes, data lifecycle changes, broad refactors that alter boundaries, or skill workflow changes.

Skip OpenSpec only for localized fixes restoring intended behavior, typos, formatting, comments, docs-only updates without contract impact, tests for existing behavior, or low-risk config tweaks.

## Superpowers triggers

Use Superpowers for approved implementation, multi-step changes, TDD, systematic debugging, code review, and verification-before-completion. Only skip the implementation plan when the user explicitly says to skip it.

## Step Evidence Gate

Use compact evidence by default; use the full template for high-risk, multi-step, or contract-changing steps. See `references/step-evidence-gate.md`.

Minimum compact evidence:

1. Step goal
2. Code facts with `path:line` evidence when code is involved
3. Positive and negative checks
4. Gap and root cause
5. Change scope
6. Verification
7. Self-review and residual risk
8. Next-step permission: yes/no

## Reference guide

- Read `references/workflow-overview.md` for the full workflow.
- Read `references/step-evidence-gate.md` for evidence gate details.
- Read `references/sdd-comparison.md` when explaining why this is not ordinary SDD.
- Read `references/fablecodex-caveman-review.md` before discussing FableCodex or caveman-style output.
- Read `references/obsidian-knowledge-base.md` when asked to turn findings into long-term notes.
