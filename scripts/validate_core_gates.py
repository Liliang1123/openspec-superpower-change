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

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - exercised when PyYAML is absent
    yaml = None


START = "<!-- COOP_HANDOFF_CONTRACT_START -->"
END = "<!-- COOP_HANDOFF_CONTRACT_END -->"
RISK_PROFILES = {"compact", "standard", "strict"}
BATCH_PROFILES = {"single", "cohesive", "staged"}
BUSINESS_ACCEPTANCE = {"required", "optional", "not-applicable"}
MODES = {
    "review-only",
    "discovery-first",
    "openspec-proposal",
    "approved-implementation",
    "direct-change",
    "self-evolution",
}
APPROVAL_STATUSES = {"not-required", "proposed", "approved", "blocked"}
EXECUTORS = {"codex", "external-agent"}
GOVERNORS = {"codex", "codex-brief-antigravity-review"}
NEXT_OWNERS = {"codex", "codex-brief-antigravity-review", "external-agent", "user"}


def parse_scalar(value: str):
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.isdigit():
        return int(value)
    return value


def simple_yaml_load(text: str) -> dict:
    result: dict = {}
    current_key: str | None = None
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        if indent == 0 and not line.startswith("- "):
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            if value.strip():
                result[key] = parse_scalar(value)
                current_key = None
            else:
                result[key] = {}
                current_key = key
        elif indent == 2 and current_key and line.startswith("- "):
            if not isinstance(result[current_key], list):
                result[current_key] = []
            result[current_key].append(parse_scalar(line[2:]))
        elif indent == 2 and current_key and ":" in line:
            if not isinstance(result[current_key], dict):
                result[current_key] = {}
            key, value = line.split(":", 1)
            result[current_key][key.strip()] = parse_scalar(value)
    return result


def yaml_load(text: str):
    if yaml is not None:
        return yaml.safe_load(text)
    return simple_yaml_load(text)

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


def extract_handoff_contract(text: str, label: str) -> dict:
    if text.count(START) != 1 or text.count(END) != 1:
        raise AssertionError(f"{label}: handoff contract must have exactly one marker block")
    body = text.split(START, 1)[1].split(END, 1)[0].strip()
    if body.startswith("```yaml"):
        body = body.removeprefix("```yaml").strip()
    if body.endswith("```"):
        body = body[:-3].strip()
    data = yaml_load(body)
    if not isinstance(data, dict):
        raise AssertionError(f"{label}: handoff contract must be a YAML mapping")
    return data


