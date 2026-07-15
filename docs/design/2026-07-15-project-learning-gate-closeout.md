# Project Learning Gate Closeout

Date: 2026-07-15  
Change: `add-project-learning-gate`  
Status: **ARCHIVED — publication and temporary-resource cleanup pending**

## Outcome

- Domain Context Check now precedes material-choice routing. Clear work skips
  grilling; unresolved project language uses `grill-with-docs` when installed
  or the complete portable Discovery First fallback.
- Project Learning Closeout promotes repeated or high-severity project-local
  lessons and always runs when the user explicitly asks to archive and distill.
- Domain meaning stays in `CONTEXT.md`; implementation/agent traps go to
  engineering guidance; mechanically enforceable rules require tests or
  validators; Candidate Cards preserve non-sensitive provenance.
- Managed governance is version 4 with `CCG-015`; 37 portable files pass parity
  on Codex, Antigravity CLI, and Grok CLI.

## Corrective Review loops

The first independent High Review returned `FAIL` because archive/distill was
not discoverable in Skill frontmatter and concatenated validator checks allowed
rules to move into the wrong artifact. Both findings received RED tests,
implementation fixes, full validation, and fresh High Review `PASS`.

The lesson was then promoted through:

- `docs/engineering-invariants.md`;
- `docs/learning-candidates/2026-07-15-project-learning-closeout.md`;
- the `AGENTS.md` loading pointer;
- deterministic frontmatter and artifact-relocation regression tests.

A focused independent learning Review found no sensitive data, confirmed all
provenance hashes, and returned `PASS`. No `CONTEXT.md` was created because the
lesson is an engineering/workflow invariant rather than domain glossary.

## Verification

- Router source: quick validation PASS, core validator PASS, 128/128 tests PASS.
- Companion source: quick validation PASS, template validator PASS, 72/72 tests
  PASS; English/Chinese READMEs document both legal routes.
- Forward evidence: 8/8 new baseline-RED/current-GREEN learning scenarios.
- Runtime: all three required targets PASS 37/37 parity, installed validators,
  managed-rule checks, and target-appropriate discovery; Grok inspect was
  consumed.
- Final source audit: 0 sensitive categories; both indexes empty; both diff
  checks PASS.
- Pre-archive Final High Review: PASS with no actionable findings.

## Archive

`openspec archive add-project-learning-gate -y` updated the canonical
`skill-workflow-governance` spec with four requirements and moved the change to
`openspec/changes/archive/2026-07-15-add-project-learning-gate`.

The CLI appended one blank line at canonical spec EOF. Post-archive diff check
identified it; the blank line was removed without semantic change. Fresh strict
validation then reported 1 passed / 0 failed, and `git diff --check` passed.
Archived tasks are 25 checked / 2 pending: publication and post-publication
cleanup remain intentionally open.

Fresh main validation after the first cherry-pick then exposed a malformed
four-backtick YAML fence that the dependency-free fallback tolerated but PyYAML
rejected. Push stopped. The fixture was corrected, dual-parser validation was
made explicit in `docs/engineering-invariants.md`, and the evidence-discovered
lesson was promoted in `docs/learning-candidates/2026-07-15-dual-parser-fixtures.md`.
Both parser paths and independent Review passed; publication may resume with a
supplemental fix commit and fresh main validation.

## Pending authorized closeout

1. Commit both feature branches with the reviewed scope.
2. Remove the exact stale untracked paths in router main that would conflict,
   then cherry-pick each feature commit into its corresponding main branch.
3. Revalidate both main repositories, push the authorized main branches, and
   verify remote SHAs.
4. Mark archived task 6.4 complete, remove task-owned backups/plans and both
   extra worktrees, mark task 6.5 complete, and verify final clean state.

Feature branches must be retained; worktree removal must not delete branches.
