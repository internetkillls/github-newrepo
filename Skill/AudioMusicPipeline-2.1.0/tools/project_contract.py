"""Validate the portable music contract and compile its MIDI tracks.

The JSON schema describes field-level constraints. These helpers add the
cross-field checks that JSON Schema cannot express without changing the data
model: unique track IDs, positions inside the project, and ordered bands.
"""

from __future__ import annotations

import json
import math
import os
import tempfile
from pathlib import Path
from typing import Any

try:
    from .smf_midi import MidiEvent, MidiFile, MidiTrack
except ImportError:
    from smf_midi import MidiEvent, MidiFile, MidiTrack


SCHEMA_PATH = Path(__file__).resolve().parents[1] / "contracts" / "crossmodal_contract.schema.json"


def _type_matches(value: Any, kind: str) -> bool:
    if kind == "object":
        return isinstance(value, dict)
    if kind == "array":
        return isinstance(value, list)
    if kind == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if kind == "number":
        return (isinstance(value, int) and not isinstance(value, bool)) or (isinstance(value, float) and math.isfinite(value))
    if kind == "string":
        return isinstance(value, str)
    if kind == "boolean":
        return isinstance(value, bool)
    raise ValueError(f"Unsupported schema type: {kind}")


def _validate_node(value: Any, schema: dict[str, Any], path: str, errors: list[dict[str, str]]) -> None:
    kind = schema.get("type")
    if kind and not _type_matches(value, kind):
        errors.append({"path": path, "code": "type", "message": f"Expected {kind}"})
        return
    if "enum" in schema and value not in schema["enum"]:
        errors.append({"path": path, "code": "enum", "message": "Value is not supported"})
        return
    if kind in ("number", "integer"):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append({"path": path, "code": "minimum", "message": f"Must be >= {schema['minimum']}"})
        if "maximum" in schema and value > schema["maximum"]:
            errors.append({"path": path, "code": "maximum", "message": f"Must be <= {schema['maximum']}"})
    elif kind == "string":
        if len(value) < schema.get("minLength", 0):
            errors.append({"path": path, "code": "minLength", "message": "String is too short"})
    elif kind == "array":
        if len(value) < schema.get("minItems", 0):
            errors.append({"path": path, "code": "minItems", "message": "Array is too short"})
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append({"path": path, "code": "maxItems", "message": "Array is too long"})
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                _validate_node(item, item_schema, f"{path}/{index}", errors)
    elif kind == "object":
        for key in schema.get("required", []):
            if key not in value:
                errors.append({"path": f"{path}/{key}", "code": "required", "message": "Required field is missing"})
        for key, item in value.items():
            child = schema.get("properties", {}).get(key)
            if child is not None:
                _validate_node(item, child, f"{path}/{key}", errors)


