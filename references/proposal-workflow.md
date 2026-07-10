# Proposal Workflow

Use this workflow when OpenSpec is required.

1. Run repository context checks from `openspec/AGENTS.md` when present.
2. Inspect existing specs and active changes.
3. Use Discovery First if domain language, boundaries, or design choices are unclear.
4. Pick a short verb-led `change-id`.
5. Create or update:
   - `openspec/changes/<change-id>/proposal.md`;
   - `openspec/changes/<change-id>/tasks.md`;
   - `openspec/changes/<change-id>/design.md` when the change is cross-cutting, performance-sensitive, migration-heavy, or architecturally meaningful;
   - one or more spec deltas under `openspec/changes/<change-id>/specs/...`.
6. Validate with `openspec validate <change-id> --strict`.
7. Present the proposal summary and exact `change-id`; record explicit user
   approval of that scoped contract before code changes.

When `superpowers:brainstorming` is needed, use it to clarify alternatives and
write the accepted decisions into OpenSpec `design.md`/spec deltas. The approved
OpenSpec artifacts are the single design contract; do not require a duplicate
`docs/superpowers/specs/` artifact, commit, and approval for the same decision.

Do not implement OpenSpec-required work before approval.
