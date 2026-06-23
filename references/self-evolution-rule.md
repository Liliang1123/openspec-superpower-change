# Self-Evolution Rule

Use this reference when the user asks to improve, refactor, repair, extend, test, or synchronize `openspec-superpower-change` itself.

## Positioning

This skill may improve its own instructions, references, templates, examples, and validation fixtures only through controlled self-evolution.

Self-evolution must never weaken approval gates, evidence gates, verification requirements, or user-control boundaries. Any change that affects request routing, OpenSpec decision rules, Superpowers execution rules, Step Evidence Gate signoff conditions, or completion-claim rules requires an approved change contract before implementation.

## Triggers

Enter Self-Evolution mode when the user asks to:

- optimize, refactor, or repair this skill;
- add or reorganize references;
- update `SKILL.md` trigger description or navigation;
- convert repeated lessons into durable skill rules;
- improve examples, templates, validation fixtures, or forward-tests;
- synchronize local and open-source versions of this skill;
- change how this skill routes OpenSpec, Superpowers, discovery, evidence, or completion gates.

## Change levels

| Level | Examples | OpenSpec | Backup | Forward-test | Direct edit allowed |
|---|---|---:|---:|---:|---:|
| Patch | typo, formatting, broken link, minor wording | No | Yes | Optional | Yes |
| Minor | new reference, template, example, response pattern, validation fixture | Usually no | Yes | Recommended | Yes with report |
| Major | trigger scope, request routing, OpenSpec boundary, Superpowers boundary, evidence signoff, completion-claim rule | Yes | Yes | Required | No before approval |

If unsure whether a self-evolution change is Minor or Major, treat it as Major.

## Required workflow

1. State that Self-Evolution mode is active.
2. Read current `SKILL.md` and affected references.
3. Classify the change level: Patch, Minor, or Major.
4. Create a timestamped backup before editing.
5. State the change intent, affected files, expected behavior impact, and rollback path.
6. Decide whether OpenSpec is required.
7. Implement only within the approved skill scope.
8. Run `quick_validate.py` for the skill folder.
9. Run static semantic checks relevant to the change.
10. Run forward-test for Minor changes when practical and for all Major changes after approval.
11. Report changed files, validation results, forward-test results, residual risks, and rollback path.

## Hard prohibitions

- Do not self-modify without a backup.
- Do not delete or overwrite backups.
- Do not weaken Non-negotiables.
- Do not bypass OpenSpec approval for Major self-evolution.
- Do not remove verification-before-completion.
- Do not remove Step Evidence Gate signoff conditions.
- Do not silently broaden the skill trigger scope.
- Do not install third-party plugins, alter other skills, or modify production projects unless explicitly requested and separately gated.
- Do not sync to GitHub or push without explicit user approval.

## Validation checklist

Minimum validation after any self-evolution edit:

```bash
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/elvis/.codex/skills/openspec-superpower-change
```

Static checks should confirm:

- `SKILL.md` frontmatter has only `name` and `description`.
- New references are linked from `SKILL.md` when they are part of the routing surface.
- Non-negotiables remain present.
- OpenSpec, Superpowers, Step Evidence Gate, and verification boundaries remain present.
- The change does not introduce private project details into a shareable artifact.

## Forward-test guidance

Use fresh subagents or isolated fixtures. Prompts should ask the agent to use the skill naturally, not to inspect your expected answer.

Recommended self-evolution forward-tests:

1. Review-only request about improving a reference: should not modify files.
2. Minor self-evolution request in a temporary copy: should backup, edit, validate, and report.
3. Major self-evolution request: should require OpenSpec approval before implementation.

## Report format

After self-evolution, report:

- change level;
- backup path;
- files changed;
- why the change was made;
- behavior impact;
- validation commands and results;
- forward-test results;
- residual risks;
- rollback command or path.
