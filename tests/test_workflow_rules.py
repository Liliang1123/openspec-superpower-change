import importlib.util
import os
import hashlib
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF_ROOT = Path(os.environ.get(
    "BRIEF_SKILL_SOURCE", ROOT.parent / "codex-brief-antigravity-review"
)).resolve()
BRIEF_HANDOFF = BRIEF_ROOT / "references" / "handoff-contract.md"


def artifact(path: str) -> dict[str, str]:
    return {"path": path, "sha256": "a" * 64}


def evidence_manifest(
    role: str,
    result: str,
    change_id: str = "add-example-change",
    current_batch: int = 1,
    attempt: int = 1,
    contract_revision: int = 1,
    canonical_sha256: str = "b" * 64,
    agent_identity: str | None = None,
    agent_role: str | None = None,
) -> str:
    if agent_identity is None or agent_role is None:
        defaults = {
            "attempt-report": ("antigravity-cli", "executor"),
            "batch-review": ("grok-cli", "independent-reviewer"),
            "preflight-review": ("codex", "decision-owner"),
            "timeout-audit": ("codex", "decision-owner"),
            "final-verification": ("codex", "decision-owner"),
            "final-review": ("codex", "decision-owner"),
        }
        default_identity, default_role = defaults[role]
        agent_identity = agent_identity or default_identity
        agent_role = agent_role or default_role
    return (
        "<!-- COOP_EVIDENCE_MANIFEST_START -->\n"
        "```yaml\n"
        "evidence_schema_version: 1\n"
        f"evidence_role: {role}\n"
        f"evidence_result: {result}\n"
        f"change_id: {change_id}\n"
        f"current_batch: {current_batch}\n"
        f"attempt: {attempt}\n"
        f"contract_revision: {contract_revision}\n"
        f"canonical_sha256: {canonical_sha256}\n"
        f"agent_identity: {agent_identity}\n"
        f"agent_role: {agent_role}\n"
        "```\n"
        "<!-- COOP_EVIDENCE_MANIFEST_END -->\n"
    )


def schema5_evidence_manifest(
    role: str,
    result: str,
    change_id: str = "add-example-change",
    current_batch: int = 1,
    attempt: int = 1,
    contract_revision: int = 1,
    canonical_sha256: str = "b" * 64,
    high_review: bool = True,
) -> str:
    assignments = {
        "attempt-report": ("antigravity-cli", "antigravity-executor-01", "executor", "cohesive-medium"),
        "batch-review": ("grok-cli", "grok-reviewer-01", "independent-reviewer", "control-plane-high"),
        "preflight-review": ("codex", "codex-control-01", "control-plane", "control-plane-high"),
        "timeout-audit": ("codex", "codex-control-01", "control-plane", "control-plane-high"),
        "final-verification": ("codex", "codex-control-01", "control-plane", "control-plane-high"),
        "final-review": ("codex", "codex-control-01", "control-plane", "control-plane-high"),
    }
    product, instance, agent_role, profile = assignments[role]
    text = (
        "<!-- COOP_EVIDENCE_MANIFEST_START -->\n"
        "```yaml\n"
        "evidence_schema_version: 2\n"
        f"evidence_role: {role}\n"
        f"evidence_result: {result}\n"
        f"change_id: {change_id}\n"
        f"current_batch: {current_batch}\n"
        f"attempt: {attempt}\n"
        f"contract_revision: {contract_revision}\n"
        f"canonical_sha256: {canonical_sha256}\n"
        f"agent_product: {product}\n"
        f"agent_instance_id: {instance}\n"
        f"agent_role: {agent_role}\n"
        f"capability_profile: {profile}\n"
        "```\n"
        "<!-- COOP_EVIDENCE_MANIFEST_END -->\n"
    )
    if high_review and role in {"batch-review", "final-review"}:
        text += (
            "\nActual files and complete diff inspected\n"
            "Copy/transform/production wiring trace\n"
            "Critical reruns\n"
            "Claim-to-mechanism support\n"
            "Independent adversarial probe\n"
        )
    return text


