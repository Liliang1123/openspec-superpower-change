#!/usr/bin/env python3
"""Plan, apply, and verify allowlisted synchronization across CLI runtimes."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import tempfile
from pathlib import Path, PurePosixPath


MANAGED_BLOCK_START = "<!-- CROSS_CLI_GOVERNANCE_BEGIN version={version} -->"
MANAGED_BLOCK_END = "<!-- CROSS_CLI_GOVERNANCE_END version={version} -->"
TARGET_IDS = {"codex", "antigravity-cli", "grok-cli"}
PORTABLE_TOP_LEVEL = {"SKILL.md", "references", "scripts", "templates", "agents"}
DENIED_SEGMENTS = {
    "auth", "authentication", "credential", "credentials", "token", "tokens",
    "session", "sessions", "history", "log", "logs", "cache", "caches",
    "model-settings", "settings", "hook", "hooks", "mcp", "bin", "binary",
    "binaries", "keys",
}
DENIED_SUFFIXES = {".key", ".pem", ".p12", ".pfx"}
REQUIRED_MANIFEST_KEYS = {"schema_version", "skills", "managed_rules", "targets"}
PORTABLE_MANIFEST_PATH = "references/cross-cli-portable-manifest.json"


def _nonblank(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _safe_relative_syntax(relative_path) -> str:
    if not isinstance(relative_path, (str, os.PathLike)):
        raise ValueError("path must be relative text")
    value = os.fspath(relative_path)
    if not value or "\0" in value or "\\" in value or "://" in value:
        raise ValueError(f"unsafe path: {value!r}")
    if re.match(r"^[A-Za-z]:/", value):
        raise ValueError(f"unsafe path: {value!r}")
    pure = PurePosixPath(value)
    parts = value.split("/")
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in parts):
        raise ValueError(f"unsafe path: {value!r}")
    return value


def _denied_category(relative_path: str) -> str | None:
    lowered = relative_path.lower()
    if lowered == ".env" or any(lowered.endswith(suffix) for suffix in DENIED_SUFFIXES):
        return "sensitive-file"
    for raw_part in lowered.split("/"):
        stem = raw_part.rsplit(".", 1)[0]
        if raw_part in DENIED_SEGMENTS or stem in DENIED_SEGMENTS:
            return raw_part
        if raw_part.startswith(("auth-", "token-", "credential-", "session-")):
            return raw_part
    return None


def _require_portable_path(relative_path: str) -> str:
    value = _safe_relative_syntax(relative_path)
    category = _denied_category(value)
    if category:
        raise ValueError(f"denied category {category!r} at path {value!r}")
    first = value.split("/", 1)[0]
    if first not in PORTABLE_TOP_LEVEL:
        raise ValueError(f"path is outside portable allowlist: {value!r}")
    if first == "agents" and value != "agents/openai.yaml":
        raise ValueError(f"path is outside portable allowlist: {value!r}")
    return value


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def classify_sync_trigger(changed_paths, manifest):
    """Return whether changed source paths require the cross-runtime gate."""
    validated = validate_manifest(manifest)
    portable = {
        item["path"]
        for skill in validated["skills"]
        for item in skill["files"]
    }
    portable.add(validated["managed_rules"]["source"])
    portable.add(PORTABLE_MANIFEST_PATH)
    for changed in changed_paths:
        try:
            normalized = _safe_relative_syntax(changed)
        except ValueError:
            continue
        if normalized in portable:
            return True
    return False


def validate_manifest(manifest):
    """Validate the path-free portable-file and target declaration manifest."""
    if not isinstance(manifest, dict) or set(manifest) != REQUIRED_MANIFEST_KEYS:
        raise ValueError("manifest must contain only the declared top-level fields")
    if manifest["schema_version"] != 1:
        raise ValueError("manifest schema_version must be 1")
    if not isinstance(manifest["skills"], list) or not manifest["skills"]:
        raise ValueError("manifest skills must be a non-empty list")
    seen_skills: set[str] = set()
    for skill in manifest["skills"]:
        _validate_skill_manifest(skill, seen_skills)
    rules = manifest["managed_rules"]
    if not isinstance(rules, dict) or set(rules) != {"version", "source", "invariant_ids"}:
        raise ValueError("managed_rules fields are invalid")
    if type(rules["version"]) is not int or rules["version"] < 1:
        raise ValueError("managed_rules version must be a positive integer")
    _require_portable_path(rules["source"])
    expected_ids = [f"CCG-{number:03d}" for number in range(1, 9)]
    if rules["invariant_ids"] != expected_ids:
        raise ValueError("managed_rules invariant_ids must be CCG-001..CCG-008")
    if not isinstance(manifest["targets"], list) or not manifest["targets"]:
        raise ValueError("manifest targets must be a non-empty list")
    _validate_target_states(manifest["targets"], allow_pending=True)
    return manifest


def _validate_skill_manifest(skill, seen_skills: set[str]) -> None:
    if not isinstance(skill, dict) or set(skill) != {"name", "source_alias", "files"}:
        raise ValueError("skill manifest fields are invalid")
    if not _nonblank(skill["name"]) or skill["name"] in seen_skills:
        raise ValueError("skill names must be non-blank and unique")
    seen_skills.add(skill["name"])
    if not _nonblank(skill["source_alias"]) or "/" in skill["source_alias"]:
        raise ValueError("source_alias must be path-free text")
    if not isinstance(skill["files"], list) or not skill["files"]:
        raise ValueError("skill files must be a non-empty list")
    seen_paths: set[str] = set()
    for item in skill["files"]:
        if not isinstance(item, dict) or set(item) != {"path", "targets"}:
            raise ValueError("portable file entries require path and targets")
        path = _require_portable_path(item["path"])
        if path in seen_paths:
            raise ValueError(f"duplicate portable path: {path!r}")
        seen_paths.add(path)
        targets = item["targets"]
        if not isinstance(targets, list) or not targets or set(targets) - TARGET_IDS:
            raise ValueError(f"invalid targets for portable path {path!r}")


def validate_relative_path(root, relative_path, *, must_exist=True):
    """Resolve one safe regular file below root without symlink escape."""
    value = _safe_relative_syntax(relative_path)
    root_path = Path(root)
    if not root_path.exists() or not root_path.is_dir() or root_path.is_symlink():
        raise ValueError(f"invalid declared root: {root_path}")
    resolved_root = root_path.resolve(strict=True)
    candidate = root_path.joinpath(*value.split("/"))
    current = root_path
    for part in value.split("/"):
        current = current / part
        if current.exists() or current.is_symlink():
            if current.is_symlink():
                raise ValueError(f"symlink path is not allowed: {value!r}")
    if not candidate.exists():
        if must_exist:
            raise ValueError(f"missing regular file: {value!r}")
        parent = candidate.parent.resolve(strict=True)
        try:
            parent.relative_to(resolved_root)
        except ValueError as exc:
            raise ValueError(f"path escapes declared root: {value!r}") from exc
        return candidate
    resolved = candidate.resolve(strict=True)
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"path escapes declared root: {value!r}") from exc
    if not stat.S_ISREG(candidate.stat(follow_symlinks=False).st_mode):
        raise ValueError(f"path is not a regular file: {value!r}")
    return candidate


def build_portable_manifest(source_root, relative_paths):
    """Return relative-path/SHA-256 records for allowlisted source files."""
    records = []
    for relative_path in relative_paths:
        value = _require_portable_path(relative_path)
        path = validate_relative_path(source_root, value)
        records.append({"path": value, "sha256": _sha256(path)})
    return records


def validate_portable_parity(source_root, target_root, file_records):
    """Validate exact portable-file path and SHA-256 parity."""
    if not isinstance(file_records, list) or not file_records:
        raise ValueError("portable parity requires file records")
    for record in file_records:
        if not isinstance(record, dict) or set(record) != {"path", "sha256"}:
            raise ValueError("portable parity records require path and sha256")
        value = _require_portable_path(record["path"])
        digest = record["sha256"]
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError(f"invalid SHA-256 for path {value!r}")
        source = validate_relative_path(source_root, value)
        target = validate_relative_path(target_root, value)
        if _sha256(source) != digest or _sha256(target) != digest:
            raise ValueError(f"portable parity drift at path {value!r}")
    return True


def _marker_parts(text: str, version: int) -> tuple[str, str, str]:
    if not isinstance(text, str):
        raise ValueError("managed-rule input must be text")
    start = MANAGED_BLOCK_START.format(version=version)
    end = MANAGED_BLOCK_END.format(version=version)
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError("managed-rule file must contain exactly one matching marker pair")
    remaining = text.replace(start, "", 1).replace(end, "", 1)
    if "CROSS_CLI_GOVERNANCE_BEGIN" in remaining or "CROSS_CLI_GOVERNANCE_END" in remaining:
        raise ValueError("managed-rule file contains an additional marker")
    start_index = text.index(start) + len(start)
    end_index = text.index(end)
    if end_index < start_index or "CROSS_CLI_GOVERNANCE_" in text[start_index:end_index].split("\n", 1)[0]:
        raise ValueError("managed-rule markers are nested or out of order")
    body = text[start_index:end_index]
    if "CROSS_CLI_GOVERNANCE_BEGIN" in body or "CROSS_CLI_GOVERNANCE_END" in body:
        raise ValueError("managed-rule markers must not be nested or mismatched")
    return text[:start_index], body, text[end_index:]


def extract_managed_block(text, *, version):
    """Extract the unique versioned managed-rule body with LF normalization."""
    _, body, _ = _marker_parts(text, version)
    body = body.replace("\r\n", "\n")
    if body.startswith("\n"):
        body = body[1:]
    return body


def replace_managed_block(original, canonical_body, *, version):
    """Replace only the unique managed-rule body and preserve outside bytes."""
    prefix, old_body, suffix = _marker_parts(original, version)
    newline = "\r\n" if old_body.startswith("\r\n") else "\n"
    normalized = canonical_body.replace("\r\n", "\n").replace("\r", "\n")
    rendered = normalized.replace("\n", newline)
    if not rendered.endswith(newline):
        rendered += newline
    return prefix + newline + rendered + suffix


def install_managed_block(original, canonical_body, *, version):
    """Install one managed block or replace the one valid existing block."""
    marker_token = "CROSS_CLI_GOVERNANCE_"
    start = MANAGED_BLOCK_START.format(version=version)
    end = MANAGED_BLOCK_END.format(version=version)
    start_count = original.count(start)
    end_count = original.count(end)
    if start_count == end_count == 1:
        return replace_managed_block(original, canonical_body, version=version)
    if marker_token in original or start_count or end_count:
        raise ValueError("managed-rule file has partial, mismatched, or duplicate markers")
    newline = "\r\n" if "\r\n" in original and "\n" not in original.replace("\r\n", "") else "\n"
    separator = "" if not original or original.endswith(("\n", "\r")) else newline
    normalized = canonical_body.replace("\r\n", "\n").replace("\r", "\n")
    body = normalized.replace("\n", newline)
    if not body.endswith(newline):
        body += newline
    return f"{original}{separator}{start}{newline}{body}{end}{newline}"


def validate_managed_rule_parity(
    canonical_body, target_text, *, version, invariant_ids
):
    """Validate normalized body equality and stable invariant IDs."""
    canonical = canonical_body.replace("\r\n", "\n").replace("\r", "\n")
    if not canonical.endswith("\n"):
        canonical += "\n"
    actual = extract_managed_block(target_text, version=version)
    if actual != canonical:
        raise ValueError("managed-rule body hash mismatch")
    for invariant_id in invariant_ids:
        if canonical.count(f"[{invariant_id}]") != 1:
            raise ValueError(f"missing or duplicate invariant ID: {invariant_id}")
    return True


def _validate_target_states(targets, *, allow_pending):
    if not isinstance(targets, list) or not targets:
        raise ValueError("target states must be a non-empty list")
    seen: set[str] = set()
    has_required = False
    for target in targets:
        required_fields = {
            "id", "selection", "result", "decision_owner", "evidence",
            "reason", "resume_condition",
        }
        if not isinstance(target, dict) or set(target) != required_fields:
            raise ValueError("target state fields are invalid")
        target_id = target["id"]
        if target_id not in TARGET_IDS or target_id in seen:
            raise ValueError("target IDs must be canonical and unique")
        seen.add(target_id)
        if target["decision_owner"] != "codex":
            raise ValueError("target decision_owner must be codex")
        if not all(_nonblank(target[field]) for field in ("evidence", "reason", "resume_condition")):
            raise ValueError("target evidence, reason, and resume_condition must be non-blank")
        selection = target["selection"]
        result = target["result"]
        if selection == "required":
            has_required = True
            allowed_results = {"pass", "pending"} if allow_pending else {"pass"}
            if result not in allowed_results:
                raise ValueError(f"required target is not complete: {target_id}")
        elif selection == "not-applicable":
            if result != "not-applicable":
                raise ValueError("failed required target cannot be mislabeled not-applicable")
            reason = target["reason"].lower()
            if not any(term in reason for term in ("not installed", "unsupported", "excluded")):
                raise ValueError("not-applicable reason is not an allowed condition")
        else:
            raise ValueError("target selection must be required or not-applicable")
    if has_required and seen != TARGET_IDS:
        raise ValueError("all three default required targets must be declared")
    return True


def validate_target_states(targets):
    """Require completion-ready states for every declared target."""
    return _validate_target_states(targets, allow_pending=False)


def validate_completion_authority(decision):
    """Require Codex ownership and reject auxiliary self-authorization."""
    if not isinstance(decision, dict) or decision.get("decision_owner") != "codex":
        raise ValueError("only codex may own the authoritative completion decision")
    if decision.get("result") not in {"pass", "fail", "blocked"}:
        raise ValueError("completion result is invalid")
    return True


def _regular_file(path: Path, label: str) -> os.stat_result:
    try:
        metadata = path.stat(follow_symlinks=False)
    except FileNotFoundError as exc:
        raise ValueError(f"missing {label}: {path}") from exc
    if not stat.S_ISREG(metadata.st_mode):
        raise ValueError(f"{label} is not a regular file: {path}")
    return metadata


def create_secure_backup(source, backup_dir, *, sensitive=False):
    """Create a non-discoverable backup; sensitive backups use mode 0600."""
    source_path = Path(source)
    metadata = _regular_file(source_path, "backup source")
    backup_root = Path(backup_dir)
    current = backup_root
    while not current.exists():
        if current.is_symlink():
            raise ValueError(f"backup directory cannot use symlinks: {backup_root}")
        current = current.parent
    if current.is_symlink() or backup_root.is_symlink():
        raise ValueError(f"backup directory cannot use symlinks: {backup_root}")
    resolved_backup = backup_root.resolve(strict=False)
    if "skills" in {part.lower() for part in resolved_backup.parts}:
        raise ValueError(f"backup directory must be outside skill discovery roots: {backup_root}")
    backup_root.mkdir(parents=True, exist_ok=True)
    if not backup_root.is_dir() or backup_root.is_symlink():
        raise ValueError(f"invalid backup directory: {backup_root}")
    descriptor, name = tempfile.mkstemp(prefix="cross-cli-backup-", dir=backup_root)
    backup = Path(name)
    try:
        mode = 0o600 if sensitive else stat.S_IMODE(metadata.st_mode)
        os.fchmod(descriptor, mode)
        with os.fdopen(descriptor, "wb") as output, source_path.open("rb") as input_file:
            for chunk in iter(lambda: input_file.read(65536), b""):
                output.write(chunk)
            output.flush()
            os.fsync(output.fileno())
    except BaseException:
        try:
            os.close(descriptor)
        except OSError:
            pass
        backup.unlink(missing_ok=True)
        raise
    return backup


def atomic_replace(path, content, *, mode=None):
    """Replace one regular file through a same-directory temporary file."""
    target = Path(path)
    metadata = _regular_file(target, "atomic replacement target")
    if not isinstance(content, (bytes, bytearray)):
        raise ValueError("atomic replacement content must be bytes")
    target_mode = stat.S_IMODE(metadata.st_mode) if mode is None else mode
    descriptor, name = tempfile.mkstemp(prefix=".cross-cli-sync.", dir=target.parent)
    temporary = Path(name)
    try:
        os.fchmod(descriptor, target_mode)
        with os.fdopen(descriptor, "wb") as output:
            output.write(bytes(content))
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, target)
        directory_fd = os.open(target.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        temporary.unlink(missing_ok=True)
    return target


def _create_parent_directories(parent: Path) -> list[Path]:
    missing: list[Path] = []
    current = parent
    while not current.exists():
        if current.is_symlink():
            raise ValueError(f"symlink parent is not allowed: {current}")
        missing.append(current)
        current = current.parent
    if not current.is_dir() or current.is_symlink():
        raise ValueError(f"invalid existing parent: {current}")
    created: list[Path] = []
    for directory in reversed(missing):
        directory.mkdir(mode=0o755)
        created.append(directory)
    return created


def atomic_create(path, content, *, mode=0o644):
    """Create one missing regular file without replacing any existing path."""
    target = Path(path)
    if target.exists() or target.is_symlink():
        raise FileExistsError(f"create target already exists: {target}")
    if not isinstance(content, (bytes, bytearray)):
        raise ValueError("atomic creation content must be bytes")
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    descriptor = os.open(target, flags, mode)
    try:
        with os.fdopen(descriptor, "wb") as output:
            output.write(bytes(content))
            output.flush()
            os.fsync(output.fileno())
    except BaseException:
        target.unlink(missing_ok=True)
        raise
    directory_fd = os.open(target.parent, os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)
    return target


def apply_sync_transaction(operations, backup_dir, *, verify=None):
    """Apply operations as a group or restore already changed files."""
    if not isinstance(operations, list) or not operations:
        raise ValueError("sync transaction requires operations")
    backups: list[tuple[Path, Path, int]] = []
    created_files: list[Path] = []
    created_directories: list[Path] = []
    try:
        for operation in operations:
            if not isinstance(operation, dict) or not {"path", "content"} <= set(operation):
                raise ValueError("sync operation fields are invalid")
            target = Path(operation["path"])
            if operation.get("create"):
                if target.exists() or target.is_symlink():
                    raise FileExistsError(f"create target already exists: {target}")
                continue
            metadata = _regular_file(target, "sync target")
            backup = create_secure_backup(target, backup_dir, sensitive=bool(operation.get("sensitive", False)))
            backups.append((target, backup, stat.S_IMODE(metadata.st_mode)))
        for operation in operations:
            if operation.get("inject_failure"):
                raise RuntimeError("injected sync failure")
            target = Path(operation["path"])
            if operation.get("create"):
                directories = _create_parent_directories(target.parent)
                created_directories.extend(directories)
                atomic_create(target, operation["content"], mode=operation.get("mode", 0o644))
                created_files.append(target)
            else:
                atomic_replace(target, operation["content"], mode=operation.get("mode"))
        if verify is not None:
            verify()
    except BaseException:
        for target, backup, original_mode in reversed(backups):
            atomic_replace(target, backup.read_bytes(), mode=original_mode)
        for target in reversed(created_files):
            target.unlink(missing_ok=True)
        for directory in reversed(created_directories):
            try:
                directory.rmdir()
            except OSError:
                pass
        raise
    return [backup for _, backup, _ in backups]


def cleanup_success_artifacts(backup_paths, temporary_paths):
    """Remove successful-run backup and temporary regular files."""
    for path in [*backup_paths, *temporary_paths]:
        candidate = Path(path)
        if not candidate.exists():
            continue
        _regular_file(candidate, "cleanup artifact")
        candidate.unlink()
    return True


def validate_grok_discovery(inspect_output, expected_skills, expected_root):
    """Validate ``grok inspect --json`` skill names and canonical paths."""
    try:
        payload = json.loads(inspect_output)
    except (TypeError, json.JSONDecodeError) as exc:
        raise ValueError("invalid grok inspect JSON") from exc
    skills = payload.get("skills")
    if not isinstance(skills, list):
        raise ValueError("grok inspect JSON has no skills list")
    expected_root_text = os.path.normpath(os.fspath(expected_root))
    found: dict[str, str] = {}
    for skill in skills:
        if not isinstance(skill, dict) or not isinstance(skill.get("source"), dict):
            continue
        if skill["source"].get("type") != "user":
            continue
        found[skill.get("name")] = os.path.normpath(str(skill["source"].get("path", "")))
    for name in expected_skills:
        expected = os.path.join(expected_root_text, name, "SKILL.md")
        if found.get(name) != expected:
            raise ValueError(f"grok discovery missing expected skill path: {name}")
    return True


def validate_antigravity_discovery(runtime_root, expected_skills, file_records):
    """Validate Antigravity root and deterministic portable-file closure."""
    root = Path(runtime_root)
    if not root.exists() or not root.is_dir() or root.is_symlink():
        raise ValueError(f"invalid antigravity runtime root: {root}")
    if set(file_records) != set(expected_skills):
        raise ValueError("antigravity discovery records do not match expected skills")
    for name in expected_skills:
        if not _nonblank(name) or "/" in name or "\\" in name:
            raise ValueError("invalid skill name")
        skill_root = root / name
        if not skill_root.is_dir() or skill_root.is_symlink():
            raise ValueError(f"missing antigravity skill directory: {name}")
        for record in file_records[name]:
            if not isinstance(record, dict) or "path" not in record:
                raise ValueError(f"invalid discovery record for skill: {name}")
            path = validate_relative_path(skill_root, record["path"])
            digest = record.get("sha256")
            if digest is not None and _sha256(path) != digest:
                raise ValueError(f"antigravity portable drift: {name}/{record['path']}")
    return True


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _absolute_without_symlink_resolution(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _contained(root: Path, candidate: Path, label: str) -> Path:
    resolved_root = root.resolve(strict=True)
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"{label} escapes declared root: {candidate}") from exc
    return candidate


def _target_arguments(args) -> dict[str, dict[str, str]]:
    return {
        "codex": {
            "skills_root": str(args.codex_skills_root.resolve()),
            "rule_file": str(args.codex_rule_file.resolve()),
        },
        "antigravity-cli": {
            "skills_root": str(args.antigravity_skills_root.resolve()),
            "rule_file": str(args.antigravity_rule_file.resolve()),
        },
        "grok-cli": {
            "skills_root": str(args.grok_skills_root.resolve()),
            "rule_file": str(args.grok_rule_file.resolve()),
        },
    }


def generate_plan(args) -> dict:
    manifest_path = args.manifest.resolve(strict=True)
    manifest = _load_json(manifest_path)
    validate_manifest(manifest)
    sources = {
        "openspec": args.openspec_source.resolve(strict=True),
        "brief": args.brief_source.resolve(strict=True),
    }
    for alias, root in sources.items():
        if not root.is_dir() or root.is_symlink():
            raise ValueError(f"invalid {alias} source root: {root}")
    target_paths = _target_arguments(args)
    target_states = {item["id"]: dict(item) for item in manifest["targets"]}
    targets: dict[str, dict] = {}
    for target_id, paths in target_paths.items():
        skills_root = Path(paths["skills_root"])
        rule_file = Path(paths["rule_file"])
        if not skills_root.is_dir() or skills_root.is_symlink():
            raise ValueError(f"invalid target skill root: {target_id}")
        _regular_file(rule_file, f"{target_id} global rule file")
        targets[target_id] = {**target_states[target_id], **paths, "files": []}
    for skill in manifest["skills"]:
        source_root = sources[skill["source_alias"]]
        for item in skill["files"]:
            source = validate_relative_path(source_root, item["path"])
            digest = _sha256(source)
            for target_id in item["targets"]:
                targets[target_id]["files"].append(
                    {
                        "skill": skill["name"],
                        "source_alias": skill["source_alias"],
                        "path": item["path"],
                        "sha256": digest,
                    }
                )
    rules = manifest["managed_rules"]
    rule_source = validate_relative_path(sources["openspec"], rules["source"])
    return {
        "schema_version": 1,
        "manifest_path": str(manifest_path),
        "manifest_sha256": _sha256(manifest_path),
        "sources": {alias: str(root) for alias, root in sources.items()},
        "managed_rules": {
            "version": rules["version"],
            "source_alias": "openspec",
            "path": rules["source"],
            "sha256": _sha256(rule_source),
            "invariant_ids": rules["invariant_ids"],
        },
        "targets": targets,
    }


def _validate_plan(plan: dict) -> dict:
    required = {"schema_version", "manifest_path", "manifest_sha256", "sources", "managed_rules", "targets"}
    if not isinstance(plan, dict) or set(plan) != required or plan["schema_version"] != 1:
        raise ValueError("sync plan fields or schema are invalid")
    manifest_path = Path(plan["manifest_path"])
    if _sha256(validate_relative_path(manifest_path.parent, manifest_path.name)) != plan["manifest_sha256"]:
        raise ValueError("sync plan manifest SHA-256 drift")
    manifest = _load_json(manifest_path)
    validate_manifest(manifest)
    if set(plan["sources"]) != {"openspec", "brief"} or set(plan["targets"]) != TARGET_IDS:
        raise ValueError("sync plan sources or targets are invalid")
    source_roots = {alias: Path(root) for alias, root in plan["sources"].items()}
    for root in source_roots.values():
        path = Path(root)
        if not path.is_dir() or path.is_symlink():
            raise ValueError(f"invalid source root in plan: {path}")
    rules = manifest["managed_rules"]
    rule_source = validate_relative_path(source_roots["openspec"], rules["source"])
    expected_rules = {
        "version": rules["version"],
        "source_alias": "openspec",
        "path": rules["source"],
        "sha256": _sha256(rule_source),
        "invariant_ids": rules["invariant_ids"],
    }
    if plan["managed_rules"] != expected_rules:
        raise ValueError("sync plan managed-rule binding is stale or tampered")
    manifest_targets = {item["id"]: item for item in manifest["targets"]}
    state_fields = set(next(iter(manifest_targets.values())))
    for target_id, target in plan["targets"].items():
        if not isinstance(target, dict) or set(target) != state_fields | {"skills_root", "rule_file", "files"}:
            raise ValueError(f"sync plan target fields are invalid: {target_id}")
        if {key: target[key] for key in state_fields} != manifest_targets[target_id]:
            raise ValueError(f"sync plan target state is stale or tampered: {target_id}")
        skills_root = Path(target["skills_root"])
        if not skills_root.is_dir() or skills_root.is_symlink():
            raise ValueError(f"invalid target skill root in plan: {target_id}")
        _regular_file(Path(target["rule_file"]), f"{target_id} global rule file")
        expected_files = []
        for skill in manifest["skills"]:
            for item in skill["files"]:
                if target_id not in item["targets"]:
                    continue
                source = validate_relative_path(source_roots[skill["source_alias"]], item["path"])
                expected_files.append(
                    {
                        "skill": skill["name"],
                        "source_alias": skill["source_alias"],
                        "path": item["path"],
                        "sha256": _sha256(source),
                    }
                )
        if target["files"] != expected_files:
            raise ValueError(f"sync plan portable-file binding is stale or tampered: {target_id}")
    return plan


def _read_plan(path: Path) -> dict:
    return _validate_plan(_load_json(path.resolve(strict=True)))


def _target_records(plan: dict, target_id: str) -> dict[str, list[dict]]:
    records: dict[str, list[dict]] = {}
    for item in plan["targets"][target_id]["files"]:
        records.setdefault(item["skill"], []).append(
            {"path": item["path"], "sha256": item["sha256"]}
        )
    return records


def apply_target(plan: dict, target_id: str, backup_root: Path) -> list[Path]:
    if target_id not in TARGET_IDS:
        raise ValueError(f"unknown target: {target_id}")
    target = plan["targets"][target_id]
    skills_root = Path(target["skills_root"])
    if not skills_root.is_dir() or skills_root.is_symlink():
        raise ValueError(f"invalid target skill root: {target_id}")
    operations = []
    for item in target["files"]:
        source_root = Path(plan["sources"][item["source_alias"]])
        source = validate_relative_path(source_root, item["path"])
        if _sha256(source) != item["sha256"]:
            raise ValueError(f"source SHA-256 drift: {item['skill']}/{item['path']}")
        destination = skills_root / item["skill"] / Path(item["path"])
        _contained(skills_root, destination, "skill destination")
        if destination.exists() or destination.is_symlink():
            _regular_file(destination, "portable target")
            create = False
        else:
            create = True
        operations.append({"path": destination, "content": source.read_bytes(), "create": create})
    rule = plan["managed_rules"]
    rule_source = validate_relative_path(Path(plan["sources"][rule["source_alias"]]), rule["path"])
    if _sha256(rule_source) != rule["sha256"]:
        raise ValueError("managed-rule source SHA-256 drift")
    rule_file = Path(target["rule_file"])
    _regular_file(rule_file, "global rule target")
    original = rule_file.read_text(encoding="utf-8")
    updated = install_managed_block(original, rule_source.read_text(encoding="utf-8"), version=rule["version"])
    operations.append({"path": rule_file, "content": updated.encode("utf-8"), "sensitive": True})
    return apply_sync_transaction(
        operations,
        backup_root / target_id,
        verify=lambda: verify_target(plan, target_id),
    )


def verify_target(plan: dict, target_id: str) -> bool:
    if target_id not in TARGET_IDS:
        raise ValueError(f"unknown target: {target_id}")
    target = plan["targets"][target_id]
    skills_root = Path(target["skills_root"])
    for skill, records in _target_records(plan, target_id).items():
        source_alias = next(item["source_alias"] for item in target["files"] if item["skill"] == skill)
        validate_portable_parity(
            Path(plan["sources"][source_alias]), skills_root / skill, records
        )
    rule = plan["managed_rules"]
    canonical = validate_relative_path(Path(plan["sources"][rule["source_alias"]]), rule["path"]).read_text(encoding="utf-8")
    rule_text = Path(target["rule_file"]).read_text(encoding="utf-8")
    validate_managed_rule_parity(
        canonical,
        rule_text,
        version=rule["version"],
        invariant_ids=rule["invariant_ids"],
    )
    return True


def audit_sources(source_roots) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    content_patterns = (
        ("private-key", re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
        ("assigned-secret", re.compile(rb"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"][A-Za-z0-9_./+\-=]{16,}")),
    )
    for root in source_roots:
        root_path = Path(root).resolve(strict=True)
        for path in root_path.rglob("*"):
            if ".git" in path.parts or not path.is_file() or path.is_symlink():
                continue
            relative = path.relative_to(root_path).as_posix()
            category = _denied_category(relative)
            if category:
                findings.append({"path": relative, "category": category})
                continue
            data = path.read_bytes()
            for label, pattern in content_patterns:
                if pattern.search(data):
                    findings.append({"path": relative, "category": label})
    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    plan = commands.add_parser("plan")
    plan.add_argument("--manifest", type=Path, required=True)
    plan.add_argument("--openspec-source", type=Path, required=True)
    plan.add_argument("--brief-source", type=Path, required=True)
    for prefix in ("codex", "antigravity", "grok"):
        plan.add_argument(f"--{prefix}-skills-root", type=Path, required=True)
        plan.add_argument(f"--{prefix}-rule-file", type=Path, required=True)
    plan.add_argument("--output", type=Path, required=True)

    for name in ("apply", "verify"):
        command = commands.add_parser(name)
        command.add_argument("--target", choices=sorted(TARGET_IDS), required=True)
        command.add_argument("--plan", type=Path, required=True)
        if name == "apply":
            command.add_argument("--backup-root", type=Path, required=True)

    verify_all = commands.add_parser("verify-all")
    verify_all.add_argument("--plan", type=Path, required=True)

    discovery = commands.add_parser("verify-discovery")
    discovery.add_argument("--target", choices=["grok-cli"], required=True)
    discovery.add_argument("--inspect-json", type=Path, required=True)
    discovery.add_argument("--plan", type=Path, required=True)
    discovery.add_argument("--consume", action="store_true")

    audit = commands.add_parser("audit")
    audit.add_argument("--openspec-source", type=Path, required=True)
    audit.add_argument("--brief-source", type=Path, required=True)
    audit.add_argument("--report-paths-only", action="store_true", required=True)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "plan":
            output = _absolute_without_symlink_resolution(args.output)
            _create_parent_directories(output.parent)
            plan = generate_plan(args)
            content = (json.dumps(plan, indent=2, sort_keys=True) + "\n").encode("utf-8")
            if output.exists() or output.is_symlink():
                _regular_file(output, "sync plan output")
                atomic_replace(output, content, mode=0o600)
            else:
                atomic_create(output, content, mode=0o600)
            print(json.dumps({"plan": "pass", "output": str(output)}, sort_keys=True))
        elif args.command == "apply":
            plan = _read_plan(args.plan)
            backups = apply_target(plan, args.target, args.backup_root.resolve())
            print(json.dumps({"apply": "pass", "target": args.target, "backup_count": len(backups)}, sort_keys=True))
        elif args.command == "verify":
            verify_target(_read_plan(args.plan), args.target)
            print(json.dumps({"verify": "pass", "target": args.target}, sort_keys=True))
        elif args.command == "verify-all":
            plan = _read_plan(args.plan)
            for target_id, target in plan["targets"].items():
                if target["selection"] == "required":
                    verify_target(plan, target_id)
            print(json.dumps({"verify_all": "pass", "targets": sorted(plan["targets"])}, sort_keys=True))
        elif args.command == "verify-discovery":
            plan = _read_plan(args.plan)
            inspect_path = _absolute_without_symlink_resolution(args.inspect_json)
            metadata = _regular_file(inspect_path, "Grok inspect artifact")
            if stat.S_IMODE(metadata.st_mode) != 0o600:
                raise ValueError("Grok inspect artifact must use mode 0600")
            records = _target_records(plan, "grok-cli")
            validate_grok_discovery(
                inspect_path.read_text(encoding="utf-8"),
                sorted(records),
                plan["targets"]["grok-cli"]["skills_root"],
            )
            if args.consume:
                inspect_path.unlink()
            print(json.dumps({"discovery": "pass", "target": "grok-cli", "consumed": args.consume}, sort_keys=True))
        elif args.command == "audit":
            findings = audit_sources([args.openspec_source, args.brief_source])
            for finding in findings:
                print(f"{finding['category']}: {finding['path']}")
            if findings:
                raise ValueError(f"{len(findings)} sensitive categories found")
            print("0 sensitive categories found")
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"cross-cli sync validation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
