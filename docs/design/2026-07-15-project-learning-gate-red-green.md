# Project Learning Gate RED/GREEN Evidence

## Baseline

Before new contract tests or portable implementation changes:

- router quick validation: PASS
- dependency-free core validation: PASS
- router unittest suite: PASS, 117 tests
- strict OpenSpec validation: PASS, 2 items
- diff check: PASS

## RED 1: Routing and project learning contract

Command: focused six-test `WorkflowRulesTest` invocation from the approved plan.

- exit: 1
- result: 5 expected assertion failures, 1 fixture-classification PASS
- expected missing behavior:
  - no explicit `Domain Context Check` in the phase-aware route;
  - canonical context durability does not reject intentional ignore rules;
  - `references/project-learning-closeout.md` does not exist;
  - `templates/learning-candidate-template.md` does not exist;
  - completion/archive blocking is not wired.
- test integrity: failures are assertions, not setup/import/syntax errors.
- qagent-shaped fixture: PASS, proving the sanitized test input itself separates
  semantic, engineering, and mechanical-regression knowledge.

## RED 2: Portable governance version and closure

Initial run exposed managed version 4 as an unhandled `ValueError`. The test was
corrected without changing production code so unsupported version 4 becomes an
explicit assertion failure.

Corrected command: focused two-test `ManifestAndTriggerTests` invocation from
the approved plan.

- exit: 1
- result: 4 expected assertion failures
- expected missing behavior:
  - sync validator supports managed versions 1-3 only;
  - canonical portable manifest omits
    `references/local-instruction-checkpoint.md`;
  - canonical portable manifest omits
    `references/project-learning-closeout.md`;
  - canonical portable manifest omits
    `templates/learning-candidate-template.md`.
- test integrity: all failures are explicit assertions tied to approved missing
  behavior.

## GREEN

The combined focused command reran all six router-learning tests and both
portable-governance tests after minimal implementation.

- exit: 0
- result: PASS, 8 tests
- router learning behavior: 6/6 PASS
- managed version 4 / portable closure: 2/2 PASS
- dependency-free core validator: PASS after the same source revision
- canonical manifest validation through `validate_manifest()`: PASS

One GREEN validation finding was corrected before signoff: the core validator
uses literal contract substrings, while two required local-checkpoint phrases
were split by Markdown wrapping. The reference was reflowed without weakening
the validator; the same core/focused checks then passed.
