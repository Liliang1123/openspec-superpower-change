# Design: add-project-learning-gate

## Context

Three existing mechanisms cover adjacent concerns but do not yet form one
closed loop:

1. `grill-with-docs` sharpens domain language and keeps `CONTEXT.md` as a
   glossary.
2. `openspec-superpower-change` routes Discovery First and defines completion
   gates.
3. `learning-candidate-pipeline.md` captures corrections and global promotion
   thresholds.

The missing connection is project-level promotion. A future agent needs both a
semantic source it is required to load and executable evidence that rejects the
old behavior. Storing the whole incident in `CONTEXT.md` would violate the
glossary boundary; storing it only in Review or chat would make it undiscoverable.

## Goals / Non-Goals

### Goals

- Make domain-context routing explicit, conditional, and cross-CLI safe.
- Promote foundational, easy-to-miss project lessons discovered through human
  correction and independent Review.
- Make the user's explicit session archive/distill request a deterministic
  Project Learning Closeout trigger.
- Preserve a strict artifact boundary between domain language, engineering
  invariants, architecture decisions, evidence history, and executable tests.
- Prevent a completion claim while required project learning remains only in
  transient conversation or Review output.
- Keep the workflow proportionate when no domain ambiguity or project-local
  learning candidate exists.

### Non-Goals

- Turn `CONTEXT.md` into a bug log, implementation guide, task list, or OpenSpec
  substitute.
- Persist full chat transcripts, private prompts, credentials, customer data, or
  sensitive Review contents.
- Require every low-risk correction to create permanent project documentation.
- Treat an external reviewer as the promotion or completion authority.
- Require Git staging, commit, or push without explicit authorization.
- Modify qagent business code or rewrite its local `CONTEXT.md` in this change.
- Change Handoff schema 5 or companion lifecycle semantics.

## Decisions

### 1. Use an entry check and a closeout gate

The entry-side Domain Context Check runs before material-choice classification:

```text
request facts
-> inspect affected project context and existing decisions when relevant
-> domain language clear: continue
-> domain language unclear/conflicting: grill-with-docs or Discovery First fallback
-> material product/authorization choice remains: brainstorming
-> OpenSpec/direct-change/implementation route
```

This separates vocabulary and boundary clarification from solution selection.
`grill-with-docs` does not replace brainstorming, and neither replaces OpenSpec.

The closeout-side Project Learning Gate runs after implementation Review has
produced its findings but before final completion evidence and archive:

```text
Implement -> Verify -> Review PASS
-> Project Learning Closeout
-> promote required knowledge and regression enforcement
-> verify/review the promotion diff
-> final verification and final Review
-> reconcile tasks and archive/strictly validate
-> produce session archive/distillation summary
```

If learning promotion changes executable behavior, it re-enters the ordinary
approved implementation loop instead of being hidden as documentation.

### 2. Support automatic and explicit promotion triggers

Automatic promotion becomes mandatory when either condition holds:

- two independent correction or Review signals establish the same generalized
  invariant; or
- one high-severity security, integrity, data-loss, or false-PASS event
  establishes it.

Evidence is independent only when it comes from a distinct observation path;
repeated paraphrases of one source do not count twice. A user correction plus a
separate reviewer finding can satisfy the threshold.

An explicit user request to archive and distill the session always runs the
learning audit. The audit promotes every confirmed `project-local` key point
through the repository's normal change path even when the automatic evidence
threshold was not reached. Task-local notes remain in the session summary;
global candidates still follow the existing separate Self-Evolution proposal
threshold and approval path.

### 3. Split promoted knowledge by responsibility

The default target resolver is:

| Knowledge | Durable target | Boundary |
|---|---|---|
| Project-specific domain term, semantic meaning, relationship, or resolved ambiguity | nearest `CONTEXT.md` selected through `CONTEXT-MAP.md`, or a lazily created root `CONTEXT.md` | no implementation cause, chronology, task, or solution detail |
| Easy-to-miss implementation or agent operating invariant | repository-authoritative guidance; default `docs/engineering-invariants.md` | concise generalized mechanism, affected scope, counterexample, and loading pointer |
| Hard-to-reverse, surprising trade-off with real alternatives | `docs/adr/NNNN-slug.md` | decision and reason only |
| Mechanically enforceable behavior | deterministic regression test or validator | must fail for the prior wrong assumption |
| Candidate provenance | default `docs/learning-candidates/YYYY-MM-DD-<slug>.md` | summarized evidence references, no full transcript or sensitive content |

