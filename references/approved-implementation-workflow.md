# Approved Implementation Workflow

Use after an OpenSpec proposal is approved, or after Direct Change has
classified and authorized an implementation that will use an external agent.

## OpenSpec And Superpowers Boundary

1. OpenSpec proposal/design/spec deltas are the approved change contract.
2. For OpenSpec-required work, that approval is the single design approval and
   does not require a duplicate `docs/superpowers/specs/` artifact or approval.
3. After approval, invoke `superpowers:writing-plans` for multi-step work and
   save the executable plan under the project-preferred path.
4. OpenSpec `tasks.md` tracks contract progress; it does not replace the plan.
5. A compact Direct Change needs no large plan unless complexity justifies it.

Follow `references/superpowers-adapter.md`; a generated plan does not grant Git
permission and must not create a second design approval.

## Plan And Evidence Granularity

- Group work by complete business slice, not by file count or technical layer.
- Include exact files, test commands, evidence profile, batch profile, negative
  searches, acceptance, rollback, and stop conditions.
- Apply Step Evidence Gate before and after each business slice or risk
  milestone, not every TDD micro-step. TDD owns RED/GREEN inside the slice.
- Use `superpowers:systematic-debugging` before changing unexplained failures.
- Use `superpowers:test-driven-development` for behavior changes, not for a
  test-only assertion of already-defined behavior.

## Plan And Brief Preflight Review

Before inline implementation or external dispatch, Review the current Plan or
Brief revision for contract coverage, placeholders, allowed scope, production
wiring where applicable, acceptance, exact verification commands, evidence
profile, rollback/stop conditions, branch/worktree choice, and Git authority.

- `compact` may use a focused inline Preflight Review.
- `standard` and `strict` require a distinct critical pass.
- Preflight uses only `PASS` or `BLOCKED`. Any actionable finding is
  `BLOCKED`; revise the artifact and Review it again. Reserve `FAIL` for
  implementation or post-implementation Review, where executed behavior can
  actually be wrong.
- Preflight `PASS` authorizes execution only; it is not design re-approval,
  implementation Review, or completion evidence.
- Rerun only when the artifact revision changes.

## Inline Implementation

1. Execute the plan inline with TDD/debugging as applicable.
2. Run slice verification.
3. For `compact`, run a focused diff/self-review.
4. For `standard` or `strict` inline implementation, invoke
   `superpowers:requesting-code-review` after implementation and before final
   verification. Review PASS is required.
5. Any finding returns to the same slice: fix, refresh verification, and Review
   again. Do not carry unresolved findings into the next slice.

## External Implementation

1. Create one schema-version-5 Handoff Contract at canonical `status.md`, with
   immutable control-plane/executor/reviewer product, instance, role, and profile
   assignments, decision provenance, and a Confirmation Lease. A visible active
   schema-4 contract blocks runtime schema-5 deployment and finishes under v4.
2. A low-risk Direct Change may use `compact`/`single`; approved public/API
   restoration remains `strict`, and OpenSpec-backed work uses its approved
   evidence and batch profiles.
3. Hand Brief/Report/Review attempts to `codex-brief-antigravity-review`.
4. The external Review is the batch code-review gate; do not duplicate it with
   a second Superpowers review for the same batch.
5. `FAIL` or `BLOCKED` stays on the same batch and must re-enter Review with
   fresh attempt evidence.
6. Non-final `PASS` advances one batch. Final `PASS` sets
   `awaiting-final-verification` and returns ownership to this router.
7. Brief and Report carry the same execution-revision canonical SHA-256. A
   mismatch blocks Review and batch promotion.
8. Every evidence-bearing transition validates its proposed status against the
   actual prior canonical status before replacement. New schema-2 manifests bind
   product/instance/role/profile plus result/change/batch/attempt/source
   revision/SHA-256. Standard/strict executor and reviewer instance IDs differ,
   even for the same product; compact null reviewer requires a non-blank reason
   and control-plane inline Review. Historical schema-4/schema-1 evidence is
   immutable.
9. Manual copy/paste of a state-changing standard/strict Brief does not downgrade
   governance. Validate the same Handoff and evidence chain before promotion.

## Final Completion

After all inline slices pass, or after external handback:

1. Run fresh `final_critical` once and persist its hashed evidence manifest in a
   new `awaiting-final-verification` revision. Later implementation changes
   invalidate it.
2. Review final diff, scope, tests/logs, documentation/contract consistency,
   sensitive information, temporary files, and unrelated changes.
3. If Review or verification fails, return to implementation and repeat the
   fix -> verify -> Review loop.
4. Persist final Review evidence, then mark external lifecycle `complete` only
   when attempt Report, batch Review, final verification, and final Review
   artifacts are present and runtime-validated with `--previous-status`.
5. Invoke `superpowers:verification-before-completion` before any success claim.

## OpenSpec closeout

For OpenSpec-backed work after implementation gates pass:

1. Reconcile `tasks.md`; no unexplained unchecked task may remain.
2. Update project-required design/closeout documentation.
3. If repository completion semantics allow archival now, archive the change and
   run strict validation after archive.
4. If deployment or release is still required, keep the change active, record
   owner/resume condition, and do not call the contract closed.
5. Any closeout validation or Review finding returns to correction and Review.

For OpenSpec-backed multi-step work, skip the Superpowers plan only when the
user explicitly says to skip it. Compact Direct Change does not require a large
plan by default. Never skip final verification or Review.

## Tiered Authorization And High Review

Route capability through `agent-capability-routing.md`. Platform permission,
workflow scope, and business/production authorization are independent layers.
Reuse an unchanged Confirmation Lease for safe checks and same-finding loops;
request a new user decision for any invalidating production, risk, scope,
credential, external-effect, destructive-Git, evidence, or user-decision change.

For standard/strict work, High Review inspects actual files and the complete
diff, traces copy/transform/production wiring and every behavior claim to its
mechanism, reruns critical evidence, and adds an independent adversarial or real
business-chain probe. Executor PASS cannot substitute for this Review.
