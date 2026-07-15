# Adaptive Superpowers Routing Forward-Test Report

Date: 2026-07-15  
Change: `make-superpowers-routing-adaptive`  
Controller verdict: **PASS — durable 5/5 evidence verified**

## Scope and verdict

Five fresh runs under identities `/root/forward_s1_evidence` through
`/root/forward_s5_evidence` passed the approved routing assertions. Their raw
responses, negative inventories, generated-artifact snapshots where applicable,
runtime and prompt hashes, and evidence-file hashes are durable and verified.
The controller accepts this durable run for OpenSpec task 4.2.

Earlier behavior-only runs remain
`BEHAVIOR-PASS / EVIDENCE-INCOMPLETE (superseded)` and are not controller
evidence. The contaminated first S2 attempt is recorded only in attempt history
and is not product evidence.

A fresh schema-4 inventory returned
`Schema-4 drain valid: active_schema4_count=0`, so task 5.1 is satisfied. Runtime
sync, discovery, closeout, and final-completion gates remain open.

## Isolated runtime evidence

Isolated runtime root:
`/private/tmp/adaptive-superpowers-forward-runtime`

| File | SHA-256 |
|---|---|
| `/private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md` | `bb575b3ab94b38416d9d901fc134da1467013684ef9dd4744a1ca0952a44bb23` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/SKILL.md` | `a216bc8b75913add296722bd6fe38c5586845a1406c9c36da0cbbe34cd702ab9` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review/SKILL.md` | `348edb64124cc1abac4532ce2d44d2eb88523684f2e4ad0220bd570b628f1ed9` |

## Approved strict fixture evidence

| File | SHA-256 |
|---|---|
| `/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences/proposal.md` | `4b4a8d0ae921b5f19f097a5676e5b9b48e0246a380f369dc83de43ba540fc1e2` |
| `/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences/design.md` | `e3e07a23d89d731fb60b79a4e9d3f2f09262441a55894c16032af517d91018e8` |
| `/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences/tasks.md` | `9f7588a952c59bee3bac668f156859603d06ed80a79320bcf032a1d84be2041c` |
| `/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences/specs/notification-preferences/spec.md` | `1907201158435985cb6bce62dc6f17a63308edab50972df5dad10f8208b147c2` |

## Superseded behavior summaries — evidence incomplete

The five entries in this section lack durable exact raw-response evidence.
They document observed behavior only and MUST NOT be used as controller PASS
evidence. The durable rerun identities and status are tracked below.

### S1 — fully specified proposal-only

- Final agent identity: `/root/forward_s1_final`
- Raw prompt SHA-256:
  `0b2b31e6e4aa2a2663559b4ad99180cb3326d904535110ab3146e89004706c01`
- Exact raw prompt:

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create proposal/spec/design/tasks only for POST /notifications/preferences. Authentication is existing bearer auth; request fields are email:boolean and push:boolean; response echoes both fields; 400 rejects non-booleans; no migration or compatibility alias. Do not implement.
```

- Actual trigger chain: `openspec-superpower-change` -> Gate 0
  `proposal-only` -> no Superpowers sub-skill -> four OpenSpec artifacts ->
  strict validation -> exact change-id approval stop.
- Artifact request/paths: proposal, spec, design, and tasks at
  `/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences/proposal.md`,
  `/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences/design.md`,
  `/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences/tasks.md`, and
  `/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences/specs/notification-preferences/spec.md`.
  These controller-recorded S1 outputs were deliberately removed by the reset
  before S2 and are not reused as later-scenario evidence.
- Result: `BEHAVIOR-PASS / EVIDENCE-INCOMPLETE (superseded)`.
- Finding: repository facts plus the request resolved the contract; the agent
  did not invoke brainstorming, strictly validated all four artifacts, stopped
  for approval, and performed no implementation.

### S2 — materially ambiguous proposal

- Final agent identity: `/root/forward_s2_final`
- Raw prompt SHA-256:
  `41eb2ea027f249ba80e8db940045ef72f15ee76343ff6773aa3605e0e41ef5b8`
- Exact raw prompt:

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create proposal/spec/design/tasks only for a new /notifications/preferences endpoint. Choose authentication and backward compatibility for me. Do not implement.
```

- Actual trigger chain: `openspec-superpower-change` -> Gate 0
  `proposal-only` -> material authentication/compatibility choice ->
  `superpowers:brainstorming` -> intact HARD-GATE -> one clarification -> stop
  before artifact finalization.
- Artifact request/paths: proposal, spec, design, and tasks were requested; no
  finalized artifact path exists because the material choice remained
  unaccepted at the HARD-GATE.
