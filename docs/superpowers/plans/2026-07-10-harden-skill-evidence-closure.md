# Harden Skill Evidence and Closure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use the approved OpenSpec contract,
> `superpowers:writing-skills`, TDD-style RED/GREEN tests, and profile-appropriate
> Review. Git mutation is authorized only for the final scoped repository commits
> and pushes requested by the user.

**Goal:** Remove the remaining evidence, routing, Superpowers-integration, and
OpenSpec-closeout bypasses without making compact inline work heavy.

**Architecture:** Keep `openspec-superpower-change` as the router/final owner and
`codex-brief-antigravity-review` as the standalone artifact reviewer/external
governor. Upgrade only external Handoff state to schema 3; inline work continues
to use compact evidence and Review.

**Tech Stack:** Markdown skills/templates, Python standard library validators and
`unittest`, OpenSpec CLI.

---

### Task 1: Add RED validator coverage

**Files:**
- Modify: `openspec-superpower-change/tests/test_workflow_rules.py`
- Modify: `codex-brief-antigravity-review/tests/test_workflow_rules.py`

- [x] Add failing tests for empty/blank critical commands and stop conditions.
- [x] Add failing tests for blank blocker details and boolean integer fields.
- [x] Add failing tests for evidence-free completion and unsafe artifact paths.
- [x] Add a failing test proving final verification PASS cannot yet be persisted.
- [x] Run both suites and confirm the new cases fail for the intended reasons.

### Task 2: Implement schema version 3

**Files:**
- Modify: both `references/handoff-contract.md` files
- Modify: both validator scripts

- [x] Add batch/final evidence fields and safe relative-path validation.
- [x] Require non-blank commands, stop conditions, blocker fields, and strategies.
- [x] Reject booleans as positive integers and require exact readonly fields.
- [x] Allow an evidenced final-verification revision before final Review.
- [x] Require that intermediate revision before `complete`.
- [x] Run validator/unit GREEN tests in both repositories.

### Task 3: Tighten routing and Superpowers integration

**Files:**
- Modify: both `SKILL.md` files
- Modify: `references/request-modes.md`
- Modify: `references/approved-implementation-workflow.md`
- Modify: `references/openspec-decision-rule.md`
- Modify: `references/self-evolution-rule.md`
- Modify: Brief/Report/Review templates and `agents/openai.yaml` when needed

- [x] Narrow Brief implicit triggers and unify Direct Change public restoration.
- [x] Add the OpenSpec-specific Superpowers adapter and Git authorization rule.
- [x] Add current-revision Plan/Brief Preflight Review and correction loop.
- [x] Clarify actionable findings versus accepted residual observations.
- [x] Require a concrete approved OpenSpec contract for Major Self-Evolution.

### Task 4: Closeout, portability, and documentation

**Files:**
- Modify: OpenSpec proposal/completion references and final report template
- Modify: both README/AGENTS/CHANGELOG files as needed
- Create: both project `docs/design/` closeout records

- [x] Add tasks reconciliation, archive, and post-archive strict validation.
- [x] Make default single-repo tests skip only optional sibling parity checks.
- [x] Update schema migration and validation examples.
- [x] Keep user-specific runtime paths out of general installation commands.

### Task 5: Sync, Review, archive, and publish

- [x] Sync reviewed source files to both runtime skill directories.
- [x] Run source/runtime quick validation, project validators, unittest, and diff checks.
- [x] Run adversarial and natural-language routing forward-tests.
- [x] Obtain independent routing, integration, and closure Review PASS; fix and re-review.
- [x] Reconcile and archive this OpenSpec change; run strict validation after archive.
- [x] Commit and push each repository separately under the user's existing authorization.
- [x] Delete the structured temporary backup only after publication checks pass.

## Plan Self-Review

- Spec coverage: every approved recommendation maps to Tasks 1-5.
- Placeholder scan: no implementation placeholder remains in executable steps.
- Scope: only the two skill repositories, runtime copies, and temporary backup.
- Git authorization: final scoped commits/pushes are authorized; per-task commits
  are intentionally omitted.
- Rollback: structured backup path is recorded in the OpenSpec design.

## Current-Revision Preflight Review

文档类型：Implementation Plan Preflight Review
日志及版本：2026-07-10 v2（独立集成 Review 修正后）

**Result: PASS**

- Contract/spec coverage: current OpenSpec proposal/design/spec and Tasks 1-5
  cover schema, routing, Superpowers, validation, sync, and closeout.
- Placeholders/executability: no unresolved placeholder or unauthorized Git
  step remains; exact repository validation commands are defined by each
  `AGENTS.md`.
- Branch/worktree decision: continue on each existing `main`. In this session the
  user required separate commits/pushes, confirmed these repositories' main
  branches are only user-maintained, then instructed “继续” and “按你建议推进实施”.
  This is recorded as explicit current-branch/publication consent; no isolated
  worktree is needed for these two private-maintainer skill repositories.
- Git authority: authorization applies only to scoped final commits and pushes;
  it does not authorize destructive cleanup or unrelated Git mutation.
- Evidence/rollback: schema-3 tests, validators, independent Reviews, runtime
  parity, final diff/security checks, and the structured backup remain required.
- Findings: the independent integration Review found that the original plan had
  only Self-Review and did not persist Preflight/branch evidence. Work paused,
  this section was added, and the current revision was reviewed again. This is a
  corrective record, not a retroactive claim that the new rule existed before
  it was introduced by this change.
