# Streamline Workflow Prompt Contracts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement the five approved `streamline-workflow-prompt-contracts` changes without weakening approval, evidence, Review, Git, learning, Handoff, or completion boundaries.

**Architecture:** Keep the Router as the only whole-task completion owner, move its normative completion checklist to one validated reference, and make the Companion entry thin while retaining the full Handoff governor in a route-only reference. Correct the independent Superpowers Option 2 defect in its own repository. Select the Companion structure only from recorded runtime-loading evidence; `UNKNOWN` never becomes a token-savings claim.

**Tech Stack:** Markdown Skill contracts, Python standard-library validators/tests, Node.js built-in test runner for the Superpowers contract, OpenSpec CLI, existing cross-CLI sync tooling.

**Authorization:** The user approved implementation of change-id `streamline-workflow-prompt-contracts`. No `git add`, `git commit`, `git push`, `git reset`, or `git clean` is authorized. Work occurs only in the three feature worktrees listed below.

---

## Worktrees

- Router: `/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/streamline-workflow-prompt-contracts`
- Companion: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts`
- Superpowers: `/Users/elvis/.config/superpowers/worktrees/superpowers/streamline-workflow-prompt-contracts`

## Task 1: Record prompt-load evidence and select the Companion structure

**Files:**

- Create: `docs/design/evidence/2026-07-17-companion-prompt-load.md`
- Modify: `openspec/changes/streamline-workflow-prompt-contracts/tasks.md`

- [ ] Record Codex's documented progressive-disclosure contract: metadata is discoverable, the activated `SKILL.md` body loads after selection, and references load as needed. Bind the evidence to the inspected `skill-creator/SKILL.md` SHA-256.
- [ ] Run a non-mutating standalone prompt through `agy --print` with a private `/tmp` log and through `grok --single` with a private `/tmp` debug log. Search the logs only for Companion Skill/reference paths; do not persist or echo prompt/session content.
- [ ] Record each target as `observed`, `documented`, or `UNKNOWN`, including command, version, evidence path/hash, limitation, and decision consequence.
- [ ] Select one thin Companion Skill plus a Handoff-only reference if the supported skill contract establishes on-demand references and no target proves eager reference injection. If a target proves unavoidable eager injection, stop and use the spec-approved split-Skill branch. Do not use file bytes as runtime evidence.
- [ ] Review the evidence document for secret/session leakage before continuing.

**Acceptance:** The structure decision cites reproducible evidence, unknown targets remain explicit, and no token reduction is claimed from word/byte count.

**Stop:** If evidence proves that the thin-reference structure breaks discovery or valid-Handoff loading on a required target, do not edit the Companion; revise the plan within the approved split branch and Preflight Review it again.

## Task 2: RED — reproduce the Option 2 contradiction

**Files:**

- Create: `/Users/elvis/.config/superpowers/worktrees/superpowers/streamline-workflow-prompt-contracts/tests/finishing-branch-policy.test.js`

- [ ] Add a Node built-in test that reads `skills/finishing-a-development-branch/SKILL.md`, extracts Option 2 and Step 5, and asserts that Option 2 says the worktree is preserved, does not direct cleanup, Step 5 lists only Options 1 and 4, and Quick Reference/Red Flags agree.
- [ ] Run `node --test tests/finishing-branch-policy.test.js`.
- [ ] Preserve the expected RED output showing the current Option 2 cleanup text violates the contract.

**Acceptance:** RED fails because of the existing contradictory Skill text, not a test syntax or path error.

## Task 3: GREEN — correct Option 2 without granting Git authority

**Files:**

- Modify: `/Users/elvis/.config/superpowers/worktrees/superpowers/streamline-workflow-prompt-contracts/skills/finishing-a-development-branch/SKILL.md`
- Test: `/Users/elvis/.config/superpowers/worktrees/superpowers/streamline-workflow-prompt-contracts/tests/finishing-branch-policy.test.js`

- [ ] Replace Option 2's cleanup instruction with an explicit preserved-worktree result.
- [ ] Change Step 5 from `Options 1, 2, 4` to `Options 1 and 4`; state Options 2 and 3 preserve worktrees.
- [ ] Leave push/PR commands, test verification, typed discard confirmation, and force-push prohibition otherwise unchanged.
- [ ] Run the Node test and `/opt/anaconda3/bin/python3 /Users/elvis/.codex-account-a/skills/.system/skill-creator/scripts/quick_validate.py skills/finishing-a-development-branch`.

**Acceptance:** Test GREEN; every active Option 2 statement preserves the worktree; no new Git authorization appears.

## Task 4: RED — canonical completion and prompt-collision contracts

**Files:**

- Modify: `tests/test_workflow_rules.py`
- Modify: `scripts/validate_core_gates.py`

- [ ] Add `test_completion_contract_is_canonical_and_discoverable` requiring `references/completion-contract.md`, the Router pointer, and stable obligations for fresh final evidence, final Review PASS, learning, OpenSpec reconciliation/archive, cross-CLI sync, Git/publication authority, stop conditions, and residual risk.
- [ ] Add `test_secondary_completion_surfaces_reference_canonical_contract` requiring `response-patterns.md`, `approved-implementation-workflow.md`, and `step-evidence-gate.md` to name the canonical file while retaining route-specific evidence.
- [ ] Add `test_prompt_collision_contracts_cover_phase_git_and_hard_gate` requiring paired unauthorized/authorized Git cases, proposal-only `none`, material brainstorming, and selected HARD-GATE preservation.
- [ ] Extend `validate_core_gates.py` with the same canonical-file and navigation requirements.
- [ ] Run only the new tests and preserve expected RED failures for the missing canonical reference/fixtures.

**Acceptance:** RED is caused by missing approved contracts, while all existing tests remain unchanged.

## Task 5: GREEN — add the Router-owned Completion Contract

**Files:**

- Create: `references/completion-contract.md`
- Modify: `SKILL.md`
- Modify: `references/response-patterns.md`
- Modify: `references/approved-implementation-workflow.md`
- Modify: `references/step-evidence-gate.md`
- Modify: `references/cross-cli-portable-manifest.json`
- Modify: `scripts/validate_core_gates.py`
- Modify: `tests/test_workflow_rules.py`
- Modify: `README.md`
- Modify: `CHANGELOG.md`

- [ ] Write the canonical result contract with sections `Success`, `Evidence`, `Stop`, `Learning and reconciliation`, `Cross-CLI sync`, `Git/publication authority`, and `Residual risk`.
- [ ] Keep Router frontmatter/body entry-discoverable and make whole-task completion read the canonical reference.
- [ ] Replace duplicated normative whole-task checklists in the three secondary references with concise pointers; preserve batch/slice-specific evidence and prohibitions.
- [ ] Add `references/completion-contract.md` to the portable manifest for all three required runtimes.
- [ ] Make validator ownership explicit: validate the canonical file independently rather than concatenating unrelated files.
- [ ] Run focused tests and `python3 scripts/validate_core_gates.py .` until GREEN.

**Acceptance:** One file owns the normative whole-task checklist; secondary surfaces remain safe and route-specific; missing/divergent canonical ownership fails deterministically.

## Task 6: RED — require a thin Companion entry and intact governor reference

**Files:**

- Modify: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/tests/test_workflow_rules.py`
- Modify: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/scripts/validate_templates.py`

- [ ] Add `test_thin_entry_routes_handoff_detail_to_reference` requiring `SKILL.md` to retain route selection, standalone contract, common authority/Git boundaries, and a direct `references/handed-off-external-execution.md` pointer while excluding embedded Artifact Paths/State Machine/Evidence Profiles detail.
- [ ] Add `test_handoff_governor_reference_preserves_complete_contract` requiring the new reference to retain schema 5, schema-4 completion, artifact paths, state machine transitions, evidence profiles, identity binding, Preflight, High Review, `awaiting-final-verification`, and correction loops.
- [ ] Extend `validate_templates.py` with the same independently-owned checks.
- [ ] Run the two focused tests and preserve expected RED failures.

**Acceptance:** RED proves the current combined body does not provide route isolation; existing Handoff schema/template tests remain untouched.

## Task 7: GREEN — implement the measured Companion structure

**Files:**

- Modify: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/SKILL.md`
- Create: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/references/handed-off-external-execution.md`
- Modify: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/scripts/validate_templates.py`
- Modify: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/tests/test_workflow_rules.py`
- Modify: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/README.md`
- Modify: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/README_cn.md`
- Modify: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/streamline-workflow-prompt-contracts/CHANGELOG.md`
- Modify: `references/cross-cli-portable-manifest.json`

