# Integration Notes

## OpenSpec

OpenSpec owns the approved change contract: what changes, why it changes, and what acceptance scenarios must hold.

## Superpowers

Superpowers owns execution discipline: planning, TDD, systematic debugging, code review, and verification-before-completion.

When OpenSpec is required, brainstorming decisions are recorded in the
OpenSpec proposal/design. OpenSpec approval satisfies the design approval; do
not create a duplicate Superpowers design artifact for the same decision.

`references/superpowers-adapter.md` also makes plan Git steps conditional on
current user authorization and requires Plan/Brief Preflight Review before
execution without duplicating post-implementation Review.

## codex-brief-antigravity-review

This companion owns standalone task-prompt/diff review and Handoff-backed
external Brief/Report/Review attempts. It does not own change classification or
final completion. Final external batch PASS returns here for final verification.
Schema 3 binds Report/Review/final evidence through project-relative paths and
SHA-256. Each file also carries a schema-1 manifest for role, result, change,
batch, attempt, and source canonical revision/SHA-256. A complete transition is
validated against the actual previous status before the router may close it.

## grill-with-docs

grill-with-docs clarifies domain language, boundaries, and design trade-offs before a contract is written.

## FableCodex

FableCodex is an optional external reference. Do not use it as a second execution layer when this skill is already active.

## pi-caveman / caveman-style

Caveman-style output is allowed only for chat-layer compression. It must not reduce auditability of official artifacts.

## Obsidian

Obsidian can store research, retrospectives, templates, and best practices. It is not required to execute the workflow.

## Why not a three-layer parallel architecture

Parallel execution disciplines create conflicting sources of truth. This project keeps one entry gate and treats external systems as references or style guides unless explicitly integrated through a reviewed change.
