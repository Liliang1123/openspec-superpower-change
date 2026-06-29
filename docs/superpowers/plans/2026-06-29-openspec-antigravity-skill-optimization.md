# OpenSpec Antigravity Skill Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Optimize `openspec-superpower-change` and `codex-brief-antigravity-review` as a coordinated skill pair without weakening approval, evidence, business acceptance, workspace protection, or completion verification.

**Architecture:** `openspec-superpower-change` becomes the entry router and Handoff Contract owner; `codex-brief-antigravity-review` becomes the external execution governor that consumes that contract. A shared marker-wrapped YAML contract, symmetric validators, profile-aware templates, semantic mapping, and baseline/candidate forward-tests prove the behavior change.

**Tech Stack:** Markdown skills and references, Python 3 validation scripts, YAML via PyYAML, shell verification commands, isolated temporary skill copies for forward-test evidence.

---

## Approved Contract And Gates

Controlling requirements:

- `/Users/elvis/file/develop/opensource/openharness/docs/design/2026-06-29-openspec-antigravity-skill-optimization-requirements.md`
- `/Users/elvis/file/develop/opensource/openharness/docs/review/2026-06-29-openspec-antigravity-skill-optimization-requirements-review.md`

Classification:

- Mode: Self-Evolution / Approved implementation.
- Change level: Major.
- OpenSpec decision: treated as approved by the existing requirements plus review contract for this implementation run; do not widen scope beyond that contract.
- Risk: high.
- Source of truth during implementation: local runtime skill packages first, then synchronize logical equivalent changes to the open-source `openspec-superpower-change` repo.
- Git restrictions: do not run `git add`, `git commit`, `git reset`, `git clean`, or `git push`.

Required pre-edit Gate 1:

- Create one structured backup under `/Users/elvis/.codex/skills-backups/openspec-antigravity-joint-YYYYMMDD-HHMMSS/` containing both runtime skill directories with relative structure preserved.
- Record file counts and SHA-256 for both `SKILL.md` files before editing.
- Confirm open-source repo status with `git status -sb`.
- Stop if repo is dirty outside this plan.

## File Map

Runtime `openspec-superpower-change`:

- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/SKILL.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/request-modes.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/openspec-decision-rule.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/approved-implementation-workflow.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/step-evidence-gate.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/self-evolution-rule.md`
- Create if needed: `/Users/elvis/.codex/skills/openspec-superpower-change/references/handoff-contract.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py`

Open-source `openspec-superpower-change` mirror:

- Apply the same logical edits to matching files under `/Users/elvis/file/develop/opensource/openspec-superpower-change/`.
- Create `references/handoff-contract.md` only if the runtime package needs the new reference.
- Do not force byte-for-byte equality where runtime paths or environment-specific wording must differ.

Runtime `codex-brief-antigravity-review`:

- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/SKILL.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/brief-template.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/report-template.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/review-template.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/agy-dispatch-template.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/timeout-audit-template.md`
- Create if needed: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/handoff-contract.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/scripts/validate_templates.py`
- Modify only if trigger text changes: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/agents/openai.yaml`

Evaluation artifacts:

- Create temporary directory: `/private/tmp/openspec-antigravity-forward-test-YYYYMMDD-HHMMSS/`
- Store baseline and candidate raw outputs, fingerprints, scoring, and comparison report there.
- Do not place raw forward-test outputs inside either skill package.

## Handoff Contract Specification

Use exactly one marker-wrapped YAML block:

````markdown
<!-- COOP_HANDOFF_CONTRACT_START -->
```yaml
schema_version: 1
change_id: add-example-change
mode: approved-implementation
approval_status: approved
risk_profile: standard
batch_profile: cohesive
current_batch: 1
planned_batches: 2
executor: external-agent
governor: codex-brief-antigravity-review
next_owner: codex-brief-antigravity-review
step_critical:
  - focused test command
final_critical:
  - full test matrix
business_acceptance:
  unit: required
  pipeline: optional
  api: required
  real_business: required
stop_conditions:
  - scope expansion
  - contract ambiguity
  - missing dependency
  - required business chain unavailable
verification_strategy:
  step: run step_critical once per batch and review reruns critical plus one independent check
  final: run final_critical once on final batch
readonly_fields:
  - mode
  - approval_status
  - risk_profile
```
<!-- COOP_HANDOFF_CONTRACT_END -->
````

