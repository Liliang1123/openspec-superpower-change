from __future__ import annotations

import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts import validate_cross_cli_sync as sync


SKILLS = ["openspec-superpower-change", "codex-brief-antigravity-review"]
INVARIANTS = [f"CCG-{number:03d}" for number in range(1, 9)]


def required_target(target_id: str, result: str = "pass") -> dict:
    return {
        "id": target_id,
        "selection": "required",
        "result": result,
        "decision_owner": "codex",
        "evidence": f"evidence/{target_id}.json",
        "reason": "selected collaboration runtime",
        "resume_condition": "rerun parity and discovery checks",
    }


def portable_manifest() -> dict:
    return {
        "schema_version": 1,
        "skills": [
            {
                "name": SKILLS[0],
                "source_alias": "openspec",
                "files": [
                    {"path": "SKILL.md", "targets": ["codex", "antigravity-cli", "grok-cli"]},
                    {
                        "path": "references/cross-cli-sync.md",
                        "targets": ["codex", "antigravity-cli", "grok-cli"],
                    },
                    {
                        "path": "scripts/validate_core_gates.py",
                        "targets": ["codex", "antigravity-cli", "grok-cli"],
                    },
                ],
            },
            {
                "name": SKILLS[1],
                "source_alias": "brief",
                "files": [
                    {"path": "SKILL.md", "targets": ["codex", "antigravity-cli", "grok-cli"]}
                ],
            },
        ],
        "managed_rules": {
            "version": 1,
            "source": "references/shared-global-governance.md",
            "invariant_ids": INVARIANTS,
        },
        "targets": [
            required_target("codex"),
            required_target("antigravity-cli"),
            required_target("grok-cli"),
        ],
    }


class ManifestAndTriggerTests(unittest.TestCase):
    def test_portable_manifest_accepts_only_declared_schema(self):
        self.assertEqual(sync.validate_manifest(portable_manifest()), portable_manifest())

    def test_manifest_accepts_version_2_tiered_governance_invariants(self):
        manifest = portable_manifest()
        manifest["managed_rules"]["version"] = 2
        manifest["managed_rules"]["invariant_ids"] = [
            f"CCG-{number:03d}" for number in range(1, 14)
        ]
        self.assertEqual(sync.validate_manifest(manifest), manifest)

    def test_manifest_rejects_sensitive_categories(self):
        for denied in (
            "auth.json",
            "tokens/access-token",
            "sessions/current.json",
            "history/events.json",
            "logs/sync.log",
            "cache/index",
            "model-settings.json",
            "settings.json",
            "hooks/pre-run.sh",
            "mcp/credentials.json",
            "bin/agent",
            ".env",
            "keys/client.pem",
        ):
            with self.subTest(denied=denied):
                manifest = portable_manifest()
                manifest["skills"][0]["files"].append(
                    {"path": denied, "targets": ["codex"]}
                )
                with self.assertRaisesRegex(ValueError, "denied"):
                    sync.validate_manifest(manifest)

    def test_trigger_requires_sync_for_any_portable_or_shared_rule_change(self):
        for changed in (
            ["SKILL.md"],
            ["references/cross-cli-sync.md"],
            ["references/shared-global-governance.md"],
            ["references/cross-cli-portable-manifest.json"],
        ):
            with self.subTest(changed=changed):
                self.assertTrue(sync.classify_sync_trigger(changed, portable_manifest()))

    def test_repository_only_changes_do_not_trigger_runtime_sync(self):
        changed = [
            "README.md",
            "CHANGELOG.md",
            "tests/test_cross_cli_sync.py",
            "docs/design/history.md",
            "openspec/changes/archive/change/proposal.md",
        ]
        self.assertFalse(sync.classify_sync_trigger(changed, portable_manifest()))

    def test_companion_validator_metadata_is_portable_to_every_required_runtime(self):
        manifest = json.loads(
            (Path(__file__).parents[1] / "references" / "cross-cli-portable-manifest.json")
            .read_text(encoding="utf-8")
        )
        metadata = [
            item
            for skill in manifest["skills"]
            if skill["name"] == "codex-brief-antigravity-review"
            for item in skill["files"]
            if item["path"] == "agents/openai.yaml"
        ]
        self.assertEqual(len(metadata), 1)
        self.assertEqual(set(metadata[0]["targets"]), {"codex", "antigravity-cli", "grok-cli"})


