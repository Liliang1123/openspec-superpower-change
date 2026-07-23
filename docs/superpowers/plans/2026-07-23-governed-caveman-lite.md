# Governed Caveman Lite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILLS:
> `superpowers:subagent-driven-development` for task execution,
> `superpowers:writing-skills` before any Skill-source edit,
> `superpowers:test-driven-development` for RED/GREEN source work,
> `superpowers:requesting-code-review` after source implementation and runtime
> synchronization, and `superpowers:verification-before-completion` before any
> success claim. Use `superpowers:systematic-debugging` before changing an
> unexplained failure. Steps use checkbox (`- [ ]`) syntax for tracking. The
> project prohibition on unrequested Git mutation overrides generic commit
> steps: do not run `git add`, `git commit`, `git push`, `git reset`, or
> `git clean`.

**Goal:** Add a built-in, opt-in `governed-caveman-lite` presentation profile
with the canonical commands `OpenSpec 精简模式` and `OpenSpec 正常模式`, while
preserving every governance and safety obligation.

**Architecture:** `SKILL.md` owns entry discovery, activation, style,
conversation lifecycle, precedence, and governance boundaries.
`references/response-patterns.md` owns response-surface rules; the bilingual
READMEs teach the shortest usage. `scripts/validate_core_gates.py` and
`tests/test_workflow_rules.py` mechanically bind each rule to its owning
artifact. The READMEs remain repository-only; runtime validation accepts their
paired absence while still validating every portable owner. Runtime
synchronization uses the repository's allowlisted path/hash-based transaction.

**Tech Stack:** Markdown Skill contracts, Python standard-library validation and
`unittest`, OpenSpec CLI, cross-CLI sync validator.

**Approved contract:** `openspec/changes/add-governed-caveman-lite/`

**Evidence profile:** `standard`

**Worktree:** `/private/tmp/openspec-superpower-change-add-governed-caveman-lite`
on branch `codex/add-governed-caveman-lite`

**Backup:** `/private/tmp/add-governed-caveman-lite-backup-20260723-001`

**Allowed source files:**

- `SKILL.md`
- `references/response-patterns.md`
- `README.md`
- `README_cn.md`
- `scripts/validate_core_gates.py`
- `tests/test_workflow_rules.py`
- `openspec/changes/add-governed-caveman-lite/**`
- `openspec/specs/skill-workflow-governance/spec.md` (archive merge only)
- `openspec/changes/archive/2026-07-23-add-governed-caveman-lite/**`
  (archive move only)
- `docs/superpowers/plans/2026-07-23-governed-caveman-lite.md`

**Stop conditions:** Stop on scope expansion, invalid approval, unexplained test
failure, unresolved Review finding, active incompatible schema-4 lifecycle,
runtime target restore failure, sensitive-data concern, or required target
drift/discovery failure.

## Standard Step Evidence Gate map

Emit each Gate record in concise full form. TDD RED/GREEN checkboxes are
micro-steps inside the source slice and do not create extra Gate records.

### Source-contract slice

Gate 1, before the first test edit:

- Evidence gathered: approved OpenSpec proposal/design/spec/tasks, baseline
  validation PASS, structured backup, current implementation plan, and
  independent Preflight `PASS`.
- Root cause candidate: the Router has generic token-lean guidance but no
  canonical built-in `governed-caveman-lite` lifecycle or artifact-owned
  enforcement.
- Files allowed to change: the six source/test/doc files and approved OpenSpec
  and plan files listed above; archive-only paths remain closed in this slice.
- Tests to add/run: the two focused RED/GREEN tests, core validator, required
  project validation matrix, seven isolated forward scenarios, and complete
  diff Review.
- Rollback path: the structured source backup plus the isolated worktree;
  restore only on an explicit rollback decision.
- Stop condition: wrong RED cause, unrelated failure, scope drift, invalid
  approval, missing evidence, or unresolved Review finding.

