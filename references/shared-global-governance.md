- [CCG-001] Codex is the primary orchestrator and the sole owner of routing,
  approval, canonical state transitions, evidence acceptance, final verification,
  and final completion.
- [CCG-002] Antigravity CLI and Grok CLI act only in explicitly assigned
  executor or reviewer roles; their results remain advisory until Codex audits
  the evidence and records the authoritative decision.
- [CCG-003] Standard and strict external work separates the executor from the
  independent reviewer; an agent cannot independently review its own work.
- [CCG-004] Governed work follows Preflight Review -> Implement -> Verify ->
  Review, and every actionable finding returns to Fix -> Verify -> Review.
- [CCG-005] Completion requires fresh evidence and Review PASS; missing, stale,
  failed, blocked, or unresolved evidence cannot be promoted to completion.
- [CCG-006] Git staging, commit, destructive commands, and push remain subject
  to their explicit user authorization boundaries.
- [CCG-007] A portable core-skill or shared-rule optimization is incomplete
  until every declared required runtime passes synchronization, validation,
  discovery, parity, and final Codex Review.
- [CCG-008] Cross-CLI synchronization excludes credentials, auth and token
  files, sessions, history, logs, caches, model settings, hooks, MCP secrets,
  CLI binaries, and every CLI-native configuration outside the managed block.
