# openspec-superpower-change

`openspec-superpower-change` is a project-level AI development change gate. It is not a generic SDD workflow, not an OpenSpec alias, and not a Superpowers wrapper.

It combines:

- `grill-with-docs` for domain language, boundaries, and design clarification.
- OpenSpec for the approved change contract: what changes, why it changes, and what acceptance scenarios must hold.
- Superpowers for execution discipline: implementation planning, TDD, systematic debugging, code review, and verification-before-completion.
- Step Evidence Gate for evidence-based progress and completion claims.

## Why this is not ordinary SDD

Ordinary SDD usually focuses on:

```text
spec -> plan -> tasks -> implement
```

`openspec-superpower-change` focuses on:

```text
read local rules
-> classify request mode
-> clarify domain language when needed
-> require OpenSpec approval when contract/risk changes
-> use Superpowers after approval for planning, TDD, debugging, implementation, verification
-> keep evidence at every gated step
-> claim completion only after verification evidence exists
```

This makes it a governance orchestrator for AI-assisted development, especially for complex existing codebases.

## Relationship to OpenSpec, Superpowers, and grill-with-docs

| Capability | Responsibility |
|---|---|
| OpenSpec | Defines what changes, why it changes, and the acceptance contract. |
| Superpowers | Defines how approved work is planned, implemented, tested, debugged, reviewed, and verified. |
| grill-with-docs | Clarifies domain terms, boundaries, actors, lifecycle states, and design decisions. |
| openspec-superpower-change | Decides when to use each capability, in what order, and which gates must pass. |

## Change paths

### Lightweight path

Use for low-risk direct changes:

- typos, comments, formatting
- README or documentation small fixes without contract changes
- tests for already-defined behavior
- localized bug fixes that restore intended behavior

Expected gates:

- local instructions check
- scoped evidence when useful
- targeted verification
- concise final report

### Standard path

Use for already-approved or existing-contract implementation:

- multi-step bug fixes
- implementation of already-approved OpenSpec changes
- refactors that do not change public behavior
- moderate-risk direct changes

Expected gates:

- Superpowers implementation plan when work is multi-step
- TDD or systematic debugging as applicable
- compact Step Evidence Gate
- verification-before-completion

### Strict path

Use for contract-changing or high-risk work:

- new capabilities
- architecture or lifecycle changes
- API, schema, persistence, security, sandbox, or tool-call changes
- migrations, deployment/recovery semantics, or operator-visible behavior
- skill workflow changes

Expected gates:

- domain clarification when needed
- OpenSpec proposal, tasks, optional design, and spec deltas
- strict OpenSpec validation
- user approval before implementation
- Superpowers implementation plan after approval
- full or compact Step Evidence Gate depending on risk
- formal verification before completion

## When not to use the full strict path

Do not force OpenSpec for:

- typo fixes
- formatting-only changes
- comments
- docs-only changes with no contract impact
- tests for existing behavior
- localized bug fixes that restore intended behavior

Still explain the verification method before claiming completion.

## FableCodex and caveman-style output

FableCodex is treated as an optional reference checklist, not a parallel execution layer. Its inspect-first and evidence concepts may inspire reviews, but it must not replace OpenSpec tasks, Superpowers plans, or Step Evidence Gate.

Caveman-style output may compress chat messages, progress updates, commit messages, or short summaries. It must not compress official engineering artifacts such as OpenSpec proposals, design docs, spec deltas, Superpowers plans, evidence gates, verification records, risk notes, rollback notes, or customer-facing delivery documents.

## Installation

Copy this folder into a Codex skills directory or keep it as a standalone open-source skill project.

```bash
cp -R openspec-superpower-change "${CODEX_HOME:-$HOME/.codex}/skills/openspec-superpower-change"
```

## Example prompts

```text
Use openspec-superpower-change review-only mode. Read local rules, inspect the design, and report whether implementation would require OpenSpec. Do not modify files.
```

```text
Use openspec-superpower-change as the only entry gate. First determine whether this requires Discovery First or OpenSpec. If OpenSpec is required, create proposal artifacts and stop for approval before implementation.
```

```text
Use Direct Change mode. Confirm this restores intended behavior, reproduce the bug, make the smallest fix, add or update a regression test, run verification, and report root cause, changes, verification, and residual risk.
```

## Risk model

This skill intentionally adds process cost. Use the lightweight path for low-risk tasks and the strict path only when contracts, architecture, safety, runtime semantics, or user/operator-visible behavior can change.

## Roadmap

- Keep `SKILL.md` short and procedural.
- Keep long explanations in `references/`.
- Add realistic examples and templates.
- Forward-test the skill on review-only, direct bugfix, and OpenSpec-backed implementation scenarios.