`step_critical` for this slice:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s tests -p 'test_workflow_rules.py' -k governed_caveman_lite -v
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
```

Before source-slice Gate 2, use `superpowers:requesting-code-review`. The
distinct standard Review must inspect the actual complete source diff, rerun
both `step_critical` commands, and independently remove one protected-surface
phrase from an in-memory fixture to prove the validator rejects it.

Gate 2 must record actual changed files, both `step_critical` results, the full
validation and forward-scenario results, residual risk, unrelated-file audit,
and the distinct Review result/evidence. Its whole-task decision is exactly
`deferred to references/completion-contract.md`. Do not enter runtime
synchronization until every field is present and Review is `PASS`.

### Runtime-sync slice

Gate 1, after source Review PASS and before the first runtime apply:

- Evidence gathered: reviewed path/hash-only sync plan, fresh pre-apply
  path/hash/mode baseline for every required target, source Review PASS, and no
  active incompatible schema-4 lifecycle.
- Root cause candidate: portable source and required runtime copies differ only
  by the approved profile change.
- Files allowed to change: allowlisted portable files and managed global-rule
  blocks declared by the reviewed sync plan; no README or CLI-native state.
- Tests to add/run: per-target apply/verify, runtime core/Skill validators,
  `verify-all`, discovery, sensitive-path audit, and final cross-target Review.
- Rollback path: transaction backups plus byte/mode comparison against the
  fresh pre-apply baseline.
- Stop condition: plan drift, unallowlisted path, apply/verify failure,
  restoration mismatch, discovery failure, validator failure, or sensitive
  path/content finding.

`step_critical` for this slice:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify-all \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json
```

Before runtime-slice Gate 2, use `superpowers:requesting-code-review`. The
distinct standard Review must inspect the applied plan and target hashes, rerun
`verify-all`, rerun all six runtime validation commands, and use fresh Grok
discovery as the independent behavior probe.

Gate 2 must record actual runtime paths changed, per-target apply/verify and
validator results, restore-baseline evidence, discovery/audit results, residual
risk, unrelated-target audit, and the distinct Review result/evidence. Its
whole-task decision is exactly `deferred to references/completion-contract.md`.

### Final completion boundary

After implementation Review PASS and Project Learning Closeout, invoke
`superpowers:verification-before-completion`. `final_critical` is the fresh
post-archive project validation matrix, `verify-all`, consumed Grok discovery,
all six runtime validation commands, and final complete-diff Review described
in Task 4 Step 9. Any later source or runtime mutation invalidates affected
final evidence.

---

### Task 1: Add RED contract tests

**Files:**

- Modify: `tests/test_workflow_rules.py`
- Contract: `openspec/changes/add-governed-caveman-lite/specs/skill-workflow-governance/spec.md`

Before Step 1, apply `superpowers:writing-skills` and
`superpowers:test-driven-development`; execute Task 1 and Task 2 through
`superpowers:subagent-driven-development`.

- [ ] **Step 1: Load the profile's owning artifacts in the test fixture**

Add these fields to `WorkflowRulesTest.setUpClass`:

```python
cls.response_patterns = (
    ROOT / "references" / "response-patterns.md"
).read_text(encoding="utf-8")
cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
cls.readme_cn = (ROOT / "README_cn.md").read_text(encoding="utf-8")
```

- [ ] **Step 2: Add an entry-discovery and boundary test**

Add:

```python
def test_governed_caveman_lite_profile_is_entry_discoverable_and_bounded(self):
    description = self.skill.split("---", 2)[1]
    for command in ("OpenSpec 精简模式", "OpenSpec 正常模式"):
        self.assertIn(command, description)

    heading = "## Governed Caveman Lite output mode"
    self.assertIn(heading, self.skill)
    profile = self.skill.split(heading, 1)[1].split("\n## ", 1)[0]
    normalized_profile = " ".join(profile.split())
    for obligation in (
        "governed-caveman-lite",
        "OpenSpec 精简模式：<任务>",
        "OpenSpec 正常模式",
        "concise professional full sentences",
        "current conversation",
        "latest explicit OpenSpec mode command",
        "presentation state only",
        "never invokes or delegates to a separate `caveman` skill",
        "works when one is unavailable",
        "does not activate by default",
        "routing, approval, evidence, Review, verification, completion, Git, or publication authority",
        "Gate 0",
        "mandatory governance/approval fields",
        "OpenSpec artifacts",
        "plans",
        "Handoff/evidence artifacts",
        "canonical state transitions",
        "PASS/FAIL/BLOCKED",
        "final verification",
        "final Review",
        "critical commands",
        "rollback instructions",
        "security warnings",
        "destructive confirmations",
    ):
        self.assertIn(obligation, normalized_profile)

    for text in (self.response_patterns, self.readme, self.readme_cn):
        self.assertIn("OpenSpec 精简模式", text)
        self.assertIn("OpenSpec 正常模式", text)
```

