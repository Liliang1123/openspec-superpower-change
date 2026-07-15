# Example: OpenSpec-backed Change

## Scenario

Add a new skill workflow or change sandbox/tool-call behavior.

## Path

Strict path.

## Expected behavior

- Read local instructions and existing specs/changes.
- Run the Domain Context Check; skip `grill-with-docs` when project language is
  already clear, otherwise use it or the complete portable Discovery First
  fallback to clarify terms and boundaries.
- Classify the immediate phase as proposal-only. Inspect repository facts first;
  use bounded assumptions for reversible approval-time details and brainstorming
  only for material unresolved choices. Generic create/modify wording alone does
  not trigger Superpowers.
- Create OpenSpec proposal, tasks, optional design, and spec deltas.
- Run strict validation.
- Stop for approval before implementation.
- After approval, create Superpowers implementation plan.
- Preflight Review the current plan revision before implementation.
- Execute complete business slices with Step Evidence Gate and formal verification.
- Review each required slice; findings return to fix, re-verification, and Review.
- Run Project Learning Closeout after implementation Review PASS. Automatic
  thresholds or an explicit archive-and-distill request promote confirmed
  project-local knowledge and require regression enforcement when mechanical.
- Run fresh final verification and final diff/scope Review before completion.
- Reconcile tasks, archive when repository semantics allow, and validate after archive.
