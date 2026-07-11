---
name: openspec-superpower-change
description: "Use when a request may modify files or behavior, asks review-and-fix, changes skill/workflow/template files, needs OpenSpec or Direct Change classification or Superpowers routing, or decides evidence-based final completion; also trigger on 开发变更、变更准入、OpenSpec、Review并修复、实施闭环、Skill自演进. 可按用户要求输出 caveman 风格摘要，但不改治理约束。"
---

# OpenSpec + Superpowers Change Gate

Single entry gate for state-changing development work. It classifies the
request, protects approval boundaries, selects implementation discipline, and
owns final review and verification. It does not own standalone prompt wording
or an already-handed-off external batch.

## Token-lean / Caveman output mode

`caveman` is **输出压缩层**，非治理机制。该层只优化表达密度，不改变任何
路由/批准/证据/状态变更规则。

- 触发：用户明确要求“少 token/更短/更精简/像 caveman 说”。
- 允许：路由结论、Gate 0 摘要、发现列表、风险要点、验证命令说明。
- 禁止：OpenSpec 提案正文、handoff/contracts、schema-1/3 evidence artifact 本体、
  验收状态转移、final verification 结论、关键命令、敏感数据、最终闭环证据。
- 对于治理 artifact，本地化输出可压缩为更短段落，但不得省略必填字段。

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
| Modify, fix, implement, change behavior, change workflow/template files, or dispatch without a valid Handoff | This skill |
| Review architecture, OpenSpec need, implementation authorization, or whole-task completion evidence | This skill / Review-only |
| Write or refine a task prompt, Brief, or checklist without changing files | `codex-brief-antigravity-review` / standalone |
| Read-only review of a diff, Report, or evidence without fixing it | `codex-brief-antigravity-review` / standalone |
| Execute, resume, or review a batch with a valid Handoff Contract | `codex-brief-antigravity-review` / handed-off |

“Review and fix” is implementation, not Review-only. A Direct Change that uses
an external agent still enters here first; create a profile-appropriate Handoff
Contract before handing execution to the governor. Only work that remains
low-risk may default to `compact`.

When a valid Handoff already exists, its dispatch/resume/review route takes
priority and goes directly to `codex-brief-antigravity-review`.

This skill owns request classification, OpenSpec approval, risk/evidence and
batch profiles, Handoff creation, and final completion. The brief skill owns
Brief/Report/Review attempts only after handoff and returns the final batch to
this router.

Codex is the authoritative collaboration owner. Antigravity CLI and Grok CLI
may be assigned as external executors or independent reviewers, but their
results remain evidence inputs until Codex validates them and records the
canonical transition. Standard/strict external batches require distinct
executor/reviewer identities; compact work may remain inline.

## Reference Read Matrix

Read `SKILL.md` first, then only the matching references:

| Task | Required references |
|---|---|
| Review-only / route review | `references/request-modes.md`, `references/response-patterns.md` |
| Implementation / bugfix | `references/request-modes.md`, `references/openspec-decision-rule.md`, `references/step-evidence-gate.md`, `references/superpowers-adapter.md` |
| Direct Change | `references/direct-change-rule.md`, `references/step-evidence-gate.md` |
| Runtime / tool / workflow change | `references/openspec-decision-rule.md`, `references/proposal-workflow.md`, `references/approved-implementation-workflow.md`, `references/superpowers-adapter.md` |
| External execution | `references/approved-implementation-workflow.md`, `references/handoff-contract.md` |
| Skill self-evolution | `references/self-evolution-rule.md`, `references/step-evidence-gate.md` |
| Runtime/source sync | `references/sync-checklist.md` |
| Cross-CLI skill/global-rule sync | `references/cross-cli-sync.md`, `references/sync-checklist.md` |

## OpenSpec Boundary

OpenSpec is required for new functionality, architecture or pattern changes,
public/operator-visible behavior, security, migrations, API/schema/data
lifecycle, broad refactors, runtime control flow, routing, or workflow lifecycle.

OpenSpec may be skipped for localized internal restoration of defined behavior,
small config-only changes, typo/comment/formatting updates, non-contractual docs,
or tests for existing behavior. Changing a skill's trigger, routing, required
artifact, state transition, evidence rule, or completion rule is workflow
behavior and requires OpenSpec. Editorial wording that changes none of those
contracts may use Direct Change.

