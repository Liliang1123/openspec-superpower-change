# Tasks: add-internal-readiness-endpoint

## 1. Proposal and contract

- [x] 1.1 Inspect project conventions, existing specs, and active changes.
- [x] 1.2 Define the endpoint method, exposure, lifecycle semantics, request and
  response schemas, errors, compatibility, and rollback contract.
- [x] 1.3 Write the `internal-readiness` spec delta and design.
- [x] 1.4 Run `openspec validate add-internal-readiness-endpoint --strict` and
  correct every finding.
- [ ] 1.5 Present the exact change-id and obtain explicit approval of this scoped
  contract before implementation.

## 2. Approved implementation

- [ ] 2.1 After approval, create an executable implementation plan and pass a
  current-revision Preflight Review against the actual router and lifecycle
  integration points.
- [ ] 2.2 Use TDD to cover internal/public listener routing, method and request
  rejection, every lifecycle state, exact JSON schemas, and required headers.
- [ ] 2.3 Implement the lifecycle readiness adapter and internal route without
  adding public exposure, external I/O, persistence, or diagnostic fields.
- [ ] 2.4 Update internal operator documentation with the exact probe contract.

## 3. Verification and closeout

- [ ] 3.1 Run focused unit and contract tests plus the repository's official
  type, build, and test checks.
- [ ] 3.2 Run a real HTTP probe for `200`, `503`, `400`, and `405`, plus a
  negative probe proving `/internal/readiness` is unavailable on the public
  listener.
- [ ] 3.3 Complete a distinct implementation Review; fix, re-verify, and
  re-review every actionable finding.
- [ ] 3.4 Persist fresh final verification and final Review evidence, reconcile
  every task, archive when appropriate, and validate strictly after archive.
