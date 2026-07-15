# Adaptive Superpowers Routing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the two-skill workflow select Superpowers by phase, material ambiguity, and risk while keeping explicit standalone OpenSpec review concise and request-scoped.

**Architecture:** Add one managed global precedence invariant so the change gate classifies governed work before broad Superpowers metadata. Encode the phase-aware decision in the router and proposal adapter, then narrow the companion's standalone trigger/output without changing its handed-off lifecycle. Existing OpenSpec approval, HARD-GATE after selection, TDD, Review, evidence, schema-5, and completion boundaries remain intact.

**Tech Stack:** Markdown Codex skills and references, JSON portable manifest, Python standard-library `unittest`, OpenSpec CLI, project validators.

---

## Working directories and authority

- Router worktree: `/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive`
- Companion worktree: `/Users/elvis/.config/superpowers/worktrees/codex-brief-antigravity-review/feature-make-superpowers-routing-adaptive`
- Approved OpenSpec change: `make-superpowers-routing-adaptive`
- Evidence profile: `standard`; capability profile for implementation: `cohesive-medium`; Review/final decisions: `control-plane-high`.
- Temporary rollback backup: `/private/tmp/adaptive-superpowers-self-evolution-20260715-103712/`.
- Git authority: no `git add`, `git commit`, `git reset`, `git clean`, or `git push` in this plan.
- Stop conditions: any scope expansion into Handoff schema/evidence/completion semantics, any active schema-4 deployment drain, any stale required runtime target, any failed Review, or any unresolved material routing ambiguity.

### Task 1: Add router RED contract tests

**Files:**
- Modify: `tests/test_workflow_rules.py`
- Modify: `tests/test_cross_cli_sync.py`

- [ ] **Step 1: Add phase-aware router assertions**

Extend `WorkflowRulesTest.setUpClass` with:

```python
cls.proposal_workflow = (
    ROOT / "references" / "proposal-workflow.md"
).read_text(encoding="utf-8")
cls.superpowers_adapter = (
    ROOT / "references" / "superpowers-adapter.md"
).read_text(encoding="utf-8")
cls.shared_governance = (
    ROOT / "references" / "shared-global-governance.md"
).read_text(encoding="utf-8")
```

Add these tests before the handoff lifecycle tests:

```python
def test_phase_aware_superpowers_activation_precedes_broad_metadata(self):
    for text in (self.skill, self.superpowers_adapter):
        self.assertIn("phase-aware", text.lower())
        self.assertIn("generic create/modify wording", text.lower())
    self.assertIn("CCG-014", self.shared_governance)
    self.assertIn("phase classification", self.shared_governance)

def test_proposal_only_can_select_no_superpowers_subskill(self):
    for expected in (
        "proposal-only", "bounded assumption", "material unresolved",
        "security", "compatibility", "data lifecycle", "testable acceptance",
    ):
        self.assertIn(expected, self.proposal_workflow)
    self.assertIn("HARD-GATE", self.superpowers_adapter)

def test_model_identity_never_selects_workflow_weight(self):
    combined = self.skill + self.superpowers_adapter
    self.assertIn("model identity", combined)
    self.assertIn("does not grant", combined)
```

- [ ] **Step 2: Upgrade the managed-rule contract test**

Replace `test_manifest_accepts_version_2_tiered_governance_invariants` in
`tests/test_cross_cli_sync.py` with:

```python
def test_manifest_accepts_version_3_adaptive_routing_invariants(self):
    manifest = portable_manifest()
    manifest["managed_rules"]["version"] = 3
    manifest["managed_rules"]["invariant_ids"] = [
        f"CCG-{number:03d}" for number in range(1, 15)
    ]
    self.assertEqual(sync.validate_manifest(manifest), manifest)
```

- [ ] **Step 3: Run focused tests and observe RED**