def validate_handoff_contract(data: dict, label: str) -> None:
    required = {
        "schema_version",
        "change_id",
        "mode",
        "approval_status",
        "risk_profile",
        "batch_profile",
        "current_batch",
        "planned_batches",
        "executor",
        "governor",
        "next_owner",
        "step_critical",
        "final_critical",
        "business_acceptance",
        "stop_conditions",
        "verification_strategy",
    }
    missing = sorted(required - set(data))
    if missing:
        raise AssertionError(f"{label}: missing contract fields: {missing}")
    if data["mode"] not in MODES:
        raise AssertionError(f"{label}: invalid mode")
    if data["approval_status"] not in APPROVAL_STATUSES:
        raise AssertionError(f"{label}: invalid approval_status")
    if data["risk_profile"] not in RISK_PROFILES:
        raise AssertionError(f"{label}: invalid risk_profile")
    if data["batch_profile"] not in BATCH_PROFILES:
        raise AssertionError(f"{label}: invalid batch_profile")
    if data["executor"] not in EXECUTORS:
        raise AssertionError(f"{label}: invalid executor")
    if data["governor"] not in GOVERNORS:
        raise AssertionError(f"{label}: invalid governor")
    if data["next_owner"] not in NEXT_OWNERS:
        raise AssertionError(f"{label}: invalid next_owner")
    if int(data["current_batch"]) < 1 or int(data["current_batch"]) > int(data["planned_batches"]):
        raise AssertionError(f"{label}: current_batch must be between 1 and planned_batches")
    acceptance = data["business_acceptance"]
    for key in ("unit", "pipeline", "api", "real_business"):
        if key not in acceptance:
            raise AssertionError(f"{label}: missing business_acceptance.{key}")
        if acceptance[key] not in BUSINESS_ACCEPTANCE:
            raise AssertionError(f"{label}: invalid business_acceptance.{key}")
    if data["risk_profile"] in {"standard", "strict"}:
        for key in ("step_critical", "final_critical"):
            if not isinstance(data[key], list) or not data[key] or not all(isinstance(item, str) for item in data[key]):
                raise AssertionError(f"{label}: {key} must be a non-empty string list")


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
    handoff = read(root / "references" / "handoff-contract.md")

    validate_frontmatter(skill)
    validate_reference_links(root, skill)

    # Core identity and routing gates.
    require(skill, "OpenSpec + Superpowers Change Gate", "SKILL.md")
    require(skill, "Self-Evolution", "SKILL.md")
    require(skill, "Do not implement OpenSpec-required work before approval", "SKILL.md")
    require(skill, "Do not claim completion without verification evidence", "SKILL.md")
    require(skill, "Self-evolution cannot weaken approval gates", "SKILL.md")
    require(skill, "Never run `git add`, `git commit`, `git reset`, or `git clean`", "SKILL.md")
    require_any(skill, ["Step Evidence Gate", "evidence gate"], "SKILL.md")
    require_any(skill, ["Superpowers", "superpowers"], "SKILL.md")
    require(skill, "Handoff Contract", "SKILL.md")
    require(skill, "codex-brief-antigravity-review", "SKILL.md")

    # Self-evolution hard boundaries.
    require(self_rule, "Patch", "self-evolution-rule.md")
    require(self_rule, "Minor", "self-evolution-rule.md")
    require(self_rule, "Major", "self-evolution-rule.md")
    require(self_rule, "Do not self-modify without a backup", "self-evolution-rule.md")
    require(self_rule, "Do not bypass OpenSpec approval for Major self-evolution", "self-evolution-rule.md")
    require(self_rule, "Do not sync to GitHub or push without explicit user approval", "self-evolution-rule.md")
    require(self_rule, "quick_validate.py", "self-evolution-rule.md")
    require(self_rule, "short-circuit only unrelated business-project OpenSpec recursion", "self-evolution-rule.md")
    require(self_rule, "Do not short-circuit user approval", "self-evolution-rule.md")
    require(self_rule, "Backups created for self-evolution are temporary rollback aids, not history.", "self-evolution-rule.md")
    require(self_rule, "After validation/forward-test pass", "self-evolution-rule.md")
    require(self_rule, "Never leave backup skill directories under `/Users/elvis/.codex/skills/`", "self-evolution-rule.md")

    # Evidence gate hard boundaries.
    require(evidence, "path:line", "step-evidence-gate.md")
    require(evidence, "Formal verification", "step-evidence-gate.md")
    require_any(evidence, ["try`/`except", "try/except"], "step-evidence-gate.md")
    require_any(evidence, ["Next-step permission", "Next-step permission"], "step-evidence-gate.md")
    require(evidence, "Runtime behavior change", "step-evidence-gate.md")
    require(evidence, "API/schema/contract change", "step-evidence-gate.md")
    require(evidence, "compact", "step-evidence-gate.md")
    require(evidence, "standard", "step-evidence-gate.md")
    require(evidence, "strict", "step-evidence-gate.md")

    contract = extract_handoff_contract(handoff, "handoff-contract.md")
    validate_handoff_contract(contract, "handoff-contract.md")
    require(handoff, "codex-brief-antigravity-review` must not overwrite `mode`", "handoff-contract.md")
    require(handoff, "current_batch", "handoff-contract.md")
    require(handoff, "planned_batches", "handoff-contract.md")

    print(f"Core gates valid: {root}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except AssertionError as exc:
        print(f"Core gate validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