A public/user/operator-visible restoration may use Direct Change only when an
approved existing spec or equivalent project-authoritative contract explicitly
defines the intended behavior, Gate 0 records its exact path, and no contract,
schema, compatibility, or lifecycle behavior changes. Otherwise use OpenSpec.

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
- Before implementation or dispatch, run a current-revision Plan/Brief
  **Preflight Review**. Any finding revises the artifact and restarts preflight.
  Preflight authorizes execution only; it is not implementation Review.

Every implementation follows:

```text
Plan/Brief Preflight PASS -> Implement -> Verify -> Review
Review FAIL -> Fix same scope -> Verify -> Review again
Review BLOCKED -> Resolve/decide -> refresh evidence -> Review again
Review PASS -> next slice, or final verification when no slice remains
```

The final external batch `PASS` means `awaiting-final-verification`, not task
completion. This router persists fresh `final_critical` evidence before final
Review, then reviews final diff/scope/security or sensitive-data concerns and
fixes/reviews again for every actionable finding. Completion requires hashed
batch/final evidence, final Review PASS, OpenSpec task reconciliation, and the
repository-appropriate archive/validation closeout.

When portable files of either core workflow skill or the shared governance
block change, completion also requires the cross-CLI sync gate: validated source
must be synchronized and verified on every declared required Codex,
Antigravity CLI, and Grok CLI runtime. Repository-only docs/history changes do
not trigger this gate. See `references/cross-cli-sync.md`.

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
| Execute a reviewed plan | `superpowers:subagent-driven-development` or `superpowers:executing-plans` |
| Isolate work unless current branch use is explicitly authorized | `superpowers:using-git-worktrees` |
| Feature, bugfix, refactor, behavior change | `superpowers:test-driven-development` |
| Unexplained failure | `superpowers:systematic-debugging` |
| Inline standard/strict implementation review | `superpowers:requesting-code-review` |
| Completion/fixed/passing/ready claim | `superpowers:verification-before-completion` |
| Editing a skill | `superpowers:writing-skills` |
| Complete a branch workflow | `superpowers:finishing-a-development-branch` |

Apply `references/superpowers-adapter.md`. It maps Superpowers artifact and
permission defaults onto this workflow without weakening brainstorming, TDD,
debugging, Review, or verification discipline.

## Self-Evolution

Use Self-Evolution for changes to this skill or its companion's trigger,
routing, templates, validation, evidence, completion, or runtime/source sync.
Major self-evolution requires an approved contract, structured backup,
RED/GREEN forward-test, validation, rollback, final report, and final Review.

For global personal skill edits, short-circuit only unrelated business-project
OpenSpec recursion. Do not short-circuit user approval or any self-evolution
gate. Product behavior published from an OpenSpec-managed repository requires
an approved OpenSpec change.

Portable self-evolution is not complete after updating only the source repository
or Codex runtime. Run the declared cross-CLI target plan/apply/verify sequence;
a missing, stale, undiscoverable, or failed required target is `BLOCKED`.

## Non-Negotiables

- Do not let `CONTEXT.md` replace OpenSpec artifacts.
- Do not let OpenSpec `tasks.md` replace a Superpowers implementation plan.
- Do not use Superpowers planning to bypass OpenSpec approval.
- Do not implement OpenSpec-required work before approval.
- Do not gate every TDD micro-step; do not skip the business-slice evidence gate.
- Do not advance with `FAIL`, `BLOCKED`, stale evidence, or unresolved findings.
- Do not claim completion without fresh verification evidence and Review PASS.
- Do not accept empty critical commands, blank blocker details, evidence-free
  external PASS, or an atomic final-verification/final-Review completion update.
- External artifacts must carry the schema-1 evidence manifest binding role,
  result, change, batch, attempt, source canonical revision/SHA-256, producing
  agent identity, and agent role. Runtime `complete` validation requires the
  actual previous status.
- Codex is the only decision owner; auxiliary executor/reviewer output cannot
  self-authorize a canonical transition or final completion.
- Do not claim a portable global skill optimization complete while any declared
  required Codex, Antigravity CLI, or Grok CLI target is stale or unverified.
- Do not duplicate mutable Handoff Contract blocks outside canonical `status.md`.
- Self-evolution cannot weaken approval, evidence, review, verification, or
  user-control boundaries.
- Never run `git add`, `git commit`, `git reset`, or `git clean` unless the user
  explicitly commands it.
- Do not push without explicit user approval.