- [ ] Move the complete handed-off execution sections to the one-level reference without changing their normative content.
- [ ] Keep `SKILL.md` as the thin route entry, standalone contract, shared Non-Negotiables, template pointers, and maintenance boundary.
- [ ] Add the new reference to the Router-owned portable manifest for all three required targets.
- [ ] Update English/Chinese README routing diagrams and changelog without claiming measured token savings.
- [ ] Run Companion focused tests, template validator, and complete 72-test suite.

**Acceptance:** Standalone selection does not require reading governor procedure; valid Handoff selection explicitly requires the complete reference; batch PASS still returns to Router.

## Task 8: Prompt-collision forward-tests and source validation

**Files:**

- Create or modify isolated fixtures under `tests/fixtures/` only when needed.
- Modify: `openspec/changes/streamline-workflow-prompt-contracts/tasks.md`

- [ ] Run raw proposal-only, material-ambiguity, unauthorized Git, authorized Git, standalone Companion, and valid-Handoff scenarios without expected-answer leakage.
- [ ] Verify observable outputs only; do not assert hidden reasoning or metadata-only loading.
- [ ] Run Router `quick_validate.py`, `validate_core_gates.py`, and all unittests with both PyYAML and dependency-free supported interpreters.
- [ ] Run Companion `quick_validate.py`, `validate_templates.py`, template formatting checks, and all unittests.
- [ ] Run Superpowers Node regression and quick validation.
- [ ] Run `openspec validate streamline-workflow-prompt-contracts --strict` and all three `git diff --check` commands.

**Acceptance:** Every command exits 0; warnings are classified; all RED evidence has corresponding GREEN evidence.

## Task 9: High Review, synchronization, and closeout

**Files:**

- Modify: Review/evidence artifacts, task reconciliation, README/changelog closeout only as required.

- [ ] Run a distinct High Review over all three complete diffs, actual navigation, validators, runtime load evidence, Git authority, and Non-Goals.
- [ ] Fix every finding and repeat verification/Review.
- [ ] Read `references/sync-checklist.md`, inventory active schema-4 contracts, create a path/hash-only sync plan, and Review it before applying.
- [ ] Apply and verify Codex, Antigravity CLI, and Grok CLI one at a time; restore and stop on any failure.
- [ ] Run Project Learning Closeout only for newly confirmed candidates, then fresh final verification and final Review.
- [ ] Reconcile OpenSpec tasks, archive the change, validate strictly after archive, and remove temporary backups only after every gate passes.

**Acceptance:** Source and every required runtime target pass parity/discovery/validators; final Review PASS exists; no required task remains unexplained; no Git commit/push occurs.