Run from the router worktree:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_workflow_rules.WorkflowRulesTest.test_phase_aware_superpowers_activation_precedes_broad_metadata \
  tests.test_workflow_rules.WorkflowRulesTest.test_proposal_only_can_select_no_superpowers_subskill \
  tests.test_workflow_rules.WorkflowRulesTest.test_model_identity_never_selects_workflow_weight \
  tests.test_cross_cli_sync.ManifestAndTriggerTests.test_manifest_accepts_version_3_adaptive_routing_invariants -v
```

Expected: FAIL because `phase-aware`, `CCG-014`, proposal-only bounded-assumption rules, and manifest version 3 are absent. Confirm failures are assertions about those missing contracts, not import or syntax errors.

### Task 2: Implement the router GREEN contract

**Files:**
- Modify: `SKILL.md`
- Modify: `references/request-modes.md`
- Modify: `references/proposal-workflow.md`
- Modify: `references/superpowers-adapter.md`
- Modify: `references/shared-global-governance.md`
- Modify: `references/cross-cli-portable-manifest.json`
- Modify: `scripts/validate_cross_cli_sync.py`
- Test: `tests/test_workflow_rules.py`
- Test: `tests/test_cross_cli_sync.py`

- [ ] **Step 1: Add phase-aware activation to the router**

Insert `## Phase-Aware Superpowers Activation` before `## Superpowers Mapping`
in `SKILL.md` with these rules:

```markdown
## Phase-Aware Superpowers Activation

For governed state-changing work, this change gate performs phase-aware
classification before broad Superpowers metadata selects a sub-skill. Gate 0
selects sub-skills from the current phase, material unresolved decisions, and
implementation risk. Generic create/modify wording does not activate a
Superpowers sub-skill by itself.

- `proposal-only`: inspect repository facts first. If a reviewable contract can
  be drafted with explicit bounded assumptions, create and validate it with no
  implementation sub-skill.
- Invoke brainstorming only for a material unresolved choice affecting scope,
  security, compatibility, data lifecycle, production authority, or testable
  acceptance. Once selected, preserve its complete HARD-GATE.
- Refresh Gate 0 when approved implementation begins; required planning, TDD,
  Preflight, Review, evidence, and verification then apply normally.

Model identity or version does not grant approval and does not select workflow
weight. Use task facts and stable capability/evidence profiles.
```

Change the brainstorming mapping row to:

```markdown
| Material unresolved choice after repository inspection | `superpowers:brainstorming` |
```

- [ ] **Step 2: Encode proposal-only and adapter decisions**

In `references/request-modes.md`, expand **OpenSpec proposal** to say that it is
`proposal-only`, uses repository facts and bounded assumptions, and loads no
implementation sub-skill unless a material unresolved choice requires
brainstorming.

In `references/proposal-workflow.md`, add before the numbered artifact steps:

```markdown
Treat artifact drafting as `proposal-only`. Inspect existing specs, conventions,
and active changes before asking questions. A bounded assumption is allowed only
when it is reversible at approval time, explicit in proposal/design, and does
not decide security, compatibility, destructive migration, data lifecycle,
production authority, or testable acceptance. A material unresolved choice
affecting any excluded boundary requires `superpowers:brainstorming`.
```

In `references/superpowers-adapter.md`, insert a `## Phase-Aware Selective
Invocation` section containing the same predicate plus:

```markdown
Generic create/modify wording does not activate a sub-skill by itself. Gate 0
may record no applicable sub-skill for proposal drafting. Once a sub-skill is
selected, follow it completely; selective invocation never weakens its
HARD-GATE or discipline.

Concrete model identity does not grant authority or choose workflow weight.
```

- [ ] **Step 3: Add the shared precedence invariant**

Append to `references/shared-global-governance.md`:

```markdown
- [CCG-014] Governed state-changing work enters
  `openspec-superpower-change` phase classification before broad Superpowers
  metadata selects a sub-skill. Generic create/modify wording alone does not
  activate a sub-skill; once selected, that sub-skill's full rules remain in force.
```

