#!/usr/bin/env python3
"""Validate core gates for openspec-superpower-change.

This script intentionally checks for non-negotiable governance text that should
not be weakened by self-evolution. It complements, but does not replace,
skill-creator quick_validate.py.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise AssertionError(f"missing required file: {path}")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing required text: {needle!r}")


def require_any(text: str, needles: list[str], label: str) -> None:
    if not any(n in text for n in needles):
        raise AssertionError(f"{label}: missing one of required texts: {needles!r}")


def validate_frontmatter(skill: str) -> None:
    if not skill.startswith("---\n"):
        raise AssertionError("SKILL.md: missing YAML frontmatter")
    parts = skill.split("---\n", 2)
    if len(parts) < 3:
        raise AssertionError("SKILL.md: malformed YAML frontmatter")
    keys = []
    for line in parts[1].splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" in line:
            keys.append(line.split(":", 1)[0].strip())
    if keys != ["name", "description"]:
        raise AssertionError(f"SKILL.md: frontmatter keys must be name, description only; got {keys}")


def validate_reference_links(root: Path, skill: str) -> None:
    for link in re.findall(r"`(references/[^`]+\.md)`", skill):
        if not (root / link).is_file():
            raise AssertionError(f"SKILL.md: linked reference missing: {link}")


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path.cwd().resolve()
    skill = read(root / "SKILL.md")
    self_rule = read(root / "references" / "self-evolution-rule.md")
    evidence = read(root / "references" / "step-evidence-gate.md")

    validate_frontmatter(skill)
    validate_reference_links(root, skill)

    # Core identity and routing gates.
    require(skill, "OpenSpec + Superpowers Change Gate", "SKILL.md")
    require(skill, "Self-Evolution", "SKILL.md")
    require(skill, "Do not implement OpenSpec-required work before approval", "SKILL.md")
    require(skill, "Do not claim completion without verification evidence", "SKILL.md")
    require(skill, "Self-evolution cannot weaken approval gates", "SKILL.md")
    require_any(skill, ["Step Evidence Gate", "evidence gate"], "SKILL.md")
    require_any(skill, ["Superpowers", "superpowers"], "SKILL.md")

    # Self-evolution hard boundaries.
    require(self_rule, "Patch", "self-evolution-rule.md")
    require(self_rule, "Minor", "self-evolution-rule.md")
    require(self_rule, "Major", "self-evolution-rule.md")
    require(self_rule, "Do not self-modify without a backup", "self-evolution-rule.md")
    require(self_rule, "Do not bypass OpenSpec approval for Major self-evolution", "self-evolution-rule.md")
    require(self_rule, "Do not sync to GitHub or push without explicit user approval", "self-evolution-rule.md")
    require(self_rule, "quick_validate.py", "self-evolution-rule.md")

    # Evidence gate hard boundaries.
    require(evidence, "path:line", "step-evidence-gate.md")
    require(evidence, "Formal verification", "step-evidence-gate.md")
    require_any(evidence, ["try`/`except", "try/except"], "step-evidence-gate.md")
    require_any(evidence, ["Next-step permission", "Next-step permission"], "step-evidence-gate.md")
    require(evidence, "Runtime behavior change", "step-evidence-gate.md")
    require(evidence, "API/schema/contract change", "step-evidence-gate.md")

    print(f"Core gates valid: {root}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except AssertionError as exc:
        print(f"Core gate validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
