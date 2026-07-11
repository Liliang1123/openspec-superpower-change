# Superpowers Adapter

This adapter maps Superpowers artifact and permission defaults onto the
project's approved workflow. It does not weaken brainstorming, TDD, systematic
debugging, Review, worktree safety, or verification discipline.

## Single OpenSpec Design Contract

When OpenSpec is required, brainstorming still explores intent, alternatives,
and trade-offs before implementation, but its design output and user-review
gate map to the **single OpenSpec design contract**: the same proposal/design,
change-id, and approval. Do not create, commit, or approve a second
`docs/superpowers/specs/` artifact for the same decision.

A scoped Direct Change that restores an already-defined behavior without a
creative design decision does not need a duplicate brainstorming artifact.
Ambiguity or a new behavior choice returns to brainstorming/OpenSpec.

## Executable Plan And Preflight Review

`superpowers:writing-plans` produces executable steps after approval. Before
implementation or external dispatch, run **Preflight Review** against the
current artifact revision:

- contract/spec coverage and absence of placeholders;
- allowed files, boundaries, production wiring, and acceptance;
- exact verification commands, evidence profile, rollback, and stop conditions;
- branch/worktree decision and unauthorized Git or duplicate-design steps.

Preflight uses only `PASS` or `BLOCKED`. Any finding is `BLOCKED`, returns
the Plan/Brief to its author, and does not authorize execution. Fix the artifact
and Review again. Preflight `PASS`
authorizes execution only; it is not implementation Review or completion
evidence. Do not repeat ceremony when the artifact revision is unchanged;
rerun Preflight Review whenever that artifact revision changes.

Use `superpowers:subagent-driven-development` for suitable independent tasks in
the current session, or `superpowers:executing-plans` for a separate execution
session. An explicitly named external executor instead uses the Handoff-backed
brief governor. Do not create two execution governors for the same slice.

## Git And Worktree Permission

A Superpowers plan **never grants Git permission**. Remove `git add`,
`git commit`, `git push`, `git reset`, `git clean`, or equivalent publication
steps unless the current user explicitly authorizes those commands for this
task. Record any removal or authorization in Preflight Review.

Use a worktree when the selected execution skill or repository rules require
isolation. Never start implementation on `main`/`master` merely because a plan
mentions it; current-branch use requires explicit user consent.

## Granularity And Completion

Superpowers may retain RED/GREEN implementation actions inside a plan, but Step
Evidence Gate and Review operate on a complete business slice or explicit risk
milestone, not every two-to-five-minute action. Review findings restart the
appropriate fix/verification/Review loop. `verification-before-completion`
remains mandatory after final Review and OpenSpec closeout.

## Capability Profiles And Confirmation Reuse

A Superpowers execution style does not grant decision authority. Bind work to
`control-plane-high`, `cohesive-medium`, or `mechanical-low` and escalate when a
profile reaches its ceiling. Platform sandbox/prefix permission is only the tool
layer; it cannot satisfy workflow scope or business/production authorization.
An unchanged Confirmation Lease avoids duplicate prompts for safe commands and
the same finding's fix/verify/Review loop. Material revision, scope, risk,
production, credential, external-effect, destructive-Git, evidence, or user
changes invalidate the lease.
