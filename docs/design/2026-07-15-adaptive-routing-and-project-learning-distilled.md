# Adaptive Routing And Project Learning — Distilled Design

Date: 2026-07-15

## Problem resolved

The workflow had two coupled failure modes:

1. broad Superpowers metadata could make every task look heavy before the
   request's actual phase and unresolved choices were understood;
2. hard-won bug lessons could remain only in a session summary, so a fresh
   agent could repeat the same project-level mistake.

## Core design

The router now makes decisions in this order:

```text
local instructions and shared context
-> Domain Context Check
-> phase and material-choice classification
-> OpenSpec / Direct Change / Review-only route
-> only the Superpowers skills required for that phase
-> Plan/Preflight/TDD/Verify/Review as applicable
-> Project Learning Closeout
-> fresh final verification and final Review
-> OpenSpec reconciliation/archive
-> Git publication when separately authorized
-> session distillation referencing durable artifacts
```

This keeps clear work lean. Unresolved domain terms, actors, boundaries, states,
or lifecycle semantics invoke `grill-with-docs` when installed; other CLIs use
the complete portable Discovery First fallback. Material product/security/data/
compatibility choices still invoke brainstorming and retain its HARD-GATE.

## Durable learning rule

Project-local promotion becomes mandatory after either two independent
correction/Review signals for the same invariant or one high-severity security,
integrity, data-loss, or false-PASS event. An explicit user request to archive
and distill always runs the audit and promotes every confirmed project-local key
point even below that automatic threshold.

Knowledge is stored by responsibility:

| Knowledge | Durable target |
|---|---|
| Domain terms and relationships | nearest `CONTEXT.md`; glossary only |
| Easy-to-miss implementation/agent invariant | project guidance, default `docs/engineering-invariants.md` |
| Hard-to-reverse surprising decision | ADR |
| Provenance and promotion decision | Candidate Card |
| Mechanically enforceable behavior | deterministic test or validator |

A chat summary is never the only durable store. Canonical shared context must
not be intentionally ignored, but this rule does not invent permission for
`git add`, commit, or push.

## False-PASS defenses learned during implementation

The independent High Review found two generic workflow traps and both became
project invariants:

- A mandatory closeout rule must be discoverable in Skill frontmatter; putting
  it only in already-loaded prose cannot guarantee a fresh-session trigger.
- Validators must bind semantics to the artifact that owns them. Concatenating
  closeout and template text allowed rules to move into the wrong file while a
  keyword validator still passed.

Regression tests now reject a missing archive/distill frontmatter trigger and
reject both closeout-to-template and template-to-closeout relocation bypasses.
The generalized rule lives in `docs/engineering-invariants.md`; provenance lives
in `docs/learning-candidates/2026-07-15-project-learning-closeout.md`.

## Companion boundary

`codex-brief-antigravity-review` has exactly two legal routes:

- explicit, request-scoped, non-state-changing Standalone wording/read-only
  Review with no Handoff mutation or auto-chain;
- a valid canonical Handoff lifecycle for Preflight, dispatch, Report audit,
  Review, retries, batch promotion, and final handback.

File edits, review-and-fix, workflow changes, or final completion always return
to the router. Batch PASS never impersonates whole-task completion.

## Runtime result

The portable contract is managed governance version 4 with `CCG-015`. All 37
declared portable files and the managed rule body passed parity and validators
on Codex, Antigravity CLI, and Grok CLI; Grok discovery also passed its real
inspection check. Source and runtime evidence is recorded in the associated
review, forward-test, correction, and runtime-sync design documents.
