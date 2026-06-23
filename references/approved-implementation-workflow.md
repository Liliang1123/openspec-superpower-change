# Approved Implementation Workflow

Use only after the user approves an OpenSpec-backed proposal.

1. Invoke `superpowers:writing-plans`.
2. Save the plan to `docs/superpowers/plans/YYYY-MM-DD-<change-id>.md`.
3. Include exact files, test commands, and small executable steps.
4. For each executable step, include:
   - gate type;
   - allowed files;
   - expected code fact anchors;
   - likely negative-search terms;
   - formal verification commands;
   - signoff conditions.
5. Ask how to execute the plan:
   - `superpowers:subagent-driven-development` when independent tasks can be split;
   - `superpowers:executing-plans` when work should stay inline.
6. Apply Step Evidence Gate to each executable plan step before implementation and before moving to the next step.
7. Use `superpowers:test-driven-development` for feature, refactor, and bugfix code unless the user explicitly forbids it.
8. Use `superpowers:systematic-debugging` before changing code for unexplained failures or unstable behavior.
9. Use `superpowers:requesting-code-review` before handoff when the change is substantial.
10. Use `superpowers:verification-before-completion` before any success claim.

Only skip the Superpowers plan when the user explicitly says to skip it.
