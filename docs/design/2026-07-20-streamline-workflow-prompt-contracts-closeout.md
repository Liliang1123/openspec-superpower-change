# Streamlined Workflow Prompt Contracts Closeout

Date: 2026-07-20
Change: `streamline-workflow-prompt-contracts`
Status: **COMPLETE — push/publication decision remains pending**

## Outcome

The targeted redesign keeps the original governance strength while reducing
competing prompt contracts and route load:

- The Superpowers feature source now consistently preserves the Option 2
  worktree; automatic cleanup applies only to Options 1 and 4 and grants no Git
  authority. Installed-main integration remains blocked as recorded below.
- Router whole-task completion has one canonical owner in
  `references/completion-contract.md`; secondary artifacts retain local
  slice/batch reminders and validated pointers instead of second checklists.
- Companion keeps one thin, mutually exclusive route entry. Standalone review
  stays request-scoped; valid-Handoff execution loads the complete governor in
  `references/handed-off-external-execution.md`.
- Prompt-collision evidence comes from raw isolated scenarios with no embedded
  expected answers. Observable routing, Git authority, and selected HARD-GATE
  behavior are distinguished from hidden reasoning or metadata assumptions.
- Prompt-load decisions use documented or observed runtime evidence. File size
  is not presented as token evidence.

## Measured load evidence and remaining unknown

- Codex: supported progressive-disclosure behavior is documented by the local
  Skill authoring contract.
- Grok CLI: standalone and valid-Handoff route outcomes were observed against
  the feature source; the two routes reported the expected distinct reference
  sets.
- Antigravity CLI: reference-load observability remains `UNKNOWN`; no token or
  measured-savings claim is made. The single discoverable entry and direct
  Handoff pointer remain the conservative compatibility choice.

## Correction and Review closure

The first adversarial implementation Review found a weakened draft Completion
Contract, self-asserting collision fixtures, invalid Companion RED coverage,
premature task bookkeeping, and incomplete provenance. Every finding returned
to correction, focused verification, and independent Review. The post-fix
source Review, corrected sync-plan Review, final cross-target Review, Project
Learning Review, and post-learning final High Review all returned PASS.

Project Learning promoted one new high-severity project-local invariant:
external CLI raw debug traces remain sensitive temporary evidence even at mode
`0600`. The durable Candidate Card, engineering invariant, and deterministic
regression prohibit quoting/echoing or durable raw-trace promotion and require
sanitized metadata plus post-gate cleanup.

## Fresh verification

- Router: quick validation and core validator PASS; 132/132 tests PASS under
  Python 3.11.7/PyYAML and Python 3.14.2 dependency-free fallback, with the
  Companion feature source explicitly bound and zero skips.
- Companion: quick validation and template validator PASS; 74/74 tests PASS
  under each interpreter.
- Superpowers: quick validation PASS; Option 2 Node regression 1/1 PASS.
- OpenSpec active change strict validation and all three worktree diff checks:
  PASS.
- Codex, Antigravity CLI, and Grok CLI runtime `verify-all`: PASS; path-only
  source audit: `0 sensitive categories found`.
- Final independent High Review: PASS with no actionable findings.

## Runtime and rollback

The reviewed mode-`0600` path/hash plan synchronized 39 allowlisted portable
files per target. All three targets match source hashes, managed governance,
validators, and supported discovery checks. The non-discoverable transaction
backup retains exact pre-apply bytes and modes until archive/post-archive Review
removes the rollback need; tests also cover atomic restore and removal of newly
created target paths.

## Archive

`openspec archive streamline-workflow-prompt-contracts -y` applied the four
approved requirements to the canonical `skill-workflow-governance` spec and
moved the change to
`openspec/changes/archive/2026-07-20-streamline-workflow-prompt-contracts`.
The command reported 25/27 tasks because archive verification and cleanup were
intentionally still open at invocation time.

The OpenSpec writer appended one blank line at canonical spec EOF. The first
post-archive `git diff --check` caught it; removing only that blank line restored
the expected one-newline EOF without changing the merged requirements. Fresh
post-archive strict validation then reported 1 passed / 0 failed, the four new
requirement headers appeared exactly once, the active change path was absent,
and `git diff --check` passed.

## Residuals and boundaries

