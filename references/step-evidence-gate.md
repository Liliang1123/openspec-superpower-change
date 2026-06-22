# Step Evidence Gate

Use Step Evidence Gate to prevent unsupported implementation claims, scope drift, and hidden contract mismatches.

## Compact template

Use this by default for direct changes and moderate-risk steps:

1. Step goal
2. Code facts with `path:line` evidence when code is involved
3. Positive checks
4. Negative search
5. Gap and root cause
6. Change scope
7. Verification commands and results
8. Self-review, residual risk, and next-step permission

## Full template

Use this for high-risk, multi-step, or contract-changing implementation steps.

1. Step goal
   - State the current task, boundary, risk, review entry point, and acceptance criteria.
2. Code fact table
   - Every fact must include `path:line` evidence.
   - Cover entry point, call chain, behavior location, test coverage, missing verification, docs/type/schema/spec contract location, and old error path or residual.
3. Positive check result
   - Identify existing correct capability, partial implementation, test foundation, and docs/type/schema/spec synchronization points.
4. Negative search result
   - Search old fields, old API paths, old schema shapes, old docs examples, old test assertions, fallback or compatibility logic, deprecated aliases, old error messages, and outdated public claims.
5. Root cause and gap analysis
   - Explain why the current state does not satisfy the step and locate the root cause layer.
6. Implementation strategy
   - State the minimal change and why it does not hide root cause with fallback behavior unless the approved contract requires it.
7. Step change scope
   - List allowed files and actual files changed.
8. Verification commands and tests
   - List official tests, type checks, build, and OpenSpec validation when applicable.
9. Verification result
   - State pass/fail for each command.
10. Self-review result
    - Check scope drift, fake contracts, test-only claims, docs-only claims, and cross-artifact consistency.
11. Residual risk
    - List unresolved non-blocking issues.
12. Next-step permission
    - Write `yes` only when all signoff conditions are satisfied.

## Signoff conditions

Allow the next step only when:

- code facts were produced when code is involved;
- every fact has evidence;
- positive checks are complete;
- negative searches are complete;
- formal verification has run;
- there are no out-of-scope edits;
- no fake contract was introduced;
- no old error path or outdated public claim remains in scope;
- acceptance criteria pass.

## Change-type rule

- Runtime behavior change: runtime code and a regression test are required.
- API/schema/contract change: synchronize implementation, schema/type definitions, docs/specs, and tests.
- Docs-only, test-only, or proposal-only: do not claim runtime behavior changed.
- Refactor-only: rely on existing behavior tests only when they cover the touched behavior.
