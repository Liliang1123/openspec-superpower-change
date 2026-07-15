# Project Learning Gate Runtime Sync Evidence

Date: 2026-07-15  
Change: `add-project-learning-gate`  
Result: **PASS**

## Preconditions

- Corrected implementation High Review: PASS with no actionable findings.
- Source matrix: quick validation PASS, core validator PASS, 127/127 unit tests
  PASS with the explicit companion feature source, strict OpenSpec 2/2 PASS,
  diff check PASS, path-only sensitive audit 0 categories.
- Schema-4 deployment drain was run immediately before the first runtime apply:
  `active_schema4_count=0`.
- Structured pre-apply snapshots were created at
  `/private/tmp/add-project-learning-gate-sync-preapply-20260715-182820`;
  rule snapshots are mode `0600`.

## Reviewed plan

- Plan: `/private/tmp/add-project-learning-gate-sync-plan.json`
- SHA-256: `a7c6a7f155a2e5bc0269a809e4db70d3170dc402f26e2a318644ad3cc8c3bef5`
- Mode: `0600`
- Targets: Codex, Antigravity CLI, and Grok CLI; all three are `required`.
- Portable closure: 37 files per target.
- Managed governance: version 4, `CCG-001` through `CCG-015`.
- Managed body SHA-256:
  `3cec896a53b16c1b2782343cb08301c62e38ac71c44cb45c82daa1ca8f054ac3`.
- Source audit: 0 sensitive categories.

## Per-target result

| Target | Apply/parity | Router validators | Companion validators | Discovery |
|---|---|---|---|---|
| Codex | PASS, 37/37 | quick + core PASS | quick + template PASS | deterministic path/parity PASS |
| Antigravity CLI | PASS, 37/37 | quick + core PASS | quick + template PASS | manifest/reference closure PASS |
| Grok CLI | PASS, 37/37 | quick + core PASS | quick + template PASS | `grok inspect --json` path check PASS |

`verify-all` returned PASS for all three targets. The Grok inspection artifact
was mode `0600`, its contents were not logged, and `--consume` removed it after
verification. Direct comparisons also confirmed the new `SKILL.md`, Project
Learning Closeout reference, and Candidate Card template match every runtime.

## Rollback and cleanup

No rollback was required. The structured pre-apply snapshot, transaction
backup, and path/hash plan remain available until final publication and remote
verification. They must then be removed with the other task-owned temporary
resources; they are rollback aids, not durable history.
