# Agent Capability Routing

Capability profiles are stable routing and authority ceilings. They are not
model names, vendor tiers, security identities, or evidence of approval.

## Profiles

| Profile | Suitable work | Authority ceiling |
|---|---|---|
| `control-plane-high` | architecture, OpenSpec, security, migration, ambiguous debugging, Preflight, evidence audit, independent probes, promotion, archive, completion | may propose and audit decisions; user-owned gates still require the user |
| `cohesive-medium` | approved cohesive multi-file implementation with closed architecture and authorization | may implement only the bound scope; cannot change OpenSpec scope, risk, acceptance, production authority, canonical promotion, or completion |
| `mechanical-low` | deterministic one-to-two-file edits, generation, focused tests, command execution, evidence collection | cannot design, broaden scope, decide security/production matters, or resolve ambiguity |

A profile recommends capability and limits authority; it never grants authority
because a concrete model happens to be powerful. Optional model metadata is
observational only and MUST NOT influence validation, routing, or approval.

## Mandatory escalation

`mechanical-low` and `cohesive-medium` return `BLOCKED` without changing scope
when they encounter an unexpected failure, ambiguous contract, security field,
forbidden path, production credential, approval change, destructive action, or
open architecture decision. Medium also blocks on any proposed change to risk,
acceptance, production authority, canonical state, or final completion.

## Assignment rules

Schema-5 assignments bind `agent_product`, a non-sensitive contract-local
`agent_instance_id`, `agent_role`, and `capability_profile`. Standard and strict
work bind different executor and independent-reviewer instance IDs. They may use
the same product; product equality never permits self-review. The control-plane
owner is a Codex instance with `control-plane-high` and remains the only owner of
routing, evidence acceptance, promotion, archive, and completion decisions.