In `references/cross-cli-portable-manifest.json`, change managed rule version
from `2` to `3` and append `"CCG-014"` to `invariant_ids`. Do not change the
portable file list or target selections.

In `scripts/validate_cross_cli_sync.py`, change:

```python
MANAGED_RULE_INVARIANT_COUNT = {1: 8, 2: 13, 3: 14}
```

This makes the version-3 manifest executable while leaving version-1 and
version-2 history valid.

- [ ] **Step 4: Run focused tests and observe GREEN**

Run the Task 1 focused command again. Expected: 4 tests PASS.

- [ ] **Step 5: Run router regression checks**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Expected: validator success and all router tests PASS, with only companion-parity skips when `BRIEF_SKILL_SOURCE` is not set.

### Task 3: Align router examples and public guidance

**Files:**
- Modify: `examples/openspec-change.md`
- Modify: `README.md`
- Modify: `README_cn.md`

- [ ] **Step 1: Update the OpenSpec example**

Before the artifact creation bullet, add:

```markdown
- Classify the immediate phase as proposal-only. Inspect repository facts first;
  use bounded assumptions for reversible approval-time details and brainstorming
  only for material unresolved choices. Generic create/modify wording alone does
  not trigger Superpowers.
```

Keep the existing stop-for-approval, post-approval plan, Preflight, TDD, Review,
verification, and archive bullets unchanged.

- [ ] **Step 2: Update both README workflow diagrams**

Immediately after `Gate 0 request classification`, add the English line:

```text
-> select Superpowers by phase, material ambiguity, and risk (generic create/modify wording is insufficient)
```

Add the Chinese equivalent:

```text
-> 按任务阶段、实质歧义和风险选择 Superpowers（通用创建/修改语义不足以触发）
```

Add one paragraph below each Request Modes table explaining that proposal-only
drafting can select no Superpowers sub-skill, but a selected brainstorming
HARD-GATE and all approved-implementation gates remain intact.

- [ ] **Step 3: Verify documentation consistency**

```bash
rg -n "proposal-only|phase-aware|CCG-014|Generic create/modify|通用创建/修改" \
  SKILL.md references examples README.md README_cn.md
```

Expected: matches in the router, adapter, shared governance, example, and both READMEs; no claim that Superpowers, approval, Review, or verification was disabled.

### Task 4: Add companion RED tests and GREEN behavior

**Files:**
- Modify: companion `tests/test_workflow_rules.py`
- Modify: companion `SKILL.md`
- Modify: companion `README.md`
- Modify: companion `README_cn.md`

- [ ] **Step 1: Write request-scoped standalone Review tests**

Add after `test_standalone_path_does_not_require_handoff`:

```python
def test_standalone_review_is_request_scoped_and_not_auto_chained(self):
    section = self.skill.split("## Standalone Lightweight", 1)[1].split("## ", 1)[0]
    self.assertIn("request-scoped", section)
    self.assertIn("Do not auto-chain", section)
    self.assertIn("explicit", section)

def test_standalone_openspec_review_is_brief_and_contract_complete(self):
    section = self.skill.split("## Standalone Lightweight", 1)[1].split("## ", 1)[0]
    for expected in (
        "proposal scope", "spec scenarios", "design decisions",
        "task traceability", "cross-artifact consistency",
        "scope/evidence", "actionable findings", "verdict", "next action",
    ):
        self.assertIn(expected, section)
    self.assertIn("omit governance narration", section)
```

- [ ] **Step 2: Run the focused tests and observe RED**

From the companion worktree run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_workflow_rules.WorkflowRulesTest.test_standalone_review_is_request_scoped_and_not_auto_chained \
  tests.test_workflow_rules.WorkflowRulesTest.test_standalone_openspec_review_is_brief_and_contract_complete -v