- [ ] **Step 3: Add an artifact-owned validator regression**

Add:

```python
def test_governed_caveman_lite_validator_binds_owning_artifacts(self):
    def strip_owned_section(text, heading, needle):
        prefix, remainder = text.split(heading, 1)
        section, suffix = remainder.split("\n## ", 1)
        self.assertIn(needle, section)
        section = section.replace(needle, "removed protected contract", 1)
        return f"{prefix}{heading}{section}\n## {suffix}"

    self.assertTrue(
        hasattr(self.validator, "validate_governed_caveman_lite"),
        "validator must own governed Caveman Lite checks",
    )
    self.validator.validate_governed_caveman_lite(
        self.skill, self.response_patterns, self.readme, self.readme_cn
    )
    self.validator.validate_governed_caveman_lite(
        self.skill, self.response_patterns
    )
    with self.assertRaisesRegex(AssertionError, "bilingual READMEs"):
        self.validator.validate_governed_caveman_lite(
            self.skill, self.response_patterns, self.readme, None
        )
    stripped_skill = self.skill.replace(
        "OpenSpec 精简模式：<任务>", "missing governed enable form", 1
    )
    with self.assertRaisesRegex(
        AssertionError, "SKILL.md governed Caveman Lite"
    ):
        self.validator.validate_governed_caveman_lite(
            stripped_skill, self.response_patterns, self.readme, self.readme_cn
        )

    protected_skill = (
        "routing, approval, evidence, Review, verification, completion, Git, or publication authority",
        "Gate 0",
        "mandatory governance/approval fields",
        "OpenSpec artifacts",
        "plans",
        "Handoff/evidence artifacts",
        "canonical state transitions",
        "PASS/FAIL/BLOCKED",
        "final verification",
        "final Review",
        "critical commands",
        "rollback instructions",
        "security warnings",
        "destructive confirmations",
    )
    for needle in protected_skill:
        with self.subTest(owner="SKILL.md", needle=needle):
            mutated = strip_owned_section(
                self.skill, "## Governed Caveman Lite output mode", needle
            )
            with self.assertRaisesRegex(
                AssertionError, "SKILL.md governed Caveman Lite"
            ):
                self.validator.validate_governed_caveman_lite(
                    mutated,
                    self.response_patterns,
                    self.readme,
                    self.readme_cn,
                )

    protected_responses = (
        "presentation state only",
        "routing, approval, evidence, Review, verification, completion, Git, or publication authority",
        "Gate 0",
        "mandatory governance-step or approval field",
        "OpenSpec artifacts",
        "plans",
        "Handoff/evidence artifacts",
        "canonical state transitions",
        "PASS/FAIL/BLOCKED",
        "final verification",
        "final Review",
        "critical commands",
        "rollback instructions",
        "security warnings",
        "destructive confirmations",
    )
    for needle in protected_responses:
        with self.subTest(owner="response-patterns.md", needle=needle):
            mutated = strip_owned_section(
                self.response_patterns, "### Governed Caveman Lite", needle
            )
            with self.assertRaisesRegex(
                AssertionError, "response-patterns.md governed Caveman Lite"
            ):
                self.validator.validate_governed_caveman_lite(
                    self.skill, mutated, self.readme, self.readme_cn
                )
```

- [ ] **Step 4: Run the focused test and verify RED**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s tests -p 'test_workflow_rules.py' -k governed_caveman_lite -v
```

Expected: two intentional assertion failures—one reporting the first missing
entry-discoverable profile obligation (`OpenSpec 精简模式`) and one reporting the
missing validator function. The guarded heading assertion prevents an
`IndexError` after partial implementation. An `IndexError`, passing test,
import error, or unrelated failure does not satisfy RED.

- [ ] **Step 5: Review the RED diff**

Confirm only the test fixture and two focused tests changed. Confirm the tests
assert activation, disable, lite semantics, lifecycle, latest-command
precedence, no external dependency, default-off behavior, and protected
governance surfaces.

---

### Task 2: Implement the minimal source contract

**Files:**

- Modify: `SKILL.md`
- Modify: `references/response-patterns.md`
- Modify: `README.md`
- Modify: `README_cn.md`
- Modify: `scripts/validate_core_gates.py`
- Test: `tests/test_workflow_rules.py`

- [ ] **Step 1: Make the commands entry-discoverable**

Extend only the `SKILL.md` frontmatter description's trigger list with
`OpenSpec 精简模式` and `OpenSpec 正常模式`. Keep the frontmatter keys exactly
`name` and `description`; do not summarize implementation workflow there.

- [ ] **Step 2: Replace the generic output section with the approved profile**

Keep the implementation concise, but include rules equivalent to:

```markdown
## Governed Caveman Lite output mode