def materialize_schema5_lease(data: dict, root: Path) -> None:
    text = (
        "<!-- COOP_CONFIRMATION_LEASE_START -->\n"
        "```yaml\n"
        "decision_id: decision-001\n"
        "artifact_revision: 2\n"
        f"artifact_sha256: {'a' * 64}\n"
        "approved_scope: approved source implementation\n"
        "approved_actions:\n"
        "  - run-safe-tests\n"
        "risk_profile: standard\n"
        "decision_source: ai-proposed/user-approved\n"
        "owner_instance_id: codex-control-01\n"
        "status: valid\n"
        "invalidation_conditions:\n"
        "  - scope-change\n"
        "```\n"
        "<!-- COOP_CONFIRMATION_LEASE_END -->\n"
    )
    target = root / data["confirmation_lease"]["path"]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    data["confirmation_lease"]["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()


def schema4_contract(validator, handoff: str, **overrides) -> dict:
    data = validator.extract_handoff_contract(handoff, "handoff")
    for key in (
        "control_plane_owner", "executor_assignment",
        "independent_reviewer_assignment", "decision_source",
        "confirmation_lease", "confirmation_lease_status",
    ):
        data.pop(key, None)
    identity_fields = {
        "executor_agent": "antigravity-cli",
        "independent_reviewer_agent": "grok-cli",
        "decision_owner": "codex",
        "independent_review_not_applicable_reason": None,
    }
    data.update(schema_version=4, **identity_fields)
    data["readonly_fields"] = list(validator.LEGACY_IMMUTABLE_FIELDS)
    data.update(overrides)
    return data


def load_validator():
    path = ROOT / "scripts" / "validate_core_gates.py"
    spec = importlib.util.spec_from_file_location("validate_core_gates", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class WorkflowRulesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.request_modes = (ROOT / "references" / "request-modes.md").read_text(encoding="utf-8")
        cls.approved = (ROOT / "references" / "approved-implementation-workflow.md").read_text(encoding="utf-8")
        cls.completion = (
            ROOT / "references" / "completion-contract.md"
        ).read_text(encoding="utf-8")
        cls.handoff = (ROOT / "references" / "handoff-contract.md").read_text(encoding="utf-8")
        cls.proposal_workflow = (
            ROOT / "references" / "proposal-workflow.md"
        ).read_text(encoding="utf-8")
        cls.superpowers_adapter = (
            ROOT / "references" / "superpowers-adapter.md"
        ).read_text(encoding="utf-8")
        cls.shared_governance = (
            ROOT / "references" / "shared-global-governance.md"
        ).read_text(encoding="utf-8")
        cls.agent_capability_routing = (
            ROOT / "references" / "agent-capability-routing.md"
        ).read_text(encoding="utf-8")
        cls.local_checkpoint = (
            ROOT / "references" / "local-instruction-checkpoint.md"
        ).read_text(encoding="utf-8")
        cls.learning = (
            ROOT / "references" / "learning-candidate-pipeline.md"
        ).read_text(encoding="utf-8")

    def test_description_does_not_claim_brief_or_external_batch_work(self):
        description = self.skill.split("---", 2)[1]
        self.assertNotIn("task or step breakdowns", description)
        self.assertNotIn("external-agent handoff", description)
        self.assertIn("modify files or behavior", description)

    def test_description_routes_explicit_archive_and_distill_requests(self):
        description = self.skill.split("---", 2)[1]
        self.assertIn("archive and distill", description)
        self.assertIn("Project Learning Closeout", description)
        self.assertIn("归档并蒸馏", description)

    def test_review_and_fix_is_not_review_only(self):
        self.assertIn("Review and fix", self.request_modes)
        self.assertIn("not Review-only", self.request_modes)

    def test_direct_change_uses_risk_appropriate_evidence_profile_everywhere(self):
        direct = (ROOT / "references" / "direct-change-rule.md").read_text(encoding="utf-8")
        responses = (ROOT / "references" / "response-patterns.md").read_text(encoding="utf-8")
        for text in (self.request_modes, direct, responses):
            self.assertIn("public/API restoration", text)
            self.assertIn("strict", text)
        self.assertIn("Low-risk Direct Change", responses)
        self.assertIn("compact", responses)
        self.assertNotIn("Use compact Step Evidence Gate", direct)
        self.assertIn("Use the profile-appropriate Step Evidence Gate", direct)

    def test_openspec_and_superpowers_do_not_duplicate_design_approval(self):
        self.assertIn("single design approval", self.approved)
        self.assertIn("does not require a duplicate", self.approved)

    def test_evidence_gate_operates_on_slices_not_micro_steps(self):
        self.assertIn("business slice", self.approved)
        self.assertIn("not every TDD micro-step", self.approved)

    def test_inline_step_evidence_stays_handoff_free(self):
        inline = (ROOT / "templates" / "evidence-template.md").read_text(encoding="utf-8")
        final = (ROOT / "templates" / "final-verification-template.md").read_text(encoding="utf-8")
        self.assertNotIn("COOP_EVIDENCE_MANIFEST_START", inline)
        self.assertIn("evidence_role: final-verification", final)

    def test_inline_implementation_requires_review(self):
        self.assertIn("inline implementation", self.approved)
        self.assertIn("Review PASS", self.approved)

    def test_completion_contract_is_canonical_and_discoverable(self):
        path = ROOT / "references" / "completion-contract.md"
        self.assertTrue(path.is_file(), "canonical completion contract missing")
        completion = path.read_text(encoding="utf-8")
        normalized = " ".join(completion.split())
        for heading in (
            "## Success", "## Evidence", "## Stop conditions",
            "## Learning and reconciliation", "## Cross-CLI sync",
            "## Git and publication authority", "## Residual risk",
        ):
            self.assertIn(heading, completion)
        for obligation in (
            "fresh final evidence", "final Review PASS",
            "Project Learning Closeout", "OpenSpec task reconciliation",
            "strict validation after archive", "every declared required runtime",
            "explicit user authorization", "FAIL", "BLOCKED",
            "final_critical", "hashed evidence manifest", "--previous-status",
            "tests/logs", "sensitive information", "temporary files",
            "unrelated changes", "superpowers:verification-before-completion",
            "A chat-only summary is not durable promotion",
            "Reconcile `tasks.md`", "Update project-required design/closeout documentation",
        ):
            self.assertIn(obligation, normalized)
        self.assertIn(
            "Run Project Learning Closeout after implementation Review PASS "
            "and before fresh final verification",
            normalized,
        )
        self.assertNotIn(
            "Run Project Learning Closeout after implementation Review PASS when",
            normalized,
        )
        self.assertIn("references/completion-contract.md", self.skill)

    def test_secondary_completion_surfaces_reference_canonical_contract(self):
        for relative in (
            "references/response-patterns.md",
            "references/approved-implementation-workflow.md",
            "references/step-evidence-gate.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("references/completion-contract.md", text, relative)
        evidence = (ROOT / "references" / "step-evidence-gate.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("business slice", evidence)
        self.assertIn("batch Review", evidence)
        skill_closure = self.skill.split("## Implementation And Closure", 1)[1].split(
            "## Capability And Evidence Profiles", 1
        )[0]
        approved_final = self.approved.split("## Final Completion", 1)[1].split(
            "## Tiered Authorization And High Review", 1
        )[0]
        self.assertNotIn("run Project Learning Closeout", skill_closure)
        self.assertNotIn("persist fresh `final_critical`", approved_final)
        self.assertNotIn("--previous-status", approved_final)
        self.assertNotIn("superpowers:verification-before-completion", approved_final)
        self.assertNotIn("Completion claim allowed", evidence)
        self.assertIn("whole-task decision is deferred", evidence)

    def test_phase_aware_superpowers_activation_precedes_broad_metadata(self):
        normalized_skill = " ".join(self.skill.split())
        normalized_adapter = " ".join(self.superpowers_adapter.split())
        normalized_governance = " ".join(self.shared_governance.split())
        self.assertIn("Phase-Aware Superpowers Activation", self.skill)
        self.assertIn(
            "Generic create/modify wording does not activate a Superpowers "
            "sub-skill by itself.",
            normalized_skill,
        )
        self.assertIn(
            "Generic create/modify wording does not activate a sub-skill by itself.",
            normalized_adapter,
        )
        self.assertIn(
            "[CCG-014] Governed state-changing work enters "
            "`openspec-superpower-change` phase classification before broad "
            "Superpowers metadata selects a sub-skill. Generic create/modify "
            "wording alone does not activate a sub-skill; once selected, that "
            "sub-skill's full rules remain in force.",
            normalized_governance,
        )

    def test_proposal_only_can_select_no_superpowers_subskill(self):
        normalized_skill = " ".join(self.skill.split())
        normalized = " ".join(self.proposal_workflow.split())
        normalized_adapter = " ".join(self.superpowers_adapter.split())
        normalized_request_modes = " ".join(self.request_modes.split())
        self.assertIn("proposal-only", normalized)
        self.assertIn("no implementation sub-skill", normalized)
        self.assertIn(
            "Public API implementation remains `strict`; its proposal-only draft "
            "does not automatically load implementation planning, TDD, or code Review.",
            normalized_request_modes,
        )
        self.assertIn(
            "Gate 0 loads no implementation sub-skill for proposal drafting. A "
            "material unresolved choice requires brainstorming.",
            normalized_request_modes,
        )
        self.assertIn(
            "A bounded assumption is allowed only when it is reversible at approval "
            "time, explicit in proposal/design, and does not decide security, "
            "compatibility, destructive migration, data lifecycle, production "
            "authority, or testable acceptance.",
            normalized,
        )
        self.assertIn(
            "A material unresolved choice affecting scope, security, compatibility, "
            "data lifecycle, production authority, or testable acceptance requires "
            "`superpowers:brainstorming`.",
            normalized,
        )
        self.assertIn(
            "A request to choose for the user does not resolve a material choice; "
            "invoke brainstorming and obtain acceptance before artifact finalization.",
            normalized_skill,
        )
        self.assertIn(
            "User delegation to choose an excluded boundary does not make it a "
            "bounded assumption; invoke brainstorming and obtain user acceptance "
            "before finalizing artifacts.",
            normalized,
        )
        self.assertIn(
            "Once a sub-skill is selected, follow it completely; selective "
            "invocation never weakens its HARD-GATE or discipline.",
            normalized_adapter,
        )

    def test_prompt_collision_scenario_catalog_covers_phase_git_and_hard_gate(self):
        path = ROOT / "tests" / "fixtures" / "prompt-collision-cases.json"
        self.assertTrue(path.is_file(), "prompt-collision fixture missing")
        cases = {case["id"]: case for case in json.loads(path.read_text(encoding="utf-8"))}
        expected_ids = {
            "proposal_only", "material_choice", "unauthorized_git",
            "authorized_git", "selected_hard_gate",
        }
        self.assertEqual(set(cases), expected_ids)
        for case in cases.values():
            self.assertTrue(case["prompt"].strip())
            self.assertTrue(case["observable"].strip())
            self.assertNotIn("expected", case)
        normalized = " ".join((self.skill + self.superpowers_adapter).split())
        self.assertIn("never grants Git permission", normalized)
        self.assertIn("current user explicitly authorizes", normalized)
        self.assertIn("no implementation sub-skill", " ".join(self.proposal_workflow.split()))
        self.assertIn("HARD-GATE", normalized)

    def test_model_identity_never_selects_workflow_weight(self):
        normalized_skill = " ".join(self.skill.split())
        normalized_adapter = " ".join(self.superpowers_adapter.split())
        normalized_capability_routing = " ".join(
            self.agent_capability_routing.split()
        )
        self.assertIn(
            "Model identity or version does not grant approval and does not select "
            "workflow weight.",
            normalized_skill,
        )
        self.assertIn(
            "Concrete model identity does not grant authority or choose workflow weight.",
            normalized_adapter,
        )
        self.assertIn(
            "Capability profiles are stable routing and authority ceilings. They are "
            "not model names, vendor tiers, security identities, or evidence of approval.",
            normalized_capability_routing,
        )
        self.assertIn(
            "Optional model metadata is observational only and MUST NOT influence "
            "validation, routing, or approval.",
            normalized_capability_routing,
        )

    def test_domain_context_check_is_conditional_and_precedes_material_choice(self):
        normalized = " ".join((self.skill + self.request_modes).split())
        self.assertIn("Domain Context Check", normalized)
        self.assertIn("before material", normalized)
        self.assertIn("does not invoke `grill-with-docs`", normalized)
        self.assertIn("complete portable Discovery First", normalized)
        self.assertIn("references/local-instruction-checkpoint.md", self.skill)

    def test_ignored_canonical_context_cannot_satisfy_shared_promotion(self):
        normalized = " ".join(self.local_checkpoint.split())
        self.assertIn("must not be intentionally ignored", normalized)
        self.assertIn(
            "does not require `git add`, commit, or push", normalized
        )

    def test_project_learning_gate_has_automatic_and_explicit_triggers(self):
        path = ROOT / "references" / "project-learning-closeout.md"
        self.assertTrue(path.is_file(), "project learning closeout reference missing")
        learning_closeout = path.read_text(encoding="utf-8")
        normalized = " ".join((self.learning + learning_closeout).split())
        self.assertIn("two independent correction or Review signals", normalized)
        self.assertIn("security, integrity, data-loss, or false-PASS", normalized)
        self.assertIn("archive and distill", normalized)
        self.assertIn("every confirmed project-local key point", normalized)
        self.assertIn("single low-risk task-local correction", normalized)
        self.assertIn("without creating durable documentation noise", normalized)

    def test_required_project_learning_blocks_completion_and_archive(self):
        path = ROOT / "references" / "project-learning-closeout.md"
        self.assertTrue(path.is_file(), "project learning closeout reference missing")
        learning_closeout = path.read_text(encoding="utf-8")
        normalized = " ".join(
            (self.skill + self.approved + learning_closeout).split()
        )
        self.assertIn("Project Learning Closeout", normalized)
        self.assertIn("final completion is `BLOCKED`", normalized)
        self.assertIn("before fresh final verification", normalized)
        self.assertIn("before OpenSpec", normalized)

    def test_learning_artifacts_are_layered_and_mechanical_rules_are_executable(self):
        closeout_path = ROOT / "references" / "project-learning-closeout.md"
        template_path = ROOT / "templates" / "learning-candidate-template.md"
        self.assertTrue(
            closeout_path.is_file(), "project learning closeout reference missing"
        )
        self.assertTrue(
            template_path.is_file(), "learning candidate template missing"
        )
        learning_closeout = closeout_path.read_text(encoding="utf-8")
        learning_template = template_path.read_text(encoding="utf-8")
        normalized = " ".join((learning_closeout + learning_template).split())
        self.assertIn("CONTEXT.md", normalized)
        self.assertIn("docs/engineering-invariants.md", normalized)
        self.assertIn("deterministic regression test or validator", normalized)
        self.assertIn("prose-only", normalized)
        self.assertIn("sensitive", normalized)

    def test_project_learning_validator_binds_rules_to_owned_artifacts(self):
        closeout = (
            ROOT / "references" / "project-learning-closeout.md"
        ).read_text(encoding="utf-8")
        template = (
            ROOT / "templates" / "learning-candidate-template.md"
        ).read_text(encoding="utf-8")
        self.validator.validate_project_learning_gate(
            self.skill, self.approved, self.completion, closeout, template
        )

        relocated_closeout = "# Project Learning Closeout\n\nPlaceholder.\n"
        with self.assertRaisesRegex(AssertionError, "project-learning-closeout"):
            self.validator.validate_project_learning_gate(
                self.skill,
                self.approved,
                self.completion,
                relocated_closeout,
                template + "\n" + closeout,
            )

        relocated_template = "# Learning Candidate Card\n\nPlaceholder.\n"
        with self.assertRaisesRegex(AssertionError, "learning-candidate-template"):
            self.validator.validate_project_learning_gate(
                self.skill,
                self.approved,
                self.completion,
                closeout + "\n" + template,
                relocated_template,
            )

    def test_project_learning_guidance_is_discoverable_from_project_instructions(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        invariants_path = ROOT / "docs" / "engineering-invariants.md"
        self.assertTrue(invariants_path.is_file(), "engineering invariants missing")
        invariants = invariants_path.read_text(encoding="utf-8")
        normalized = " ".join(invariants.split())
        self.assertIn("docs/engineering-invariants.md", agents)
        self.assertIn("references/project-learning-closeout.md", agents)
        self.assertIn("entry-discoverable and artifact-bound", normalized)
        self.assertIn("deterministic negative regression", normalized)

    def test_external_cli_debug_traces_are_temporary_and_not_durable(self):
        invariants = (ROOT / "docs" / "engineering-invariants.md").read_text(
            encoding="utf-8"
        )
        normalized = " ".join(invariants.split()).lower()
        for required in (
            "external cli debug traces",
            "temporary evidence",
            "mode `0600`",
            "must not be quoted or echoed",
            "remove the raw trace after final gates",
        ):
            with self.subTest(required=required):
                self.assertIn(required, normalized)

        durable_roots = (
            ROOT / "docs",
            ROOT / "openspec",
            ROOT / "references",
        )
        raw_traces = sorted(
            str(path.relative_to(ROOT))
            for durable_root in durable_roots
            for path in durable_root.rglob("*")
            if path.is_file()
            and (
                path.name.endswith(".debug.log")
                or path.name.endswith(".debug.jsonl")
            )
        )
        self.assertEqual([], raw_traces, "raw external CLI traces became durable")

    def test_qagent_fixture_separates_semantics_mechanism_and_regression(self):
        fixture = (
            ROOT
            / "tests"
            / "fixtures"
            / "project-learning"
            / "qagent-merged-paragraph.md"
        ).read_text(encoding="utf-8")
        self.assertIn("table-level annotation, not tabular data", fixture)
        self.assertIn("engineering invariant", fixture)
        self.assertIn("mechanical regression", fixture)

    def test_handoff_schema_has_closure_fields(self):
        for expected in (
            "schema_version: 5",
            "lifecycle_state:",
            "attempt:",
            "attempt_report_artifact:",
            "last_review_result:",
            "last_review_artifact:",
            "blocker_owner:",
            "resume_condition:",
            "final_verification:",
            "final_verification_artifact:",
            "final_review_result:",
            "final_review_artifact:",
        ):
            self.assertIn(expected, self.handoff)

    def test_complete_contract_requires_review_and_final_verification(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="complete",
            last_review_result="fail",
            final_verification="pending",
            final_review_result="pending",
            next_owner="user",
        )
        with self.assertRaisesRegex(AssertionError, "complete"):
            self.validator.validate_handoff_contract(data, "invalid-complete")

    def test_schema4_requires_bound_agent_identities_and_codex_decision_owner(self):
        data = schema4_contract(self.validator, self.handoff)
        self.validator.validate_handoff_contract(data, "schema4-identities")
        self.assertEqual(self.validator.LEGACY_SCHEMA_VERSION, 4)
        for field in (
            "executor_agent", "independent_reviewer_agent", "decision_owner",
        ):
            self.assertIn(field, self.validator.LEGACY_IMMUTABLE_FIELDS)

        for field, value in (
            ("executor_agent", "agy"),
            ("independent_reviewer_agent", "grok"),
            ("decision_owner", "antigravity-cli"),
        ):
            invalid = dict(data)
            invalid[field] = value
            with self.subTest(field=field, value=value):
                with self.assertRaisesRegex(AssertionError, "agent|identity|decision_owner"):
                    self.validator.validate_handoff_contract(invalid, "invalid-identity")

    def test_standard_and_strict_require_a_distinct_reviewer(self):
        self.assertEqual(self.validator.LEGACY_SCHEMA_VERSION, 4)
        for profile in ("standard", "strict"):
            same_agent = schema4_contract(
                self.validator, self.handoff, risk_profile=profile,
                independent_reviewer_agent="antigravity-cli",
            )
            with self.subTest(profile=profile, case="self-review"):
                with self.assertRaisesRegex(AssertionError, "reviewer|distinct|self-review"):
                    self.validator.validate_handoff_contract(same_agent, "self-review")

            no_reviewer = schema4_contract(
                self.validator, self.handoff, risk_profile=profile,
                independent_reviewer_agent="not-applicable",
                independent_review_not_applicable_reason="reviewed inline",
            )
            with self.subTest(profile=profile, case="not-applicable"):
                with self.assertRaisesRegex(AssertionError, "reviewer|not-applicable|compact"):
                    self.validator.validate_handoff_contract(no_reviewer, "missing-reviewer")

    def test_compact_not_applicable_reviewer_requires_a_reason(self):
        valid = schema4_contract(
            self.validator, self.handoff, risk_profile="compact",
            independent_reviewer_agent="not-applicable",
            independent_review_not_applicable_reason="Codex performs the inline Review",
        )
        self.validator.validate_handoff_contract(valid, "compact-inline-review")

        for reason in (None, "", "   "):
            invalid = dict(valid)
            invalid["independent_review_not_applicable_reason"] = reason
            with self.subTest(reason=reason):
                with self.assertRaisesRegex(AssertionError, "reason|non-blank"):
                    self.validator.validate_handoff_contract(invalid, "missing-na-reason")

        concrete = schema4_contract(
            self.validator, self.handoff, risk_profile="compact",
            independent_review_not_applicable_reason="must be null",
        )
        with self.assertRaisesRegex(AssertionError, "reason|not-applicable|null"):
            self.validator.validate_handoff_contract(concrete, "unexpected-na-reason")

    def test_schema4_agent_identity_fields_are_immutable(self):
        before = schema4_contract(self.validator, self.handoff)
        after = dict(before)
        after.update(
            lifecycle_state="ready-for-execution",
            contract_revision=before["contract_revision"] + 1,
            next_owner="external-agent",
            executor_agent="grok-cli",
            independent_reviewer_agent="codex",
        )
        with self.assertRaisesRegex(
            AssertionError,
            "readonly field changed: (executor_agent|independent_reviewer_agent)",
        ):
            self.validator.validate_transition(before, after, "identity-change")

    def test_attempt_report_manifest_binds_executor_identity_and_role(self):
        data = schema4_contract(
            self.validator, self.handoff, lifecycle_state="ready-for-review",
            contract_revision=2, next_owner="codex-brief-antigravity-review",
            attempt_report_artifact=artifact("report.md"),
        )
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = root / "report.md"
            report.write_text(evidence_manifest("attempt-report", "pass"), encoding="utf-8")
            data["attempt_report_artifact"] = {
                "path": "report.md", "sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
            }
            self.validator.validate_handoff_contract(data, "executor-evidence")
            self.validator.validate_evidence_artifacts(data, root, "executor-evidence")

            report.write_text(evidence_manifest(
                "attempt-report", "pass", agent_identity="grok-cli", agent_role="independent-reviewer",
            ), encoding="utf-8")
            data["attempt_report_artifact"]["sha256"] = hashlib.sha256(report.read_bytes()).hexdigest()
            with self.assertRaisesRegex(AssertionError, "identity|role|executor|impersonation"):
                self.validator.validate_evidence_artifacts(data, root, "executor-impersonation")

    def test_batch_review_rejects_executor_self_review_and_impersonation(self):
        data = schema4_contract(
            self.validator, self.handoff, lifecycle_state="awaiting-final-verification",
            current_batch=2, contract_revision=3, last_review_result="pass",
            next_owner="openspec-superpower-change",
        )
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = root / "report.md"
            review = root / "review.md"
            report.write_text(evidence_manifest(
                "attempt-report", "pass", current_batch=2, contract_revision=1,
            ), encoding="utf-8")
            review.write_text(evidence_manifest(
                "batch-review", "pass", current_batch=2, contract_revision=2,
                agent_identity="antigravity-cli", agent_role="independent-reviewer",
            ), encoding="utf-8")
            data["attempt_report_artifact"] = {
                "path": "report.md", "sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
            }
            data["last_review_artifact"] = {
                "path": "review.md", "sha256": hashlib.sha256(review.read_bytes()).hexdigest(),
            }
            self.validator.validate_handoff_contract(data, "review-impersonation")
            with self.assertRaisesRegex(AssertionError, "identity|reviewer|self-review|impersonation"):
                self.validator.validate_evidence_artifacts(data, root, "review-impersonation")

    def test_timeout_audit_binds_codex_decision_owner_for_shared_artifact(self):
        data = schema4_contract(
            self.validator, self.handoff, lifecycle_state="blocked", contract_revision=2,
            last_review_result="blocked", blocked_reason="executor timeout",
            blocker_owner="external-agent", resume_condition="redispatch",
            next_owner="codex-brief-antigravity-review",
        )
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            timeout = root / "timeout.md"
            timeout.write_text(evidence_manifest("timeout-audit", "blocked"), encoding="utf-8")
            ref = {"path": "timeout.md", "sha256": hashlib.sha256(timeout.read_bytes()).hexdigest()}
            data["attempt_report_artifact"] = ref
            data["last_review_artifact"] = ref
            self.validator.validate_handoff_contract(data, "timeout-identity")
            self.validator.validate_evidence_artifacts(data, root, "timeout-identity")

    def test_fallback_scalar_parser_handles_yaml_booleans_and_null(self):
        self.assertIs(self.validator.parse_scalar("true"), True)
        self.assertIs(self.validator.parse_scalar("false"), False)
        self.assertIsNone(self.validator.parse_scalar("null"))

    def test_fail_transition_cannot_advance_batch(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(
            lifecycle_state="ready-for-review",
            last_review_result="not-run",
            attempt_report_artifact=artifact("docs/agent-collab/change/report.md"),
        )
        after = dict(before)
        after.update(
            lifecycle_state="needs-fix",
            last_review_result="fail",
            last_review_artifact=artifact("docs/review/fail.md"),
            attempt=before["attempt"] + 1,
            contract_revision=before["contract_revision"] + 1,
            next_owner="codex-brief-antigravity-review",
        )
        after["current_batch"] = before["current_batch"] + 1
        with self.assertRaisesRegex(AssertionError, "same batch"):
            self.validator.validate_transition(before, after, "invalid-fail")

    def test_final_batch_pass_hands_back_to_router(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(
            lifecycle_state="ready-for-review",
            current_batch=before["planned_batches"],
            last_review_result="not-run",
            attempt_report_artifact=artifact("docs/agent-collab/change/report.md"),
        )
        after = dict(before)
        after.update(
            lifecycle_state="awaiting-final-verification",
            last_review_result="pass",
            last_review_artifact=artifact("docs/review/batch.md"),
            contract_revision=before["contract_revision"] + 1,
            next_owner="openspec-superpower-change",
        )
        self.validator.validate_transition(before, after, "final-pass")

    def test_both_skills_publish_same_closure_fields(self):
        if not BRIEF_HANDOFF.is_file():
            self.skipTest("companion repository is not checked out")
        brief_handoff = BRIEF_HANDOFF.read_text(encoding="utf-8")
        for expected in (
            "schema_version: 5",
            "lifecycle_state:",
            "attempt:",
            "attempt_report_artifact:",
            "last_review_result:",
            "last_review_artifact:",
            "final_verification:",
            "final_verification_artifact:",
            "final_review_result:",
            "final_review_artifact:",
        ):
            self.assertIn(expected, self.handoff)
            self.assertIn(expected, brief_handoff)

    def test_execution_contract_rejects_unapproved_proposal_mode(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            mode="openspec-proposal",
            approval_status="proposed",
            executor="codex",
            governor="openspec-superpower-change",
        )
        with self.assertRaisesRegex(AssertionError, "execution contract"):
            self.validator.validate_handoff_contract(data, "proposal")

    def test_regular_transition_cannot_change_batch_attempt_or_owner(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        after = dict(before)
        after.update(
            lifecycle_state="ready-for-execution",
            current_batch=before["current_batch"] + 1,
            attempt=99,
            next_owner="user",
            contract_revision=before["contract_revision"] + 1,
        )
        with self.assertRaisesRegex(AssertionError, "same batch and attempt|next_owner"):
            self.validator.validate_transition(before, after, "illegal-jump")

    def test_blocked_contract_requires_blocked_review_result(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="blocked",
            last_review_result="pass",
            blocked_reason="dependency unavailable",
            blocker_owner="dependency",
            resume_condition="dependency restored",
            next_owner="user",
        )
        with self.assertRaisesRegex(AssertionError, "blocked|tuple"):
            self.validator.validate_handoff_contract(data, "blocked-pass")

    def test_compact_contract_still_requires_typed_evidence_fields(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            risk_profile="compact",
            step_critical="pytest",
            final_critical="pytest",
            stop_conditions="none",
            verification_strategy="run tests",
        )
        with self.assertRaisesRegex(AssertionError, "list|mapping"):
            self.validator.validate_handoff_contract(data, "untyped-compact")

    def test_complete_state_is_terminal(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(
            lifecycle_state="complete",
            current_batch=before["planned_batches"],
            last_review_result="pass",
            final_review_result="pass",
            final_verification="pass",
            attempt_report_artifact=artifact("docs/agent-collab/change/report.md"),
            last_review_artifact=artifact("docs/review/batch.md"),
            final_verification_artifact=artifact("docs/agent-collab/change/final-verification.md"),
            final_review_artifact=artifact("docs/review/final.md"),
            next_owner="user",
        )
        after = dict(before)
        after.update(attempt=2, contract_revision=before["contract_revision"] + 1)
        with self.assertRaisesRegex(AssertionError, "terminal"):
            self.validator.validate_transition(before, after, "mutate-complete")

    def test_change_id_must_be_path_safe_slug(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data["change_id"] = "../escape"
        with self.assertRaisesRegex(AssertionError, "change_id"):
            self.validator.validate_handoff_contract(data, "unsafe-change-id")

    def test_shared_handoff_contract_is_byte_identical(self):
        if not BRIEF_HANDOFF.is_file():
            self.skipTest("companion repository is not checked out")
        brief_handoff = BRIEF_HANDOFF.read_text(encoding="utf-8")
        self.assertEqual(self.handoff, brief_handoff)

    def test_shared_validator_core_is_byte_identical_when_companion_exists(self):
        brief_validator = BRIEF_ROOT / "scripts" / "validate_templates.py"
        if not brief_validator.is_file():
            self.skipTest("companion repository is not checked out")
        openspec_text = (ROOT / "scripts" / "validate_core_gates.py").read_text(encoding="utf-8")
        brief_text = brief_validator.read_text(encoding="utf-8")

        def core(text: str) -> str:
            return text.split("START =", 1)[1].split("def validate_frontmatter", 1)[0]

        self.assertEqual(core(openspec_text), core(brief_text))

    def test_final_gate_failure_can_return_to_fix_with_new_attempt(self):
        before = self._awaiting_contract("pass")
        after = dict(before)
        after.update(
            lifecycle_state="needs-fix",
            attempt=before["attempt"] + 1,
            contract_revision=before["contract_revision"] + 1,
            final_review_result="fail",
            final_review_artifact=artifact("docs/review/final-fail.md"),
            next_owner="openspec-superpower-change",
        )
        self.validator.validate_transition(before, after, "final-gate-fix")

    def test_all_external_profiles_require_nonblank_critical_commands(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(risk_profile="compact", step_critical=[], final_critical=[])
        with self.assertRaisesRegex(AssertionError, "step_critical|final_critical"):
            self.validator.validate_handoff_contract(data, "empty-critical")

        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(step_critical=["   "], final_critical=["\t"])
        with self.assertRaisesRegex(AssertionError, "non-blank"):
            self.validator.validate_handoff_contract(data, "blank-critical")

    def test_blank_stop_and_blocker_values_are_rejected(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data["stop_conditions"] = [" "]
        with self.assertRaisesRegex(AssertionError, "stop_conditions"):
            self.validator.validate_handoff_contract(data, "blank-stop")

        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="blocked",
            last_review_result="blocked",
            last_review_artifact=artifact("docs/review/blocked.md"),
            attempt_report_artifact=artifact("docs/agent-collab/change/report-abort.md"),
            blocked_reason=" ",
            blocker_owner="dependency",
            resume_condition="\t",
            next_owner="user",
        )
        with self.assertRaisesRegex(AssertionError, "blocked_reason|resume_condition"):
            self.validator.validate_handoff_contract(data, "blank-blocker")

    def test_boolean_is_not_a_positive_integer(self):
        for key in ("current_batch", "planned_batches", "attempt", "contract_revision"):
            data = self.validator.extract_handoff_contract(self.handoff, "handoff")
            data[key] = True
            with self.subTest(key=key):
                with self.assertRaisesRegex(AssertionError, "positive integer"):
                    self.validator.validate_handoff_contract(data, f"bool-{key}")

    def test_readonly_fields_must_match_exactly_without_duplicates(self):
        base = self.validator.extract_handoff_contract(self.handoff, "handoff")
        for readonly in (
            list(base["readonly_fields"]) + ["attempt"],
            list(base["readonly_fields"]) + [base["readonly_fields"][0]],
            list(base["readonly_fields"])[1:],
        ):
            data = dict(base)
            data["readonly_fields"] = readonly
            with self.subTest(readonly=readonly):
                with self.assertRaisesRegex(AssertionError, "readonly_fields"):
                    self.validator.validate_handoff_contract(data, "readonly-mismatch")

    def test_result_and_artifact_fields_are_strictly_paired(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data["last_review_artifact"] = artifact("docs/review/unexpected.md")
        with self.assertRaisesRegex(AssertionError, "last_review_artifact"):
            self.validator.validate_handoff_contract(data, "unexpected-review-artifact")

        data = self._awaiting_contract("pass")
        data["final_verification_artifact"] = None
        with self.assertRaisesRegex(AssertionError, "final_verification_artifact"):
            self.validator.validate_handoff_contract(data, "missing-final-evidence")

    def test_artifact_reference_must_be_safe_relative_path_and_sha256(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="ready-for-brief",
            last_review_result="pass",
            last_review_artifact={"path": "../escape", "sha256": "x"},
        )
        with self.assertRaisesRegex(AssertionError, "artifact|sha256|relative"):
            self.validator.validate_handoff_contract(data, "unsafe-artifact")

    def test_runtime_artifact_validation_checks_file_size_and_hash(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="ready-for-brief",
            current_batch=2,
            contract_revision=4,
            last_review_result="pass",
            last_review_artifact=artifact("docs/review/batch.md"),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            materialize_schema5_lease(data if "data" in locals() else current, root)
            review = root / "docs" / "review" / "batch.md"
            review.parent.mkdir(parents=True)
            review.write_text(schema5_evidence_manifest("batch-review", "pass"), encoding="utf-8")
            data["last_review_artifact"]["sha256"] = hashlib.sha256(review.read_bytes()).hexdigest()
            self.validator.validate_evidence_artifacts(data, root, "runtime")
            data["last_review_artifact"]["sha256"] = "0" * 64
            with self.assertRaisesRegex(AssertionError, "sha256"):
                self.validator.validate_evidence_artifacts(data, root, "runtime")

    def _awaiting_contract(self, verification: str = "pending") -> dict:
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="awaiting-final-verification",
            current_batch=data["planned_batches"],
            last_review_result="pass",
            attempt_report_artifact=artifact("docs/agent-collab/change/report.md"),
            last_review_artifact=artifact("docs/review/batch.md"),
            final_verification=verification,
            final_verification_artifact=(
                artifact("docs/agent-collab/change/final-verification.md")
                if verification != "pending" else None
            ),
            final_review_result="pending",
            final_review_artifact=None,
            next_owner="openspec-superpower-change",
        )
        return data

    def test_final_verification_pass_can_be_persisted_before_final_review(self):
        before = self._awaiting_contract()
        after = self._awaiting_contract("pass")
        after["contract_revision"] = before["contract_revision"] + 1
        self.validator.validate_transition(before, after, "persist-final-verification")

    def test_complete_requires_persisted_verification_and_all_artifacts(self):
        before = self._awaiting_contract()
        after = self._awaiting_contract("pass")
        after.update(
            lifecycle_state="complete",
            final_review_result="pass",
            final_review_artifact=artifact("docs/review/final.md"),
            next_owner="user",
            contract_revision=before["contract_revision"] + 1,
        )
        with self.assertRaisesRegex(AssertionError, "persisted final verification"):
            self.validator.validate_transition(before, after, "atomic-complete")

        before = self._awaiting_contract("pass")
        after = dict(before)
        after.update(
            lifecycle_state="complete",
            final_review_result="pass",
            final_review_artifact=artifact("docs/review/final.md"),
            next_owner="user",
            contract_revision=before["contract_revision"] + 1,
        )
        self.validator.validate_transition(before, after, "evidenced-complete")

    def test_batch_blocked_cannot_resume_directly_to_review(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(
            lifecycle_state="blocked",
            last_review_result="blocked",
            attempt_report_artifact=artifact("docs/agent-collab/change/abort.md"),
            last_review_artifact=artifact("docs/review/blocked.md"),
            blocked_reason="dependency unavailable",
            blocker_owner="dependency",
            resume_condition="dependency restored",
            next_owner="user",
        )
        after = dict(before)
        after.update(
            lifecycle_state="ready-for-review",
            last_review_result="not-run",
            last_review_artifact=None,
            blocked_reason=None,
            blocker_owner="none",
            resume_condition=None,
            next_owner="codex-brief-antigravity-review",
            attempt=before["attempt"] + 1,
            contract_revision=before["contract_revision"] + 1,
        )
        with self.assertRaisesRegex(AssertionError, "invalid lifecycle transition"):
            self.validator.validate_transition(before, after, "skip-report")

    def test_needs_fix_accepts_batch_and_each_final_failure_stage(self):
        batch = self.validator.extract_handoff_contract(self.handoff, "handoff")
        batch.update(
            lifecycle_state="needs-fix",
            last_review_result="fail",
            attempt_report_artifact=artifact("docs/agent-collab/change/report.md"),
            last_review_artifact=artifact("docs/review/batch-fail.md"),
        )
        self.validator.validate_handoff_contract(batch, "batch-fail")

        verification = self._awaiting_contract()
        verification.update(
            lifecycle_state="needs-fix",
            final_verification="fail",
            final_verification_artifact=artifact("docs/agent-collab/change/final-verification-fail.md"),
        )
        self.validator.validate_handoff_contract(verification, "verification-fail")

        review = self._awaiting_contract("pass")
        review.update(
            lifecycle_state="needs-fix",
            final_review_result="fail",
            final_review_artifact=artifact("docs/review/final-fail.md"),
        )
        self.validator.validate_handoff_contract(review, "final-review-fail")

    def test_blocked_accepts_batch_and_each_final_block_stage(self):
        common = {
            "lifecycle_state": "blocked",
            "blocked_reason": "dependency unavailable",
            "blocker_owner": "dependency",
            "resume_condition": "dependency restored",
            "next_owner": "user",
        }
        batch = self.validator.extract_handoff_contract(self.handoff, "handoff")
        batch.update(
            **common,
            last_review_result="blocked",
            attempt_report_artifact=artifact("docs/agent-collab/change/abort.md"),
            last_review_artifact=artifact("docs/review/batch-blocked.md"),
        )
        self.validator.validate_handoff_contract(batch, "batch-blocked")

        verification = self._awaiting_contract()
        verification.update(
            **common,
            final_verification="blocked",
            final_verification_artifact=artifact("docs/agent-collab/change/final-verification-blocked.md"),
        )
        self.validator.validate_handoff_contract(verification, "verification-blocked")

        review = self._awaiting_contract("pass")
        review.update(
            **common,
            final_review_result="blocked",
            final_review_artifact=artifact("docs/review/final-blocked.md"),
        )
        self.validator.validate_handoff_contract(review, "final-review-blocked")

    def test_preflight_blocked_does_not_require_an_attempt_report(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="blocked",
            last_review_result="blocked",
            last_review_artifact=artifact("docs/review/preflight-blocked.md"),
            blocked_reason="brief has an unauthorized git step",
            blocker_owner="codex-brief-antigravity-review",
            resume_condition="brief revised and preflight rerun",
            next_owner="codex-brief-antigravity-review",
        )
        self.assertIsNone(data["attempt_report_artifact"])
        self.validator.validate_handoff_contract(data, "preflight-blocked")

    def test_final_review_blocked_resume_preserves_verification_evidence(self):
        before = self._awaiting_contract("pass")
        before.update(
            lifecycle_state="blocked",
            final_review_result="blocked",
            final_review_artifact=artifact("docs/review/final-blocked.md"),
            blocked_reason="reviewer unavailable",
            blocker_owner="dependency",
            resume_condition="reviewer available",
            next_owner="user",
        )
        after = dict(before)
        after.update(
            lifecycle_state="awaiting-final-verification",
            final_review_result="pending",
            final_review_artifact=None,
            blocked_reason=None,
            blocker_owner="none",
            resume_condition=None,
            next_owner="openspec-superpower-change",
            contract_revision=before["contract_revision"] + 1,
        )
        self.validator.validate_transition(before, after, "resume-final-review")

        replaced = dict(after)
        replaced["attempt_report_artifact"] = artifact("docs/agent-collab/change/replacement-report.md")
        replaced["last_review_artifact"] = artifact("docs/review/replacement-batch.md")
        with self.assertRaisesRegex(AssertionError, "cannot rewrite"):
            self.validator.validate_transition(before, replaced, "resume-final-review-rewrite")

    def test_runtime_artifact_validation_rejects_missing_empty_and_symlink_escape(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="ready-for-brief",
            current_batch=2,
            contract_revision=4,
            last_review_result="pass",
            attempt_report_artifact=artifact("docs/agent-collab/change/report.md"),
            last_review_artifact=artifact("docs/review/batch.md"),
        )
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / "root"
            root.mkdir()
            materialize_schema5_lease(data, root)
            with self.assertRaisesRegex(AssertionError, "exist and be non-empty"):
                self.validator.validate_evidence_artifacts(data, root, "missing")

            report = root / "docs" / "agent-collab" / "change" / "report.md"
            review = root / "docs" / "review" / "batch.md"
            report.parent.mkdir(parents=True)
            review.parent.mkdir(parents=True)
            report.write_text(schema5_evidence_manifest("attempt-report", "pass"), encoding="utf-8")
            review.write_text("", encoding="utf-8")
            data["attempt_report_artifact"]["sha256"] = hashlib.sha256(report.read_bytes()).hexdigest()
            with self.assertRaisesRegex(AssertionError, "exist and be non-empty"):
                self.validator.validate_evidence_artifacts(data, root, "empty")

            outside = base / "outside.md"
            outside.write_text("outside\n", encoding="utf-8")
            review.unlink()
            review.symlink_to(outside)
            data["last_review_artifact"]["sha256"] = hashlib.sha256(outside.read_bytes()).hexdigest()
            with self.assertRaisesRegex(AssertionError, "outside artifact root"):
                self.validator.validate_evidence_artifacts(data, root, "symlink")

    def test_nonfinal_batch_promotion_requires_review_pass_and_keeps_decision_evidence(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(
            lifecycle_state="ready-for-review",
            attempt_report_artifact=artifact("docs/agent-collab/change/report.md"),
            next_owner="codex-brief-antigravity-review",
        )
        after = dict(before)
        after.update(
            lifecycle_state="ready-for-brief",
            current_batch=before["current_batch"] + 1,
            attempt=1,
            contract_revision=before["contract_revision"] + 1,
            attempt_report_artifact=None,
            last_review_result="not-run",
            last_review_artifact=None,
            next_owner="codex-brief-antigravity-review",
        )

        with self.assertRaisesRegex(AssertionError, "Review PASS|review evidence"):
            self.validator.validate_transition(before, after, "promote-without-review")

    def test_batch_decision_cannot_replace_the_report_that_was_reviewed(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(
            lifecycle_state="ready-for-review",
            current_batch=before["planned_batches"],
            attempt_report_artifact=artifact("docs/agent-collab/change/original-report.md"),
            next_owner="codex-brief-antigravity-review",
        )
        after = dict(before)
        after.update(
            lifecycle_state="awaiting-final-verification",
            contract_revision=before["contract_revision"] + 1,
            attempt_report_artifact=artifact("docs/agent-collab/change/replacement-report.md"),
            last_review_result="pass",
            last_review_artifact=artifact("docs/review/batch-pass.md"),
            next_owner="openspec-superpower-change",
        )

        with self.assertRaisesRegex(AssertionError, "attempt_report_artifact|reviewed Report"):
            self.validator.validate_transition(before, after, "replace-reviewed-report")

    def test_final_review_cannot_start_in_the_revision_that_first_persists_verification_pass(self):
        before = self._awaiting_contract()
        after = dict(before)
        after.update(
            lifecycle_state="blocked",
            contract_revision=before["contract_revision"] + 1,
            final_verification="pass",
            final_verification_artifact=artifact("docs/agent-collab/change/final-verification.md"),
            final_review_result="blocked",
            final_review_artifact=artifact("docs/review/final-review-blocked.md"),
            blocked_reason="reviewer unavailable",
            blocker_owner="dependency",
            resume_condition="reviewer available",
            next_owner="user",
        )

        with self.assertRaisesRegex(AssertionError, "persisted final verification|final Review"):
            self.validator.validate_transition(before, after, "atomic-final-verification-and-review")

    def test_blocked_self_transition_cannot_change_gate_tuple_or_evidence(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(
            lifecycle_state="blocked",
            current_batch=before["planned_batches"],
            attempt_report_artifact=artifact("docs/agent-collab/change/report-abort.md"),
            last_review_result="blocked",
            last_review_artifact=artifact("docs/review/batch-blocked.md"),
            blocked_reason="batch dependency unavailable",
            blocker_owner="dependency",
            resume_condition="batch dependency restored",
            next_owner="user",
        )
        after = dict(before)
        after.update(
            contract_revision=before["contract_revision"] + 1,
            last_review_result="pass",
            last_review_artifact=artifact("docs/review/fabricated-batch-pass.md"),
            final_verification="pass",
            final_verification_artifact=artifact("docs/agent-collab/change/fabricated-final-verification.md"),
            final_review_result="blocked",
            final_review_artifact=artifact("docs/review/final-review-blocked.md"),
            blocked_reason="final reviewer unavailable",
            resume_condition="final reviewer available",
        )

        with self.assertRaisesRegex(AssertionError, "blocked self-transition|result tuple|evidence"):
            self.validator.validate_transition(before, after, "rewrite-blocked-stage")

    def test_runtime_complete_snapshot_rejects_reused_artifact_with_mismatched_role_and_result(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "evidence.md"
            evidence.write_text(
                "# Review Result: FAIL\nNo verification commands were run.\n",
                encoding="utf-8",
            )
            shared_ref = {
                "path": "evidence.md",
                "sha256": hashlib.sha256(evidence.read_bytes()).hexdigest(),
            }
            data.update(
                lifecycle_state="complete",
                current_batch=data["planned_batches"],
                attempt_report_artifact=dict(shared_ref),
                last_review_result="pass",
                last_review_artifact=dict(shared_ref),
                final_verification="pass",
                final_verification_artifact=dict(shared_ref),
                final_review_result="pass",
                final_review_artifact=dict(shared_ref),
                next_owner="user",
            )

            with self.assertRaisesRegex(AssertionError, "artifact|evidence|result|role|distinct"):
                self.validator.validate_handoff_contract(data, "mixed-complete")
                self.validator.validate_evidence_artifacts(data, root, "mixed-complete")

    def test_runtime_evidence_manifest_binds_artifact_role_and_result(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="complete",
            current_batch=data["planned_batches"],
            contract_revision=5,
            last_review_result="pass",
            final_verification="pass",
            final_review_result="pass",
            next_owner="user",
        )
        specs = {
            "attempt_report_artifact": ("attempt-report.md", "attempt-report", "pass", 1),
            "last_review_artifact": ("batch-review.md", "batch-review", "pass", 2),
            "final_verification_artifact": ("final-verification.md", "final-verification", "pass", 3),
            "final_review_artifact": ("final-review.md", "final-review", "fail", 4),
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            materialize_schema5_lease(data if "data" in locals() else current, root)
            for key, (path, role, result, revision) in specs.items():
                target = root / path
                target.write_text(
                    schema5_evidence_manifest(role, result, current_batch=2, contract_revision=revision),
                    encoding="utf-8",
                )
                data[key] = {"path": path, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}
            self.validator.validate_handoff_contract(data, "distinct-complete")
            with self.assertRaisesRegex(AssertionError, "evidence result"):
                self.validator.validate_evidence_artifacts(data, root, "distinct-complete")

    def test_timeout_audit_can_bind_report_and_review_without_other_role_reuse(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            materialize_schema5_lease(data if "data" in locals() else current, root)
            timeout = root / "timeout-audit.md"
            timeout.write_text(schema5_evidence_manifest("timeout-audit", "blocked"), encoding="utf-8")
            ref = {"path": timeout.name, "sha256": hashlib.sha256(timeout.read_bytes()).hexdigest()}
            data.update(
                lifecycle_state="blocked",
                contract_revision=2,
                attempt_report_artifact=dict(ref),
                last_review_result="blocked",
                last_review_artifact=dict(ref),
                blocked_reason="external agent timed out",
                blocker_owner="external-agent",
                resume_condition="timeout audit resolved",
                next_owner="codex-brief-antigravity-review",
            )
            self.validator.validate_handoff_contract(data, "timeout")
            self.validator.validate_evidence_artifacts(data, root, "timeout")

        conflicting = dict(data)
        conflicting["last_review_artifact"] = dict(data["last_review_artifact"])
        conflicting["last_review_artifact"]["sha256"] = "c" * 64
        with self.assertRaisesRegex(AssertionError, "distinct by role"):
            self.validator.validate_handoff_contract(conflicting, "timeout-conflict")

    def test_complete_rejects_preflight_review_as_batch_review_evidence(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        data.update(
            lifecycle_state="complete",
            current_batch=data["planned_batches"],
            contract_revision=5,
            last_review_result="pass",
            final_verification="pass",
            final_review_result="pass",
            next_owner="user",
        )
        specs = {
            "attempt_report_artifact": ("attempt.md", "attempt-report", "pass", 1),
            "last_review_artifact": ("preflight.md", "preflight-review", "pass", 2),
            "final_verification_artifact": ("verification.md", "final-verification", "pass", 3),
            "final_review_artifact": ("final-review.md", "final-review", "pass", 4),
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            materialize_schema5_lease(data if "data" in locals() else current, root)
            for key, (path, role, result, revision) in specs.items():
                target = root / path
                target.write_text(
                    schema5_evidence_manifest(role, result, current_batch=2, contract_revision=revision),
                    encoding="utf-8",
                )
                data[key] = {"path": path, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}
            self.validator.validate_handoff_contract(data, "preflight-as-batch")
            with self.assertRaisesRegex(AssertionError, "evidence role|batch-review"):
                self.validator.validate_evidence_artifacts(data, root, "preflight-as-batch")

    def test_timeout_audit_is_blocked_only_and_cannot_satisfy_complete(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            timeout = root / "timeout.md"
            timeout.write_text(evidence_manifest("timeout-audit", "pass"), encoding="utf-8")
            shared = {"path": timeout.name, "sha256": hashlib.sha256(timeout.read_bytes()).hexdigest()}
            data.update(
                lifecycle_state="complete",
                current_batch=data["planned_batches"],
                attempt_report_artifact=dict(shared),
                last_review_result="pass",
                last_review_artifact=dict(shared),
                final_verification="pass",
                final_verification_artifact=artifact("verification.md"),
                final_review_result="pass",
                final_review_artifact=artifact("final-review.md"),
                next_owner="user",
            )
            with self.assertRaisesRegex(AssertionError, "timeout-audit|distinct|blocked"):
                self.validator.validate_handoff_contract(data, "timeout-complete")

    def test_runtime_rejects_stale_batch_and_attempt_evidence(self):
        data = self._awaiting_contract()
        data.update(attempt=9, contract_revision=10)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            materialize_schema5_lease(data if "data" in locals() else current, root)
            specs = {
                "attempt_report_artifact": ("report.md", "attempt-report", 1),
                "last_review_artifact": ("review.md", "batch-review", 2),
            }
            for key, (path, role, revision) in specs.items():
                target = root / path
                target.write_text(
                    schema5_evidence_manifest(role, "pass", current_batch=1, attempt=1, contract_revision=revision),
                    encoding="utf-8",
                )
                data[key] = {"path": path, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}
            with self.assertRaisesRegex(AssertionError, "required batch|required attempt"):
                self.validator.validate_evidence_artifacts(data, root, "stale-evidence")

    def test_runtime_complete_requires_and_validates_previous_status(self):
        previous = self._awaiting_contract("pass")
        previous["contract_revision"] = 4
        current = dict(previous)
        current.update(
            lifecycle_state="complete",
            contract_revision=5,
            final_review_result="pass",
            final_review_artifact=artifact("final-review.md"),
            next_owner="user",
        )
        previous_bytes = b"canonical previous status revision 4\n"
        previous_sha = hashlib.sha256(previous_bytes).hexdigest()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            materialize_schema5_lease(data if "data" in locals() else current, root)
            specs = {
                "attempt_report_artifact": ("report.md", "attempt-report", "pass", 1, "b" * 64),
                "last_review_artifact": ("batch-review.md", "batch-review", "pass", 2, "c" * 64),
                "final_verification_artifact": ("verification.md", "final-verification", "pass", 3, "d" * 64),
                "final_review_artifact": ("final-review.md", "final-review", "pass", 4, previous_sha),
            }
            for key, (path, role, result, revision, source_sha) in specs.items():
                target = root / path
                target.write_text(
                    schema5_evidence_manifest(
                        role,
                        result,
                        current_batch=2,
                        contract_revision=revision,
                        canonical_sha256=source_sha,
                    ),
                    encoding="utf-8",
                )
                current[key] = {"path": path, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}
            previous.update(
                attempt_report_artifact=current["attempt_report_artifact"],
                last_review_artifact=current["last_review_artifact"],
                final_verification_artifact=current["final_verification_artifact"],
            )
            with self.assertRaisesRegex(AssertionError, "requires previous canonical status"):
                self.validator.validate_evidence_artifacts(current, root, "complete-without-history")
            self.validator.validate_evidence_artifacts(
                current,
                root,
                "complete-with-history",
                previous=previous,
                previous_status_sha256=previous_sha,
            )

    def test_previous_status_binds_nonfinal_promotion_to_reviewed_attempt(self):
        previous = self.validator.extract_handoff_contract(self.handoff, "handoff")
        previous.update(
            lifecycle_state="ready-for-review",
            attempt=3,
            contract_revision=3,
            attempt_report_artifact=artifact("report.md"),
            next_owner="codex-brief-antigravity-review",
        )
        current = dict(previous)
        current.update(
            lifecycle_state="ready-for-brief",
            current_batch=2,
            attempt=1,
            contract_revision=4,
            last_review_result="pass",
            last_review_artifact=artifact("review.md"),
            next_owner="codex-brief-antigravity-review",
        )
        previous_sha = hashlib.sha256(b"reviewed attempt 3 status\n").hexdigest()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            materialize_schema5_lease(data if "data" in locals() else current, root)
            report = root / "report.md"
            review = root / "review.md"
            report.write_text(
                schema5_evidence_manifest("attempt-report", "pass", attempt=2, contract_revision=1),
                encoding="utf-8",
            )
            review.write_text(
                schema5_evidence_manifest(
                    "batch-review",
                    "pass",
                    attempt=2,
                    contract_revision=3,
                    canonical_sha256=previous_sha,
                ),
                encoding="utf-8",
            )
            report_ref = {"path": report.name, "sha256": hashlib.sha256(report.read_bytes()).hexdigest()}
            review_ref = {"path": review.name, "sha256": hashlib.sha256(review.read_bytes()).hexdigest()}
            previous["attempt_report_artifact"] = report_ref
            current["attempt_report_artifact"] = report_ref
            current["last_review_artifact"] = review_ref
            with self.assertRaisesRegex(AssertionError, "wrong source attempt"):
                self.validator.validate_evidence_artifacts(
                    current,
                    root,
                    "wrong-attempt-promotion",
                    previous=previous,
                    previous_status_sha256=previous_sha,
                )

    def test_major_self_evolution_requires_specific_validated_contract(self):
        rule = (ROOT / "references" / "self-evolution-rule.md").read_text(encoding="utf-8")
        self.assertIn("specific OpenSpec change", rule)
        self.assertIn("passes\nstrict validation", rule)
        self.assertNotIn("after user approval or an explicitly approved", rule)

    def test_openspec_closeout_requires_task_reconciliation_and_archive_validation(self):
        self.assertIn("OpenSpec closeout", self.approved)
        self.assertIn("references/completion-contract.md", self.approved)
        self.assertNotIn("Reconcile `tasks.md`", self.approved)
        self.assertNotIn("strict validation after archive", self.approved)
        normalized_completion = " ".join(self.completion.split())
        self.assertIn("Reconcile `tasks.md`", normalized_completion)
        self.assertIn("strict validation after archive", normalized_completion)

    def test_superpowers_adapter_and_preflight_review_are_explicit(self):
        adapter = (ROOT / "references" / "superpowers-adapter.md").read_text(encoding="utf-8")
        self.assertIn("single OpenSpec design contract", adapter)
        self.assertIn("never grants Git permission", adapter)
        self.assertIn("Preflight Review", adapter)
        self.assertIn("artifact revision", adapter)
        self.assertIn("Preflight uses only `PASS` or `BLOCKED`", adapter)
        self.assertNotIn("Preflight `FAIL`", adapter + self.approved)

    def test_brief_trigger_excludes_state_changing_and_final_completion(self):
        if not (BRIEF_ROOT / "SKILL.md").is_file():
            self.skipTest("companion repository is not checked out")
        description = (BRIEF_ROOT / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
        for expected in (
            "non-state-changing", "read-only", "does not request fixes",
            "final completion", "valid Handoff Contract", "file edits",
            "workflow/template changes",
        ):
            self.assertIn(expected, description)


    def _valid_lease(self):
        return {
            "decision_id": "decision-001",
            "artifact_revision": 2,
            "artifact_sha256": "a" * 64,
            "approved_scope": "approved source implementation",
            "approved_actions": ["run-safe-tests", "fix-review-finding"],
            "risk_profile": "standard",
            "decision_source": "ai-proposed/user-approved",
            "owner_instance_id": "codex-control-01",
            "status": "valid",
            "invalidation_conditions": ["scope-change", "risk-change", "user-correction"],
        }

    def _valid_review_evidence(self):
        return {
            "actual_diff_inspected": True,
            "production_wiring_trace": ["source -> transform -> runtime"],
            "critical_reruns": ["python3 -m unittest focused -v"],
            "independent_probe": {
                "kind": "adversarial",
                "command": "probe --bounded-input",
                "result": "pass",
            },
            "copy_fields": {
                "expected": ["id", "version"],
                "observed": ["id", "version"],
            },
            "claims": [{
                "claim": "restart recovery",
                "mechanism": "runner retry state machine",
                "evidence": "focused recovery probe",
            }],
        }

    def _schema5_contract(self):
        data = self.validator.extract_handoff_contract(self.handoff, "handoff")
        for key in (
            "executor_agent", "independent_reviewer_agent", "decision_owner",
        ):
            data.pop(key, None)
        data.update({
            "schema_version": 5,
            "control_plane_owner": {
                "agent_product": "codex",
                "agent_instance_id": "codex-control-01",
                "agent_role": "control-plane",
                "capability_profile": "control-plane-high",
            },
            "executor_assignment": {
                "agent_product": "codex",
                "agent_instance_id": "codex-executor-01",
                "agent_role": "executor",
                "capability_profile": "cohesive-medium",
            },
            "independent_reviewer_assignment": {
                "agent_product": "codex",
                "agent_instance_id": "codex-reviewer-01",
                "agent_role": "independent-reviewer",
                "capability_profile": "control-plane-high",
            },
            "decision_source": "ai-proposed/user-approved",
            "confirmation_lease": {
                "decision_id": "decision-001",
                "path": "docs/agent-collab/add-example-change/confirmation-lease.md",
                "sha256": "c" * 64,
            },
        })
        data["readonly_fields"] = list(self.validator.IMMUTABLE_FIELDS)
        return data

    def test_tiered_01_platform_permission_reuses_safe_command_lease(self):
        validate = getattr(self.validator, "validate_confirmation_lease", None)
        self.assertTrue(callable(validate), "Confirmation Lease behavior is not implemented")
        result = validate(self._valid_lease(), {
            "action": "run-safe-tests",
            "artifact_revision": 2,
            "artifact_sha256": "a" * 64,
            "scope": "approved source implementation",
            "risk_profile": "standard",
            "platform_authorized": True,
            "business_authorized": False,
        })
        self.assertEqual("reuse", result)

    def test_tiered_02_platform_permission_cannot_authorize_production_deletion(self):
        validate = getattr(self.validator, "validate_confirmation_lease", None)
        self.assertTrue(callable(validate), "layered authorization behavior is not implemented")
        with self.assertRaisesRegex(AssertionError, "business/production authorization"):
            validate(self._valid_lease(), {
                "action": "production-deletion",
                "artifact_revision": 2,
                "artifact_sha256": "a" * 64,
                "scope": "approved source implementation",
                "risk_profile": "strict",
                "platform_authorized": True,
                "business_authorized": False,
            })

    def test_tiered_03_ai_proposed_user_approved_provenance_is_preserved(self):
        validate = getattr(self.validator, "validate_decision_source", None)
        self.assertTrue(callable(validate), "decision provenance behavior is not implemented")
        self.assertEqual(
            "ai-proposed/user-approved",
            validate("ai-proposed/user-approved"),
        )
        with self.assertRaisesRegex(AssertionError, "decision_source"):
            validate("user-originated-from-ai-proposal")

    def test_tiered_04_mechanical_low_ambiguity_blocks_instead_of_designing(self):
        validate = getattr(self.validator, "validate_capability_action", None)
        self.assertTrue(callable(validate), "capability authority behavior is not implemented")
        self.assertEqual(
            "BLOCKED",
            validate("mechanical-low", "bounded-edit", ambiguity=True),
        )

    def test_tiered_05_high_review_detects_copy_field_loss_after_executor_pass(self):
        validate = getattr(self.validator, "validate_high_review_evidence", None)
        self.assertTrue(callable(validate), "High Review behavior is not implemented")
        evidence = self._valid_review_evidence()
        evidence["copy_fields"]["observed"] = ["id"]
        with self.assertRaisesRegex(AssertionError, "copy-field loss"):
            validate(evidence)

    def test_tiered_06_high_review_requires_independent_adversarial_probe(self):
        validate = getattr(self.validator, "validate_high_review_evidence", None)
        self.assertTrue(callable(validate), "independent probe behavior is not implemented")
        evidence = self._valid_review_evidence()
        evidence["independent_probe"] = None
        with self.assertRaisesRegex(AssertionError, "independent.*probe"):
            validate(evidence)

    def test_tiered_07_high_review_traces_claim_to_runtime_mechanism(self):
        validate = getattr(self.validator, "validate_high_review_evidence", None)
        self.assertTrue(callable(validate), "claim-to-mechanism behavior is not implemented")
        evidence = self._valid_review_evidence()
        evidence["claims"][0]["mechanism"] = ""
        with self.assertRaisesRegex(AssertionError, "claim-to-mechanism"):
            validate(evidence)

    def test_tiered_08_same_product_instances_cannot_self_review(self):
        contract = self._schema5_contract()
        self.validator.validate_handoff_contract(contract, "same-product-distinct-instance")
        contract["independent_reviewer_assignment"]["agent_instance_id"] = "codex-executor-01"
        with self.assertRaisesRegex(AssertionError, "instance"):
            self.validator.validate_handoff_contract(contract, "same-instance-self-review")

    def test_tiered_09_single_correction_creates_candidate_without_promotion(self):
        evaluate = getattr(self.validator, "evaluate_learning_candidate", None)
        self.assertTrue(callable(evaluate), "Learning Candidate behavior is not implemented")
        result = evaluate({
            "severity": "low",
            "scope": "task-local",
            "independent_reproductions": 1,
            "event_kind": "wording-correction",
        })
        self.assertTrue(result["candidate_created"])
        self.assertFalse(result["proposal_allowed"])
        self.assertFalse(result["implementation_allowed"])

    def test_tiered_10_high_severity_candidate_is_proposal_only_without_approval(self):
        evaluate = getattr(self.validator, "evaluate_learning_candidate", None)
        self.assertTrue(callable(evaluate), "Learning Candidate promotion behavior is not implemented")
        result = evaluate({
            "severity": "high",
            "scope": "global",
            "independent_reproductions": 1,
            "event_kind": "false-pass",
            "openspec_approval": False,
        })
        self.assertTrue(result["proposal_allowed"])
        self.assertFalse(result["implementation_allowed"])


    def _lease_artifact_text(
        self, owner_instance_id="codex-control-01", risk_profile="standard",
        decision_source="ai-proposed/user-approved",
    ):
        return (
            "<!-- COOP_CONFIRMATION_LEASE_START -->\n"
            "```yaml\n"
            "decision_id: decision-001\n"
            "artifact_revision: 2\n"
            f"artifact_sha256: {'a' * 64}\n"
            "approved_scope: approved source implementation\n"
            "approved_actions:\n"
            "  - run-safe-tests\n"
            f"risk_profile: {risk_profile}\n"
            f"decision_source: {decision_source}\n"
            f"owner_instance_id: {owner_instance_id}\n"
            "status: valid\n"
            "invalidation_conditions:\n"
            "  - scope-change\n"
            "```\n"
            "<!-- COOP_CONFIRMATION_LEASE_END -->\n"
        )

    def test_schema5_runtime_validates_confirmation_lease_artifact(self):
        validate = getattr(self.validator, "validate_confirmation_lease_artifact", None)
        self.assertTrue(callable(validate), "runtime lease artifact validation is not implemented")
        data = self._schema5_contract()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / data["confirmation_lease"]["path"]
            target.parent.mkdir(parents=True)
            target.write_text(self._lease_artifact_text(), encoding="utf-8")
            data["confirmation_lease"]["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
            validate(data, root, "valid-lease")
            target.write_text(self._lease_artifact_text("wrong-owner"), encoding="utf-8")
            data["confirmation_lease"]["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
            with self.assertRaisesRegex(AssertionError, "owner_instance_id"):
                validate(data, root, "wrong-owner")
            target.write_text(self._lease_artifact_text(risk_profile="strict"), encoding="utf-8")
            data["confirmation_lease"]["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
            with self.assertRaisesRegex(AssertionError, "risk_profile"):
                validate(data, root, "wrong-risk")
            target.write_text(self._lease_artifact_text(decision_source="revoked"), encoding="utf-8")
            data["confirmation_lease"]["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
            with self.assertRaisesRegex(AssertionError, "revoked|valid"):
                validate(data, root, "revoked-lease")

    def test_schema5_high_review_artifact_requires_mechanism_sections(self):
        validate = getattr(self.validator, "validate_high_review_artifact_text", None)
        self.assertTrue(callable(validate), "runtime High Review artifact validation is not implemented")
        incomplete = schema5_evidence_manifest("batch-review", "pass", high_review=False)
        with self.assertRaisesRegex(AssertionError, "actual diff|production wiring|claim-to-mechanism|independent"):
            validate(incomplete, "incomplete-review")
        complete = incomplete + (
            "\nActual files and complete diff inspected\n"
            "Copy/transform/production wiring trace\n"
            "Critical reruns\n"
            "Claim-to-mechanism support\n"
            "Independent adversarial probe\n"
        )
        validate(complete, "complete-review")

    def test_schema4_inventory_blocks_active_and_allows_complete_history(self):
        inventory = getattr(self.validator, "inventory_active_schema4_statuses", None)
        self.assertTrue(callable(inventory), "schema-4 drain inventory is not implemented")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            status = root / "docs" / "agent-collab" / "legacy" / "status.md"
            status.parent.mkdir(parents=True)
            status.write_text(
                "<!-- COOP_HANDOFF_CONTRACT_START -->\n```yaml\n"
                "schema_version: 4\nchange_id: legacy\ncontract_revision: 2\n"
                "lifecycle_state: ready-for-execution\n```\n"
                "<!-- COOP_HANDOFF_CONTRACT_END -->\n",
                encoding="utf-8",
            )
            self.assertEqual([status.resolve()], inventory([root]))
            status.write_text(status.read_text().replace("ready-for-execution", "complete"), encoding="utf-8")
            self.assertEqual([], inventory([root]))


    def test_schema5_revoked_lease_blocks_and_cannot_be_reactivated(self):
        before = self._schema5_contract()
        before["confirmation_lease_status"] = "valid"
        after = dict(before)
        after.update(
            lifecycle_state="blocked",
            contract_revision=before["contract_revision"] + 1,
            last_review_result="blocked",
            last_review_artifact=artifact("docs/review/revoked-lease.md"),
            blocked_reason="user revoked the prior decision",
            blocker_owner="user",
            resume_condition="create a new explicitly authorized contract and Lease",
            next_owner="user",
            confirmation_lease_status="revoked",
        )
        self.validator.validate_transition(before, after, "revoke-lease")
        recovered = dict(after)
        recovered.update(
            lifecycle_state="ready-for-execution",
            contract_revision=after["contract_revision"] + 1,
            attempt=after["attempt"] + 1,
            last_review_result="not-run",
            last_review_artifact=None,
            blocked_reason=None,
            blocker_owner="none",
            resume_condition=None,
            next_owner="external-agent",
            confirmation_lease_status="valid",
        )
        with self.assertRaisesRegex(AssertionError, "revoked|new.*Lease|reactivat"):
            self.validator.validate_transition(after, recovered, "reactivate-old-lease")


if __name__ == "__main__":
    unittest.main()