def validate_project(project: Any) -> dict[str, Any]:
    """Return field and musical-timeline diagnostics without modifying input."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors: list[dict[str, str]] = []
    _validate_node(project, schema, "$", errors)
    if not isinstance(project, dict):
        return {"valid": False, "errors": errors}

    transport = project.get("time_transport")
    total_beats = None
    if isinstance(transport, dict):
        numerator = transport.get("meter_numerator")
        denominator = transport.get("meter_denominator")
        bars = transport.get("total_bars")
        if all(_type_matches(v, "integer") for v in (numerator, denominator, bars)) and denominator > 0:
            # Coordinates are quarter-note beats; a 6/8 bar spans 3 of them.
            total_beats = bars * numerator * 4 / denominator

    harmonic = project.get("harmonic_system")
    if isinstance(harmonic, dict) and isinstance(harmonic.get("chord_progression"), list):
        for i, chord in enumerate(harmonic["chord_progression"]):
            if isinstance(chord, dict) and isinstance(chord.get("bar"), int) and isinstance(transport, dict):
                if _type_matches(transport.get("total_bars"), "integer") and chord["bar"] > transport["total_bars"]:
                    errors.append({"path": f"$/harmonic_system/chord_progression/{i}/bar", "code": "outside_project", "message": "Chord bar exceeds total_bars"})

    tracks = project.get("tracks")
    seen_ids: set[str] = set()
    note_count = 0
    if isinstance(tracks, list):
        for i, track in enumerate(tracks):
            if not isinstance(track, dict):
                continue
            track_id = track.get("track_id")
            if isinstance(track_id, str):
                if track_id in seen_ids:
                    errors.append({"path": f"$/tracks/{i}/track_id", "code": "duplicate", "message": "Track ID must be unique"})
                seen_ids.add(track_id)
            notes = track.get("notes", [])
            if not isinstance(notes, list):
                continue
            note_count += len(notes)
            for j, note in enumerate(notes):
                if not isinstance(note, dict) or total_beats is None:
                    continue
                start, duration = note.get("start_beat"), note.get("duration_beats")
                if _type_matches(start, "number") and _type_matches(duration, "number"):
                    if start + duration > total_beats + 1e-9:
                        errors.append({"path": f"$/tracks/{i}/notes/{j}", "code": "outside_project", "message": "Note ends after the project boundary"})

    mappings = project.get("crossmodal_mappings")
    if isinstance(mappings, dict):
        audio = mappings.get("audio_to_visual")
        bands = audio.get("spectral_bands") if isinstance(audio, dict) else None
        if isinstance(bands, dict):
            for key, pair in bands.items():
                if isinstance(pair, list) and len(pair) == 2 and all(_type_matches(v, "number") for v in pair):
                    if pair[0] >= pair[1]:
                        errors.append({"path": f"$/crossmodal_mappings/audio_to_visual/spectral_bands/{key}", "code": "range_order", "message": "Lower frequency must be below upper frequency"})

    result: dict[str, Any] = {"valid": not errors, "errors": errors}
    if not errors:
        result["project_id"] = project["project_id"]
        result["summary"] = {"tracks": len(tracks), "notes": note_count, "duration_quarter_beats": total_beats}
    return result


def compile_project_midi(project: dict[str, Any]) -> tuple[bytes, dict[str, Any]]:
    """Compile a validated project to SMF Type 1 without hiding lost features."""
    result = validate_project(project)
    if not result["valid"]:
        raise ValueError(json.dumps(result["errors"], ensure_ascii=False))
    harmonic = project["harmonic_system"]
    unsupported = []
    if harmonic["tuning_cents_a4"] != 440.0:
        unsupported.append("non-440 A4 tuning")
    if any(note.get("microtone_cents", 0) != 0 for track in project["tracks"] for note in track.get("notes", [])):
        unsupported.append("microtone_cents")
    if unsupported:
        raise ValueError("SMF export does not encode: " + ", ".join(unsupported))

    transport = project["time_transport"]
    tpq = transport["ticks_per_quarter"]
    final_tick = round(result["summary"]["duration_quarter_beats"] * tpq)
    midi = MidiFile(ticks_per_quarter=tpq, format_=1)
    conductor = MidiTrack("Conductor")
    conductor.add_event(MidiEvent(0, "set_tempo", tempo_us=round(60_000_000 / transport["bpm"])))
    conductor.add_event(MidiEvent(0, "time_signature", numerator=transport["meter_numerator"], denominator=transport["meter_denominator"]))
    midi.add_track(conductor)
    for source_track in project["tracks"]:
        track = MidiTrack(source_track["name"])
        for note in source_track.get("notes", []):
            start_tick = round(note["start_beat"] * tpq)
            end_tick = round((note["start_beat"] + note["duration_beats"]) * tpq)
            if end_tick <= start_tick or start_tick >= final_tick or end_tick > final_tick:
                raise ValueError("Note timing cannot be represented inside the project at this ticks_per_quarter")
            track.add_note(note["pitch"], note["velocity"], start_tick, end_tick - start_tick, source_track["midi_channel"])
        midi.add_track(track)
    return midi.serialize(), result["summary"]


def render_project_midi(project: dict[str, Any], output_path: str, *, dry_run: bool = False, overwrite: bool = False) -> dict[str, Any]:
    data, summary = compile_project_midi(project)
    if not isinstance(output_path, str) or not output_path or Path(output_path).suffix.lower() != ".mid":
        raise ValueError("output_path must name a .mid file")
    path = Path(output_path).expanduser().resolve()
    if path.exists() and not overwrite:
        raise FileExistsError(f"File already exists: {path}")
    if dry_run:
        return {"status": "preview", "path": str(path), "bytes": len(data), **summary}
    if not path.parent.is_dir():
        raise FileNotFoundError(f"Output directory does not exist: {path.parent}")
    with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent, prefix=".audio-music-", suffix=".mid", delete=False) as temp:
        temporary_path = Path(temp.name)
        temp.write(data)
    try:
        if overwrite:
            os.replace(temporary_path, path)
        else:
            os.link(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)
    return {"status": "created", "path": str(path), "bytes": len(data), **summary}
