# Major Self-Evolution Review Draft: streamline-workflow-prompt-contracts

## Observed failures and risks

1. Installed `superpowers:finishing-a-development-branch` gives contradictory
   instructions for Option 2: its execution path and cleanup step remove the
   worktree, while its quick reference and safety guidance preserve it.
2. Completion obligations are semantically aligned but repeated across the
   Router, Step Evidence Gate, approved workflow, response patterns, and
   Companion boundary. The model must synthesize several sources instead of
   consulting one canonical completion contract.
3. The Companion's lightweight and Handoff routes share one large Skill body.
   Whether this causes material runtime prompt load is not yet proven, so a
   split must not be selected from file size alone.
4. Superpowers discovery, brainstorming, planning, and Git defaults have known
   textual collision surfaces with the Router adapter. Existing precedence is
   a mitigation; actual route behavior needs deterministic forward-tests.
5. Previous prompt-load estimates used file bytes as a proxy. That is not
   sufficient evidence for a semantic split or a claimed token reduction.

These findings do not establish that governance has failed or that a particular
model is inherently unstable.

## Desired behavior

- Option 2 consistently preserves its worktree after a PR is created.
- Whole-task completion has one canonical result-oriented contract; other
  workflow files reference it without independently redefining the same rules.
- Standalone Companion use exposes only its lightweight contract when supported
  by the runtime. Handoff governance remains complete and unchanged when active.
- Prompt-collision tests prove phase routing, brainstorming selection, and Git
  authority behavior without weakening selected Superpowers HARD-GATE rules.
- Runtime loading and token claims use measured traces or a documented tokenizer,
  including uncertainty and unsupported-runtime results.

## Expected file boundary

Candidate source changes after approval:

- Router: `SKILL.md`, a canonical completion reference, affected navigation and
  validators/tests.
- Companion: `SKILL.md`, Handoff-only reference organization, and affected
  validators/tests. A second Skill is conditional on measurement evidence.
- Superpowers runtime/source under explicit scope:
  `finishing-a-development-branch/SKILL.md` and its regression fixture.
- OpenSpec spec, tests, README/README.zh-CN, changelog, sync manifests, and
  declared Codex/Antigravity CLI/Grok CLI runtime copies where portable files
  change.

Out of scope: redesigning Project Learning, `CONTEXT.md` responsibility,
`grill-with-docs`, caveman semantics, Handoff schema 5, evidence manifests,
capability profiles, or approval strength.

## Candidate rule snippets

The exact implementation wording remains Review-controlled, but it must express
these normative rules:

```text
Option 2 (Push and Create PR) preserves the feature worktree. Automatic
worktree cleanup applies only to Options 1 and 4.
```

```text
The Router owns one canonical Completion Contract. Other workflow artifacts may
add route-specific evidence but must not redefine whole-task completion.
```

```text
Companion standalone routing must not require Handoff lifecycle instructions.
The complete Handoff Governor contract loads only for a valid Handoff route.
```

```text
Prompt-load optimization decisions require measured runtime evidence. Byte or
word counts alone cannot authorize a split or support a token-savings claim.
```

## Validation and forward-test plan

- Add a negative fixture reproducing the Option 2 cleanup contradiction, then
  make the corrected source pass.
- Add validator tests that reject duplicated or divergent whole-task completion
  definitions while preserving route-specific batch evidence.
- Add prompt-collision scenarios for proposal-only routing, material
  brainstorming, unauthorized Git steps, and selected HARD-GATE preservation.
- Record supported runtime Skill/reference loads for standalone and Handoff
  scenarios; use tokenizer results only where the exact loaded prompt is known.
- Run both repositories' required validators and unit tests, isolated forward
  tests, cross-CLI sync verification, and independent final Review.

## Stop conditions

- Stop before implementation until the user explicitly approves the exact
  OpenSpec change-id and scoped contract.
- Return `BLOCKED` rather than selecting a Companion split when runtime loading
  cannot be measured on any declared supported target.
- Do not proceed if a proposed simplification weakens approval, evidence,
  independent Review, Git authority, or completion requirements.
- Any implementation finding returns to fix, verification, and Review.

## Rollback

Before implementation, create fresh structured backups of every approved source
and runtime target. Restore only the affected target on failure, verify the
restored hashes and validators, stop later synchronization, and report
`BLOCKED`. Repository history remains long-term rollback; temporary backups are
removed only after successful final verification and Review.
