import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF_ROOT = ROOT.parent / "codex-brief-antigravity-review"


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
        cls.handoff = (ROOT / "references" / "handoff-contract.md").read_text(encoding="utf-8")

    def test_description_does_not_claim_brief_or_external_batch_work(self):
        description = self.skill.split("---", 2)[1]
        self.assertNotIn("task or step breakdowns", description)
        self.assertNotIn("external-agent handoff", description)
        self.assertIn("development change", description)

    def test_review_and_fix_is_not_review_only(self):
        self.assertIn("Review and fix", self.request_modes)
        self.assertIn("not Review-only", self.request_modes)

    def test_openspec_and_superpowers_do_not_duplicate_design_approval(self):
        self.assertIn("single design approval", self.approved)
        self.assertIn("does not require a duplicate", self.approved)

    def test_evidence_gate_operates_on_slices_not_micro_steps(self):
        self.assertIn("business slice", self.approved)
        self.assertIn("not every TDD micro-step", self.approved)

    def test_inline_implementation_requires_review(self):
        self.assertIn("inline implementation", self.approved)
        self.assertIn("Review PASS", self.approved)

    def test_handoff_schema_has_closure_fields(self):
        for expected in (
            "schema_version: 2",
            "lifecycle_state:",
            "attempt:",
            "last_review_result:",
            "blocker_owner:",
            "resume_condition:",
            "final_verification:",
            "final_review_result:",
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

    def test_fallback_scalar_parser_handles_yaml_booleans_and_null(self):
        self.assertIs(self.validator.parse_scalar("true"), True)
        self.assertIs(self.validator.parse_scalar("false"), False)
        self.assertIsNone(self.validator.parse_scalar("null"))

    def test_fail_transition_cannot_advance_batch(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(lifecycle_state="ready-for-review", last_review_result="not-run")
        after = dict(before)
        after.update(
            lifecycle_state="needs-fix",
            last_review_result="fail",
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
        )
        after = dict(before)
        after.update(
            lifecycle_state="awaiting-final-verification",
            last_review_result="pass",
            contract_revision=before["contract_revision"] + 1,
            next_owner="openspec-superpower-change",
        )
        self.validator.validate_transition(before, after, "final-pass")

    def test_both_skills_publish_same_closure_fields(self):
        brief_handoff = (BRIEF_ROOT / "references" / "handoff-contract.md").read_text(encoding="utf-8")
        for expected in (
            "schema_version: 2",
            "lifecycle_state:",
            "attempt:",
            "last_review_result:",
            "final_verification:",
            "final_review_result:",
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
        with self.assertRaisesRegex(AssertionError, "blocked review"):
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
        brief_handoff = (BRIEF_ROOT / "references" / "handoff-contract.md").read_text(encoding="utf-8")
        self.assertEqual(self.handoff, brief_handoff)

    def test_final_gate_failure_can_return_to_fix_with_new_attempt(self):
        before = self.validator.extract_handoff_contract(self.handoff, "handoff")
        before.update(
            lifecycle_state="awaiting-final-verification",
            current_batch=before["planned_batches"],
            last_review_result="pass",
            next_owner="openspec-superpower-change",
        )
        after = dict(before)
        after.update(
            lifecycle_state="needs-fix",
            attempt=before["attempt"] + 1,
            contract_revision=before["contract_revision"] + 1,
            last_review_result="fail",
            final_review_result="fail",
            next_owner="openspec-superpower-change",
        )
        self.validator.validate_transition(before, after, "final-gate-fix")


if __name__ == "__main__":
    unittest.main()