```

Expected: both tests FAIL because the request-scoped trigger and OpenSpec
checklist are absent.

- [ ] **Step 3: Implement the minimal standalone contract**

Change the frontmatter description prefix to:

```yaml
description: "Use when the user explicitly requests standalone non-state-changing Antigravity/Codex prompt or brief wording, read-only diff/report/evidence review that does not request fixes or decide final completion, or dispatch/review/resume of an external-agent batch with an existing valid Handoff Contract. Do not use for file edits, review-and-fix, final completion, or workflow/template changes. 可按用户要求用 caveman 风格压缩表达。"
```

Add to `## Standalone Lightweight`:

```markdown
This route is request-scoped. Do not auto-chain it after producing an OpenSpec
change or another artifact; use it only for the current explicit wording or
read-only Review request.

For OpenSpec artifacts, inspect proposal scope, spec scenarios, design
decisions and risks, task traceability, and cross-artifact consistency. Default
to findings-first output: scope/evidence, actionable findings, verdict, and next
action. Omit governance narration unless it changes the result or next action.
```

Do not modify Handed-off External Execution, evidence profiles, Non-Negotiables,
templates, validators, or agents metadata unless validation proves metadata is
stale.

- [ ] **Step 4: Align companion READMEs**

Add a highlight in both languages stating that standalone Review is explicit,
request-scoped, findings-first, and never auto-chained after change generation.
Add the five OpenSpec checklist items to the standalone workflow explanation.

- [ ] **Step 5: Run companion GREEN and regression checks**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_workflow_rules.WorkflowRulesTest.test_standalone_review_is_request_scoped_and_not_auto_chained \
  tests.test_workflow_rules.WorkflowRulesTest.test_standalone_openspec_review_is_brief_and_contract_complete -v
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_templates.py .
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Expected: focused tests, validator, and all companion tests PASS.

### Task 5: Cross-repository source verification and Review

**Files:**
- Modify: `openspec/changes/make-superpowers-routing-adaptive/tasks.md`
- Review: complete diffs in both worktrees

- [ ] **Step 1: Run source quick validation with PyYAML**

From each worktree:

```bash
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 \
  /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

Expected: `Skill is valid!` twice.

- [ ] **Step 2: Run cross-repository parity tests**

From the router worktree:

```bash
BRIEF_SKILL_SOURCE=../../codex-brief-antigravity-review/feature-make-superpowers-routing-adaptive \
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Expected: all tests PASS without companion-parity skips.

- [ ] **Step 3: Review scope and mechanics**

Run:

```bash
git diff --check
git diff -- SKILL.md references scripts tests examples README.md README_cn.md
git -C ../../codex-brief-antigravity-review/feature-make-superpowers-routing-adaptive diff --check
git -C ../../codex-brief-antigravity-review/feature-make-superpowers-routing-adaptive diff -- SKILL.md tests README.md README_cn.md
```

Review must trace broad metadata -> CCG-014 -> Gate 0 -> proposal-only/material
decision -> selected sub-skill, and explicit Review request -> companion
standalone checklist. Confirm Handoff schema/evidence/completion files are
unchanged. Every finding returns to fix -> verify -> Review.

- [ ] **Step 4: Reconcile implementation tasks 2 through 4**

Mark only completed source tasks in the active OpenSpec `tasks.md`; keep runtime
sync and closeout tasks open until their fresh evidence exists.

### Task 6: Forward-test and synchronize required runtimes

**Files:**
- Runtime portable files selected by `references/cross-cli-portable-manifest.json`
- Managed global rule blocks for Codex, Antigravity CLI, and Grok CLI
- Create: `docs/design/2026-07-15-adaptive-superpowers-routing-forward-test.md`
- Create: `tests/fixtures/approved-strict-change/add-notification-preferences/proposal.md`
- Create: `tests/fixtures/approved-strict-change/add-notification-preferences/design.md`
- Create: `tests/fixtures/approved-strict-change/add-notification-preferences/tasks.md`
- Create: `tests/fixtures/approved-strict-change/add-notification-preferences/specs/notification-preferences/spec.md`
- Modify: `openspec/changes/make-superpowers-routing-adaptive/tasks.md`

- [ ] **Step 1: Inventory schema-4 deployment drain**