When future agents would not otherwise discover the engineering-invariant
guidance, add a minimal pointer to the nearest repository agent-instruction file
through the project's normal change path. Do not duplicate the full rule there.

For the qagent-shaped example, “a merged paragraph row is a table-level
annotation, not tabular data” is domain semantics suitable for context. Function
names, column-expansion order, and the incident chronology stay out of context;
the generalized parser invariant belongs in engineering guidance and the prior
failure becomes a regression fixture.

### 4. Make shared knowledge durable without stealing Git authority

In a Git repository, a canonical shared `CONTEXT.md` or engineering-invariant
artifact must not be intentionally excluded by ignore rules. During active work
it may be untracked or modified because `git add`, commit, and push remain
separately authorized actions. Completion evidence must include the artifact in
the changed-file inventory and must report pending publication honestly.

This catches the qagent failure mode—an ignored local file shadowing missing
shared knowledge—without turning the workflow into implicit Git publication.

### 5. Candidate Cards bind evidence to promotion

A Candidate Card records the existing fields plus status, promotion trigger,
evidence references, independence rationale, selected durable targets,
mechanical-enforcement decision, verification, and Review result. The control
plane owns classification and redaction. External Report/Review artifacts may be
referenced by project-relative path and hash but cannot self-promote a lesson.

The default card is durable only for promoted project-local knowledge. A single
low-risk task-local correction may remain in the current Plan/Review/session
summary and does not create repository noise.

### 6. Block completion only when the contract requires promotion

Completion is `BLOCKED` when a mandatory or explicitly requested project-local
promotion lacks any of:

- classified Candidate Card and non-sensitive evidence provenance;
- correct durable target artifact;
- non-ignored shared context/guidance where Git is used;
- deterministic regression test/validator for a mechanically enforceable
  invariant; or
- an explicit infeasibility reason plus adversarial Review scenario when
  deterministic enforcement is impossible;
- focused verification and Review PASS over the promotion diff.

The gate is skipped when the learning audit finds no confirmed project-local
candidate. This prevents forced documentation churn on every task.

### 7. Keep cross-CLI behavior equivalent

Codex may invoke the installed `grill-with-docs` skill. Antigravity CLI or Grok
CLI may not have it, so portable router rules retain the complete Discovery First
fallback. The managed governance invariant requires equivalent Domain Context
Check and Project Learning Closeout outcomes rather than requiring a particular
skill package on every CLI.

Portable rule and manifest changes require a new three-target sync and fresh
forward evidence after approval. Prior adaptive-routing sync evidence is not
reused as proof of this contract.

## Risks / Trade-offs

| Risk | Mitigation |
|---|---|
| Every bug produces documentation noise | Promote only confirmed project-local knowledge; task-local notes remain transient |
| `CONTEXT.md` becomes an implementation dump | Enforce target classification and the glossary-only boundary in validators/tests |
| Archive/distill becomes a chat summary ritual | Require repository promotion and regression enforcement before the summary |
| Completion is blocked by unauthorized Git operations | Require changed-file inclusion and non-ignored durability, not staging/commit/push |
| Sensitive Review evidence leaks into knowledge files | Store summarized path/hash provenance and run sensitive-data Review |
| Other CLIs lack `grill-with-docs` | Preserve an equivalent portable Discovery First fallback |
| External agents promote their own claims | Keep Codex as the sole classification and completion owner |

## Migration / Rollback

Existing projects are checked lazily; there is no bulk migration. A future task
that touches affected domain language or runs Project Learning Closeout surfaces
an ignored/stale canonical artifact as a finding and fixes it only through that
project's normal authorization path.

Implementation backup is rooted at
`/private/tmp/context-learning-gate-self-evolution-20260715-175013/`. If approved
implementation fails, restore only this change's router/runtime files, verify
source/runtime parity, and leave the already archived adaptive-routing change
intact. Delete the backup only after validation, Review, cross-CLI sync,
publication, and rollback closure all pass.

