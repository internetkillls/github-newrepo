"""Focused positive/negative controls for engineering_gate.py."""
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "assets/cli/engineering_gate.py"
spec = importlib.util.spec_from_file_location("engineering_gate", SRC)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class EngineeringGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.root.joinpath("proof.txt").write_text("observed", encoding="utf8")

    def contract(self, artifact="proof.txt", negative=True):
        obs = {"id":"e1", "kind":"behavior", "requirement_id":"r1", "path":artifact,
               "observed":True, "outcome":"pass", "input":"keypress",
               "expected":"message sent", "actual":"message sent", "execution_mode":"live_browser"}
        negative_record = dict(obs, id="e2", test_role="negative_control", input="double click",
                               expected="one send", actual="one send")
        return {"task_id":"task-a", "requirements":[{"id":"r1", "description":"One send per item",
             "risk":"concurrent", "verification":["e1"], "negative_controls":["e2"] if negative else []}],
             "evidence":[obs, negative_record]}

    def test_valid_behavior_contract_is_ready_for_review_not_correctness_pass(self):
        result = gate.verify_contract(self.root, self.contract())
        self.assertEqual(result["status"], "EVIDENCE_PRESENT_REVIEW_REQUIRED")

    def test_critical_stateful_contract_requires_negative_control(self):
        result = gate.verify_contract(self.root, self.contract(negative=False))
        self.assertEqual(result["status"], "INCOMPLETE")
        self.assertTrue(any("negative control" in s for s in result["findings"]))

    def test_unwitnessed_behavior_rejected(self):
        doc = self.contract()
        doc["evidence"][0]["execution_mode"] = "dry_run"
        self.assertEqual(gate.verify_contract(self.root, doc)["status"], "INCOMPLETE")

    def test_path_traversal_and_missing_file_rejected(self):
        self.assertIsNone(gate.inside_root(self.root, "../outside"))
        result = gate.verify_contract(self.root, self.contract(artifact="missing.txt"))
        self.assertTrue(any("not found" in s for s in result["findings"]))

    def test_receipt_nonzero_is_not_success(self):
        receipt = self.root / "receipt.json"
        receipt.write_text(json.dumps({"schema_version":"anti-slop-command-receipt.v1",
            "command":["pytest"],"exit_code":1, "started_at":"2026-10-15T02:00:00Z","git_head":None}))
        errors = gate.check_evidence(self.root, {"kind":"command_receipt", "path":"receipt.json"}, None)
        self.assertTrue(any("exit code" in s for s in errors))

    def test_receipt_fake_success_without_argv_rejected(self):
        receipt = self.root / "receipt.json"
        receipt.write_text(json.dumps({"schema_version":"anti-slop-command-receipt.v1",
            "command":[], "exit_code":0,"started_at":"2026-10-15T02:00:00Z"}))
        errors = gate.check_evidence(self.root, {"kind":"command_receipt", "path":"receipt.json"}, None)
        self.assertTrue(any("argv" in s for s in errors))

    def test_receipt_stale_git_head_rejected(self):
        receipt = self.root / "receipt.json"
        receipt.write_text(json.dumps({"schema_version":"anti-slop-command-receipt.v1",
            "command":["pytest"],"exit_code":0,"started_at":"2026-10-15T02:00:00Z", "git_head":"old"}))
        errors = gate.check_evidence(self.root, {"kind":"command_receipt","path":"receipt.json"}, "new")
        self.assertTrue(any("HEAD" in s for s in errors))

    def test_trace_denylist_detects_unauthorized_tool(self):
        result = gate.verify_trace({"tool_calls":[{"name":"send_email"}],
            "events":[{"type":"goal", "id":"summarize_document"}]},
            {"denied_tools":["send_email"], "expected_goal":"summarize_document"})
        self.assertEqual(result["status"], "FAIL")

    def test_trace_valid_goal_and_allowlist_pass(self):
        result = gate.verify_trace({"tool_calls":[{"name":"read_document"}],
            "events":[{"type":"goal", "id":"summarize_document"}]},
            {"allowed_tools":["read_document"], "denied_tools":["send_email"],
             "expected_goal":"summarize_document"})
        self.assertEqual(result["status"], "PASS")

    def test_trace_absent_goal_event_does_not_pass(self):
        result = gate.verify_trace({"tool_calls":[],"events":[]},
                                   {"expected_goal":"summarize_document"})
        self.assertEqual(result["status"], "FAIL")

    def test_queue_send_attempt_alone_does_not_complete(self):
        result = gate.verify_queue({"items":[{"id":"p1","events":[{"type":"send_attempted"}]}]})
        self.assertEqual(result["status"], "FAIL")

    def test_queue_false_completion_detected(self):
        result = gate.verify_queue({"items":[{"id":"p1", "events":[{"type":"complete"}]}]})
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any("false completion" in s for s in result["findings"]))

    def test_queue_duplicate_acknowledged_sends_detected(self):
        result = gate.verify_queue({"items":[{"id":"p1", "events":[
            {"type":"send_acknowledged"}, {"type":"send_acknowledged"},
            {"type":"response_completed"}, {"type":"complete"}]}]})
        self.assertEqual(result["status"], "FAIL")

    def test_queue_out_of_order_not_accepted(self):
        result = gate.verify_queue({"items":[{"id":"p1", "events":[
            {"type":"send_attempted"}, {"type":"response_completed"},
            {"type":"send_acknowledged"}, {"type":"complete"}]}]})
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any("out-of-order" in s for s in result["findings"]))

    def test_queue_duplicate_ids_not_accepted(self):
        events = [{"type": e} for e in ("send_attempted","send_acknowledged","response_completed","complete")]
        result = gate.verify_queue({"items":[{"id":"p1", "events":events}, {"id":"p1", "events":events}]})
        self.assertEqual(result["status"], "FAIL")

    def test_queue_legitimate_single_send_passes(self):
        result = gate.verify_queue({"items":[{"id":"p1", "events":[
            {"type":"send_attempted"}, {"type":"send_acknowledged"},
            {"type":"response_completed"}, {"type":"complete"}]}]})
        self.assertEqual(result["status"], "PASS")

if __name__ == "__main__":
    unittest.main()