Run from the router worktree:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py . \
  --schema4-inventory-root /Users/elvis/file/develop
```

Expected: `Schema-4 drain valid: active_schema4_count=0`. If any path is active,
stop with `BLOCKED`; never migrate or ignore it.

- [ ] **Step 2: Run isolated GREEN forward-tests**

Create an approved strict fixture with change-id `add-notification-preferences`.
Its proposal records strict risk plus explicit approval; its design fixes bearer
auth, POST semantics, boolean `email`/`push` fields, 400 validation, no migration,
and no compatibility alias; its spec has success and non-boolean rejection
scenarios; its tasks require plan/TDD/real API Review/verification. The fixture
is test evidence only and does not enter `openspec/changes/`.

Write `proposal.md` as:

```markdown
# Change: Add notification preferences endpoint fixture

## Why
Exercise approved strict implementation routing with a concrete public API contract.

## What Changes
- Add `POST /notifications/preferences` under existing bearer authentication.
- Accept and return boolean `email` and `push`; reject non-booleans with 400.
- Add no migration and no compatibility alias.

## Impact
- Fixture risk profile: `strict` public API/schema behavior.
- Fixture scope: routing forward-test only; no production authorization.

## Approval Status
- Change-id: `add-notification-preferences`
- [x] Strict fixture contract approved for routing forward-test
```

Write `design.md` as:

```markdown
# Design: add-notification-preferences fixture

## Decisions
- Reuse bearer authentication and implement one POST handler.
- Request/response fields are required booleans `email` and `push`.
- Non-boolean input returns 400; no migration or compatibility alias exists.

## Risk / Rollback
Public API/schema work is strict. Rollback removes the handler, schema, tests,
and docs together; real API acceptance and independent Review are mandatory.
```

Write `tasks.md` as:

```markdown
# Tasks: add-notification-preferences fixture

- [ ] Create executable implementation plan and pass Preflight Review.
- [ ] Use TDD for schema validation and handler behavior.
- [ ] Run real API acceptance plus unit/type/build checks.
- [ ] Complete independent Review and final verification before completion.
```

Write `specs/notification-preferences/spec.md` as:

```markdown
# notification-preferences Fixture Specification

## Requirements
### Requirement: Update notification preferences
The API SHALL expose bearer-authenticated `POST /notifications/preferences`
with required boolean `email` and `push` request/response fields.

#### Scenario: Valid preferences
- **WHEN** an authenticated user posts boolean `email` and `push`
- **THEN** the response returns both values

#### Scenario: Non-boolean preference
- **WHEN** either field is not boolean
- **THEN** the endpoint returns HTTP 400
```

Populate an isolated runtime from the revised source, not installed live skills:

```bash
mkdir -p /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change
mkdir -p /private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review
rsync -a --exclude='.git' ./ /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/
rsync -a --exclude='.git' ../../codex-brief-antigravity-review/feature-make-superpowers-routing-adaptive/ /private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review/
cp references/shared-global-governance.md /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review
shasum -a 256 tests/fixtures/approved-strict-change/add-notification-preferences/proposal.md tests/fixtures/approved-strict-change/add-notification-preferences/design.md tests/fixtures/approved-strict-change/add-notification-preferences/tasks.md tests/fixtures/approved-strict-change/add-notification-preferences/specs/notification-preferences/spec.md
```

Record the four fixture hashes before dispatch. Dispatch five fresh agents with
`fork_turns="none"`; every raw prompt tells the agent to read the isolated
`AGENTS.md` and use the isolated skill path, never the installed runtime:

1. `Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create proposal/spec/design/tasks only for POST /notifications/preferences. Authentication is existing bearer auth; request fields are email:boolean and push:boolean; response echoes both fields; 400 rejects non-booleans; no migration or compatibility alias. Do not implement.`
2. `Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create proposal/spec/design/tasks only for a new /notifications/preferences endpoint. Choose authentication and backward compatibility for me. Do not implement.`
3. `Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. The exact approved strict fixture is /Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences. Describe the required implementation route for that contract and stop before editing.`
4. `Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review for a concise read-only Review of the approved strict fixture at /Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences. Do not fix files.`
5. `Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create and strictly validate proposal/spec/design/tasks for a fully specified internal endpoint, then stop for approval. Do not review the generated change with another skill.`

Create `docs/design/2026-07-15-adaptive-superpowers-routing-forward-test.md`
with the isolated runtime path/hash, four strict-fixture path/hashes, and one row
per scenario containing raw prompt SHA-256, agent/task identity, actual trigger
chain, artifact requests, result, and finding. Controller-side assertions are:

- scenario 1: router -> proposal-only -> no brainstorming;
- scenario 2: router -> brainstorming -> HARD-GATE before artifact finalization;
- scenario 3: refreshed Gate 0 -> plan/TDD/Preflight/Review/verification;
- scenario 4: companion Standalone Lightweight -> five-part checklist -> no Handoff;
- scenario 5: router only -> no companion auto-chain.

Any mismatch is `FAIL`, returns to source correction, refreshes tests, and reruns
all five scenarios with fresh agents.

- [ ] **Step 3: Audit sources and extend the structured pre-apply backup**

Run the path-only source audit:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py audit \
  --openspec-source . \
  --brief-source ../../codex-brief-antigravity-review/feature-make-superpowers-routing-adaptive \
  --report-paths-only
```

