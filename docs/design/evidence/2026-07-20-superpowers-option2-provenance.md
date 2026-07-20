# Superpowers Option 2 Provenance

Date: 2026-07-20
Change: `streamline-workflow-prompt-contracts`

## Upstream identity

- Repository: `https://github.com/obra/superpowers.git`
- Source revision: `917e5f53b16b115b70a3a355ed5f4993b9f8b73d`
- Package version: `5.0.7`
- Governed source path:
  `skills/finishing-a-development-branch/SKILL.md`

## Content fingerprints

- Source before correction SHA-256:
  `dd2f82c6dc8582b621f9eb57fcb65f557f88eadf872727ac81d0840ae12c504e`
- Source after correction SHA-256:
  `0b037a0c381c7cb956e22ac20f68ef70a6fd896719b8e85c192697cb38c45455`
- Regression path: `tests/finishing-branch-policy.test.js`
- Regression SHA-256:
  `8952175adbfb5168e043f3d03cd279028f5be831328e44d6950ee992f5325dfa`

## Preserved contract

- Option 1 and Option 4 clean up their worktrees.
- Option 2 and Option 3 preserve their worktrees.
- Quick Reference, Common Mistakes, Step 5, and Red Flags agree.
- Push/PR commands, typed discard confirmation, test gates, and the force-push
  prohibition are unchanged by this correction.

## Upgrade guard

After any Superpowers source revision or package-version change, rerun:

```bash
node --test tests/finishing-branch-policy.test.js
```

The semantic regression is authoritative across harmless Markdown edits. The
recorded source hash is provenance, not a reason to reject an intentional
upstream update; a changed hash requires diff inspection and a fresh regression
result before this correction may be considered preserved.
