# Project Learning Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add conditional project-context discovery and a completion-blocking Project Learning Closeout that turns costly corrections and Review findings into discoverable project knowledge plus executable regression enforcement.

**Architecture:** The router gains two coordinated boundaries: an entry-side Domain Context Check and a closeout-side Project Learning Gate. Portable policy lives in focused references and a Candidate Card template; core/static validators and cross-CLI manifest version 4 make the rules mechanically durable. `CONTEXT.md` remains a domain glossary while engineering mechanisms and regression behavior stay in their own artifacts.

**Tech Stack:** Markdown skill contracts, OpenSpec, Python `unittest`, dependency-free Python validators, JSON portable manifest, shell validation commands.

---

## Worktree, authority, and evidence

- Worktree: `/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive`
- Branch: `feature/make-superpowers-routing-adaptive` (not `main`)
- Approved change: `add-project-learning-gate`
- Approval provenance: `ai-proposed/user-approved`, user replied `同意` immediately after exact change-id presentation.
- Evidence profile: `standard`; capability profile: `control-plane-high` for routing/promotion/Review and `mechanical-low` for deterministic edits/checks.
- Backup: `/private/tmp/context-learning-gate-self-evolution-20260715-175013/`
- Git authority: the user previously authorized final commit, cherry-pick, push, and extra-worktree cleanup. Do not create per-slice commits because this worktree contains the preceding approved change awaiting one intentional publication sequence. Never use `git reset` or `git clean`.
- Stop on: contract scope expansion, unexplained test failure, missing runtime target, sync parity drift, sensitive-data finding, unrelated diff collision, or Review result other than PASS.

## File map

| Responsibility | Files |
|---|---|
| Entry/closeout routing | `SKILL.md`, `references/request-modes.md`, `references/local-instruction-checkpoint.md`, `references/approved-implementation-workflow.md`, `references/response-patterns.md` |
| Learning policy and artifact | `references/learning-candidate-pipeline.md`, new `references/project-learning-closeout.md`, new `templates/learning-candidate-template.md` |
| Portable enforcement | `references/shared-global-governance.md`, `references/cross-cli-portable-manifest.json`, `scripts/validate_core_gates.py`, `scripts/validate_cross_cli_sync.py` |
| Contract/regression tests | `tests/test_workflow_rules.py`, `tests/test_cross_cli_sync.py`, new `tests/fixtures/project-learning/qagent-merged-paragraph.md` |
| Public workflow | `README.md`, `README_cn.md`, `examples/openspec-change.md`, `CHANGELOG.md` |
| Evidence/closeout | new `docs/design/2026-07-15-project-learning-gate-red-green.md`, new `docs/design/2026-07-15-project-learning-gate-forward-test.md`, new `docs/design/2026-07-15-project-learning-gate-closeout.md`, `docs/design/evidence/`, OpenSpec tasks/archive |

### Task 1: Approval record and Plan Preflight

**Files:**
- Modify: `openspec/changes/add-project-learning-gate/proposal.md`
- Modify: `openspec/changes/add-project-learning-gate/tasks.md`
- Create: `docs/design/evidence/add-project-learning-gate-preflight.md`

- [ ] **Step 1: Verify the exact contract and approval record**

Run:

```bash
openspec validate add-project-learning-gate --strict --no-interactive
rg -n "add-project-learning-gate|ai-proposed/user-approved|\[x\] This specific" openspec/changes/add-project-learning-gate
```

Expected: strict validation exits 0 and the exact approved change-id/provenance is present.

- [ ] **Step 2: Preflight Review this plan against every spec requirement**

The Preflight artifact must record exactly these checks and a `PASS` or
`BLOCKED` result:

```text
contract coverage: conditional context discovery; automatic threshold; explicit
archive/distill trigger; layered artifacts; completion/archive order
allowed scope: router source, validators/tests, runtime copies, public docs only
commands: focused RED/GREEN, full source validation, strict OpenSpec, sync plan/apply/verify-all
rollback: structured backup plus target-by-target restore
Git: final publication authorized; no reset/clean; no per-slice commit
placeholders: none
result: PASS only if all entries are concrete and consistent
```

- [ ] **Step 3: Stop if Preflight is BLOCKED**

Do not edit production skill/reference/validator files until the current plan
revision has Preflight `PASS`.

### Task 2: RED routing and learning-contract tests

**Files:**
- Modify: `tests/test_workflow_rules.py`
- Create: `tests/fixtures/project-learning/qagent-merged-paragraph.md`
- Create: `docs/design/2026-07-15-project-learning-gate-red-green.md`

