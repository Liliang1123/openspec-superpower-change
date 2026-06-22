# Example: Review-only

## User prompt

```text
Use openspec-superpower-change review-only mode. Review this design and state whether implementation would require OpenSpec. Do not modify files.
```

## Expected behavior

- Read local instructions.
- Read the target artifact.
- Do not create files or proposals.
- Report unclear terms, risks, missing artifacts, and whether future implementation requires OpenSpec.