`governed-caveman-lite` is presentation state only. It never changes routing,
approval, evidence, Review, verification, completion, Git, or publication
authority. It applies directly, never invokes or delegates to a separate
`caveman` skill, and works when one is unavailable.

- Enable with `OpenSpec 精简模式：<任务>` or send `OpenSpec 精简模式` before
  the task.
- Use concise professional full sentences; remove filler and repetition without
  abbreviating technical terms or omitting ordering and required fields.
- Keep it active for the current conversation. Disable with
  `OpenSpec 正常模式`; the latest explicit OpenSpec mode command controls Router
  prose even after a prior Caveman-style instruction.
- It does not activate by default.
- Gate 0, mandatory governance/approval fields, OpenSpec artifacts, plans,
  Handoff/evidence artifacts, canonical state transitions, PASS/FAIL/BLOCKED,
  final verification, final Review, critical commands, rollback instructions,
  security warnings, and destructive confirmations remain structurally
  complete.
- Progress, findings, risk summaries, command explanations, and ordinary final
  chat summaries may be concise only when required fields and evidence remain.
```

- [ ] **Step 3: Add the response pattern**

Under `## Token budget control` in `references/response-patterns.md`, add a
`### Governed Caveman Lite` subsection with the canonical enable/disable forms,
conversation lifecycle, latest-command precedence, default-off rule, direct
operation without external Caveman invocation/delegation, and explicit
protected surfaces. Do not duplicate or redefine routing, approval, evidence,
or completion contracts.

- [ ] **Step 4: Add one short bilingual usage section**

Add `## Governed Caveman Lite` to `README.md` and `## 治理精简模式` to
`README_cn.md`. Each section must show exactly:

```text
OpenSpec 精简模式：<任务>
```

and:

```text
OpenSpec 正常模式
```

Explain that the mode is conversation-scoped, default-off, built in, and never
compresses governance/safety artifacts.

- [ ] **Step 5: Add artifact-owned validation**

Add this function near the other top-level validators in
`scripts/validate_core_gates.py`:

