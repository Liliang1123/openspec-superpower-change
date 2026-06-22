# Contributing

Thanks for improving `openspec-superpower-change`.

## Principles

- Keep `SKILL.md` concise and procedural.
- Put long explanations in `references/`.
- Put reusable prompt or artifact skeletons in `templates/`.
- Put realistic usage walkthroughs in `examples/`.
- Do not introduce a second execution discipline layer that competes with OpenSpec, Superpowers, or Step Evidence Gate.
- Do not compress official engineering artifacts so much that decisions, evidence, or risks become unauditable.

## Change rules

Use OpenSpec or an equivalent proposal process before changing public workflow semantics, request modes, evidence requirements, or artifact contracts.

For small documentation corrections, a direct change with targeted review is enough.

## Validation

Before submitting a change, check:

- `SKILL.md` frontmatter has only `name` and `description`.
- Long content is referenced from `SKILL.md` instead of duplicated.
- Examples match the documented lightweight, standard, and strict paths.
- Evidence templates still preserve commands, results, risks, and rollback notes.
