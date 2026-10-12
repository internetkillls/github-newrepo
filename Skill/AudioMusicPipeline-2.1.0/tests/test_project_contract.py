"""Behavioral checks for the portable project-to-MIDI boundary."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from project_contract import compile_project_midi, render_project_midi, validate_project
from smf_midi import MidiFile


def example():
    return json.loads((ROOT / "contracts" / "project_music_contract.example.json").read_text(encoding="utf-8"))


class ProjectContractTests(unittest.TestCase):
    def test_example_compiles_to_multitrack_midi_with_notes(self):
        project = example()
        data, summary = compile_project_midi(project)
        parsed = MidiFile.deserialize(data)
        self.assertEqual(summary["notes"], 9)
        self.assertEqual(len(parsed.tracks), 4)  # conductor + three musical tracks
        bass = parsed.tracks[2]
        self.assertEqual(bass.name, "Sub_Bass")
        self.assertEqual([(e.delta, e.data["note"], e.data["velocity"]) for e in bass.events if e.type == "note_on"],
                         [(0, 38, 95), (960, 43, 90)])

    def test_meter_6_8_uses_quarter_note_beat_coordinates(self):
        project = example()
        project["time_transport"].update({"meter_numerator": 6, "meter_denominator": 8, "total_bars": 2})
        project["harmonic_system"]["chord_progression"] = []
        project["tracks"] = [{"track_id": "one", "name": "One", "role": "lead_melody", "midi_channel": 0,
                              "notes": [{"start_beat": 5.5, "duration_beats": 0.5, "pitch": 60, "velocity": 90}]}]
        result = validate_project(project)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["summary"]["duration_quarter_beats"], 6)
        parsed = MidiFile.deserialize(compile_project_midi(project)[0])
        signature = next(e for e in parsed.tracks[0].events if e.type == "time_signature")
        self.assertEqual(signature.data["denominator"], 8)
        note_on = next(e for e in parsed.tracks[1].events if e.type == "note_on")
        self.assertEqual(note_on.delta, 2640)
        project["tracks"][0]["notes"][0]["duration_beats"] = 0.6
        self.assertIn("outside_project", [e["code"] for e in validate_project(project)["errors"]])

    def test_invalid_fields_and_duplicate_ids_are_reported(self):
        project = example()
        project["time_transport"]["bpm"] = True
        project["tracks"][1]["track_id"] = project["tracks"][0]["track_id"]
        project["crossmodal_mappings"]["audio_to_visual"]["spectral_bands"]["sub"] = [90, 20]
        errors = validate_project(project)["errors"]
        self.assertEqual({e["code"] for e in errors}, {"type", "duplicate", "range_order"})

    def test_microtone_is_rejected_instead_of_silently_dropped(self):
        project = example()
        project["tracks"][0]["notes"][0]["microtone_cents"] = 25
        self.assertTrue(validate_project(project)["valid"])
        with self.assertRaisesRegex(ValueError, "microtone_cents"):
            compile_project_midi(project)

    def test_subtick_duration_is_rejected_instead_of_extended(self):
        project = example()
        project["time_transport"]["ticks_per_quarter"] = 1
        project["tracks"][0]["notes"][0]["duration_beats"] = 0.1
        self.assertTrue(validate_project(project)["valid"])
        with self.assertRaisesRegex(ValueError, "cannot be represented"):
            compile_project_midi(project)

    def test_dry_run_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "song.mid"
            preview = render_project_midi(example(), str(path), dry_run=True)
            self.assertEqual(preview["status"], "preview")
            self.assertFalse(path.exists())
            created = render_project_midi(example(), str(path))
            self.assertEqual(created["status"], "created")
            initial = path.read_bytes()
            with self.assertRaises(FileExistsError):
                render_project_midi(example(), str(path))
            self.assertEqual(path.read_bytes(), initial)

    def test_stdio_mcp_handshake_and_tool_result(self):
        requests = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "test", "version": "1"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "validate_music_project", "arguments": {"project_data": example()}}},
            {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "render_project_midi", "arguments": {"project_data": {}, "output_path": "/tmp/invalid.mid", "dry_run": True}}},
        ]
        proc = subprocess.run([sys.executable, str(ROOT / "tools" / "mcp_audio_server.py")],
                              input="\n".join(json.dumps(r) for r in requests) + "\n", text=True, capture_output=True, check=True)
        responses = [json.loads(line) for line in proc.stdout.splitlines()]
        self.assertEqual(len(responses), 4)
        self.assertEqual(responses[0]["result"]["protocolVersion"], "2025-11-25")
        self.assertIn("render_project_midi", [t["name"] for t in responses[1]["result"]["tools"]])
        self.assertTrue(responses[2]["result"]["structuredContent"]["valid"])
        self.assertTrue(responses[3]["result"]["isError"])


if __name__ == "__main__":
    unittest.main()
