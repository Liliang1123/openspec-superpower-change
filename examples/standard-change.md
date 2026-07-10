# Example: Standard Change

## Scenario

Fix a localized internal bug that restores already-defined behavior.

## Path

Direct Change with compact Step Evidence Gate.

## Expected behavior

- Confirm no new behavior, architecture, security, migration, or public contract change.
- Reproduce or inspect the failure.
- Preflight Review the scoped execution outline before implementation.
- Use TDD when practical.
- Make the smallest code change.
- Run targeted tests.
- Run a focused inline diff/self-review; use a distinct Review pass if scope or risk becomes `standard`.
- Report root cause, changed files, verification, Review, and residual risk.