```python
def validate_governed_caveman_lite(
    skill: str,
    response_patterns: str,
    readme: str | None = None,
    readme_cn: str | None = None,
) -> None:
    def owned_section(text: str, heading: str, label: str) -> str:
        if text.count(heading) != 1:
            raise AssertionError(
                f"{label}: expected exactly one owned section {heading!r}"
            )
        return text.split(heading, 1)[1].split("\n## ", 1)[0]

    frontmatter = skill.split("---", 2)[1]
    for command in ("OpenSpec 精简模式", "OpenSpec 正常模式"):
        require(frontmatter, command, "SKILL.md governed Caveman Lite frontmatter")

    normalized_skill = " ".join(
        owned_section(
            skill,
            "## Governed Caveman Lite output mode",
            "SKILL.md governed Caveman Lite",
        ).split()
    )
    for needle in (
        "governed-caveman-lite",
        "OpenSpec 精简模式：<任务>",
        "OpenSpec 正常模式",
        "concise professional full sentences",
        "current conversation",
        "latest explicit OpenSpec mode command",
        "presentation state only",
        "never invokes or delegates to a separate `caveman` skill",
        "works when one is unavailable",
        "does not activate by default",
        "routing, approval, evidence, Review, verification, completion, Git, or publication authority",
        "Gate 0",
        "mandatory governance/approval fields",
        "OpenSpec artifacts",
        "plans",
        "Handoff/evidence artifacts",
        "canonical state transitions",
        "PASS/FAIL/BLOCKED",
        "final verification",
        "final Review",
        "critical commands",
        "rollback instructions",
        "security warnings",
        "destructive confirmations",
    ):
        require(normalized_skill, needle, "SKILL.md governed Caveman Lite")

    normalized_responses = " ".join(
        owned_section(
            response_patterns,
            "### Governed Caveman Lite",
            "response-patterns.md governed Caveman Lite",
        ).split()
    )
    for needle in (
        "governed-caveman-lite",
        "OpenSpec 精简模式：<任务>",
        "OpenSpec 正常模式",
        "concise professional full sentences",
        "current conversation",
        "latest explicit OpenSpec mode command",
        "presentation state only",
        "never invokes or delegates to a separate `caveman` skill",
        "works when one is unavailable",
        "does not activate by default",
        "routing, approval, evidence, Review, verification, completion, Git, or publication authority",
        "Gate 0",
        "mandatory governance-step or approval field",
        "OpenSpec artifacts",
        "plans",
        "Handoff/evidence artifacts",
        "canonical state transitions",
        "PASS/FAIL/BLOCKED",
        "final verification",
        "final Review",
        "critical commands",
        "rollback instructions",
        "security warnings",
        "destructive confirmations",
    ):
        require(
            normalized_responses,
            needle,
            "response-patterns.md governed Caveman Lite",
        )

    if (readme is None) != (readme_cn is None):
        raise AssertionError(
            "governed Caveman Lite bilingual READMEs must both exist or both "
            "be omitted from a portable runtime"
        )
    if readme is not None and readme_cn is not None:
        for text, heading, label in (
            (readme, "## Governed Caveman Lite", "README.md"),
            (readme_cn, "## 治理精简模式", "README_cn.md"),
        ):
            owned = owned_section(text, heading, label)
            require(owned, "OpenSpec 精简模式：<任务>", label)
            require(owned, "OpenSpec 正常模式", label)
```

In `main`, read `README.md` and `README_cn.md` when present, preserving `None`
when the paired repository-only files are absent from a portable runtime. Call
`validate_governed_caveman_lite(skill, response_patterns, readme, readme_cn)`
after frontmatter/reference checks and before completion-contract validation.

- [ ] **Step 6: Run the focused test and verify GREEN**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s tests -p 'test_workflow_rules.py' -k governed_caveman_lite -v
```

Expected: both focused tests PASS.

- [ ] **Step 7: Run focused validator verification**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
```

Expected: `Core gates valid: <worktree>`.

- [ ] **Step 8: Run negative searches**

Run:

```bash
rg -n "OpenSpec 精简模式|OpenSpec 正常模式|governed-caveman-lite" \
  SKILL.md references/response-patterns.md README.md README_cn.md \
  scripts/validate_core_gates.py tests/test_workflow_rules.py
rg -n -i "enable.*by default|default.*enable|invoke.*separate.*caveman|delegate.*caveman" \
  SKILL.md references/response-patterns.md README.md README_cn.md
```

Expected: the positive search covers all owning artifacts. The negative search
has no match that enables the profile by default or delegates to another skill.
Confirm the existing portable manifest still includes `SKILL.md`,
`references/response-patterns.md`, and `scripts/validate_core_gates.py` for all
three required targets, while its existing repository-only README rule remains
unchanged.

---

### Task 3: Validate source behavior and run Review loops

**Files:**

- Verify all files in the approved source scope
- Update only files already allowed when a Review finding requires correction

- [ ] **Step 1: Run the complete source validation matrix**

Run:

```bash
/opt/anaconda3/bin/python3 \
  /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
DO_NOT_TRACK=1 openspec validate add-governed-caveman-lite --strict
git diff --check
```

Expected: every command exits 0; the unittest suite reports zero failures.

- [ ] **Step 2: Run seven isolated forward-test scenarios**

Use fresh subagents or isolated fixtures without expected-answer leakage:

1. `OpenSpec 精简模式：<Review-only task>` activates concise full sentences.
2. An OpenSpec proposal remains structurally complete while the profile is active.
3. Final verification and final Review keep every evidence field.
4. `OpenSpec 正常模式` returns later Router prose to normal style.
5. The profile works when no separate Caveman skill is available.
6. The latest explicit OpenSpec mode command wins after a prior Caveman-style
   instruction.
7. A normal Router request without the enable phrase does not force the profile.

Record only sanitized scenario/result summaries, not raw private prompts or
runtime traces.

- [ ] **Step 3: Run spec-compliance Review**

