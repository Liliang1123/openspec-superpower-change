# Direct Change Rule

Use Direct Change when OpenSpec is not required.

Allowed examples:

- requested bug fix restoring intended behavior;
- low-impact config tweak;
- formatting change;
- comment update;
- typo fix;
- docs-only update without contract impact;
- test-only change for existing behavior.

Rules:

- Proceed without OpenSpec artifacts.
- Direct change means no proposal gate; it does not mean skipping code facts, scoped evidence, TDD/debugging, or verification when those gates apply.
- Still read applicable local instructions such as `AGENTS.md`.
- Use `superpowers:systematic-debugging` before changing code for unexplained failures.
- Use `superpowers:test-driven-development` for bugfix code, tests, or already-approved/already-defined implementation work unless explicitly forbidden.
- Use compact Step Evidence Gate when the direct change is more than a typo, formatting, comment, small config-only, review-only, proposal-only, docs-only, or test-only task.
- New feature behavior still requires OpenSpec unless it is already covered by an approved spec.
- Provide verification evidence before claiming completion.
- Do not create OpenSpec artifacts or Superpowers plans unless the user explicitly asks for them.
