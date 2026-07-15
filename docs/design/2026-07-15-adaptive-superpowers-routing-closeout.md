# Adaptive Superpowers Routing Closeout

Date: 2026-07-15  
Change: `make-superpowers-routing-adaptive`  
Status: **FINAL VERIFICATION PASS — Git decision remains pending**

## Outcome

The approved Major Self-Evolution is implemented and synchronized without
weakening approval, evidence, Review, verification, completion, or Git authority
boundaries.

- Router Gate 0 now classifies governed work by phase, material unresolved
  choices, and implementation risk before broad Superpowers metadata selects a
  sub-skill. Managed invariant `CCG-014` carries that precedence across Codex,
  Antigravity CLI, and Grok CLI; the portable manifest is version 3.
- A fully specified `proposal-only` request may draft and strictly validate one
  reviewable OpenSpec contract without implementation sub-skills. A material
  choice affecting scope, security, compatibility, data lifecycle, production
  authority, or testable acceptance still delegates to brainstorming. Asking
  the agent to choose does not resolve that material choice, and a selected
  brainstorming skill retains its complete HARD-GATE.
- Approved implementation continues to refresh Gate 0 and retain planning,
  TDD, Preflight, Review, evidence, and final-verification discipline. Concrete
  model identity or version grants no authority and changes no workflow weight.
- Companion Standalone Lightweight Review now runs only for the current explicit
  wording or read-only Review request. It is findings-first, checks the complete
  OpenSpec artifact set, and does not auto-chain after change generation. A
  valid Handoff still selects the complete handed-off lifecycle.

## Verification evidence

### Source repositories

| Repository | Fresh critical result |
|---|---|
| `openspec-superpower-change` | `quick_validate.py` PASS; core validator PASS; 117 unittests PASS with zero skips; post-archive strict-all validation PASS |
| `codex-brief-antigravity-review` | `quick_validate.py` PASS; template validator PASS; 72 unittests PASS |

The fresh source matrix therefore passed 117 + 72 tests. Repository diff checks
also passed.

`openspec archive make-superpowers-routing-adaptive -y` updated the canonical
`skill-workflow-governance` spec with three requirements and archived the change
as `2026-07-15-make-superpowers-routing-adaptive`. Fresh post-archive
`openspec validate --all --strict --no-interactive` reported 1 passed and 0
failed. The first archive attempt was blocked by filesystem permission before
any partial write; task 6.2 was restored to pending, the absence of partial state
was checked, and the authorized retry succeeded. The archive output also left
one blank line at the canonical spec EOF; removing only that blank line restored
`git diff --check` while strict validation and independent Quality re-Review
remained PASS.

The earlier active-change strict validation also exited 0 and reported the
change valid. Its later `PostHogFetchNetworkError: getaddrinfo ENOTFOUND
edge.openspec.dev` came from the CLI telemetry flush; it was assessed as a
non-blocking network warning and did not affect that validation result.

### Durable forward-test

All five approved scenarios passed with fresh agent identities. The durable
evidence set is 5 scenarios / 5 PASS results / 25 persisted evidence files,
including exact responses or transcripts, negative inventories, generated
artifact snapshots where applicable, and hashes.

- Report:
  `docs/design/2026-07-15-adaptive-superpowers-routing-forward-test.md`
- Report SHA-256:
  `72009bd8e1335d8e924cf98e8d57f2e54ab3f6f3d7e7e6604791d4640347bd3e`
- Controller verdict: `PASS — durable 5/5 evidence verified`

Two corrective loops are part of that evidence history:

1. The first S2 result shared workspace state with S1 and was rejected as
   invalid harness contamination, not classified as a product bug. After the
   workspace was cleared, S2 exposed the real product gap: delegated
   authentication and compatibility choices could bypass brainstorming. The
   source rule and regression assertion were corrected, then validation and
   Review were repeated to PASS.
2. The next five-scenario run established the expected behavior but retained
   only summaries, not exact durable response evidence. Every scenario was reset
   and rerun again, producing the accepted 25-file durable evidence set.

### Cross-CLI runtime synchronization

The reviewed path/hash-only plan synchronized both portable skills and the
version-3 managed governance block to every declared required target.

- Sync plan:
  `/private/tmp/make-superpowers-routing-adaptive-sync-plan.json`
- Sync plan SHA-256:
  `d60bee4498cda11a48b12478b74ef7653b5a99443925b52115157b57cf4346f8`
- `verify-all`: PASS for Codex, Antigravity CLI, and Grok CLI.
- Installed validation: 12/12 PASS — each target passed `quick_validate.py` and
  the repository-specific validator for both portable skills.
- Discovery: Antigravity deterministic manifest/reference closure and compatible
  validators PASS; Grok `inspect --json` path verification PASS and its secured
  inspection artifact was consumed; Codex deterministic path/parity checks PASS.
- Managed governance: version 3, `CCG-001` through `CCG-014`, with native CLI
  rule bytes outside the managed markers preserved.

### Pre-archive High Review

The final High Review inspected both complete source diffs, the actual runtime
copies, CCG-014 precedence, proposal-only and material-delegation predicates,
companion request scoping, and preserved Non-negotiables. Its independent
generic-create adversarial probe confirmed that generic creation wording alone
does not select a sub-skill. Final verdict: **PASS**.

The independent post-archive Quality re-Review confirmed that the active change
path is absent, the dated archive is present, the canonical requirements exactly
match the archived delta, the canonical spec ends with one newline, and archived
tasks 6.1/6.2 were complete while 6.3/6.4 remained pending at that review point.
Verdict: **PASS**.

### Post-archive Final High Review

The final independent High Review inspected the complete current tracked and
untracked scope in both worktrees, reran strict OpenSpec and diff checks, checked
the source and runtime validation matrix, verified three-target parity and
managed-rule wiring, recomputed the 25-file durable evidence closure, and ran an
adversarial route trace for generic creation wording and delegated authentication/
compatibility choices. It found zero sensitive categories, no staged or
out-of-scope changes, and only the five expected task-owned cleanup candidates.
Verdict: **PASS** with no actionable findings.

### Post-cleanup final verification

After cleanup and archived-task reconciliation, the router again passed
`quick_validate.py`, the core validator, all 117 tests with zero skips, strict
OpenSpec validation (1 passed / 0 failed), and `git diff --check`. The companion
again passed `quick_validate.py`, the template validator, all 72 tests, and
`git diff --check`. The final path-only sensitive audit found zero categories;
archived tasks are 25 checked / 0 unchecked; both Git indexes are empty; all
task-owned temporary paths and discoverable backup entries remain absent.

## Rollback and cleanup state

The controller-verified structured pre-apply snapshots were the authoritative,
independently restorable rollback source through source/runtime verification,
archive, and Final High Review. The transaction backup remained diagnostic-only
because its anonymous filenames had no persistent target-path mapping.

After every source/runtime/forward-test/Review/archive gate passed, governed
cleanup removed the structured backup, transaction backup, forward runtime,
empty forward fixture, and sync plan. Follow-up checks confirmed that all five
paths are absent and that no `.bak.*` or `*.backup*` entry exists in either
source worktree or any declared runtime skill discovery root.

The two feature worktrees and three validated runtime copies now retain the
current state. Existing Git history remains the prior-version baseline, but the
current source changes are intentionally uncommitted until the user makes a Git
decision. Preserve both worktrees; no temporary rollback snapshot remains by
design.

## Pending closeout actions

The following action is deliberately not claimed complete by this record:

1. Create a Git commit or push only after separate explicit user authorization.

No Git staging, commit, reset, clean, push, worktree deletion, or branch deletion
was performed while updating this closeout record.