Review the complete diff against
`openspec/changes/add-governed-caveman-lite/{proposal.md,design.md,tasks.md}`
and its spec delta. Return every missing or extra behavior for correction.

- [ ] **Step 4: Run code-quality and High Review**

After spec Review PASS, inspect actual files and complete diff; trace each claim
to the Skill/validator/test/docs mechanism; rerun the focused test and validator;
probe removal of the owned Skill phrase; audit sensitive data, temp traces,
unrelated files, and default-on/external-delegation risks.

- [ ] **Step 5: Correct and repeat**

Every actionable finding returns to the same allowed scope for fix, fresh
verification, spec Review, then quality Review. Do not proceed while either
Review is `FAIL` or `BLOCKED`.

---

### Task 4: Synchronize runtimes and close the change

**Files and generated evidence:**

- Source: approved repository files
- Runtime targets:
  - `/Users/elvis/.codex/skills/openspec-superpower-change`
  - `/Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change`
  - `/Users/elvis/.grok/skills/openspec-superpower-change`
- Generated sync plan:
  `/private/tmp/add-governed-caveman-lite-sync-plan.json`
- Pre-apply path/hash/mode baseline:
  `/private/tmp/add-governed-caveman-lite-runtime-baseline.json`
- Transaction backups:
  `/private/tmp/add-governed-caveman-lite-sync-backup-20260723-001`
- Temporary Grok inspect evidence:
  `/private/tmp/add-governed-caveman-lite-grok-inspect.json`

- [ ] **Step 1: Inventory active schema-4 contracts and target paths**

Run:

```bash
find docs/agent-collab -name status.md -type f -print 2>/dev/null | sort
```

If any active schema-4 contract exists, stop runtime application until it
reaches its existing terminal state.

- [ ] **Step 2: Generate and Review the path/hash-only plan**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py plan \
  --manifest references/cross-cli-portable-manifest.json \
  --openspec-source /private/tmp/openspec-superpower-change-add-governed-caveman-lite \
  --brief-source /Users/elvis/file/develop/opensource/codex-brief-antigravity-review \
  --codex-skills-root /Users/elvis/.codex/skills \
  --codex-rule-file /Users/elvis/.codex/AGENTS.md \
  --antigravity-skills-root /Users/elvis/.gemini/antigravity-cli/skills \
  --antigravity-rule-file /Users/elvis/.gemini/GEMINI.md \
  --grok-skills-root /Users/elvis/.grok/skills \
  --grok-rule-file /Users/elvis/.grok/AGENTS.md \
  --output /private/tmp/add-governed-caveman-lite-sync-plan.json
```

Review that the plan contains only allowlisted relative paths, hashes, target
roots, and managed-rule metadata. It must not include credentials, sessions,
caches, logs, model settings, hooks, or other sensitive categories.

Capture a fresh mode-`0600` path/hash/mode baseline for the two planned Skill
trees and managed rule file of every target:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import hashlib
import json
import os
import stat
from pathlib import Path

plan = json.loads(
    Path("/private/tmp/add-governed-caveman-lite-sync-plan.json").read_text(
        encoding="utf-8"
    )
)
output = Path("/private/tmp/add-governed-caveman-lite-runtime-baseline.json")
if output.exists() or output.is_symlink():
    raise SystemExit(f"refusing to replace existing baseline: {output}")


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            value.update(chunk)
    return value.hexdigest()


def entry(path):
    metadata = path.lstat()
    if stat.S_ISLNK(metadata.st_mode):
        raise SystemExit(f"baseline path may not be a symlink: {path}")
    mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
    if stat.S_ISDIR(metadata.st_mode):
        return {"kind": "directory", "mode": mode}
    if stat.S_ISREG(metadata.st_mode):
        return {"kind": "file", "mode": mode, "sha256": digest(path)}
    raise SystemExit(f"unsupported baseline path type: {path}")


def tree(root):
    if not root.is_dir() or root.is_symlink():
        raise SystemExit(f"invalid baseline Skill root: {root}")
    paths = [root, *sorted(root.rglob("*"), key=lambda item: item.as_posix())]
    return {
        ("." if path == root else path.relative_to(root).as_posix()): entry(path)
        for path in paths
    }


baseline = {}
for target_id, target in sorted(plan["targets"].items()):
    skill_names = sorted({item["skill"] for item in target["files"]})
    skills = {
        str(Path(target["skills_root"]) / skill): tree(
            Path(target["skills_root"]) / skill
        )
        for skill in skill_names
    }
    rule_path = Path(target["rule_file"])
    baseline[target_id] = {
        "skills": skills,
        "rule": {"path": str(rule_path), "state": entry(rule_path)},
    }

descriptor = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
    json.dump(baseline, stream, indent=2, sort_keys=True)
    stream.write("\n")
if stat.S_IMODE(output.stat().st_mode) != 0o600:
    raise SystemExit("runtime baseline mode is not 0600")
print("runtime baseline captured for:", ", ".join(sorted(baseline)))
PY
```

