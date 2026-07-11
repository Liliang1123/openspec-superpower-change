# Learning Candidate Pipeline

Corrections and newly discovered evidence create governed candidates; they do
not automatically edit a Skill.

## Candidate Card

A Candidate Card records: symptom, prior assumption, correction/evidence,
generalized invariant, severity, scope classification, target artifact, baseline
scenario, independent reproductions, event kind, and duplicate/conflict result.
It retains decision provenance and the current approval boundary.

## Scope and thresholds

- `task-local`: update only the current Plan, Brief, or Review.
- `project-local`: update project governance or documentation through its normal
  change path.
- `global`: may become a Self-Evolution proposal only after two independent
  reproductions, or one high-severity security, integrity, or false-PASS event.

Meeting the threshold permits proposal creation only. Global implementation still
requires an approved specific OpenSpec Change, backup, TDD RED/GREEN evidence,
forward-tests, Review PASS, runtime synchronization, and separately authorized
publication. A single low-risk wording correction remains a candidate.

Prefer a deterministic validator and regression test for mechanical invariants.
If a candidate conflicts with an existing rule, preserve both evidence sets,
mark it `BLOCKED`, and return the decision to the control plane or user rather
than silently choosing one.