- Antigravity load visibility remains `UNKNOWN` as described above.
- Raw debug traces, forward-test outputs, the sync plan, and structured backups
  were temporary through post-archive Review and were removed by Task 6.4; none
  became durable evidence.
- Root `CONTEXT.md` is unrelated user-owned workspace state and is excluded from
  publication and cleanup scope unless the user separately directs otherwise.
- No Git staging, commit, reset, clean, push, PR creation, worktree removal,
  branch deletion, release, or publication is authorized or performed by this
  closeout record.

## Cleanup and rollback proof

After source validation, runtime parity, raw forward tests, final High Review,
normal archive, strict post-archive validation, and independent post-archive
Review all passed, Task 6.4 removed only the inventoried change-owned resources:

- the mode-`0600` sync plan and three non-discoverable backup directories;
- the forward-test runner, schema inventory, route outputs, and JSON scratch
  files; and
- the mode-`0600` Grok/Antigravity load and forward debug traces that could
  contain runtime authentication material.

Path-only follow-up found no remaining `streamline*` or runner artifact under
`/private/tmp` and no `.bak.*`, `*.backup*`, or change-named backup entry under
the Codex, Antigravity CLI, or Grok CLI Skill roots. Unrelated `CONTEXT.md`, all
three feature worktrees, and every branch were preserved.

Rollback was proven before deletion: the reviewed plan bound every source and
target path/hash; backups preserved sensitive rule files at `0600`, ordinary
portable files at `0644`, and executables at `0755`; transaction regressions
proved byte/mode restoration and removal of newly created paths; and fresh
post-archive `verify-all` confirmed the deployed state. Once all gates passed,
the temporary rollback copies were removed by design. Git `HEAD` remains the
prior source baseline, while the current uncommitted worktree diffs and three
validated runtime copies retain the implemented state pending the user's
separate Git/publication decision.

## Completion correction: installed Superpowers drift

A post-cleanup control-plane audit found a material path omitted by the earlier
final Reviews:

- installed/main path:
  `/Users/elvis/.codex/superpowers/skills/finishing-a-development-branch/SKILL.md`
  at SHA-256
  `dd2f82c6dc8582b621f9eb57fcb65f557f88eadf872727ac81d0840ae12c504e`;
- reviewed feature source:
  `/Users/elvis/.config/superpowers/worktrees/superpowers/streamline-workflow-prompt-contracts/skills/finishing-a-development-branch/SKILL.md`
  at SHA-256
  `0b037a0c381c7cb956e22ac20f68ef70a6fd896719b8e85c192697cb38c45455`.

`/Users/elvis/.codex/superpowers` is the installed `main` worktree. Directly
copying or reimplementing the feature diff there would violate the instruction
to keep implementation in the feature worktree. The 39-file Codex,
Antigravity CLI, and Grok CLI parity plan covered Router/Companion portable
files, not this separately scoped Superpowers dependency.

The earlier source, archive, cleanup, and validation evidence remains valid for
the surfaces it actually inspected, but the unqualified whole-task completion
decision is superseded by the independent runtime-gap Review. Owner: user.
Resume condition: explicitly authorize a narrowly scoped Git integration that
commits only the two reviewed Superpowers feature-worktree files and
cherry-picks that commit into the installed main worktree. After installed hash
and semantic parity, Node regression, quick validation, and fresh completion
Review PASS, this blocker may close. Push remains separately authorized.

The user subsequently granted that bounded commit/cherry-pick authority without
granting push. Resolution:

- Superpowers feature commit:
  `42b964e1287be22af85251b7b719ef86eb1b47d4`;
- installed `main` cherry-pick:
  `cc7b33e`;
- installed and feature Skill SHA-256:
  `0b037a0c381c7cb956e22ac20f68ef70a6fd896719b8e85c192697cb38c45455`;
- installed-path Node regression: 1/1 PASS;
- installed-path Skill quick validation and `git diff --check`: PASS;
- feature and installed worktrees: clean.

Installed `main` is ahead of `origin/main` by this one local commit and remains
behind by 17 upstream commits. No pull, merge, rebase, push, worktree removal,
or branch deletion was performed. The fresh installed-Superpowers completion
Review inspected both patches and resulting trees, reran installed validation,
and returned PASS with no actionable findings. The archived ledger is fully
reconciled; push/publication remains a separate user decision.
