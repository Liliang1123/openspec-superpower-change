# Review Draft: Project Context and Correction Learning Gate

## Observed Failures

1. The workflow documents `Discovery First`, `grill-with-docs`, and a
   `CONTEXT.md` checkpoint, but the phase-aware top-level route does not make the
   domain-context decision explicit before material design choices are assessed.
2. `references/local-instruction-checkpoint.md` describes a mandatory context
   check but is not itself a required entry in the `SKILL.md` read matrix, and
   current validators do not protect that integration from regression.
3. In `qagent_service`, commit `0c0c5ab` removed `CONTEXT.md` from Git and added
   it to `.gitignore`. A local copy remains, but its last modification predates
   later project work. Existence alone therefore does not make context shared,
   reviewable, or durable.
4. The learning-candidate pipeline defines global promotion thresholds but does
   not require project-local promotion before completion when a foundational,
   easy-to-miss invariant is discovered through repeated correction and
   independent Review.
5. A costly finding can consequently remain only in chat or Review history.
   Future agents may repeat the same assumption even though the immediate bug
   was fixed.

## Desired Behavior

- Run a conditional Domain Context Check before choosing discovery or design
  clarification. Clear, localized work skips `grill-with-docs`; vague or
  conflicting domain language enters `grill-with-docs` when available, with the
  existing built-in Discovery First rules as the cross-CLI fallback.
- Treat `CONTEXT.md` as a canonical domain glossary, not an implementation log.
  In Git repositories it must not be intentionally ignored when used as shared
  project knowledge. Active edits need not be staged or committed without user
  authorization.
- Capture every correction or newly discovered invariant as a Candidate Card.
  Promote a project-local candidate when two independent correction/Review
  signals confirm the same invariant, or when one high-severity security,
  integrity, data-loss, or false-PASS event establishes it.
- When the user explicitly asks to archive and distill the completed session,
  always run a Project Learning Closeout. Audit the correction and Review history
  and promote every confirmed project-local key point through the repository's
  normal change path even when the automatic evidence threshold was not reached.
- Block final completion after that threshold until the generalized knowledge
  is written to the correct durable project artifact and a deterministic
  regression test or validator is added when the invariant is mechanically
  enforceable.
- Split one lesson by responsibility: domain meaning goes to `CONTEXT.md`, an
  architectural trade-off may go to an ADR, an agent-facing engineering trap
  goes to project engineering-invariant guidance, and executable behavior goes
  to a regression test or validator.
- Preserve OpenSpec, Git authorization, Review, evidence, runtime sync, and
  final-verification boundaries. Knowledge documentation does not replace any
  of them.

## Proposed Rule Snippets

```text
Domain Context Check:
Inspect the nearest CONTEXT-MAP.md / CONTEXT.md and affected ADRs when domain
terms, actors, boundaries, states, or lifecycle may change. Invoke
grill-with-docs only when language or domain boundaries remain unclear after
repository inspection; otherwise continue without discovery ceremony.
```

```text
Project-local promotion threshold:
Promote when two independent correction/Review signals establish the same
generalized invariant, or one high-severity security, integrity, data-loss, or
false-PASS event establishes it. Repeated paraphrases of one source are not
independent evidence.
```

```text
Explicit archive/distill trigger:
When the user requests session archive and experience distillation, run Project
Learning Closeout before final completion. Classify all correction and Review
findings; promote confirmed project-local key points, verify and Review the new
artifacts, then produce the session archive summary. A chat-only summary is not
durable project promotion.
```

```text
Completion gate:
When the project-local promotion threshold is met, final completion is BLOCKED
until the Candidate Card identifies the evidence and target artifacts, the
generalized invariant is persisted in the correct non-ignored project artifact,
and every mechanically enforceable invariant has a deterministic regression
test or validator. If mechanical enforcement is impossible, record why and add
an explicit Review scenario instead.
```

```text
Artifact boundary:
CONTEXT.md contains project-specific domain language, meanings, relationships,
and resolved ambiguities only. Implementation causes, incident chronology, and
agent operating instructions belong in engineering-invariant guidance; tests
and validators enforce behavior. Do not duplicate the full lesson in every
artifact.
```

## Expected Files

- `SKILL.md`
- `references/request-modes.md`
- `references/local-instruction-checkpoint.md`
- `references/learning-candidate-pipeline.md`
- a new project-knowledge-promotion reference and Candidate Card template
- `references/shared-global-governance.md`
- `references/cross-cli-portable-manifest.json`
- `scripts/validate_core_gates.py`
- `scripts/validate_cross_cli_sync.py`
- focused routing, validator, and cross-CLI tests
- English/Chinese README and workflow examples
- OpenSpec proposal, design, tasks, and governance spec delta

The companion Handoff schema is not changed. Its Review findings remain evidence
inputs; the Codex control plane owns Candidate Card classification and final
promotion decisions.

## Validation and Forward-Test Plan

1. Add RED contract tests for the Domain Context Check, conditional
   `grill-with-docs` route, project-local threshold, artifact classification,
   ignored canonical context, and completion blocking.
2. Add a qagent-shaped fixture where repeated correction plus independent Review
   discovers that a merged paragraph row is a table-level annotation. Require
   the semantic truth to enter context, implementation mechanics to stay out of
   context, and a regression test/validator obligation to remain explicit.
3. Prove a clear localized fix skips `grill-with-docs` and a single low-risk
   correction remains non-blocking.
4. Prove an explicit archive/distill request always runs the learning audit,
   promotes confirmed project-local knowledge, and prevents the session summary
   from substituting for repository artifacts and regression enforcement.
5. Run quick validation, the dependency-free core validator, full unit tests,
   strict OpenSpec validation, and isolated forward-tests.
6. Run distinct High Review; every finding returns to correction, verification,
   and Review.
7. If approved portable files or the managed governance block change, perform a
   new manifest-aware sync and verification for Codex, Antigravity CLI, and Grok
   CLI. Do not repeat prior adaptive-routing evidence as proof of this change.

## Rollback

- Temporary structured backup:
  `/private/tmp/context-learning-gate-self-evolution-20260715-175013/`
- Before publication, restore only files changed by this scoped change from the
  backup and rerun source/runtime parity validation.
- After successful validation, Review, synchronization, publication, and
  rollback closure, remove the temporary backup. Repository history remains the
  long-term rollback mechanism.
