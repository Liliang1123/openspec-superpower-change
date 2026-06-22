# Workflow Overview

## Purpose

`openspec-superpower-change` is the single entry gate for AI-assisted development changes.

It decides:

- whether the request is review-only, discovery, proposal, approved implementation, or direct change;
- whether OpenSpec is required;
- whether Superpowers planning, TDD, debugging, review, and verification are required;
- which Step Evidence Gate level applies;
- when the agent is allowed to claim completion.

## High-level workflow

```text
read local instructions
-> inspect existing specs, changes, docs, and context when relevant
-> classify request mode
-> clarify domain language when needed
-> create or update OpenSpec proposal when required
-> wait for approval before implementation
-> create Superpowers implementation plan for approved work
-> execute with TDD/debugging and Step Evidence Gate
-> run formal verification
-> report changed files, evidence, risks, and next steps
```

## Request mode matrix

| Mode | Allows file changes | OpenSpec | Superpowers plan | Evidence gate | Completion rule |
|---|---:|---:|---:|---:|---|
| Review-only | No | No automatic proposal | No | No implementation gate | State findings and whether implementation would need OpenSpec |
| Discovery First | Docs/glossary only when explicitly allowed | Maybe after clarification | No | Discovery evidence | Continue to proposal decision once terms are stable |
| OpenSpec proposal | Proposal artifacts only | Yes | No implementation plan yet | Proposal validation | Stop for approval |
| Approved implementation | Yes | Already approved | Yes unless explicitly skipped | Compact/full | Formal verification required |
| Direct Change | Yes | No | Only if non-trivial/multi-step | Scoped/compact | Targeted verification required |

## Governance boundaries

- OpenSpec defines the contract.
- Superpowers defines execution discipline.
- Step Evidence Gate defines progress evidence.
- `openspec-superpower-change` defines routing, ordering, and gate enforcement.
