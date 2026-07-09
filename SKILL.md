---
name: openspec-superpower-change
description: "Use when a development change may modify files or behavior, needs OpenSpec or Direct Change classification, requires Superpowers execution routing, changes a skill workflow, or needs evidence-based final completion; also trigger on 开发变更、变更准入、OpenSpec、实施闭环、Skill 自演进."
---

# OpenSpec + Superpowers Change Gate

Single entry gate for state-changing development work. It classifies the
request, protects approval boundaries, selects implementation discipline, and
owns final review and verification. It does not own standalone prompt wording
or an already-handed-off external batch.

## Mandatory Entry Gate

Before file modification, state-changing commands, proposal creation, or
implementation, complete Gate 0:

1. mode and references read;
2. OpenSpec decision and reason;
3. required Superpowers sub-skills;
4. risk/evidence profile, next action, and confirmation requirement.

For a typo, formatting, or other non-behavioral micro change, one compact line
may carry all four facts. Gate 0 must stay complete but must not make a light
task heavy. Inspection-only reads are allowed before Gate 0 to classify work.

## Routing Boundary

| Request | Primary skill / mode |
|---|---|
| Modify, fix, implement, change behavior, or dispatch without a valid Handoff | This skill |
| Review architecture, OpenSpec need, implementation authorization, or completion evidence | This skill / Review-only |
| Write or refine a task prompt, Brief, or checklist without changing files | `codex-brief-antigravity-review` / standalone |
| Read-only review of a diff, Report, or evidence without fixing it | `codex-brief-antigravity-review` / standalone |
| Execute, resume, or review a batch with a valid Handoff Contract | `codex-brief-antigravity-review` / handed-off |

“Review and fix” is implementation, not Review-only. A Direct Change that uses
an external agent still enters here first; create a compact Handoff Contract
before handing execution to the governor.

When a valid Handoff already exists, its dispatch/resume/review route takes
priority and goes directly to `codex-brief-antigravity-review`.

This skill owns request classification, OpenSpec approval, risk/evidence and
batch profiles, Handoff creation, and final completion. The brief skill owns
Brief/Report/Review attempts only after handoff and returns the final batch to
this router.

## Reference Read Matrix

Read `SKILL.md` first, then only the matching references:

| Task | Required references |
|---|---|
| Review-only / route review | `references/request-modes.md`, `references/response-patterns.md` |
| Implementation / bugfix | `references/request-modes.md`, `references/openspec-decision-rule.md`, `references/step-evidence-gate.md` |
| Direct Change | `references/direct-change-rule.md`, `references/step-evidence-gate.md` |
| Runtime / tool / workflow change | `references/openspec-decision-rule.md`, `references/proposal-workflow.md`, `references/approved-implementation-workflow.md` |
| External execution | `references/approved-implementation-workflow.md`, `references/handoff-contract.md` |
| Skill self-evolution | `references/self-evolution-rule.md`, `references/step-evidence-gate.md` |
| Runtime/source sync | `references/sync-checklist.md` |

## OpenSpec Boundary

OpenSpec is required for new functionality, architecture or pattern changes,
public/operator-visible behavior, security, migrations, API/schema/data
lifecycle, broad refactors, runtime control flow, routing, or workflow lifecycle.

OpenSpec may be skipped for localized restoration of defined behavior, small
config-only changes, typo/comment/formatting updates, non-contractual docs, or
tests for existing behavior. Changing a skill's trigger, routing, required
artifact, state transition, evidence rule, or completion rule is workflow
behavior and requires OpenSpec. Editorial wording that changes none of those
contracts may use Direct Change.

Do not implement OpenSpec-required work before approval.

## Implementation And Closure

- OpenSpec defines what/why/acceptance; Superpowers defines post-approval
  implementation discipline. Do not create duplicate design approvals.
- TDD applies to feature, bugfix, refactor, and behavior changes. Test-only
  coverage of already-defined behavior uses focused verification and must not
  claim runtime behavior changed.
- Step Evidence Gate signs off complete business slices or risk milestones,
  not every RED/GREEN micro-step.
- `compact` work requires focused verification and an inline diff/self-review.
- `standard` and `strict` inline work requires a distinct Review pass.
- A Handoff-backed external Review is the batch code-review gate; do not add a
  duplicate review for the same batch.

Every implementation follows:

```text
Implement -> Verify -> Review
Review FAIL -> Fix same scope -> Verify -> Review again
Review BLOCKED -> Resolve/decide -> refresh evidence -> Review again
Review PASS -> next slice, or final verification when no slice remains
```

The final external batch `PASS` means `awaiting-final-verification`, not task
completion. This router then runs fresh `final_critical`, reviews the final
diff/scope/security or sensitive-data concerns, and fixes/reviews again if any
finding remains. Completion requires final Review PASS and fresh verification.

## Evidence Profiles

- `compact`: low-risk docs, formatting, config, existing-behavior tests, or
  localized restoration; no large plan or Handoff by default.
- `standard`: default multi-file behavior slice; per-slice critical checks plus
  a distinct review; final matrix runs once after the final slice.
- `strict`: security, auth, public API/schema, persistence, migration,
  deployment/rollback, deletion/recovery, or cross-tenant work; real evidence
  cannot be replaced with mocks or unit tests.

## Superpowers Mapping

| Scenario | Required Superpowers |
|---|---|
| Ambiguous creative alternatives before a contract | `superpowers:brainstorming` |
| Multi-step approved implementation | `superpowers:writing-plans` |
| Feature, bugfix, refactor, behavior change | `superpowers:test-driven-development` |
| Unexplained failure | `superpowers:systematic-debugging` |
| Inline standard/strict implementation review | `superpowers:requesting-code-review` |
| Completion/fixed/passing/ready claim | `superpowers:verification-before-completion` |
| Editing a skill | `superpowers:writing-skills` |

When OpenSpec is required, record brainstorming decisions in the OpenSpec
proposal/design. Its explicit approval is the design approval; do not generate
and approve a second `docs/superpowers/specs/` artifact for the same decision.

## Self-Evolution

Use Self-Evolution for changes to this skill or its companion's trigger,
routing, templates, validation, evidence, completion, or runtime/source sync.
Major self-evolution requires an approved contract, structured backup,
RED/GREEN forward-test, validation, rollback, final report, and final Review.

For global personal skill edits, short-circuit only unrelated business-project
OpenSpec recursion. Do not short-circuit user approval or any self-evolution
gate. Product behavior published from an OpenSpec-managed repository requires
an approved OpenSpec change.

## Non-Negotiables

- Do not let `CONTEXT.md` replace OpenSpec artifacts.
- Do not let OpenSpec `tasks.md` replace a Superpowers implementation plan.
- Do not use Superpowers planning to bypass OpenSpec approval.
- Do not implement OpenSpec-required work before approval.
- Do not gate every TDD micro-step; do not skip the business-slice evidence gate.
- Do not advance with `FAIL`, `BLOCKED`, stale evidence, or unresolved findings.
- Do not claim completion without fresh verification evidence and Review PASS.
- Do not duplicate mutable Handoff Contract blocks outside canonical `status.md`.
- Self-evolution cannot weaken approval, evidence, review, verification, or
  user-control boundaries.
- Never run `git add`, `git commit`, `git reset`, or `git clean` unless the user
  explicitly commands it.
- Do not push without explicit user approval.
