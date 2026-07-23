# Design: add-governed-caveman-lite

## Context

The Router already states that Caveman is an output layer rather than a
governance mechanism. Its allowed and forbidden compression surfaces are split
across `SKILL.md`, request modes, response patterns, and a research reference.
The personal `caveman` skill separately defines `lite`, persistence, and stop
phrases.

The baseline prompt
`OpenSpec 精简模式：请评估……完成后告诉我怎样关闭精简模式`
produced a governance-safe response, but the fresh agent explicitly reported:

- the exact enable phrase is undefined;
- `lite` exists only in the separate Caveman skill;
- persistence/disable behavior is only partially defined by the Router;
- protected governance artifacts are already defined.

This change closes those usability gaps without creating a second governor or
making a personal skill a portable dependency.

## Goals / Non-Goals

### Goals

- Give users one memorable Chinese phrase that enables concise governed output.
- Preserve complete sentences and professional readability.
- Make activation and disable behavior deterministic for the conversation.
- Preserve all Router approval, evidence, Review, and completion contracts.
- Keep behavior portable when the separate Caveman skill is unavailable.
- Prove the contract with structural checks and isolated behavioral scenarios.

### Non-Goals

- Default-on compression.
- New workflow routing, evidence, approval, or completion states.
- Host-level slash commands or persistent preferences across conversations.
- Changes to the external Caveman skill or unrelated prompt-load architecture.

## Decisions

### 1. Built-in profile without external delegation

The Router owns a small built-in profile named `governed-caveman-lite`.
Activation must not depend on discovery of another skill. If a compatible
external Caveman skill is present, this phrase does not invoke or delegate to
it. The Router applies the profile directly, and its protected-surface rules
take precedence over every compression instruction.

### 2. One canonical conversational form

The canonical enable form is:

```text
OpenSpec 精简模式：<任务>
```

The phrase may also be sent alone before the task. It enables the profile for
the current conversation. The canonical disable phrase is:

```text
OpenSpec 正常模式
```

The latest explicit OpenSpec mode command controls Router prose.
`OpenSpec 正常模式` is an explicit user instruction to return Router responses
to normal prose even if a Caveman-style instruction was previously active.
This does not modify another skill; it applies normal style through the user's
higher-priority instruction. The Router documentation teaches only the two
canonical OpenSpec phrases as the shortest complete workflow.

### 3. Lite semantics are explicit

While active, ordinary chat uses concise professional full sentences. It removes
filler, pleasantries, repetition, and unnecessary hedging. It does not use
fragment-heavy prose, unexplained abbreviations, or omitted conjunctions that
could change technical meaning.

The profile changes presentation only. It creates no workflow state, approval,
evidence artifact, or completion transition.

### 4. Protected surfaces override compression

The following remain structurally complete:

- Gate 0 and every mandatory governance-step or approval field;
- OpenSpec proposal, design, spec delta, and tasks;
- Superpowers implementation plans;
- Handoff contracts and evidence artifacts;
- approval and canonical state transitions;
- `PASS`, `FAIL`, and `BLOCKED` results;
- final verification and final Review evidence;
- critical commands, rollback instructions, security warnings, sensitive-data
  handling, and destructive confirmations.

Gate 0, progress updates, findings, risk summaries, command explanations, and
ordinary final chat summaries may be concise only when all required fields and
evidence remain present.

### 5. Lifecycle is conversation-scoped

Activation persists until `OpenSpec 正常模式` or the conversation ends. A new
conversation starts in normal output mode. The profile never becomes a
repository, runtime, or account setting.

### 6. Validation combines deterministic and behavioral evidence

Deterministic tests will bind the enable phrase, disable phrase, lite semantics,
conversation boundary, no-hard-dependency rule, and protected surfaces to their
owning artifacts.

Isolated forward-tests will cover:

1. enable phrase plus Review-only work;
2. protected OpenSpec proposal output;
3. protected final verification/Review output;
4. disable phrase returning to normal prose;
5. operation without the external Caveman skill;
6. most-recent explicit mode command winning when another Caveman instruction
   was previously active;
7. unchanged default behavior when no enable phrase is present.

Forward prompts will state the user task naturally and will not reveal expected
answers.

## Exact Rule Draft

Implementation will add a rule equivalent to:

```markdown
### Governed Caveman Lite

- Enable with `OpenSpec 精简模式：<任务>` or send `OpenSpec 精简模式`
  before the task.
- Use concise professional full sentences. Remove filler and repetition; keep
  technical terms, ordering, and required fields exact.
- Persist for the current conversation only. Disable with
  `OpenSpec 正常模式`.
- Treat the latest explicit OpenSpec mode command as authoritative for Router
  prose; the normal-mode command restores normal prose even after a prior
  Caveman-style instruction.
- Treat this as presentation state only. It never changes routing, approval,
  evidence, Review, verification, or completion.
- Protected governance artifacts and safety-critical text remain structurally
  complete. Governance clarity overrides compression.
- Apply these rules directly even when no separate `caveman` skill is installed.
```

Final wording may be shortened during implementation, but these obligations may
not be removed.

## Files and Responsibilities

| File | Responsibility |
|---|---|
| `SKILL.md` | Entry-discoverable activation, semantics, lifecycle, precedence |
| `references/response-patterns.md` | Allowed/protected response surfaces and usage pattern |
| `README.md` | Short English-facing usage example |
| `README_cn.md` | Canonical Chinese enable/disable examples |
| `scripts/validate_core_gates.py` | Artifact-owned structural validation |
| `tests/test_workflow_rules.py` | RED/GREEN contract and negative regression tests |
| portable manifest/sync evidence | Confirm membership and generate required source/runtime hashes |

## Validation and Forward-Test Plan

1. Write and Preflight Review the implementation plan.
2. Add RED tests that fail because the current skill lacks the exact profile,
   phrases, lifecycle, fallback, and owned validation.
3. Capture the expected failures before changing the skill.
4. Add the minimal profile and documentation.
5. Run focused GREEN tests.
6. Run the required project validation matrix with PyYAML and the dependency-free
   fallback.
7. Run isolated forward-tests for all seven scenarios.
8. Review the complete diff and rerun critical evidence.
9. Synchronize and verify all declared required runtime targets.

## Rollback

Before implementation, create timestamped structured backups outside skill
discovery roots for the source and every runtime target. Source validation,
forward-test, or Review failures return to correction, fresh verification, and
Review. A source backup is restored only when rollback is explicitly chosen.

During runtime synchronization, a failed target application is restored
atomically, its prior hashes and discovery behavior are verified, and later
targets are not applied. Temporary backups remain only until correction,
rollback, or user decision resolves.

Repository history remains the long-term rollback record. No commit, push, PR,
release, or publication is authorized by this design.
