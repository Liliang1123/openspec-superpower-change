# Approved Implementation Workflow

Use only after the user approves an OpenSpec-backed proposal.

1. Invoke `superpowers:writing-plans`.
2. Save the plan to `docs/superpowers/plans/YYYY-MM-DD-<change-id>.md`.
3. Include exact files, test commands, batch profile, evidence profile, and
   executable steps grouped by complete business slices, not by file count.
4. For each executable step, include:
   - gate type;
   - allowed files;
   - expected code fact anchors;
   - likely negative-search terms;
   - formal verification commands;
   - signoff conditions.
5. Before external-agent execution, create one Handoff Contract using
   `references/handoff-contract.md`. It must include `risk_profile`,
   `batch_profile`, `current_batch`, `planned_batches`, `step_critical`,
   `final_critical`, business acceptance layers, and stop conditions.
6. If external execution is selected, hand Brief/Report/Review and batch
   promotion mechanics to `codex-brief-antigravity-review`; this skill retains
   final verification-before-completion ownership.
7. For `standard`, run `step_critical` per batch and run `final_critical` once
   at the final batch unless a later runtime change invalidates that evidence.
8. Ask how to execute the plan:
   - `superpowers:subagent-driven-development` when independent tasks can be split;
   - `superpowers:executing-plans` when work should stay inline.
9. Apply Step Evidence Gate to each executable plan step before implementation and before moving to the next step.
10. Use `superpowers:test-driven-development` for feature, refactor, and bugfix code unless the user explicitly forbids it.
11. Use `superpowers:systematic-debugging` before changing code for unexplained failures or unstable behavior.
12. Use `superpowers:requesting-code-review` before handoff when the change is substantial.
13. Use `superpowers:verification-before-completion` before any success claim.

Only skip the Superpowers plan when the user explicitly says to skip it.