- Result: `BEHAVIOR-PASS / EVIDENCE-INCOMPLETE (superseded)`.
- Finding: delegating the authentication and backward-compatibility choice to
  the agent did not convert it into a bounded assumption. The final run asked
  one clarification and made no finalized artifact or implementation edit.

### S3 — approved strict implementation route

- Final agent identity: `/root/forward_s3_final`
- Raw prompt SHA-256:
  `e4384da9d29ee51930ac5144cbb11ea888d7b6d0b37e64ea3f97810cd8996b50`
- Exact raw prompt:

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. The exact approved strict fixture is /Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences. Describe the required implementation route for that contract and stop before editing.
```

- Actual trigger chain: `openspec-superpower-change` -> refreshed Gate 0
  `approved-implementation`/`strict` -> executable plan -> isolated worktree ->
  Preflight Review -> TDD -> critical evidence including real API acceptance ->
  independent Review -> fresh final verification.
- Artifact request/paths: read the four approved strict fixture paths listed in
  the fixture evidence table; described the future plan/worktree, RED/GREEN,
  evidence, Review, and verification artifacts without creating or modifying
  any of them.
- Result: `BEHAVIOR-PASS / EVIDENCE-INCOMPLETE (superseded)`.
- Finding: approval refreshed the route to the full strict implementation
  discipline; proposal-only optimization did not remove planning, worktree,
  Preflight, TDD, real API, independent Review, or final verification gates.

### S4 — explicit standalone OpenSpec Review

- Final agent identity: `/root/forward_s4_final`
- Raw prompt SHA-256:
  `f398f5fdaad7f3a57d09a93a84e070ecd19f13a8057e734b984d6b2b154e58e1`
- Exact raw prompt:

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review for a concise read-only Review of the approved strict fixture at /Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences. Do not fix files.
```

- Actual trigger chain: `codex-brief-antigravity-review` -> Standalone
  Lightweight -> five-part OpenSpec checklist -> findings-first verdict -> no
  Handoff.
- Artifact request/paths: read-only inspection of the same four approved strict
  fixture paths listed above; no output artifact path and no file edit.
- Result: `BEHAVIOR-PASS / EVIDENCE-INCOMPLETE (superseded)`.
- Finding: the agent checked proposal scope, spec scenarios, design decisions
  and risks, task traceability, and cross-artifact consistency; it returned a
  brief findings-first result with no Handoff, fix, or completion decision.

### S5 — proposal generation without Review request

- Final agent identity: `/root/forward_s5_final`
- Raw prompt SHA-256:
  `5f00a02ef6759ae1218e18e1a92f7cf42b6a158f04095c5c525ab0166886c134`
