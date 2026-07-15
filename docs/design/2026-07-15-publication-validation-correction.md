# Publication Validation Correction

Date: 2026-07-15

## Finding

Fresh validation after cherry-pick to router main failed
`test_schema4_inventory_blocks_active_and_allows_complete_history`. The legacy
contract fixture closed its YAML fence with four backticks.

## Root cause

The feature worktree resolved default `python3` to Homebrew Python without
PyYAML, so `validate_core_gates.py` used its dependency-free fallback. Router
main resolved default `python3` to Anaconda Python with PyYAML. The fallback
ignored the stray backtick, while PyYAML rejected the malformed YAML.

The implementation files and tests were byte-identical; the false confidence
came from exercising only one parser path in each environment.

## Correction and enforcement

- Correct the fixture to a three-backtick closing fence.
- Run the focused inventory test and full suite with both
  `/opt/homebrew/bin/python3` (fallback) and `/opt/anaconda3/bin/python3`
  (PyYAML).
- Preserve the generalized dual-parser rule in
  `docs/engineering-invariants.md` and its Candidate Card.
- Keep push blocked until fresh independent Review and main validation PASS.