- [ ] **Step 1: Extend the test fixture loading**

Add these reads to `WorkflowRulesTest.setUpClass`:

```python
cls.local_checkpoint = (
    ROOT / "references" / "local-instruction-checkpoint.md"
).read_text(encoding="utf-8")
cls.learning = (
    ROOT / "references" / "learning-candidate-pipeline.md"
).read_text(encoding="utf-8")
```

Do not read the missing new files in `setUpClass`; that would error the whole
class instead of producing a precise RED assertion.

- [ ] **Step 2: Add entry-routing contract tests**

Add tests with these exact behavioral assertions:

```python
def test_domain_context_check_is_conditional_and_precedes_material_choice(self):
    normalized = " ".join((self.skill + self.request_modes).split())
    self.assertIn("Domain Context Check", normalized)
    self.assertIn("before material", normalized)
    self.assertIn("does not invoke `grill-with-docs`", normalized)
    self.assertIn("complete portable Discovery First", normalized)
    self.assertIn("references/local-instruction-checkpoint.md", self.skill)

def test_ignored_canonical_context_cannot_satisfy_shared_promotion(self):
    normalized = " ".join(self.local_checkpoint.split())
    self.assertIn("must not be intentionally ignored", normalized)
    self.assertIn("does not require `git add`, commit, or push", normalized)
```

- [ ] **Step 3: Add promotion and completion tests**

Add tests covering these exact contract fragments:

```python
def test_project_learning_gate_has_automatic_and_explicit_triggers(self):
    path = ROOT / "references" / "project-learning-closeout.md"
    self.assertTrue(path.is_file(), "project learning closeout reference missing")
    learning_closeout = path.read_text(encoding="utf-8")
    normalized = " ".join((self.learning + learning_closeout).split())
    self.assertIn("two independent correction or Review signals", normalized)
    self.assertIn("security, integrity, data-loss, or false-PASS", normalized)
    self.assertIn("archive and distill", normalized)
    self.assertIn("every confirmed project-local key point", normalized)

def test_required_project_learning_blocks_completion_and_archive(self):
    path = ROOT / "references" / "project-learning-closeout.md"
    self.assertTrue(path.is_file(), "project learning closeout reference missing")
    learning_closeout = path.read_text(encoding="utf-8")
    normalized = " ".join((self.skill + self.approved + learning_closeout).split())
    self.assertIn("Project Learning Closeout", normalized)
    self.assertIn("final completion is `BLOCKED`", normalized)
    self.assertIn("before fresh final verification", normalized)
    self.assertIn("before OpenSpec", normalized)

def test_learning_artifacts_are_layered_and_mechanical_rules_are_executable(self):
    closeout_path = ROOT / "references" / "project-learning-closeout.md"
    template_path = ROOT / "templates" / "learning-candidate-template.md"
    self.assertTrue(closeout_path.is_file(), "project learning closeout reference missing")
    self.assertTrue(template_path.is_file(), "learning candidate template missing")
    learning_closeout = closeout_path.read_text(encoding="utf-8")
    learning_template = template_path.read_text(encoding="utf-8")
    normalized = " ".join((learning_closeout + learning_template).split())
    self.assertIn("CONTEXT.md", normalized)
    self.assertIn("docs/engineering-invariants.md", normalized)
    self.assertIn("deterministic regression test or validator", normalized)
    self.assertIn("prose-only", normalized)
    self.assertIn("sensitive", normalized)
```

- [ ] **Step 4: Add the sanitized qagent-shaped fixture**

Create the fixture with no private source or transcript:

```markdown
# Merged paragraph learning candidate

- symptom: a whole-row note disappears after table conversion
- prior assumption: every colspan row is tabular data
- correction evidence: repeated human correction plus independent Review
- generalized semantic invariant: a merged paragraph row is a table-level annotation, not tabular data
- engineering invariant: normalization must preserve annotations outside rectangular cell expansion
- mechanical regression: an edge fixture must preserve leading and trailing merged paragraph rows
```

- [ ] **Step 5: Run focused tests and preserve expected RED**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_workflow_rules.WorkflowRulesTest.test_domain_context_check_is_conditional_and_precedes_material_choice \
  tests.test_workflow_rules.WorkflowRulesTest.test_ignored_canonical_context_cannot_satisfy_shared_promotion \
  tests.test_workflow_rules.WorkflowRulesTest.test_project_learning_gate_has_automatic_and_explicit_triggers \
  tests.test_workflow_rules.WorkflowRulesTest.test_required_project_learning_blocks_completion_and_archive \
  tests.test_workflow_rules.WorkflowRulesTest.test_learning_artifacts_are_layered_and_mechanical_rules_are_executable -v