Review the baseline structurally: it may contain only target paths, file
SHA-256 values, kinds, and modes; never file contents.

- [ ] **Step 3: Apply and verify one target at a time**

Define this baseline verifier in the same shell used for the target operations:

```bash
verify_runtime_baseline() {
  PYTHONDONTWRITEBYTECODE=1 python3 - "$1" <<'PY'
import hashlib
import json
import stat
import sys
from pathlib import Path

target_id = sys.argv[1]
baseline = json.loads(
    Path("/private/tmp/add-governed-caveman-lite-runtime-baseline.json").read_text(
        encoding="utf-8"
    )
)
if target_id not in baseline:
    raise SystemExit(f"unknown runtime baseline target: {target_id}")


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            value.update(chunk)
    return value.hexdigest()


def entry(path):
    metadata = path.lstat()
    if stat.S_ISLNK(metadata.st_mode):
        raise SystemExit(f"runtime path became a symlink: {path}")
    mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
    if stat.S_ISDIR(metadata.st_mode):
        return {"kind": "directory", "mode": mode}
    if stat.S_ISREG(metadata.st_mode):
        return {"kind": "file", "mode": mode, "sha256": digest(path)}
    raise SystemExit(f"unsupported runtime path type: {path}")


def tree(root):
    if not root.is_dir() or root.is_symlink():
        raise SystemExit(f"invalid runtime Skill root: {root}")
    paths = [root, *sorted(root.rglob("*"), key=lambda item: item.as_posix())]
    return {
        ("." if path == root else path.relative_to(root).as_posix()): entry(path)
        for path in paths
    }


expected = baseline[target_id]
current = {
    "skills": {
        root: tree(Path(root))
        for root in sorted(expected["skills"])
    },
    "rule": {
        "path": expected["rule"]["path"],
        "state": entry(Path(expected["rule"]["path"])),
    },
}
if current != expected:
    raise SystemExit(f"runtime restore baseline mismatch: {target_id}")
print(f"runtime baseline match: {target_id}")
PY
}
```

Run each pair in order. The pre-apply comparison detects drift after the
snapshot. An `apply` failure invokes the transaction's automatic restoration,
then the same command proves byte and mode parity before stopping:

```bash
verify_runtime_baseline codex || exit 1
if ! PYTHONDONTWRITEBYTECODE=1 python3 \
  scripts/validate_cross_cli_sync.py apply \
  --target codex \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json \
  --backup-root /private/tmp/add-governed-caveman-lite-sync-backup-20260723-001
then
  verify_runtime_baseline codex || exit 2
  exit 1
fi
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify \
  --target codex \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json || exit 1

verify_runtime_baseline antigravity-cli || exit 1
if ! PYTHONDONTWRITEBYTECODE=1 python3 \
  scripts/validate_cross_cli_sync.py apply \
  --target antigravity-cli \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json \
  --backup-root /private/tmp/add-governed-caveman-lite-sync-backup-20260723-001
then
  verify_runtime_baseline antigravity-cli || exit 2
  exit 1
fi
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify \
  --target antigravity-cli \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json || exit 1

verify_runtime_baseline grok-cli || exit 1
if ! PYTHONDONTWRITEBYTECODE=1 python3 \
  scripts/validate_cross_cli_sync.py apply \
  --target grok-cli \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json \
  --backup-root /private/tmp/add-governed-caveman-lite-sync-backup-20260723-001
then
  verify_runtime_baseline grok-cli || exit 2
  exit 1
fi
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify \
  --target grok-cli \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json || exit 1
```