class PathAndParityTests(unittest.TestCase):
    def test_path_validation_rejects_absolute_traversal_url_and_backslash(self):
        with tempfile.TemporaryDirectory() as tmp:
            for unsafe in (
                "/tmp/escape",
                "../escape",
                "references/../escape",
                "https://example.invalid/file",
                "C:/secret",
                "references\\escape.md",
                "references//empty.md",
                "references/./dot.md",
                "references/nul\0.md",
            ):
                with self.subTest(unsafe=unsafe):
                    with self.assertRaises(ValueError):
                        sync.validate_relative_path(Path(tmp), unsafe)

    def test_path_validation_rejects_symlink_escape_and_non_regular_file(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            root = Path(tmp)
            outside_file = Path(outside) / "secret"
            outside_file.write_text("do not disclose", encoding="utf-8")
            (root / "escape").symlink_to(outside_file)
            (root / "directory").mkdir()
            for candidate in ("escape", "directory"):
                with self.subTest(candidate=candidate):
                    with self.assertRaises(ValueError):
                        sync.validate_relative_path(root, candidate)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO is not supported")
    def test_path_validation_rejects_fifo(self):
        with tempfile.TemporaryDirectory() as tmp:
            fifo = Path(tmp) / "pipe"
            os.mkfifo(fifo)
            with self.assertRaises(ValueError):
                sync.validate_relative_path(Path(tmp), "pipe")

    def test_portable_manifest_records_relative_sha256(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("portable\n", encoding="utf-8")
            records = sync.build_portable_manifest(root, ["SKILL.md"])
            self.assertEqual(records[0]["path"], "SKILL.md")
            self.assertRegex(records[0]["sha256"], r"^[0-9a-f]{64}$")

    def test_portable_parity_rejects_missing_stale_and_extra_files(self):
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as target_tmp:
            source = Path(source_tmp)
            target = Path(target_tmp)
            (source / "SKILL.md").write_text("current\n", encoding="utf-8")
            records = [{"path": "SKILL.md", "sha256": "0" * 64}]
            with self.assertRaises(ValueError):
                sync.validate_portable_parity(source, target, records)


class ManagedMarkerTests(unittest.TestCase):
    def setUp(self):
        self.body = "\n".join(f"- [{item}] invariant" for item in INVARIANTS) + "\n"
        self.start = sync.MANAGED_BLOCK_START.format(version=1)
        self.end = sync.MANAGED_BLOCK_END.format(version=1)

    def test_extract_rejects_missing_duplicate_mismatched_and_nested_markers(self):
        invalid = [
            "native only\n",
            f"{self.start}\na\n{self.end}\n{self.start}\nb\n{self.end}\n",
            f"{self.start}\na\n{sync.MANAGED_BLOCK_END.format(version=2)}\n",
            f"{self.start}\n{self.start}\na\n{self.end}\n{self.end}\n",
        ]
        for text in invalid:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    sync.extract_managed_block(text, version=1)

    def test_marker_replacement_preserves_every_outside_byte(self):
        prefix = "native-prefix\r\n"
        suffix = "native-suffix\r\n"
        original = f"{prefix}{self.start}\r\nold\r\n{self.end}\r\n{suffix}"
        replaced = sync.replace_managed_block(original, self.body, version=1)
        self.assertTrue(replaced.startswith(prefix + self.start))
        self.assertTrue(replaced.endswith(self.end + "\r\n" + suffix))

    def test_first_install_appends_one_block_and_preserves_native_prefix_bytes(self):
        original = "native-prefix\r\nnative-suffix"
        installed = sync.install_managed_block(original, self.body, version=1)
        self.assertEqual(installed[: len(original)], original)
        self.assertEqual(installed.count(self.start), 1)
        self.assertEqual(installed.count(self.end), 1)
        self.assertTrue(
            sync.validate_managed_rule_parity(
                self.body, installed, version=1, invariant_ids=INVARIANTS
            )
        )

    def test_version_upgrade_replaces_markers_and_preserves_outside_bytes(self):
        v2_ids = [f"CCG-{number:03d}" for number in range(1, 14)]
        v2_body = "\n".join(f"- [{item}] invariant" for item in v2_ids) + "\n"
        prefix = "native-prefix\r\n"
        suffix = "native-suffix\r\n"
        original = f"{prefix}{self.start}\r\n{self.body}{self.end}\r\n{suffix}"
        upgraded = sync.install_managed_block(original, v2_body, version=2)
        v2_start = sync.MANAGED_BLOCK_START.format(version=2)
        v2_end = sync.MANAGED_BLOCK_END.format(version=2)
        self.assertTrue(upgraded.startswith(prefix + v2_start))
        self.assertTrue(upgraded.endswith(v2_end + "\r\n" + suffix))
        self.assertNotIn(self.start, upgraded)
        self.assertNotIn(self.end, upgraded)
        self.assertTrue(sync.validate_managed_rule_parity(
            v2_body, upgraded, version=2, invariant_ids=v2_ids
        ))

    def test_first_install_rejects_partial_or_mismatched_existing_marker(self):
        for original in (
            f"native\n{self.start}\npartial\n",
            f"native\n{sync.MANAGED_BLOCK_START.format(version=2)}\nold\n"
            f"{sync.MANAGED_BLOCK_END.format(version=2)}\n",
            f"{self.start}\n{self.body}{self.end}\n"
            f"{sync.MANAGED_BLOCK_START.format(version=2)}\nold\n"
            f"{sync.MANAGED_BLOCK_END.format(version=2)}\n",
        ):
            with self.subTest(original=original):
                with self.assertRaises(ValueError):
                    sync.install_managed_block(original, self.body, version=1)

    def test_managed_rule_parity_requires_body_hash_and_all_invariants(self):
        target = f"native\n{self.start}\n{self.body}{self.end}\noverlay\n"
        self.assertTrue(
            sync.validate_managed_rule_parity(
                self.body, target, version=1, invariant_ids=INVARIANTS
            )
        )
        with self.assertRaises(ValueError):
            sync.validate_managed_rule_parity(
                self.body,
                target.replace("CCG-008", "CCG-999"),
                version=1,
                invariant_ids=INVARIANTS,
            )


class TargetStateTests(unittest.TestCase):
    def test_all_required_targets_must_pass(self):
        self.assertTrue(
            sync.validate_target_states(
                [required_target(target_id) for target_id in ("codex", "antigravity-cli", "grok-cli")]
            )
        )

    def test_failed_required_target_cannot_be_mislabeled_not_applicable(self):
        target = required_target("grok-cli", "blocked")
        target["selection"] = "not-applicable"
        target["reason"] = "discovery failed"
        with self.assertRaises(ValueError):
            sync.validate_target_states([target])

    def test_not_applicable_requires_owner_evidence_reason_and_resume_condition(self):
        valid = {
            "id": "grok-cli",
            "selection": "not-applicable",
            "result": "not-applicable",
            "decision_owner": "codex",
            "evidence": "evidence/grok-not-installed.json",
            "reason": "CLI is not installed",
            "resume_condition": "install Grok CLI and redeclare it required",
        }
        self.assertTrue(sync.validate_target_states([valid]))
        for field in ("decision_owner", "evidence", "reason", "resume_condition"):
            with self.subTest(field=field):
                invalid = dict(valid)
                invalid[field] = ""
                with self.assertRaises(ValueError):
                    sync.validate_target_states([invalid])


class BackupAtomicAndCleanupTests(unittest.TestCase):
    def test_sensitive_backup_is_0600_and_outside_discovery_root(self):
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as backup_tmp:
            source = Path(source_tmp) / "AGENTS.md"
            source.write_text("private native overlay\n", encoding="utf-8")
            backup = sync.create_secure_backup(source, Path(backup_tmp), sensitive=True)
            self.assertEqual(stat.S_IMODE(backup.stat().st_mode), 0o600)
            self.assertFalse(str(backup).startswith(str(source.parent / "skills")))

    def test_backup_root_symlink_cannot_redirect_into_skill_discovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "AGENTS.md"
            source.write_text("native rules\n", encoding="utf-8")
            discovery = root / "runtime" / "skills" / "hidden-backups"
            discovery.mkdir(parents=True)
            redirected = root / "backup-link"
            redirected.symlink_to(discovery, target_is_directory=True)
            with self.assertRaises(ValueError):
                sync.create_secure_backup(source, redirected, sensitive=True)

    def test_atomic_replace_preserves_live_mode_and_leaves_no_temp_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "AGENTS.md"
            target.write_text("old\n", encoding="utf-8")
            target.chmod(0o644)
            sync.atomic_replace(target, b"new\n")
            self.assertEqual(target.read_bytes(), b"new\n")
            self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o644)
            self.assertEqual(list(Path(tmp).glob(".cross-cli-sync.*")), [])

    def test_transaction_rolls_back_prior_replacements_after_midway_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = root / "first.md"
            second = root / "second.md"
            first.write_text("first-old\n", encoding="utf-8")
            second.write_text("second-old\n", encoding="utf-8")
            operations = [
                {"path": first, "content": b"first-new\n"},
                {"path": second, "content": b"second-new\n", "inject_failure": True},
            ]
            with self.assertRaisesRegex(RuntimeError, "injected sync failure"):
                sync.apply_sync_transaction(operations, root / "backups")
            self.assertEqual(first.read_text(encoding="utf-8"), "first-old\n")
            self.assertEqual(second.read_text(encoding="utf-8"), "second-old\n")

    def test_transaction_rolls_back_only_files_and_directories_it_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / "existing"
            existing.mkdir()
            created = existing / "new-skill" / "references" / "rule.md"
            operations = [
                {"path": created, "content": b"portable\n", "create": True},
                {
                    "path": root / "failure.md",
                    "content": b"never-written\n",
                    "create": True,
                    "inject_failure": True,
                },
            ]
            with self.assertRaisesRegex(RuntimeError, "injected sync failure"):
                sync.apply_sync_transaction(operations, root / "backups")
            self.assertTrue(existing.is_dir())
            self.assertFalse((existing / "new-skill").exists())
            self.assertFalse((root / "failure.md").exists())

    def test_transaction_creates_missing_regular_file_without_overwriting(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "skill" / "SKILL.md"
            backups = sync.apply_sync_transaction(
                [{"path": target, "content": b"created\n", "create": True}],
                root / "backups",
            )
            self.assertEqual(backups, [])
            self.assertEqual(target.read_bytes(), b"created\n")
            with self.assertRaises((FileExistsError, ValueError)):
                sync.apply_sync_transaction(
                    [{"path": target, "content": b"overwrite\n", "create": True}],
                    root / "other-backups",
                )

    def test_transaction_rolls_back_when_post_apply_verification_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / "existing.md"
            created = root / "new-skill" / "SKILL.md"
            existing.write_text("old\n", encoding="utf-8")

            def fail_verification():
                raise ValueError("post-apply parity failure")

            with self.assertRaisesRegex(ValueError, "post-apply parity failure"):
                sync.apply_sync_transaction(
                    [
                        {"path": existing, "content": b"new\n"},
                        {"path": created, "content": b"created\n", "create": True},
                    ],
                    root / "backups",
                    verify=fail_verification,
                )
            self.assertEqual(existing.read_text(encoding="utf-8"), "old\n")
            self.assertFalse((root / "new-skill").exists())

    def test_success_cleanup_removes_backups_and_temporary_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            backup = Path(tmp) / "backup"
            temporary = Path(tmp) / ".cross-cli-sync.temp"
            backup.write_text("backup", encoding="utf-8")
            temporary.write_text("temporary", encoding="utf-8")
            sync.cleanup_success_artifacts([backup], [temporary])
            self.assertFalse(backup.exists())
            self.assertFalse(temporary.exists())

    def test_diagnostics_never_disclose_sensitive_file_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            secret = "SENSITIVE_SENTINEL_VALUE"
            denied = Path(tmp) / "auth.json"
            denied.write_text(secret, encoding="utf-8")
            with self.assertRaises(ValueError) as caught:
                sync.build_portable_manifest(Path(tmp), ["auth.json"])
            self.assertNotIn(secret, str(caught.exception))


class DiscoveryTests(unittest.TestCase):
    def test_grok_inspect_requires_both_skills_from_expected_user_root(self):
        root = "/home/user/.grok/skills"
        payload = {
            "skills": [
                {
                    "name": name,
                    "source": {"type": "user", "path": f"{root}/{name}/SKILL.md"},
                }
                for name in SKILLS
            ]
        }
        self.assertTrue(sync.validate_grok_discovery(json.dumps(payload), SKILLS, root))

    def test_grok_discovery_rejects_wrong_or_missing_skill_path(self):
        payload = {
            "skills": [
                {
                    "name": SKILLS[0],
                    "source": {"type": "project", "path": "/tmp/wrong/SKILL.md"},
                }
            ]
        }
        with self.assertRaises(ValueError):
            sync.validate_grok_discovery(
                json.dumps(payload), SKILLS, "/home/user/.grok/skills"
            )

    def test_antigravity_discovery_uses_deterministic_manifest_closure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            records = {}
            for name in SKILLS:
                skill = root / name
                skill.mkdir()
                (skill / "SKILL.md").write_text(f"name: {name}\n", encoding="utf-8")
                records[name] = [{"path": "SKILL.md"}]
            self.assertTrue(sync.validate_antigravity_discovery(root, SKILLS, records))


class CrossCliForwardTests(unittest.TestCase):
    def test_premature_completion_is_blocked_until_all_required_targets_pass(self):
        targets = [
            required_target("codex"),
            required_target("antigravity-cli"),
            required_target("grok-cli", "pending"),
        ]
        with self.assertRaises(ValueError):
            sync.validate_target_states(targets)

    def test_auxiliary_self_approval_cannot_complete_sync(self):
        with self.assertRaises(ValueError):
            sync.validate_completion_authority(
                {
                    "decision_owner": "antigravity-cli",
                    "reviewer_agent": "antigravity-cli",
                    "result": "pass",
                }
            )

    def test_missing_grok_sync_blocks_completion(self):
        with self.assertRaises(ValueError):
            sync.validate_target_states(
                [required_target("codex"), required_target("antigravity-cli")]
            )

    def test_stale_antigravity_files_block_completion(self):
        with tempfile.TemporaryDirectory() as source_tmp, tempfile.TemporaryDirectory() as target_tmp:
            source = Path(source_tmp)
            target = Path(target_tmp)
            (source / "SKILL.md").write_text("source\n", encoding="utf-8")
            (target / "SKILL.md").write_text("stale\n", encoding="utf-8")
            records = sync.build_portable_manifest(source, ["SKILL.md"])
            with self.assertRaises(ValueError):
                sync.validate_portable_parity(source, target, records)

    def test_credential_copying_is_rejected(self):
        manifest = portable_manifest()
        manifest["skills"][0]["files"].append(
            {"path": "auth/token.json", "targets": ["grok-cli"]}
        )
        with self.assertRaisesRegex(ValueError, "denied"):
            sync.validate_manifest(manifest)


class CliContractTests(unittest.TestCase):
    def test_cli_exposes_the_executable_sync_contract(self):
        result = subprocess.run(
            [sys.executable, str(Path(sync.__file__)), "--help"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in (
            "plan", "apply", "verify", "verify-all", "verify-discovery", "audit"
        ):
            self.assertIn(command, result.stdout)

    def test_plan_apply_and_verify_round_trip_in_isolated_runtimes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            openspec = root / "openspec"
            brief = root / "brief"
            openspec.mkdir()
            brief.mkdir()
            for relative in (
                "SKILL.md",
                "references/cross-cli-sync.md",
                "scripts/validate_core_gates.py",
            ):
                path = openspec / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f"portable {relative}\n", encoding="utf-8")
            (brief / "SKILL.md").write_text("portable brief\n", encoding="utf-8")
            managed = openspec / "references" / "shared-global-governance.md"
            managed.write_text(
                "\n".join(f"- [{item}] invariant" for item in INVARIANTS) + "\n",
                encoding="utf-8",
            )
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps(portable_manifest()), encoding="utf-8")
            target_args = []
            for cli in ("codex", "antigravity", "grok"):
                runtime = root / cli
                skills = runtime / "skills"
                skills.mkdir(parents=True)
                rule = runtime / "RULES.md"
                rule.write_text(f"native-{cli}\n", encoding="utf-8")
                target_args.extend(
                    [f"--{cli}-skills-root", str(skills), f"--{cli}-rule-file", str(rule)]
                )
            plan = root / "sync-plan.json"
            script = str(Path(sync.__file__))
            plan_result = subprocess.run(
                [
                    sys.executable,
                    script,
                    "plan",
                    "--manifest",
                    str(manifest),
                    "--openspec-source",
                    str(openspec),
                    "--brief-source",
                    str(brief),
                    *target_args,
                    "--output",
                    str(plan),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(plan_result.returncode, 0, plan_result.stderr)
            for target in ("codex", "antigravity-cli", "grok-cli"):
                apply_result = subprocess.run(
                    [
                        sys.executable,
                        script,
                        "apply",
                        "--target",
                        target,
                        "--plan",
                        str(plan),
                        "--backup-root",
                        str(root / "backups"),
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(apply_result.returncode, 0, apply_result.stderr)
                verify_result = subprocess.run(
                    [sys.executable, script, "verify", "--target", target, "--plan", str(plan)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(verify_result.returncode, 0, verify_result.stderr)
            verify_all = subprocess.run(
                [sys.executable, script, "verify-all", "--plan", str(plan)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(verify_all.returncode, 0, verify_all.stderr)

            tampered = json.loads(plan.read_text(encoding="utf-8"))
            tampered["targets"]["grok-cli"]["files"].pop()
            plan.write_text(json.dumps(tampered), encoding="utf-8")
            rejected = subprocess.run(
                [sys.executable, script, "verify-all", "--plan", str(plan)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("plan", rejected.stderr.lower())


if __name__ == "__main__":
    unittest.main()
