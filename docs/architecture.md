# Architecture

`openspec-superpower-change` is a procedural skill composed of a concise `SKILL.md` and progressively loaded references.

## Components

| Component | Purpose |
|---|---|
| `SKILL.md` | Trigger metadata and core routing instructions |
| `references/` | Detailed workflow, comparison, evidence, and integration guidance |
| `templates/` | Reusable artifact skeletons |
| `examples/` | Concrete usage scenarios |
| `docs/` | Project-level design and roadmap notes |

## Design choice

The skill keeps the core instructions short so Codex can load it quickly. Long explanations live in references and should be read only when relevant.