`apply` performs its own verification inside the atomic transaction. Therefore
an apply failure must restore and match the baseline. A later standalone
`verify` failure indicates post-transaction drift: stop `BLOCKED`, preserve all
backups, and do not blindly overwrite potentially concurrent external changes.

- [ ] **Step 4: Verify Grok discovery without retaining raw output**

Capture `grok inspect --json` in the declared mode-`0600` temporary path:

```bash
(
  umask 077
  /Users/elvis/.local/bin/grok inspect --json \
    > /private/tmp/add-governed-caveman-lite-grok-inspect.json
)
test "$(stat -f '%Lp' \
  /private/tmp/add-governed-caveman-lite-grok-inspect.json)" = "600"
```

Then run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py \
  verify-discovery --target grok-cli \
  --inspect-json /private/tmp/add-governed-caveman-lite-grok-inspect.json \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json \
  --consume
```

The raw inspect file must be consumed or removed after verification and must
never be copied into repository artifacts or quoted in Review output.

- [ ] **Step 5: Verify all targets and run sensitive-path audit**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py verify-all \
  --plan /private/tmp/add-governed-caveman-lite-sync-plan.json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_cross_cli_sync.py audit \
  --openspec-source /private/tmp/openspec-superpower-change-add-governed-caveman-lite \
  --brief-source /Users/elvis/file/develop/opensource/codex-brief-antigravity-review \
  --report-paths-only
```

- [ ] **Step 6: Validate each runtime skill**

Run:

```bash
/opt/anaconda3/bin/python3 \
  /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/elvis/.codex/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 python3 \
  /Users/elvis/.codex/skills/openspec-superpower-change/scripts/validate_core_gates.py \
  /Users/elvis/.codex/skills/openspec-superpower-change

/opt/anaconda3/bin/python3 \
  /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 python3 \
  /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change/scripts/validate_core_gates.py \
  /Users/elvis/.gemini/antigravity-cli/skills/openspec-superpower-change

/opt/anaconda3/bin/python3 \
  /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/elvis/.grok/skills/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 python3 \
  /Users/elvis/.grok/skills/openspec-superpower-change/scripts/validate_core_gates.py \
  /Users/elvis/.grok/skills/openspec-superpower-change
```

- [ ] **Step 7: Run Project Learning Closeout audit**

Classify the proposal/implementation Review history. Promote nothing unless two
independent signals establish the same project-local invariant or one
high-severity security, integrity, data-loss, or false-PASS event exists.

- [ ] **Step 8: Reconcile and archive OpenSpec**

Mark completed tasks with exact evidence. Before archival, preserve
`openspec/specs/skill-workflow-governance/spec.md` in the declared structured
backup. Run:

```bash
DO_NOT_TRACK=1 openspec validate add-governed-caveman-lite --strict
DO_NOT_TRACK=1 openspec archive add-governed-caveman-lite --yes
DO_NOT_TRACK=1 openspec validate --all --strict --no-interactive
```

The archive may only merge the approved delta into
`openspec/specs/skill-workflow-governance/spec.md` and move the approved change
to `openspec/changes/archive/2026-07-23-add-governed-caveman-lite/`. Any other
source change is a stop condition. Archival does not authorize Git staging,
commit, push, merge, or publication.

- [ ] **Step 9: Run fresh final verification and final Review**

After the last source, learning, archive, or runtime change, rerun the complete
project validation matrix, replacing the pre-archive change-specific command
with `DO_NOT_TRACK=1 openspec validate --all --strict --no-interactive`.
Regenerate and consume the mode-`0600` Grok inspect evidence, rerun
`verify-all`, rerun the six runtime validation commands from Step 6, and run a
final complete-diff Review. Report the backup cleanup result, runtime target
results, residual risks, and publication state.

- [ ] **Step 10: Clean temporary backups only after success**

Delete only these exact temporary paths after every source/runtime/forward-test/
Review/rollback decision passes:

```text
/private/tmp/add-governed-caveman-lite-backup-20260723-001
/private/tmp/add-governed-caveman-lite-sync-backup-20260723-001
/private/tmp/add-governed-caveman-lite-sync-plan.json
/private/tmp/add-governed-caveman-lite-runtime-baseline.json
/private/tmp/add-governed-caveman-lite-grok-inspect.json
```

Keep repository history as the long-term rollback mechanism. Do not remove the
implementation worktree until the user selects a branch-completion option.