Expected: `0 sensitive categories found`.

Before runtime mutation, add full target skill/rule snapshots under the existing
structured backup. Preserve rule-file modes and set backup rule files to `0600`:

```bash
mkdir -p /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex/skills
mkdir -p /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-cli/skills
mkdir -p /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-cli/skills
cp -a /Users/elvis/.codex/skills/openspec-superpower-change /Users/elvis/.codex/skills/codex-brief-antigravity-review /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex/skills/
cp -a /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change /Users/elvis/.gemini/antigravity-cli/skills/codex-brief-antigravity-review /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-cli/skills/
cp -a /Users/elvis/.grok/skills/openspec-superpower-change /Users/elvis/.grok/skills/codex-brief-antigravity-review /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-cli/skills/
cp -p /Users/elvis/.codex/AGENTS.md /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex-rule.md
cp -p /Users/elvis/.gemini/GEMINI.md /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-rule.md
cp -p /Users/elvis/.grok/AGENTS.md /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-rule.md
chmod 600 /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/*-rule.md
```

- [ ] **Step 4: Generate and Review the path/hash-only sync plan**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py plan \
  --manifest references/cross-cli-portable-manifest.json \
  --openspec-source . \
  --brief-source ../../codex-brief-antigravity-review/feature-make-superpowers-routing-adaptive \
  --codex-skills-root /Users/elvis/.codex/skills \
  --codex-rule-file /Users/elvis/.codex/AGENTS.md \
  --antigravity-skills-root /Users/elvis/.gemini/antigravity-cli/skills \
  --antigravity-rule-file /Users/elvis/.gemini/GEMINI.md \
  --grok-skills-root /Users/elvis/.grok/skills \
  --grok-rule-file /Users/elvis/.grok/AGENTS.md \
  --output /private/tmp/make-superpowers-routing-adaptive-sync-plan.json
```

Review only paths, hashes, selected targets, managed block version 3, CCG-001
through CCG-014, and forbidden categories. The plan file must be mode `0600`.

- [ ] **Step 5: Apply and verify Codex**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py apply --target codex --plan /private/tmp/make-superpowers-routing-adaptive-sync-plan.json --backup-root /private/tmp/make-superpowers-routing-adaptive-sync-backup
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify --target codex --plan /private/tmp/make-superpowers-routing-adaptive-sync-plan.json
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.codex/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 python3 /Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/.codex/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.codex/skills/codex-brief-antigravity-review
PYTHONDONTWRITEBYTECODE=1 python3 /Users/elvis/.codex/skills/codex-brief-antigravity-review/scripts/validate_templates.py /Users/elvis/.codex/skills/codex-brief-antigravity-review
```