```

Expected: FAIL/ERROR only because the new reference/template/rules do not exist.
Record command, exit code, failing assertions, and why each failure is expected
in the RED/GREEN report.

### Task 3: GREEN router policy and learning artifacts

**Files:**
- Modify: `SKILL.md`
- Modify: `references/request-modes.md`
- Modify: `references/local-instruction-checkpoint.md`
- Modify: `references/learning-candidate-pipeline.md`
- Modify: `references/approved-implementation-workflow.md`
- Modify: `references/response-patterns.md`
- Create: `references/project-learning-closeout.md`
- Create: `templates/learning-candidate-template.md`

- [ ] **Step 1: Add the Domain Context Check to the router**

Add the local checkpoint to the reference matrix and encode this rule without
changing the existing phase-aware Superpowers boundary:

```text
Run the Domain Context Check before material-choice classification when affected
terms, actors, boundaries, states, or lifecycle may change. Inspect repository
facts first. Clear language continues without `grill-with-docs`; unresolved or
conflicting domain language invokes it when available, otherwise the complete
portable Discovery First rules apply.
```

- [ ] **Step 2: Harden canonical project-context durability**

Update the local checkpoint with:

```text
In a Git repository, canonical shared CONTEXT.md / CONTEXT-MAP.md must not be
intentionally ignored. An ignored local copy cannot satisfy durable shared
promotion. Active edits may remain untracked or modified because this checkpoint
does not require `git add`, commit, or push without separate authorization.
```

Keep the existing direct-fix proportionality rule.

- [ ] **Step 3: Implement the Candidate Card thresholds**

Keep task-local/global semantics and add:

```text
Project-local promotion is mandatory after two independent correction or Review
signals establish the same generalized invariant, or one high-severity security,
integrity, data-loss, or false-PASS event establishes it. Repeated paraphrases of
one source are not independent. A user correction plus a distinct reviewer
observation may be independent.
```

- [ ] **Step 4: Create the Project Learning Closeout reference**

The new reference must define:

```text
Implement -> Verify -> Review PASS -> Project Learning Closeout -> promote and
verify/review learning artifacts -> fresh final verification -> final Review ->
OpenSpec reconcile/archive -> session archive/distillation summary
```

It must include automatic and explicit archive/distill triggers, the five-target
artifact resolver from the approved design, sensitive-data redaction, non-ignored
durability, mechanical-test obligation, infeasibility fallback, and `BLOCKED`
conditions.

- [ ] **Step 5: Create the Candidate Card template**

Use fixed fields:

```yaml
status: candidate | promoted | rejected | blocked
event_kind: correction | review-finding | security | integrity | data-loss | false-pass
severity: low | medium | high
scope: task-local | project-local | global
promotion_trigger: threshold | explicit-archive-distill | high-severity | none
symptom:
prior_assumption:
correction_or_evidence:
generalized_invariant:
independent_reproductions:
independence_rationale:
duplicate_or_conflict_result:
target_artifacts:
mechanical_enforcement: required | infeasible | not-applicable
mechanical_enforcement_reason:
verification:
review_result: pending | pass | fail | blocked
decision_owner: codex
decision_provenance:
```

Require summarized project-relative evidence references/hashes and forbid full
transcripts, credentials, private prompts, customer data, and secrets.

- [ ] **Step 6: Insert the closeout before final verification/archive**

Update `SKILL.md`, approved workflow, and response patterns so mandatory or
explicit project-local promotion blocks completion until its artifacts pass
focused verification and Review. A learning audit with no confirmed project-
local candidate proceeds without documentation churn.

- [ ] **Step 7: Run focused GREEN**

Run the same five-test command from Task 2. Expected: PASS.

### Task 4: RED/GREEN portable validator and governance version 4

**Files:**
- Modify: `tests/test_cross_cli_sync.py`
- Modify: `tests/test_workflow_rules.py`
- Modify: `scripts/validate_core_gates.py`
- Modify: `scripts/validate_cross_cli_sync.py`
- Modify: `references/shared-global-governance.md`
- Modify: `references/cross-cli-portable-manifest.json`

- [ ] **Step 1: Write failing manifest-version tests**

Add:

```python
def test_manifest_accepts_version_4_project_learning_invariants(self):
    manifest = portable_manifest()
    manifest["managed_rules"]["version"] = 4
    manifest["managed_rules"]["invariant_ids"] = [
        f"CCG-{number:03d}" for number in range(1, 16)
    ]
    self.assertEqual(sync.validate_manifest(manifest), manifest)
