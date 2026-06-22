# SDD Comparison

## Conclusion

`openspec-superpower-change` uses SDD ideas but is not ordinary SDD. It is a project-level AI development change gate.

## Comparison table

| Dimension | Ordinary SDD | openspec-superpower-change |
|---|---|---|
| Primary focus | Turn specs into implementation tasks | Govern AI changes from request classification to verified completion |
| Typical flow | spec -> plan -> tasks -> implement | local rules -> request mode -> discovery -> OpenSpec approval -> Superpowers execution -> evidence -> verification |
| Approval | Optional or tool-specific | Required for contract-changing work |
| Domain clarification | Usually optional | Explicitly routed through grill-with-docs when needed |
| Execution discipline | Often task-list driven | Superpowers plan, TDD, debugging, review, verification |
| Evidence | Often tests or checklist | Code facts, positive/negative checks, verification commands, self-review, residual risk |
| Best fit | Greenfield or clear feature work | Complex existing projects, enterprise projects, multi-agent workflows, skill/agent changes |

## Key distinction

SDD asks: "What should we build before coding?"

`openspec-superpower-change` asks: "Is the agent allowed to change this, which contract controls it, how should it execute, and what evidence proves it is done?"