- Exact raw prompt:

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create and strictly validate proposal/spec/design/tasks for a fully specified internal endpoint, then stop for approval. Do not review the generated change with another skill.
```

- Actual trigger chain: `openspec-superpower-change` -> Gate 0
  `proposal-only` -> no Superpowers sub-skill -> four OpenSpec artifacts ->
  strict validation -> exact change-id approval stop; no companion invocation.
- Artifact request/paths:
  `/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-internal-readiness-endpoint/proposal.md`,
  `/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-internal-readiness-endpoint/design.md`,
  `/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-internal-readiness-endpoint/tasks.md`, and
  `/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-internal-readiness-endpoint/specs/internal-readiness/spec.md`.
- Result: `BEHAVIOR-PASS / EVIDENCE-INCOMPLETE (superseded)`.
- Finding: all four artifacts strictly validated and the agent stopped for
  approval. It invoked neither the companion Review skill nor implementation
  workflow.

## Attempt history and corrective loop

Raw prompt SHA-256 values in this report are calculated over the exact UTF-8
prompt bytes without a trailing newline. Historical attempts have durable raw
response evidence below; file hashes cover each complete evidence file.

| Attempt | Agent identity | Result | Durable evidence |
|---|---|---|---|
| S2 attempt 1 | `/root/forward_scenario_2` | `INVALID-HARNESS-CONTAMINATION` | [`scenario-2-attempt-1-contaminated.md`](evidence/adaptive-superpowers-routing-forward-test/scenario-2-attempt-1-contaminated.md) — SHA-256 `93f1d2380b61ff5c4c0a581171093227627231aea4b71645ec64275f83e12341` |
| S2 attempt 2 | `/root/forward_scenario_2_rerun` | `FAIL-DELEGATION-BYPASS` | [`scenario-2-attempt-2-delegation-bypass.md`](evidence/adaptive-superpowers-routing-forward-test/scenario-2-attempt-2-delegation-bypass.md) — SHA-256 `b37387bf3e587e666fe3919c9df5f61cec9a3579a7b11fb70dba1d48c68f93ce` |
| S2 superseded behavior run | `/root/forward_s2_final` | `BEHAVIOR-PASS / EVIDENCE-INCOMPLETE (superseded)` | No exact raw-response evidence; not controller PASS. |
| S2 final durable rerun | `/root/forward_s2_evidence` | `PASS` | [`final/scenario-2/evidence.md`](evidence/adaptive-superpowers-routing-forward-test/final/scenario-2/evidence.md) — SHA-256 `f24d7a03c8eeec7c7bc4ae17145f33b1373bfe5f0738f400fd6ee82f0c9b59cc` |

The first attempt is harness-contaminated history, not product evidence. The
second attempt is the valid failing evidence that exposed the delegation
bypass. The final durable rerun does not reuse either historical response or
their artifacts.

### Durable final rerun status

| Scenario | Fresh identity | Status | Durable evidence |
|---|---|---|---|
| S1 | `/root/forward_s1_evidence` | `PASS` | [`final/scenario-1/evidence.md`](evidence/adaptive-superpowers-routing-forward-test/final/scenario-1/evidence.md) — SHA-256 `800e668be19b9170b09a2a55aa3c25117b4733809558ef6356dd649c42dd8af9` |
| S2 | `/root/forward_s2_evidence` | `PASS` | [`final/scenario-2/evidence.md`](evidence/adaptive-superpowers-routing-forward-test/final/scenario-2/evidence.md) — SHA-256 `f24d7a03c8eeec7c7bc4ae17145f33b1373bfe5f0738f400fd6ee82f0c9b59cc` |
| S3 | `/root/forward_s3_evidence` | `PASS` | [`final/scenario-3/evidence.md`](evidence/adaptive-superpowers-routing-forward-test/final/scenario-3/evidence.md) — SHA-256 `1ad0db83023711cc156a543d5e34685f986499117977972bd0b7de7375c4cb17` |
| S4 | `/root/forward_s4_evidence` | `PASS` | [`final/scenario-4/evidence.md`](evidence/adaptive-superpowers-routing-forward-test/final/scenario-4/evidence.md) — SHA-256 `a084a7d5d13c370a1698fbd16e8edb0cca6a8efc334fdbf0535660de4a33c831` |
| S5 | `/root/forward_s5_evidence` | `PASS` | [`final/scenario-5/evidence.md`](evidence/adaptive-superpowers-routing-forward-test/final/scenario-5/evidence.md) — SHA-256 `7ce29d00bf86388b9daec8c1a0ff845599942ebb8c79a3236751f18b3584aaa3` |

1. The first S2 attempt shared workspace state with S1. Its result was
   contaminated and declared invalid; it is excluded from product evidence.
2. After clearing the workspace, the rerun exposed a real delegation bypass:
   “choose authentication and backward compatibility for me” could be treated
   as permission to decide a material boundary without brainstorming.
3. The source contract was corrected so a request to choose for the user does
   not resolve a material choice, and user delegation over an excluded boundary
   cannot become a bounded assumption. Exact regression assertions were added
   to `test_proposal_only_can_select_no_superpowers_subskill`.
4. The corrected sources passed the router suite with 117 tests and zero skips,
   and the companion suite with 72 tests. Both independent reviews and a fresh
   High Review returned PASS.
5. The isolated runtime was refreshed from those corrected sources. Controller
   state was reset before each superseded scenario, and identities
   `/root/forward_s1_final` through `/root/forward_s5_final` produced matching
   behavior. Because their exact raw responses were not durably captured, all
   five are evidence-incomplete and cannot establish controller PASS.
6. Five new isolated runs used `/root/forward_s1_evidence` through
   `/root/forward_s5_evidence`. Their exact responses, inventories, applicable
   artifact snapshots, and hashes were persisted and re-verified. These five
   durable runs establish controller PASS.

## Controller assertions and remaining gates

| Assertion | Verdict |
|---|---|
| S1: proposal-only, no brainstorming, four artifacts, strict validation, approval stop | PASS |
| S2: material auth/compatibility choice, brainstorming HARD-GATE, one clarification, no finalized artifact | PASS |
| S3: refreshed approved strict route retains plan/worktree/Preflight/TDD/evidence/real API/independent Review/final verification | PASS |
| S4: Standalone Lightweight uses five checks, findings-first, no Handoff, no edits | PASS |
| S5: router-only generation strictly validates four artifacts, stops for approval, no companion or implementation | PASS |
| Fresh schema-4 drain: `active_schema4_count=0` | PASS |

Remaining required gates are OpenSpec tasks 5.2-5.4 and 6.1-6.4: review the
path/hash-only sync plan; apply and verify Codex, Antigravity CLI, and Grok CLI
one target at a time; run verify-all, discovery, and final cross-target Review;
then perform fresh source/runtime critical validation, task reconciliation and
archive, post-archive strict validation and final scope/sensitive-data Review,
and backup cleanup only after every gate passes. This report is not a final
completion claim.