- [ ] **Step 6: Apply and verify Antigravity CLI**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py apply --target antigravity-cli --plan /private/tmp/make-superpowers-routing-adaptive-sync-plan.json --backup-root /private/tmp/make-superpowers-routing-adaptive-sync-backup
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify --target antigravity-cli --plan /private/tmp/make-superpowers-routing-adaptive-sync-plan.json
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 python3 /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.gemini/antigravity-cli/skills/codex-brief-antigravity-review
PYTHONDONTWRITEBYTECODE=1 python3 /Users/elvis/.gemini/antigravity-cli/skills/codex-brief-antigravity-review/scripts/validate_templates.py /Users/elvis/.gemini/antigravity-cli/skills/codex-brief-antigravity-review
```

Deterministic manifest closure and these validators are the Antigravity
discovery evidence.

- [ ] **Step 7: Apply and verify Grok CLI**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py apply --target grok-cli --plan /private/tmp/make-superpowers-routing-adaptive-sync-plan.json --backup-root /private/tmp/make-superpowers-routing-adaptive-sync-backup
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify --target grok-cli --plan /private/tmp/make-superpowers-routing-adaptive-sync-plan.json
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.grok/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 python3 /Users/elvis/.grok/skills/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/.grok/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.grok/skills/codex-brief-antigravity-review
PYTHONDONTWRITEBYTECODE=1 python3 /Users/elvis/.grok/skills/codex-brief-antigravity-review/scripts/validate_templates.py /Users/elvis/.grok/skills/codex-brief-antigravity-review
umask 077
/Users/elvis/.grok/bin/grok inspect --json > /private/tmp/make-superpowers-routing-adaptive-grok-inspect.json
chmod 600 /private/tmp/make-superpowers-routing-adaptive-grok-inspect.json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify-discovery --target grok-cli --inspect-json /private/tmp/make-superpowers-routing-adaptive-grok-inspect.json --plan /private/tmp/make-superpowers-routing-adaptive-sync-plan.json --consume
```

- [ ] **Step 8: Restore and stop on any target failure**

The apply transaction restores its target automatically when its internal parity
verification fails. If a later target-specific validator fails, restore the
failed target from the matching `cross-cli-preapply/<target>` snapshot with
`rsync -a --delete` for both skill directories and `cp -p` for the rule file;
then verify `diff -qr` for both skills and `cmp` for the rule file. Record
`BLOCKED` and do not apply later targets. The exact Codex form is:

```bash
rsync -a --delete /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex/skills/openspec-superpower-change/ /Users/elvis/.codex/skills/openspec-superpower-change/
rsync -a --delete /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex/skills/codex-brief-antigravity-review/ /Users/elvis/.codex/skills/codex-brief-antigravity-review/
cp -p /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex-rule.md /Users/elvis/.codex/AGENTS.md
diff -qr /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex/skills/openspec-superpower-change /Users/elvis/.codex/skills/openspec-superpower-change
diff -qr /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex/skills/codex-brief-antigravity-review /Users/elvis/.codex/skills/codex-brief-antigravity-review
cmp /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/codex-rule.md /Users/elvis/.codex/AGENTS.md
```

For Antigravity CLI restoration run:

```bash
rsync -a --delete /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-cli/skills/openspec-superpower-change/ /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change/
rsync -a --delete /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-cli/skills/codex-brief-antigravity-review/ /Users/elvis/.gemini/antigravity-cli/skills/codex-brief-antigravity-review/
cp -p /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-rule.md /Users/elvis/.gemini/GEMINI.md
diff -qr /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-cli/skills/openspec-superpower-change /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change
diff -qr /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-cli/skills/codex-brief-antigravity-review /Users/elvis/.gemini/antigravity-cli/skills/codex-brief-antigravity-review
cmp /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/antigravity-rule.md /Users/elvis/.gemini/GEMINI.md
```

