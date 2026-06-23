# Workflow Overview

## Purpose

`openspec-superpower-change` is the single entry gate for AI-assisted development changes.

It decides:

- whether the request is review-only, discovery, proposal, approved implementation, or direct change;
- whether OpenSpec is required;
- whether Superpowers planning, TDD, debugging, review, and verification are required;
- which Step Evidence Gate level applies;
- when the agent is allowed to claim completion.

## Main flow

```text
read local instructions
-> inspect existing specs, changes, docs, and context when relevant
-> read required references from the Reference Read Matrix
-> complete Gate 0 before state-changing action
-> classify request mode
-> clarify domain language when needed
-> create or update OpenSpec proposal when required
-> wait for approval before implementation
-> create Superpowers implementation plan for approved work
-> execute with TDD/debugging and Step Evidence Gate
-> run formal verification
-> report changed files, evidence, risks, and next steps
```

## Orchestration model

```text
grill-with-docs when domain language or boundaries are unclear
  -> OpenSpec when the change needs an approved contract
  -> Superpowers when approved work needs planning, implementation, and verification
```

OpenSpec defines the approved change contract. Superpowers defines the execution discipline. `grill-with-docs` sharpens language and decision context before the contract is written.

## Artifact boundaries

For OpenSpec-backed work:

- OpenSpec artifacts: `openspec/changes/<change-id>/proposal.md`, `tasks.md`, optional `design.md`, and spec deltas.
- Superpowers implementation plan: `docs/superpowers/plans/YYYY-MM-DD-<change-id>.md`.
- Step Evidence Gate signoff notes for gated implementation steps.
- Verification evidence before completion.

Optional discovery artifacts:

- `CONTEXT.md` glossary entries.
- `docs/adr/NNNN-slug.md` only for decisions that are hard to reverse, surprising without context, and based on a real trade-off.

## Governance boundaries

- OpenSpec defines what changes, why it changes, and what acceptance scenarios must hold.
- Superpowers defines how approved work is planned, implemented, tested, debugged, reviewed, and verified.
- Step Evidence Gate defines progress evidence and signoff conditions.
- This skill defines routing, ordering, and gate enforcement.
