import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "assets" / "cli" / "antislop.py"
spec = importlib.util.spec_from_file_location("antislop", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def evt(event_id, actor="user", kind="decision", status="accepted", **kw):
    base = {"event_id": event_id, "turn_id": event_id, "actor": actor,
            "origin": "user-authored" if actor == "user" else "prior-assistant",
            "kind": kind, "status": status, "text": f"Example {event_id}",
            "evidence_refs": [{"source_id": "fixture", "locator": event_id}], "__line": 1}
    base.update(kw)
    return base


class TestLedger(unittest.TestCase):
    def test_assistant_proposal_is_not_accepted_without_user_anchor(self):
        rows = [evt("a", "assistant", "proposal", "accepted")]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("assistant-origin" in x for x in errors))

    def test_explicit_adoption_allows_acceptance(self):
        rows = [evt("a", "assistant", "proposal", "accepted", adopted_by="b"),
                evt("b", "user", "adoption", "accepted", target_event_id="a")]
        errors, _ = mod.validate_ledger(rows)
        self.assertFalse(errors, errors)

    def test_unaccepted_proposal_preserved(self):
        rows = [evt("a", "assistant", "proposal", "proposed"),
                evt("b", "user", "correction", "stated")]
        summary = mod.recap(rows)
        self.assertTrue(summary["valid"])
        self.assertEqual([p["event_id"] for p in summary["unadopted_proposals"]], ["a"])
        self.assertEqual([p["event_id"] for p in summary["corrections"]], ["b"])

    def test_supersession_must_point_to_known_replacement(self):
        rows = [evt("a", status="superseded", superseded_by="missing")]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("unknown event" in x for x in errors))

    def test_missing_source_anchor_blocks_material_entry(self):
        rows = [evt("a", evidence_refs=[])]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("evidence anchor" in x for x in errors))

    def test_sense_polysemy_is_not_automatically_invalid(self):
        rows = [evt("a", kind="term-sense", status="stated", text="Sense X"),
                evt("b", kind="term-sense", status="stated", text="Sense Y")]
        self.assertFalse(mod.validate_ledger(rows)[0])

    def test_findings_confirmed_require_witness(self):
        rows = [{"__line": 1, "finding_id": "f1", "class": "C", "status": "CONFIRMED"}]
        self.assertTrue(mod.validate_findings(rows))

    def test_good_finding_schema_is_not_truth_check(self):
        rows = [{"__line": 1, "finding_id": "f1", "class": "L", "status": "CONFIRMED",
                 "proof_type": "conversation_anchor", "artifact_anchor": {"locator": "turn1"},
                 "proof_anchor": {"locator": "turn2"}, "expectation": "p", "actual": "not-p",
                 "root_dependency": "attribution", "repair": "fix", "retest": "rerun"}]
        self.assertFalse(mod.validate_findings(rows))

    def test_style_hit_never_auto_fails(self):
        hits = mod.scan_text("Di era digital saat ini, bukan X tetapi Y.")
        self.assertGreaterEqual(len(hits), 1)
        self.assertTrue(all(x["status"] == "STYLE-SIGNAL" for x in hits))

    def test_plain_prose_does_not_trigger(self):
        self.assertEqual(mod.scan_text("Hasil uji berubah ketika input frekuensi dinaikkan."), [])

    def test_user_quoted_proposal_not_recorded_as_accepted(self):
        rows = [evt("a", origin="user-quoted", kind="decision", status="accepted")]
        summary = mod.recap(rows)
        self.assertFalse(summary["accepted_events"])

    def test_assistant_question_without_acceptance_not_active(self):
        rows = [evt("a", "assistant", kind="question", status="proposed"),
                evt("b", "user", kind="question", status="stated")]
        summary = mod.recap(rows)
        self.assertEqual([p["event_id"] for p in summary["active_questions"]], ["b"])

    def test_unrelated_user_adoption_does_not_authorize_proposal(self):
        rows = [evt("a", "assistant", "proposal", "accepted", adopted_by="b"),
                evt("b", "user", "adoption", "accepted", target_event_id="c"),
                evt("c", "assistant", "proposal", "proposed")]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("does not identify" in s for s in errors), errors)

    def test_generic_go_on_is_not_blanket_adoption(self):
        rows = [evt("a", "assistant", "proposal", "proposed"),
                evt("b", "user", "adoption", "stated", text="go on")]
        summary = mod.recap(rows)
        self.assertTrue(summary["valid"])
        self.assertEqual([e["event_id"] for e in summary["unadopted_proposals"]], ["a"])
        self.assertTrue(any("blanket acceptance" in w for w in summary["warnings"]))

    def test_explicit_question_replacement_is_effective(self):
        rows = [evt("q1", kind="question", status="stated", text="Build new system"),
                evt("q2", kind="question", status="stated", replaces="q1", text="Audit existing system")]
        summary = mod.recap(rows)
        self.assertTrue(summary["valid"], summary)
        self.assertEqual([x["event_id"] for x in summary["active_questions"]], ["q2"])

    def test_simultaneous_questions_different_scopes(self):
        rows = [evt("q1", kind="question", status="stated", scope="design"),
                evt("q2", kind="question", status="stated", scope="testing")]
        summary = mod.recap(rows)
        self.assertEqual(len(summary["active_questions"]), 2)
        self.assertFalse(any("multiple unresolved" in w for w in summary["warnings"]))

    def test_ambiguous_questions_same_scope_stay_visible(self):
        rows = [evt("q1", kind="question", status="stated"),
                evt("q2", kind="question", status="stated")]
        summary = mod.recap(rows)
        self.assertEqual(len(summary["active_questions"]), 2)
        self.assertTrue(any("multiple unresolved" in w for w in summary["warnings"]))

    def test_correction_target_changes_effective_commitment(self):
        rows = [evt("d1", kind="decision", status="accepted"),
                evt("corr", kind="correction", status="stated", corrects="d1")]
        summary = mod.recap(rows)
        self.assertTrue(summary["valid"])
        self.assertEqual(summary["accepted_events"], [])
        self.assertEqual([e["event_id"] for e in summary["corrected_prior_events"]], ["d1"])

    def test_correction_without_target_is_uncertain(self):
        rows = [evt("d1", kind="decision", status="accepted"),
                evt("corr", kind="correction", status="stated")]
        summary = mod.recap(rows)
        self.assertEqual(len(summary["accepted_events"]), 1)
        self.assertTrue(any("application unresolved" in w for w in summary["warnings"]))

    def test_question_replacement_cycle_rejected(self):
        rows = [evt("q1", kind="question", status="stated", replaces="q2"),
                evt("q2", kind="question", status="stated", replaces="q1")]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("cycle" in s for s in errors))

    def test_unadopted_assistant_question_cannot_reframe(self):
        rows = [evt("q1", kind="question", status="stated"),
                evt("q2", actor="assistant", kind="question", status="proposed", replaces="q1")]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("cannot replace" in s for s in errors))

    def test_out_of_order_adoption_fails(self):
        rows = [evt("b", kind="adoption", status="accepted", target_event_id="a"),
                evt("a", actor="assistant", kind="proposal", status="accepted", adopted_by="b")]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("must follow" in s for s in errors))

    def test_empty_ledger_does_not_pass(self):
        errors, _ = mod.validate_ledger([])
        self.assertTrue(errors)

    def test_index_transcript_role_count_with_no_semantic_commitments(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "chat.jsonl"
            p.write_text('\n'.join(json.dumps(e) for e in [
              {"message_id":"m1","role":"assistant","content":"Try new approach"},
              {"message_id":"m2","role":"user","content":"go on"}]),encoding="utf-8")
            result = mod.index_transcript(p)
            self.assertTrue(result["valid"])
            self.assertEqual(result["message_count"],2)
            self.assertEqual(result["coverage"], "unknown_account_coverage")
            self.assertNotIn("accepted_events",result)

    def test_index_transcript_duplicate_id_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"chat.jsonl"
            p.write_text('\n'.join([json.dumps({"message_id":"m1","role":"user","content":"first"}),json.dumps({"message_id":"m1","role":"user","content":"next"})]),encoding="utf-8")
            self.assertFalse(mod.index_transcript(p)["valid"])

    def test_coverage_without_accessible_sources_rejected(self):
        rows=[evt("q1",kind="question",status="stated")]
        self.assertFalse(mod.recap(rows,{"coverage":"complete_for_requested_range"})["valid"])

    def test_anchor_witness_verifies_matching_quote(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "chat.jsonl"
            p.write_text(json.dumps({"message_id":"t1","role":"user","content":"go on"})+"\n")
            rows = [evt("a", kind="decision", turn_id="t1", evidence_refs=[{"source_id":"chat.jsonl", "locator":"line:1", "quote":"go on"}])]
            result = mod.verify_anchors(rows, p)
            self.assertTrue(result["valid"])
            self.assertEqual(result["checked_anchors"], 1)

    def test_anchor_witness_catches_fabricated_quote(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "chat.jsonl"
            p.write_text(json.dumps({"message_id":"t1","role":"user","content":"go on"})+"\n")
            rows = [evt("a", kind="decision", turn_id="t1", evidence_refs=[{"source_id":"chat.jsonl", "locator":"line:1", "quote":"I accept everything"}])]
            result = mod.verify_anchors(rows, p)
            self.assertFalse(result["valid"])
            self.assertTrue(any("not present" in x for x in result["errors"]))

    def test_anchor_witness_catches_incorrect_attribution(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"chat.jsonl"
            p.write_text(json.dumps({"message_id":"t1","role":"assistant","content":"go on"})+"\n")
            rows=[evt("a", kind="decision", turn_id="t1", actor="user", evidence_refs=[{"source_id":"chat.jsonl","locator":"line:1","quote":"go on"}])]
            result=mod.verify_anchors(rows,p)
            self.assertFalse(result["valid"])
            self.assertTrue(any("conflicts" in x for x in result["errors"]))

    def test_anchor_witness_warns_missing_literal_quote(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"chat.jsonl"
            p.write_text(json.dumps({"message_id":"t1","role":"user","content":"go on"})+"\n")
            rows=[evt("a",kind="decision",turn_id="t1",evidence_refs=[{"source_id":"chat.jsonl","locator":"line:1"}])]
            result=mod.verify_anchors(rows,p)
            self.assertTrue(result["valid"])
            self.assertTrue(any("absent" in x for x in result["warnings"]))

    def test_invalid_event_link_types_do_not_crash(self):
        rows = [evt("a", kind="question", status="stated", replaces=["b"],
                    depends_on=[["c"]], superseded_by=["b"])]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("must be" in x for x in errors))

    def test_bad_adopted_by_type_does_not_crash(self):
        rows = [evt("a", "assistant", "proposal", "accepted", adopted_by=["b"])]
        errors, _ = mod.validate_ledger(rows)
        self.assertTrue(any("adopted_by" in x for x in errors))

    def test_cli_validates_and_exits_cleanly(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "ledger.jsonl"
            row = evt("a"); row.pop("__line")
            p.write_text(json.dumps(row) + "\n", encoding="utf-8")
            self.assertEqual(mod.main(["validate-ledger", str(p)]), 0)


if __name__ == "__main__":
    unittest.main()
