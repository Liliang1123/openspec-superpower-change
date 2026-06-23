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
7. Present the proposal summary and wait for user approval before code changes.

Do not implement OpenSpec-required work before approval.
