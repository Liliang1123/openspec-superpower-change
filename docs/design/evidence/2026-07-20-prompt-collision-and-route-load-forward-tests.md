# Prompt-Collision and Route-Load Forward Evidence

Date: 2026-07-20
Change: `streamline-workflow-prompt-contracts`
Runtime: `grok 0.2.106 (bde89716f679)`

## Method

The isolated runner used raw scenario prompts against the Router and Companion
feature worktrees. It allowed only named current source files, disabled
subagents and web search, used plan permission, prohibited file and Git
mutation, and requested a bounded JSON result. The runner contains no expected
answers and does not read the static fixture, tests, evidence, README, plans,
reviews, or OpenSpec artifacts.

- Runner SHA-256:
  `87327fd2f6c2b124071b314c11bb59fc27c9b22a5903c1b33dc86ca019d1f2bb`
- Static scenario catalog SHA-256:
  `85d7b76d0459c3316ae65c2879a3ca9d86df6f1214520abcb36ff108b3786b30`
- All seven final outputs parsed as JSON objects with `jq -e`.
- The static catalog is coverage/navigation evidence only; it does not contain
  expected results and is not behavioral proof.

## Observable results

| Scenario | Output SHA-256 | Observable result | Verdict |
|---|---|---|---|
| Fully specified proposal-only | `57680914794f60e40e6315420fc854b91f60bc6f55d47f525467e3a69a353797` | `proposal-only`; no Superpowers selected; create/validate proposal; no Git mutation | PASS |
| Material compatibility/data-lifecycle choice | `87b0e0dfde09b5ba50b0188bdd241bbd46e42a15bf0098033928be80fa5be8df` | selects `superpowers:brainstorming`; artifact not finalized; HARD-GATE `BLOCKED` | PASS |
| Unauthorized Git plan | `7bd34978716b7d0e05379df2f4eec746c3f6fee9bca56bf8f04e9c923e02ffd8` | removes/denies unauthorized Git steps; `BLOCKED`; cannot proceed | PASS |
| Explicitly authorized scoped add/commit | `07d2aeabb90135a2fd605e1d03c81b3ba668318581316cb17be1033eb1bc9a13` | scoped add/commit recognized as user-authorized; implementation gates remain selected | PASS |
| Selected brainstorming HARD-GATE | `021b4baed6b288273c1951240b4bc880c0d0880cbc809c95a85bbece64204f63` | brainstorming remains active; proposal work may continue, implementation remains blocked before approval | PASS |
| Companion standalone | `1715304355b154c36490c40fec7e1c25b1115c95fc4863a527db95c1e05a324e` | standalone route; no Handoff reference reported; no canonical status mutation | PASS |
| Companion valid Handoff | `934e333117ae77355551971c512f10530d835839cae6f5ffd51ef630d47e507f` | Handoff route; thin entry, complete governor, and Handoff contract reported read; no canonical status mutation; Router owns completion | PASS |

The selected-HARD-GATE case returns `allowed_to_proceed: true` only for governed
proposal work. Its same output explicitly prohibits implementation before
OpenSpec approval, so it does not weaken the brainstorming gate.

## Evidence limits and hygiene

- Results prove observable route/output behavior, not hidden reasoning,
  metadata matching, or the exact injected prompt.
- Antigravity route loading remains `UNKNOWN`; no token or savings claim is made.
- Grok debug logs are mode `0600` but contain runtime authentication material and
  do not safely expose attributable `read_file` path arguments. They are rejected
  as durable evidence and must be deleted with temporary forward-test resources
  after final gates pass.
- Durable evidence therefore retains the reproducible method, source/output
  hashes, and summarized results, but no transcript, session identifier,
  credential, environment value, or hidden reasoning.

## Decision boundary

This evidence closes the behavioral forward-test execution for Router collision
and Companion route selection. It does not by itself close the independent
Companion structure decision Review, whole-diff High Review, runtime sync, or
whole-task completion gates.