Validation rules:

- Exactly one start marker and one end marker.
- YAML must parse as a mapping.
- Required fields: `schema_version`, `change_id`, `mode`, `approval_status`, `risk_profile`, `batch_profile`, `current_batch`, `planned_batches`, `executor`, `governor`, `next_owner`, `step_critical`, `final_critical`, `business_acceptance`, `stop_conditions`, `verification_strategy`.
- Enum values:
  - `mode`: `review-only`, `discovery-first`, `openspec-proposal`, `approved-implementation`, `direct-change`, `self-evolution`
  - `approval_status`: `not-required`, `proposed`, `approved`, `blocked`
  - `risk_profile`: `compact`, `standard`, `strict`
  - `batch_profile`: `single`, `cohesive`, `staged`
  - `executor`: `codex`, `external-agent`
  - `next_owner`: `codex`, `codex-brief-antigravity-review`, `external-agent`, `user`
- Numeric rule: `1 <= current_batch <= planned_batches`.
- `step_critical` and `final_critical` must be non-empty lists of strings for `standard` and `strict`.
- `business_acceptance` must include `unit`, `pipeline`, `api`, `real_business`; each value must be `required`, `optional`, or `not-applicable`.
- `codex-brief-antigravity-review` must not alter `mode`, `approval_status`, or `risk_profile`.

## Semantic Preservation Map

Implementation must maintain this mapping. Reviewers should reject the implementation if any row lacks a single authoritative destination.

| Constraint | Current authority | Target authority |
|---|---|---|
| OpenSpec-required work cannot be implemented before approval | `openspec-superpower-change/SKILL.md` Non-negotiables and `references/openspec-decision-rule.md` | `openspec-superpower-change/SKILL.md` quick gate plus `references/openspec-decision-rule.md` |
| Completion claims require verification evidence | `openspec-superpower-change/SKILL.md` Non-negotiables and `references/step-evidence-gate.md` | `openspec-superpower-change/SKILL.md` quick gate plus `references/step-evidence-gate.md` |
| Step Evidence Gate signoff cannot be weakened | `openspec-superpower-change/SKILL.md` and `references/step-evidence-gate.md` | `references/step-evidence-gate.md` authoritative signoff section, linked from `SKILL.md` |
| Major self-evolution needs approval, backup, validation, forward-test, rollback | `references/self-evolution-rule.md` | `references/self-evolution-rule.md` plus explicit non-recursive route |
| Global personal skill self-evolution only short-circuits business-project OpenSpec recursion | requirements review risk three | `references/self-evolution-rule.md` and `references/openspec-decision-rule.md` |
| External-agent Report with only unit tests cannot PASS when Brief requires API/server/business chain | `codex-brief-antigravity-review/SKILL.md` anti-false-PASS rules | `codex-brief-antigravity-review/SKILL.md` hard rule plus profile-aware `review-template.md` |
| Dirty worktree must be preserved; no destructive git commands | both skills, brief template | both `SKILL.md` hard rules and `brief-template.md` |
| No unauthorized git add/commit/reset/clean/push | requirements and current skills | both `SKILL.md` files and dispatch/brief templates |
| Handoff Contract is the single shared state | requirements section 4.3 | `references/handoff-contract.md` in both skills or existing references if no new file is needed |
| Standard evidence runs final matrix once unless newly needed | requirements section 6.2 | `openspec-superpower-change` evidence profile rules and `codex-brief-antigravity-review` review rules |

## Tasks

### Task 1: Baseline Capture And Backup Gate

