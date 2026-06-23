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

Formal verification means the repository's official tests, type checks, builds, OpenSpec validation, or documented local equivalents that apply to the current change.


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

## Root-cause integrity rule

Do not use `try`/`except`, fallback, or compatibility logic to hide the root cause unless the approved contract explicitly requires it.

## Change-type rule

- Runtime behavior change: runtime code and a regression test are required.
- API/schema/contract change: synchronize implementation, schema/type definitions, docs/specs, and tests.
- Docs-only, test-only, or proposal-only: do not claim runtime behavior changed.
- Refactor-only: rely on existing behavior tests only when they cover the touched behavior.

## High-Risk Full Evidence Example: API/Schema Migration

Use this example when a change affects API compatibility, schema shape, persistence semantics, migration behavior, security, or operator-visible behavior. Do not collapse this into a compact report unless the user explicitly accepts the loss of detail and the change is no longer high risk.

### Scenario

A change renames a public API field from `token` to `accessToken`, migrates stored records, and keeps no compatibility alias unless the approved contract explicitly requires one.

### Full evidence example

1. **Step goal**
   - Goal: replace the public response field and persistence schema according to the approved spec.
   - Boundary: API serializer, schema/type definitions, migration, tests, and public docs for the affected endpoint only.
   - Risk: clients may break if old `token` output remains documented or if migration drops data.
   - Review entry point: `src/api/tokens.ts:42`, `src/db/migrations/20260623_rename_token.sql:1`.
   - Acceptance criteria: API returns `accessToken`, persisted data migrates without loss, no old public claim remains.

2. **Code fact table**

   | Fact | Evidence |
   |---|---|
   | Current API serializer emits old field | `src/api/tokens.ts:42` |
   | Public type still exposes old field | `src/types/token.ts:8` |
   | Existing migration framework applies ordered SQL files | `src/db/migrate.ts:31` |
   | Existing tests assert old field | `tests/api/tokens.test.ts:67` |
   | Public docs mention old field | `docs/api/tokens.md:24` |

3. **Positive check result**
   - Existing API tests cover token creation response.
   - Migration runner already has rollback test coverage.
   - Docs and types have clear synchronization points.

4. **Negative search result**
   - Search old field: `rg -n "\btoken\b" src tests docs openspec`.
   - Search compatibility aliases: `rg -n "accessToken.*token|token.*accessToken|legacy|compat" src tests docs`.
   - Search outdated docs examples: `rg -n "token:" docs examples`.
   - Result must explicitly list remaining matches and explain whether each is valid.

5. **Root cause and gap analysis**
   - Root cause layer: API/schema/docs contract mismatch.
   - Existing tests did not block the issue because they asserted the old contract.

6. **Implementation strategy**
   - Update serializer, types, migration, tests, docs, and spec references together.
   - Do not add fallback aliases unless the approved OpenSpec contract requires backward compatibility.

7. **Step change scope**
   - Allowed files: serializer, type definition, migration, endpoint tests, API docs, affected spec delta.
   - Actual files changed: list exact files.
   - Out-of-scope findings: record separately as residual risk.

8. **Verification commands and tests**

   ```bash
   openspec validate <change-id> --strict
   pnpm test tests/api/tokens.test.ts
   pnpm test tests/db/migrations.test.ts
   pnpm typecheck
   pnpm build
   ```

   Host-machine ad hoc commands are supporting evidence only, not formal verification.

9. **Verification result**
   - `openspec validate <change-id> --strict`: pass/fail with relevant output.
   - API test: pass/fail with relevant output.
   - Migration test: pass/fail with relevant output.
   - Typecheck/build: pass/fail with relevant output.
   - Warnings: state whether they affect the conclusion.

10. **Self-review result**
    - Scope drift: yes/no.
    - Fake contract introduced: yes/no.
    - Test-only claim without runtime change: yes/no.
    - Docs-only claim without runtime change: yes/no.
    - Tests used as only evidence: yes/no.
    - Code/tests/docs/types/spec consistency: pass/fail.

11. **Residual risk**
    - Example: external clients may still rely on old field; mitigation must be in approved migration/communication plan.
    - Blocking residuals must be fixed before signoff.

12. **Next-step permission**
    - `yes` only if all signoff conditions pass.
    - `no` if any old field, outdated public claim, missing migration verification, or failed formal command remains.

