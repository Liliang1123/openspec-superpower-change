# Request Modes

## Review-only

Use when the user asks this change gate to assess architecture, OpenSpec need,
implementation authorization, risk, or completion evidence without changing
files. Standalone prompt/Brief/checklist writing and ordinary read-only
diff/Report review belong to `codex-brief-antigravity-review`.

Rules:

- Do not create or modify files.
- Do not start an OpenSpec proposal automatically.
- Do not run implementation workflow automatically.
- State whether the described work would require OpenSpec if later implemented.
- Identify unclear terms, missing approval gates, test gaps, artifact gaps, and execution risks.
- If asked to stress-test a plan, use the `grill-with-docs` questioning style but keep it read-only unless the user explicitly asks to update docs.
- Switching from review-only to implementation requires explicit user confirmation.
- “Review and fix”, “review then implement”, or any request to edit files is
  not Review-only; reclassify it through this change gate before modification.

## Discovery First

Use before OpenSpec when:

- domain terms are vague, overloaded, or conflict with existing docs/code;
- boundaries between contexts, actors, states, or lifecycle stages are unclear;
- the change has non-obvious edge cases or scenario-dependent behavior;
- a design decision may deserve an ADR;
- the user asks to grill, stress-test, clarify, or align on language before writing the proposal.

When active:

1. Read `CONTEXT-MAP.md`, `CONTEXT.md`, and relevant `docs/adr/` files when present.
2. If `CONTEXT.md` does not exist, create it before asking discovery questions by extracting established domain terms from architecture docs and code.
3. Ask one question at a time and include a recommended answer.
4. If code or docs can answer the question, inspect them instead of asking.
5. Update `CONTEXT.md` when a domain term is resolved or clarified.
6. Keep `CONTEXT.md` a glossary only: no implementation details, specs, task lists, or scratch notes.
7. Offer an ADR only when the decision is hard to reverse, surprising without context, and based on a real trade-off.
8. Treat pre-approval ADRs as `proposed` or ADR candidates when the decision depends on OpenSpec approval.
9. Continue into the OpenSpec decision once language and boundaries are stable enough.

If `grill-with-docs` is not installed, continue with these Phase 0 rules and tell the user the dedicated skill is unavailable.

## OpenSpec proposal

Use when the request requires an approved change contract. Create proposal artifacts and stop for approval before implementation.

## Approved implementation

Use only after the user approves the specific OpenSpec change-id and scoped
contract. Create and Preflight Review a Superpowers implementation plan before
implementation unless the user explicitly says to skip the plan.

## Direct Change

Use when OpenSpec is not required: localized bug fix restoring intended behavior, low-impact config tweak, formatting, comment update, typo fix, docs-only change without contract impact, or test-only change for existing behavior.

Direct Change is forbidden when the change touches any of:

- agent runtime control flow;
- tool registration, visibility, schema, validation, or fallback;
- cache key, cache bypass, result reuse, or persistence semantics;
- request routing, skill routing, or workflow lifecycle;
- public/user-visible/operator-visible behavior;
- security or sandbox boundary;
- cross-module behavior or multi-file runtime changes.

These cases must enter Discovery First or OpenSpec proposal unless an approved
existing spec or equivalent project-authoritative contract explicitly covers the
exact behavior, Gate 0 records that path, and the restoration adds no contract,
schema, compatibility, or lifecycle behavior. A README, issue, test, current
implementation, or localized bugfix label is not automatically that contract.

If the user requests an external agent for an otherwise valid Direct Change,
this router creates a profile-appropriate Handoff Contract and then delegates
the batch to `codex-brief-antigravity-review`. Low-risk Direct Change defaults
to `compact`; an approved public/API restoration remains `strict`. External
execution does not upgrade the work to OpenSpec by itself.