```

Also assert the canonical manifest includes
`references/local-instruction-checkpoint.md`,
`references/project-learning-closeout.md`, and
`templates/learning-candidate-template.md` for all three targets.

- [ ] **Step 2: Run validator tests and verify RED**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_cross_cli_sync.ManifestAndTriggerTests.test_manifest_accepts_version_4_project_learning_invariants \
  tests.test_workflow_rules.WorkflowRulesTest.test_project_learning_gate_has_automatic_and_explicit_triggers -v
```

Expected: FAIL because managed-rule version 4 and the new portable closure are
not supported yet.

- [ ] **Step 3: Add managed invariant CCG-015**

Append exactly one stable invariant:

```text
[CCG-015] Governed work conditionally resolves affected project language before
material-choice routing. Corrections and Review findings enter Project Learning
Closeout; mandatory or explicitly requested project-local promotion blocks final
completion until durable non-sensitive knowledge and mechanically enforceable
regression evidence pass verification and Review.
```

- [ ] **Step 4: Upgrade manifest and sync validator**

Change:

```python
MANAGED_RULE_INVARIANT_COUNT = {1: 8, 2: 13, 3: 14, 4: 15}
```

Set manifest managed rules to version 4 / `CCG-001..CCG-015` and add the three
new portable files to the router allowlist.

- [ ] **Step 5: Extend core semantic validation**

Read the new reference/template in `main()` and require these phrases:

```python
for needle in (
    "Project Learning Closeout",
    "two independent correction or Review signals",
    "archive and distill",
    "every confirmed project-local key point",
    "deterministic regression test or validator",
    "final completion is `BLOCKED`",
):
    require(learning + learning_closeout + learning_template, needle, "project learning gate")
```

Also require `references/local-instruction-checkpoint.md` and the non-ignored
context rule through the reference-link validation surface.

- [ ] **Step 6: Run focused GREEN**

Run the Task 4 focused command plus:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
PYTHONDONTWRITEBYTECODE=1 python3 -c \
  'import json; from pathlib import Path; from scripts.validate_cross_cli_sync import validate_manifest; validate_manifest(json.loads(Path("references/cross-cli-portable-manifest.json").read_text(encoding="utf-8")))'
```

Expected: all exit 0.

### Task 5: Public workflow and artifact-boundary documentation

**Files:**
- Modify: `README.md`
- Modify: `README_cn.md`
- Modify: `examples/openspec-change.md`
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Detail the current English workflow**

Document this exact order:

```text
request facts -> Domain Context Check -> material-choice check -> phase/risk
route -> approved execution loop -> Project Learning Closeout -> fresh final
verification/Review -> OpenSpec archive -> authorized Git publication -> session
archive/distillation summary
```

Include a table distinguishing `CONTEXT.md`, engineering invariants, ADRs,
Candidate Cards, regression tests, and session summaries.

- [ ] **Step 2: Mirror the same contract in Chinese**

Preserve exact trigger and blocking semantics; translate explanatory text, not
normative identifiers such as `Project Learning Closeout`, `BLOCKED`, or
`CCG-015`.

- [ ] **Step 3: Update example and changelog**

The OpenSpec example must mention conditional context discovery and learning
closeout before archive. Changelog must identify the user-visible key point:
costly corrections no longer remain chat-only and prose cannot replace
mechanical regression enforcement.

- [ ] **Step 4: Check bilingual and contract consistency**

Run:

```bash
rg -n "Domain Context Check|Project Learning Closeout|CONTEXT.md|engineering-invariants|archive and distill" README.md
rg -n "Domain Context Check|Project Learning Closeout|CONTEXT.md|engineering-invariants|归档|蒸馏" README_cn.md
git diff --check
```

Expected: both READMEs contain the same normative route and diff check exits 0.

### Task 6: Full source validation, forward evidence, and High Review

**Files:**
- Create: `docs/design/2026-07-15-project-learning-gate-forward-test.md`
- Create/update: `docs/design/evidence/` validation and Review artifacts
- Modify as findings require: only approved files above

- [ ] **Step 1: Run the complete source matrix**

```bash
/opt/anaconda3/bin/python3 \
  /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
