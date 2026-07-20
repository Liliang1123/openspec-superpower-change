# Design: streamline-workflow-prompt-contracts

## Context

The archived `make-superpowers-routing-adaptive` change established phase-aware
selection before broad Superpowers metadata, preserved selected HARD-GATE rules,
and kept standalone Companion Review request-scoped. Independent architecture
Review found that the direction is sound but the combined prompt contract still
contains repeated completion definitions, an upstream worktree contradiction,
and an unmeasured route-load concern.

The accepted finding disposition is deliberately narrower than the original
Review: no P0 governance failure is established; Project Learning and context
promotion are already sufficient for the user's archive-and-distill practice;
and prompt byte counts are only risk signals. This design changes only the five
accepted items.

## Goals / Non-Goals

### Goals

- Remove the deterministic Option 2 worktree contradiction.
- Give the Router one canonical, result-oriented whole-task completion contract.
- Prevent inactive Companion Handoff procedure from burdening standalone tasks
  where supported runtime loading permits isolation.
- Prove routing and Git precedence using negative and positive forward-tests.
- Base structural prompt-load decisions on observed runtime evidence.

### Non-Goals

- Reopen adaptive-routing, Project Learning, domain discovery, or caveman design.
- Reduce required approval, evidence, Review, correction, verification, or sync.
- Make token count, model name, or model confidence an authorization signal.
- Rewrite unrelated Superpowers workflows.

## Decisions

### 1. Correct Option 2 at its source boundary

`finishing-a-development-branch` will state one behavior everywhere: Option 2
pushes/creates a PR and preserves the worktree. Automatic worktree cleanup is
limited to Options 1 and 4. A regression test or deterministic fixture must fail
against the current contradictory text before the source is changed.

The Router adapter continues to require explicit user authority for Git
mutation and publication. Correcting cleanup semantics does not authorize
push, PR creation, branch deletion, or worktree removal.

### 2. One canonical whole-task Completion Contract

The Router will own `references/completion-contract.md`. It will define:

- the successful terminal result;
- fresh final evidence and final Review PASS;
- correction and `BLOCKED` behavior;
- Project Learning Closeout when triggered;
- OpenSpec task reconciliation and archive/strict validation;
- required cross-CLI synchronization for portable changes;
- Git/publication boundaries and residual-risk reporting.

`SKILL.md` remains entry-discoverable and links this contract. Step Evidence,
approved workflow, response patterns, and Companion may retain concise safety
statements and route-specific batch evidence, but they will not maintain an
independent normative whole-task checklist. Validators will check the canonical
file, its navigation pointers, and stable required obligations.

Batch `PASS` remains distinct from task completion. The Companion continues to
return the final external batch to the Router as `awaiting-final-verification`.

### 3. Thin Companion route with an evidence-gated split

The Companion entry contract will contain only:

- mutually exclusive route selection;
- shared authority and Git boundaries;
- a compact standalone result contract;
- a pointer to complete Handoff governance for a valid Handoff route.

The implementation branch is selected from measurement:

| Observed supported-runtime behavior | Approved structure |
|---|---|
| Inactive references are not loaded | One thin Skill plus standalone/Handoff references |
| Activated Skill body is always fully injected and references cannot isolate routes | Two mutually exclusive Skill entrypoints |
| Loading cannot be observed | Record `UNKNOWN`; do not claim savings or split on byte count alone |

If different required runtimes behave differently, the portable structure must
preserve discovery and correct routing on all of them. Any split keeps the same
Router ownership, valid-Handoff requirement, external identity binding, state
machine, evidence, and final-return behavior.

### 4. Prompt-collision tests are behavior contracts

Forward-tests will use raw scenario prompts and isolated fixtures/agents without
embedding the expected answer. Required cases are:

1. a fully specified proposal-only request selects no implementation sub-skill;
2. a material unresolved acceptance choice selects brainstorming and preserves
   its complete HARD-GATE;
3. a plan with unauthorized Git mutation is `BLOCKED` or rewritten before
   implementation;
4. an explicitly authorized Git step is not falsely rejected;
5. branch completion Option 2 preserves its worktree;
6. standalone Companion Review does not enter Handoff governance;
7. a valid Handoff activates the complete unchanged governor.

These tests prove observable route/output behavior. They must not assert hidden
chain-of-thought or treat metadata matching as proof that every sub-skill loaded.

### 5. Prompt-load evidence has a reproducible hierarchy

Accepted evidence, strongest first:

1. runtime trace or tool transcript identifying loaded Skill/reference paths and
   content hashes for a scenario;
2. supported host instrumentation that exports the exact injected prompt text;
3. controlled activation logs showing references explicitly read;
4. static file inventory, labelled only as an upper-bound risk estimate.

Tokenizer measurements are valid only for exact known injected text and record
the tokenizer/model encoding, command or script, input hashes, and uncertainty.
Word or byte counts never become token facts. Unsupported runtimes record
`UNKNOWN` rather than an inferred PASS.

### 6. Preserve result-oriented governance

The redesign removes repeated procedure, not safeguards. Prompt-facing rules
prioritize goal, scope, authority, success, stop, evidence, verification, and
output. Detailed procedures remain in validators, schemas, route-specific
references, and templates when the process itself is part of the safety or
state-transition contract.

## Risks / Trade-offs

| Risk | Mitigation |
|---|---|
| Moving completion prose hides an entry trigger | Keep final-completion ownership in frontmatter/SKILL and validate the canonical pointer |
| Deduplication weakens a safety reminder | Preserve concise prohibitions; remove only independent normative redefinitions |
| Companion split creates discovery or sync drift | Split only with evidence, mutually exclusive descriptions, parity tests, and all-target sync |
| Git validator blocks explicitly authorized plans | Test both unauthorized and authorized cases; bind the result to current user authority |
| Runtime loading cannot be observed | Record `UNKNOWN`, keep safe current routing, and make no savings claim |
| Superpowers update overwrites the Option 2 correction | Track source provenance/hash and make the contradiction regression rerunnable |

## Migration and Compatibility

No Handoff or evidence schema migration occurs. Existing active external
contracts retain their current schema and lifecycle. The completion contract is
a documentation/validation ownership migration with unchanged terminal
requirements. Companion structure changes only after the measurement gate and
must remain compatible with existing valid Handoffs.

Portable changes follow the declared plan/apply/verify-all sequence for Codex,
Antigravity CLI, and Grok CLI. Native runtime configuration, credentials,
sessions, caches, hooks, and other excluded categories are never synchronized.

## Rollback

Create fresh per-target structured backups before approved implementation. If a
source or runtime target fails validation, restore that target, verify restored
hashes and behavior, stop subsequent target application, and report `BLOCKED`.
Temporary backups remain only until rollback decisions and final Review resolve;
repository history is the long-term rollback record.