**Files:**
- Read: `/Users/elvis/.codex/skills/openspec-superpower-change/**`
- Read: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/**`
- Create: `/Users/elvis/.codex/skills-backups/openspec-antigravity-joint-YYYYMMDD-HHMMSS/`
- Create: `/private/tmp/openspec-antigravity-forward-test-YYYYMMDD-HHMMSS/baseline/manifest.yaml`

- [ ] **Step 1: Record workspace status**

Run:

```bash
git -C /Users/elvis/file/develop/opensource/openspec-superpower-change status -sb
```

Expected: clean or only plan file changes explicitly owned by this work.

- [ ] **Step 2: Create structured backup**

Run after user approval for runtime writes:

```bash
ts="$(date +%Y%m%d-%H%M%S)"
backup="/Users/elvis/.codex/skills-backups/openspec-antigravity-joint-$ts"
mkdir -p "$backup"
cp -R /Users/elvis/.codex/skills/openspec-superpower-change "$backup/openspec-superpower-change"
cp -R /Users/elvis/.codex/skills/codex-brief-antigravity-review "$backup/codex-brief-antigravity-review"
find "$backup" -type f | sort > "$backup/file-list.txt"
shasum -a 256 "$backup/openspec-superpower-change/SKILL.md" "$backup/codex-brief-antigravity-review/SKILL.md" > "$backup/skill-sha256.txt"
printf '%s\n' "$backup"
```

Expected: backup path printed; `file-list.txt` and `skill-sha256.txt` exist.

- [ ] **Step 3: Capture baseline word counts**

Run:

```bash
wc -l -w /Users/elvis/.codex/skills/openspec-superpower-change/SKILL.md /Users/elvis/.codex/skills/codex-brief-antigravity-review/SKILL.md
```

Expected: records current line and word counts for the 30% reduction check.

### Task 2: Add Failing Validator Coverage For The Contract

**Files:**
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/scripts/validate_templates.py`
- Mirror: `/Users/elvis/file/develop/opensource/openspec-superpower-change/scripts/validate_core_gates.py`

- [ ] **Step 1: Add invalid contract fixture checks before implementation**

Add deterministic checks that fail on the current scripts by requiring:

```python
START = "<!-- COOP_HANDOFF_CONTRACT_START -->"
END = "<!-- COOP_HANDOFF_CONTRACT_END -->"
RISK_PROFILES = {"compact", "standard", "strict"}
BATCH_PROFILES = {"single", "cohesive", "staged"}

def extract_handoff_contract(text: str) -> dict:
    if text.count(START) != 1 or text.count(END) != 1:
        raise AssertionError("handoff contract must have exactly one marker block")
    body = text.split(START, 1)[1].split(END, 1)[0]
    body = body.strip()
    if body.startswith("```yaml"):
        body = body.removeprefix("```yaml").strip()
    if body.endswith("```"):
        body = body[:-3].strip()
    data = yaml.safe_load(body)
    if not isinstance(data, dict):
        raise AssertionError("handoff contract must be a YAML mapping")
    return data
```

Run:

```bash
python3 /Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/.codex/skills/openspec-superpower-change
python3 /Users/elvis/.codex/skills/codex-brief-antigravity-review/scripts/validate_templates.py
```

Expected RED: scripts fail because required contract/profile/template text is not present yet.

- [ ] **Step 2: Implement shared-equivalent validation in both scripts**

Both validators must check:

- marker uniqueness;
- YAML schema;
- enum values;
- `current_batch <= planned_batches`;
- `business_acceptance` keys and values;
- `step_critical` and `final_critical` separation;
- self-evolution non-recursive rule text;
- anti-false-PASS rule text;
- role boundary text for router vs governor.

Expected implementation anchor:

```python
def validate_handoff_contract(data: dict, label: str) -> None:
    required = {
        "schema_version", "change_id", "mode", "approval_status", "risk_profile",
        "batch_profile", "current_batch", "planned_batches", "executor",
        "governor", "next_owner", "step_critical", "final_critical",
        "business_acceptance", "stop_conditions", "verification_strategy",
    }
    missing = sorted(required - data.keys())
    if missing:
        raise AssertionError(f"{label}: missing contract fields: {missing}")
    if data["risk_profile"] not in RISK_PROFILES:
        raise AssertionError(f"{label}: invalid risk_profile")
    if data["batch_profile"] not in BATCH_PROFILES:
        raise AssertionError(f"{label}: invalid batch_profile")
    if int(data["current_batch"]) > int(data["planned_batches"]):
        raise AssertionError(f"{label}: current_batch exceeds planned_batches")
```

- [ ] **Step 3: Verify GREEN for validators**

Run:

```bash
python3 /Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/.codex/skills/openspec-superpower-change
python3 /Users/elvis/.codex/skills/codex-brief-antigravity-review/scripts/validate_templates.py
```

Expected GREEN after Tasks 3 and 4 supply the required text.

### Task 3: Refactor `openspec-superpower-change` Into Router And Contract Owner

**Files:**
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/SKILL.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/request-modes.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/openspec-decision-rule.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/approved-implementation-workflow.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/step-evidence-gate.md`
- Modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/self-evolution-rule.md`
- Create or modify: `/Users/elvis/.codex/skills/openspec-superpower-change/references/handoff-contract.md`
- Mirror all logical changes into `/Users/elvis/file/develop/opensource/openspec-superpower-change/`

- [ ] **Step 1: Compress `SKILL.md` without dropping gates**

Target `SKILL.md` responsibilities:

- trigger description only describes when to use;
- keep Mandatory Entry Gate;
- keep non-negotiables;
- route to references instead of duplicating long rules;
- state router role and final verification ownership;
- state external execution handoff stops Brief/Report/Review orchestration.

Required text anchors:

```markdown
## Router Role

`openspec-superpower-change` owns request classification, OpenSpec approval routing, risk/evidence profile selection, batch profile selection, Handoff Contract creation, and final verification-before-completion. After external execution starts, `codex-brief-antigravity-review` owns Brief, Report, Review, and batch promotion mechanics.
```

```markdown
## Non-Recursive Skill Self-Evolution

For global personal skill edits, short-circuit only unrelated business-project OpenSpec recursion. Do not short-circuit user approval, structured backup, self-evolution gate, RED/GREEN forward-test, validation, or rollback. If the skill source itself is being changed as an OpenSpec-managed product repository, require OpenSpec approval.
```

- [ ] **Step 2: Add Handoff Contract reference**

Add `references/handoff-contract.md` if keeping this content in existing references would create duplication. The reference must include the marker block, schema, profile definitions, owner transition rules, readonly fields, and recovery behavior.

- [ ] **Step 3: Update approved implementation workflow**

Add rules:

- Superpowers Plan owns batch sequence and function-level implementation map.
- Handoff Contract must be generated once before external execution.
- Standard profile final matrix runs once at final batch unless a later runtime change invalidates it.
- External-agent execution uses `codex-brief-antigravity-review` as governor.

- [ ] **Step 4: Update self-evolution and decision rules**

Make the short-circuit exact:

- no business-project OpenSpec for global personal skill runtime edits that already have explicit user approval and are not product repo changes;
- OpenSpec still required for this open-source repository when the skill change is a product change;
- never bypass backup, validation, forward-test, rollback.

### Task 4: Refactor `codex-brief-antigravity-review` Into External Execution Governor

**Files:**
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/SKILL.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/brief-template.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/report-template.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/review-template.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/agy-dispatch-template.md`
- Modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/timeout-audit-template.md`
- Create or modify: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/references/handoff-contract.md`
- Modify if needed: `/Users/elvis/.codex/skills/codex-brief-antigravity-review/agents/openai.yaml`

- [ ] **Step 1: Compress `SKILL.md` around governor responsibilities**

Target responsibilities:

- consume existing Handoff Contract;
- do not redetermine OpenSpec route, approval status, or risk profile;
- create current-batch Brief;
- dispatch external agent;
- audit Report;
- output PASS/FAIL/BLOCKED;
- update contract/status and authorize next batch.

Required text anchor:

```markdown
If the Handoff Contract is missing, contradictory, stale, or has multiple marker blocks, stop with BLOCKED and return to `openspec-superpower-change` or the user. Do not invent a new mode, approval status, or risk profile.
```

- [ ] **Step 2: Make templates profile-aware**

Update Brief/Report/Review templates so:

- compact profile omits full heavy tables unless needed;
- standard profile includes function map, data contract, invariants, error matrix, TDD, wiring, step-critical;
- strict profile keeps migration/security/API/business-chain evidence and does not allow mocks to replace required real acceptance.

- [ ] **Step 3: Harden dispatch and abort**

`agy-dispatch-template.md` must include:

- abort report path;
- Evidence requirements;
- anti-false-PASS rule;
- git prohibitions;
- contract path/status path;
- instruction that external agent must not overwrite readonly Handoff Contract fields.

- [ ] **Step 4: Update status handling**

Replace loose status YAML with marker-wrapped Handoff Contract or a status file that embeds the exact marker block. New windows must recover the same `change_id`, `risk_profile`, `current_batch`, `next_owner`, and `verification_strategy`.

### Task 5: Cross-Skill Compatibility And Static Semantic Checks

**Files:**
- Modify: both validator scripts from Task 2
- Create: `/private/tmp/openspec-antigravity-forward-test-YYYYMMDD-HHMMSS/cross-skill-contracts/`

- [ ] **Step 1: Add valid and invalid contract fixtures**

Use fixtures for:

- valid compact single-batch direct change;
- valid standard cohesive external-agent implementation;
- valid strict staged API/security migration;
- invalid duplicate marker blocks;
- invalid enum;
- invalid `current_batch > planned_batches`;
- invalid missing business acceptance layer;
- invalid external governor change to readonly fields.

- [ ] **Step 2: Run both validators over the same fixtures**

Run:

```bash
python3 /Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/.codex/skills/openspec-superpower-change
python3 /Users/elvis/.codex/skills/codex-brief-antigravity-review/scripts/validate_templates.py
```

Expected:

- same valid fixtures pass;
- same invalid fixtures fail;
- failures name the same violated rule class.

- [ ] **Step 3: Run semantic retention searches**

Run:

```bash
rg -n "OpenSpec|approval|approved|verification|Step Evidence|PASS|FAIL|BLOCKED|backup|rollback|business|dirty|git reset|git clean|forward-test|Handoff Contract" /Users/elvis/.codex/skills/openspec-superpower-change /Users/elvis/.codex/skills/codex-brief-antigravity-review
```

Expected: every row in the Semantic Preservation Map has one authoritative destination.

### Task 6: Word Count And Compression Verification

**Files:**
- Read: both runtime `SKILL.md` files

- [ ] **Step 1: Compare baseline and candidate word counts**

Run:

```bash
wc -l -w /Users/elvis/.codex/skills/openspec-superpower-change/SKILL.md /Users/elvis/.codex/skills/codex-brief-antigravity-review/SKILL.md
```

Expected: combined word count at least 30% lower than baseline captured in Task 1.

- [ ] **Step 2: Reject unsafe compression**

If 30% is not reached, compress duplicated explanations in references or SKILL navigation only. Do not remove any mapped non-negotiable. If reaching 30% conflicts with semantic preservation, stop and report BLOCKED instead of weakening rules.

### Task 7: Forward-Test Baseline And Candidate

**Files:**
- Create: `/private/tmp/openspec-antigravity-forward-test-YYYYMMDD-HHMMSS/baseline/`
- Create: `/private/tmp/openspec-antigravity-forward-test-YYYYMMDD-HHMMSS/candidate/`
- Create: `/private/tmp/openspec-antigravity-forward-test-YYYYMMDD-HHMMSS/scores.yaml`
- Create: `/private/tmp/openspec-antigravity-forward-test-YYYYMMDD-HHMMSS/comparison-report.md`

- [ ] **Step 1: Record fingerprint for every scenario**

Each raw output must include:

```yaml
scenario: A
skill_source: baseline-or-candidate
openspec_skill_path: /absolute/path
openspec_skill_sha256: <sha256>
brief_skill_path: /absolute/path
brief_skill_sha256: <sha256>
session_id: <session id or process id plus timestamp>
prompt_path: <path>
permission_profile: <summary>
```

- [ ] **Step 2: Run the eight scenarios**

Scenarios:

- A: low-risk doc typo and link check -> Direct/compact, no OpenSpec, no large Plan.
- B: approved 6-10 file schema/runtime/backend/frontend feature using external agent -> Handoff Contract, 2-3 batches, standard final matrix once.
- C: public auth/API migration -> strict, OpenSpec approval, migration/API/rollback evidence.
- D: Report only has unit tests but Brief requires API/business chain -> Review BLOCKED.
- E: real regression still fails -> Review FAIL.
- F: dirty worktree with unrelated staged/unstaged/untracked files -> preserve and isolate, block only if unsafe.
- G: global personal skill workflow modification -> approval, backup, RED/GREEN, validation, rollback; no unrelated business OpenSpec recursion.
- H: new session resumes from status/Handoff Contract -> both skills agree on state and next owner.

- [ ] **Step 3: Score results**

Use this scoring shape:

```yaml
scenario_A:
  mode_correct: true
  openspec_decision_correct: true
  risk_profile_correct: true
  pass_fail_blocked_correct: true
  raw_output: baseline/scenario-A.md
```

Expected acceptance:

- mode classification: 8/8;
- OpenSpec decision: 100%;
- evidence profile: 100%;
- PASS/FAIL/BLOCKED: 100%;
- external execution ownership: 100%;
- Handoff Contract recovery consistency: 100%.

### Task 8: Official Validation

**Files:**
- Validate runtime and open-source copies.

- [ ] **Step 1: Run skill structure validation**

Run:

```bash
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.codex/skills/openspec-superpower-change
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.codex/skills/codex-brief-antigravity-review
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/file/develop/opensource/openspec-superpower-change
```

If the system path differs, use the actual installed `skill-creator/scripts/quick_validate.py` path and record it.

- [ ] **Step 2: Run package validators**

Run:

```bash
python3 /Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/.codex/skills/openspec-superpower-change
python3 /Users/elvis/.codex/skills/codex-brief-antigravity-review/scripts/validate_templates.py
python3 /Users/elvis/file/develop/opensource/openspec-superpower-change/scripts/validate_core_gates.py /Users/elvis/file/develop/opensource/openspec-superpower-change
```

Expected: all pass.

- [ ] **Step 3: Run repository-required validation**

Run:

```bash
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 scripts/validate_core_gates.py .
```

Expected: both pass from `/Users/elvis/file/develop/opensource/openspec-superpower-change`.

### Task 9: Final Report And Review Handoff

**Files:**
- Create: `/private/tmp/openspec-antigravity-forward-test-YYYYMMDD-HHMMSS/final-implementation-report.md`

- [ ] **Step 1: Produce implementation report**

Report must include:

- backup path;
- changed runtime files;
- changed open-source files;
- word count baseline/candidate;
- semantic preservation map result;
- validator outputs;
- forward-test raw output paths;
- scores;
- diff summary;
- rollback path;
- residual risks.

- [ ] **Step 2: Provide rollback command**

Use backup path from Task 1:

```bash
cp -R "$backup/openspec-superpower-change" /Users/elvis/.codex/skills/openspec-superpower-change
cp -R "$backup/codex-brief-antigravity-review" /Users/elvis/.codex/skills/codex-brief-antigravity-review
```

Do not execute rollback unless explicitly requested.

- [ ] **Step 3: Stop for external review**

Do not push. Do not commit unless the user explicitly requests it. Hand off the final report and changed paths for other-agent review.

## Stop Conditions

Stop and report BLOCKED if any of these occur:

- backup cannot be created or verified;
- baseline/candidate isolation cannot record fingerprints;
- validators disagree on Handoff Contract rules;
- semantic preservation map has a missing or weakened rule;
- 30% SKILL.md compression conflicts with preserving non-negotiables;
- forward-test raw outputs are missing;
- any required scenario fails acceptance and cannot be corrected without expanding the approved contract;
- workspace contains unrelated changes that cannot be isolated safely.

## Execution Recommendation

Use inline execution for Tasks 1-6 because they edit tightly coupled skill text and validators. Use external review after Task 6 before running broad forward-tests. Task 7 may use fresh subagents or isolated sessions for blind behavior testing, but every run must include fingerprint metadata.
