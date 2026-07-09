# Two-Skill Workflow Refinement Implementation Plan

文档类型：Implementation Plan
日志及版本：2026-07-10 v1.0

> **For agentic workers:** Execute inline with evidence checkpoints. Skill behavior changes follow RED/GREEN tests; do not use external implementation because the two source trees are tightly coupled.

**Goal:** Make the two global Codex skills non-overlapping, lightweight where appropriate, and unable to complete without verification plus review.

**Architecture:** `openspec-superpower-change` remains the state-changing development router and final completion owner. `codex-brief-antigravity-review` provides a standalone read-only/prompt path and a separate Handoff-backed external execution governor. A schema-version-2 status contract records repair, blocker recovery, and final handback.

**Tech Stack:** Markdown skill instructions/templates, Python 3 standard library `unittest`, optional PyYAML with deterministic fallback, OpenSpec CLI.

---

### Task 1: Lock routing and lifecycle behavior with RED tests

**Files:**
- Create: `tests/test_workflow_rules.py`
- Create: `../codex-brief-antigravity-review/tests/test_workflow_rules.py`

- [x] Assert the seven routing scenarios from the baseline review.
- [x] Assert invalid `FAIL`, `BLOCKED`, and final-completion transitions are rejected.
- [x] Assert YAML booleans parse correctly without PyYAML.
- [x] Run both suites and confirm failures against current skill text/schema.

### Task 2: Refine the change gate

**Files:**
- Modify: `SKILL.md`
- Modify: `references/request-modes.md`
- Modify: `references/approved-implementation-workflow.md`
- Modify: `references/direct-change-rule.md`
- Modify: `references/handoff-contract.md`
- Modify: `references/step-evidence-gate.md`
- Modify: `references/workflow-overview.md`
- Modify: `scripts/validate_core_gates.py`
- Modify: `README.md`, `README_cn.md`, `AGENTS.md`, relevant examples/templates/docs

- [x] Narrow the trigger to state-changing development governance and architecture/approval review.
- [x] Define compact, standard, and strict review requirements without duplicate artifacts.
- [x] Define final verification handback and completion invariants.
- [x] Make validator and tests GREEN.

### Task 3: Refine the brief/review governor

**Files:**
- Modify: `../codex-brief-antigravity-review/SKILL.md`
- Modify: `../codex-brief-antigravity-review/agents/openai.yaml`
- Modify: `../codex-brief-antigravity-review/references/*.md`
- Modify: `../codex-brief-antigravity-review/scripts/validate_templates.py`
- Modify: `../codex-brief-antigravity-review/README.md`, `README_cn.md`, `AGENTS.md`

- [x] Add mutually exclusive standalone and handed-off paths.
- [x] Add attempt-specific artifacts and mandatory fix/review loops.
- [x] Use canonical `status.md`; final PASS returns to the change gate.
- [x] Fix fallback scalar parsing and target directory handling.
- [x] Make validator and tests GREEN.

### Task 4: Sync and verify

**Files:**
- Modify installed runtime copies under `${CODEX_HOME}/skills/` after source GREEN.
- Create final design records under each repository's `docs/design/`.

- [x] Validate the OpenSpec change in strict mode.
- [x] Run both source validators, `unittest` suites, `git diff --check`, and link/path checks.
- [x] Synchronize runtime copies and rerun validation on all four trees.
- [x] Run forward routing/lifecycle scenarios, final diff review, and sensitive-data scan.
- [ ] Commit and push each repository separately, then remove temporary backups.