For Grok CLI restoration run:

```bash
rsync -a --delete /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-cli/skills/openspec-superpower-change/ /Users/elvis/.grok/skills/openspec-superpower-change/
rsync -a --delete /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-cli/skills/codex-brief-antigravity-review/ /Users/elvis/.grok/skills/codex-brief-antigravity-review/
cp -p /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-rule.md /Users/elvis/.grok/AGENTS.md
diff -qr /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-cli/skills/openspec-superpower-change /Users/elvis/.grok/skills/openspec-superpower-change
diff -qr /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-cli/skills/codex-brief-antigravity-review /Users/elvis/.grok/skills/codex-brief-antigravity-review
cmp /private/tmp/adaptive-superpowers-self-evolution-20260715-103712/cross-cli-preapply/grok-rule.md /Users/elvis/.grok/AGENTS.md
```

- [ ] **Step 9: Verify all and update OpenSpec tasks**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify-all --plan /private/tmp/make-superpowers-routing-adaptive-sync-plan.json
```

Mark runtime synchronization tasks complete only when all three targets and
Grok discovery PASS.

### Task 7: Final verification and OpenSpec closeout

**Files:**
- Modify: `openspec/changes/make-superpowers-routing-adaptive/tasks.md`
- Modify: `CHANGELOG.md`
- Modify: companion `CHANGELOG.md`
- Create: `docs/design/2026-07-15-adaptive-superpowers-routing-closeout.md`

- [ ] **Step 1: Run the complete final matrix**

Router source:

```bash
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
BRIEF_SKILL_SOURCE=../../codex-brief-antigravity-review/feature-make-superpowers-routing-adaptive PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
openspec validate make-superpowers-routing-adaptive --strict
```

Companion source:

```bash
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_templates.py .
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Expected: every command exits 0; warnings are reported and assessed.

- [ ] **Step 2: Run final High Review**

Inspect both complete diffs and actual runtime copies. Confirm CCG-014 precedes
broad metadata, proposal-only/material predicates match the spec, companion
standalone remains explicit and brief, and no existing CCG, Handoff, evidence,
Review, verification, Git, or completion boundary weakened. Add an adversarial
probe where generic “create” wording is present but no material choice exists.

Any actionable finding is `FAIL` and returns to edit -> full source/runtime
verification -> fresh High Review. Missing runtime/discovery evidence is
`BLOCKED`; after recovery, refresh evidence and Review again. Only PASS proceeds.

- [ ] **Step 3: Reconcile and archive OpenSpec**

Mark every evidenced task complete, update both `CHANGELOG.md` files, and write
the exact validation/forward-test/runtime/Review/rollback outcome to
`docs/design/2026-07-15-adaptive-superpowers-routing-closeout.md`. Then run:

```bash
openspec archive make-superpowers-routing-adaptive -y
openspec validate --all --strict --no-interactive
```

Do not archive while runtime synchronization or Review remains pending.

- [ ] **Step 4: Clean temporary backups after verified closeout**

Only after source/runtime/final Review PASS, remove the temporary structured
backup and verify no `.bak.*` or discoverable `*.backup*` skill directory remains.
Do not remove either worktree or branch until the user chooses merge/PR/keep.

```bash
rm -rf /private/tmp/adaptive-superpowers-self-evolution-20260715-103712
rm -rf /private/tmp/make-superpowers-routing-adaptive-sync-backup
rm -rf /private/tmp/adaptive-superpowers-forward-runtime
rm -f /private/tmp/make-superpowers-routing-adaptive-sync-plan.json
test ! -e /private/tmp/adaptive-superpowers-self-evolution-20260715-103712
find /Users/elvis/.codex/skills /Users/elvis/.gemini/antigravity-cli/skills /Users/elvis/.grok/skills -maxdepth 2 \( -name '*.bak.*' -o -name '*.backup*' \) -print
```

Expected: the `test` exits 0 and `find` prints nothing.