openspec validate --all --strict --no-interactive
git diff --check
```

- [ ] **Step 2: Run isolated fixture-based forward scenarios**

Because this execution environment forbids spawning new subagents without an
explicit request, use isolated temporary copies and scenario fixtures rather
than silently dispatching agents. Prove and record:

1. clear localized fix skips `grill-with-docs`;
2. ambiguous domain term selects grill or full fallback;
3. correction plus independent Review meets promotion threshold;
4. one low-risk task-local correction is non-blocking;
5. explicit archive/distill request always runs the audit and promotes confirmed
   project-local knowledge;
6. qagent-shaped semantic/engineering/test classification is correct;
7. ignored canonical context fails durability while no Git command is implied.

- [ ] **Step 3: Run distinct High Review**

Inspect actual files and complete diff; trace each claim to SKILL/reference,
validator/test, managed invariant, manifest, runtime path, and README. Rerun the
critical focused tests plus one adversarial scenario: an agent attempts to
satisfy promotion with a chat summary and prose-only context entry.

- [ ] **Step 4: Fix every finding and repeat**

Any actionable finding returns to the affected GREEN task, source matrix,
forward scenarios, and High Review. Only PASS advances.

### Task 7: New cross-CLI synchronization

**Files:**
- Runtime copies declared by `references/cross-cli-portable-manifest.json`
- Create/update: path/hash-only sync evidence under `docs/design/evidence/`

- [ ] **Step 1: Read sync rules and inventory active schema-4 work**

Run the exact inventory required by `references/cross-cli-sync.md`; stop if any
active schema-4 contract blocks deployment.

- [ ] **Step 2: Generate and Review the version-4 sync plan**

The plan may contain only allowlisted relative paths, hashes, target IDs, and
managed-block metadata. No credentials, config, logs, sessions, or content dump.

- [ ] **Step 3: Apply and verify each target atomically**

Apply Codex, Antigravity CLI, then Grok CLI one target at a time. On failure,
restore that target from the structured backup, verify restoration, and stop.

- [ ] **Step 4: Run verify-all and runtime validators**

Require exact portable parity, managed version 4 / `CCG-015`, target discovery,
router quick validation, and dependency-free validator PASS on every declared
required target.

- [ ] **Step 5: Run final cross-target Review**

Check no native overlay outside managed markers changed and no sensitive or
extra path was synchronized.

### Task 8: Project Learning Closeout, OpenSpec archive, and publication

**Files:**
- Modify: `openspec/changes/add-project-learning-gate/tasks.md`
- Create: `docs/design/2026-07-15-project-learning-gate-closeout.md`
- Create if a confirmed project-local lesson exists: project Candidate Card and
  its correct durable target/regression enforcement
- Archive: `openspec/changes/add-project-learning-gate/`

- [ ] **Step 1: Audit this session's correction and Review history**

Classify the user's qagent/context correction, artifact-boundary clarification,
automatic threshold decision, explicit archive/distill decision, and every new
Review finding. Promote confirmed project-local knowledge; do not duplicate the
already approved general workflow rule as a narrative incident log.

- [ ] **Step 2: Verify and Review any learning-promotion diff**

Mechanically enforceable lessons require a regression test/validator. Rerun
focused and full validation after changes; Review must PASS.

- [ ] **Step 3: Run fresh final verification and final Review**

Repeat the complete source matrix and runtime verify-all after the last edit.
Inspect scope, sensitive data, temporary files, unrelated changes, and both
OpenSpec contracts.

- [ ] **Step 4: Reconcile and archive**

Mark only evidenced tasks complete, update closeout, archive with the repository
OpenSpec command, then run:

```bash
openspec validate --all --strict --no-interactive
git diff --check
```

- [ ] **Step 5: Finish the two repositories using existing authorization**

Generate concise Conventional Commit messages, stage and commit each feature
branch intentionally, preserve/back up stale main artifacts, cherry-pick to each
main, rerun full validation, fetch/recheck remote divergence, and push both main
branches. Never use reset/clean.

- [ ] **Step 6: Verify remote state and clean temporary resources**

Verify remote main SHAs, delete temporary publication/self-evolution backups,
remove only the two extra feature worktrees, retain branches unless separately
authorized for deletion, and confirm main worktrees are clean.

- [ ] **Step 7: Produce the final session archive/distillation summary**

Report whether the user's concern is solved, the key mechanism, source/runtime
validation, commit/push state, learning artifacts, worktree cleanup, residual
risks, and rollback history. The summary references durable project artifacts;
it is not their only storage location.
