#!/usr/bin/env python3
"""Dependency-free stdio MCP bridge for offline AudioMusicPipeline tools.

Implements the 2025-11-25 MCP lifecycle and tool calls. It does not claim a
live DAW connection; outputs are files or in-memory calculations.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from ableton_als_builder import AbletonSetBuilder
from crossmodal_engine import CrossModalEngine
from maxpat_builder import MaxPatcherBuilder
from project_contract import render_project_midi, validate_project

PROTOCOL_VERSION = "2025-11-25"
SERVER_VERSION = "2.1.0"

TOOLS = [
    {
        "name": "get_pipeline_capabilities",
        "description": "Report supported offline formats, contract versions, and DAW connection status.",
        "annotations": {"readOnlyHint": True},
        "inputSchema": {"type": "object", "additionalProperties": False},
    },
    {
        "name": "validate_music_project",
        "description": "Validate the complete DAW-neutral music contract and its timeline; return path-specific errors.",
        "annotations": {"readOnlyHint": True},
        "inputSchema": {
            "type": "object", "properties": {"project_data": {"type": "object"}},
            "required": ["project_data"], "additionalProperties": False,
        },
    },
    {
        "name": "render_project_midi",
        "description": "Compile a validated project into an SMF Type 1 .mid file; dry_run previews without writing. Existing files are preserved unless overwrite is true.",
        "inputSchema": {
            "type": "object", "properties": {
                "project_data": {"type": "object"},
                "output_path": {"type": "string", "minLength": 1},
                "dry_run": {"type": "boolean", "default": False},
                "overwrite": {"type": "boolean", "default": False},
            }, "required": ["project_data", "output_path"], "additionalProperties": False,
        },
    },
    {
        "name": "convert_visual_score",
        "description": "Translate a visual score into a MIDI/audio summary in memory; does not save the generated media.",
        "annotations": {"readOnlyHint": True},
        "inputSchema": {
            "type": "object", "properties": {
                "score_data": {"type": "object"},
                "bpm": {"type": "number", "minimum": 20, "maximum": 300, "default": 120},
                "total_bars": {"type": "integer", "minimum": 1, "maximum": 128, "default": 4},
            }, "required": ["score_data"], "additionalProperties": False,
        },
    },
    {
        "name": "generate_ableton_als",
        "description": "Generate a structurally checked Ableton Live 12 .als file with named, empty MIDI tracks. Live GUI loading is not verified by this tool.",
        "inputSchema": {
            "type": "object", "properties": {
                "output_path": {"type": "string", "minLength": 1},
                "tempo": {"type": "number", "minimum": 20, "maximum": 300, "default": 120},
                "track_names": {"type": "array", "items": {"type": "string", "minLength": 1}},
                "overwrite": {"type": "boolean", "default": False},
            }, "required": ["output_path"], "additionalProperties": False,
        },
    },
    {
        "name": "generate_maxpat",
        "description": "Generate a Max 8.6 OSC telemetry patcher (.maxpat).",
        "inputSchema": {
            "type": "object", "properties": {
                "output_path": {"type": "string", "minLength": 1},
                "patch_type": {"type": "string", "enum": ["osc_telemetry"], "default": "osc_telemetry"},
                "overwrite": {"type": "boolean", "default": False},
            }, "required": ["output_path"], "additionalProperties": False,
        },
    },
    {
        "name": "calculate_safe_margin",
        "description": "Clamp cube ribbon amplitude so band_span/2 + amplitude + stroke_width/2 stays within budget.",
        "annotations": {"readOnlyHint": True},
        "inputSchema": {
            "type": "object", "properties": {
                "band_span": {"type": "number", "minimum": 0},
                "candidate_amplitude": {"type": "number", "minimum": 0},
                "stroke_width": {"type": "number", "minimum": 0},
                "budget": {"type": "number", "exclusiveMinimum": 0, "default": 0.42},
            }, "required": ["band_span", "candidate_amplitude", "stroke_width"], "additionalProperties": False,
        },
    },
]

TOOL_BY_NAME = {tool["name"]: tool for tool in TOOLS}


def _tool_result(data: dict[str, Any], *, error: bool = False) -> dict[str, Any]:
    return {
        "content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False)}],
        "structuredContent": data,
        "isError": error,
    }


def _argument_errors(arguments: Any, schema: dict[str, Any]) -> list[str]:
    if not isinstance(arguments, dict):
        return ["arguments must be an object"]
    errors = []
    fields = schema.get("properties", {})
    for key in schema.get("required", []):
        if key not in arguments:
            errors.append(f"{key} is required")
    if schema.get("additionalProperties") is False:
        errors.extend(f"{key} is not supported" for key in arguments if key not in fields)
    for key, value in arguments.items():
        spec = fields.get(key)
        if spec is None:
            continue
        kind = spec.get("type")
        correct = {
            "object": isinstance(value, dict),
            "array": isinstance(value, list),
            "string": isinstance(value, str),
            "boolean": isinstance(value, bool),
            "integer": isinstance(value, int) and not isinstance(value, bool),
            "number": (isinstance(value, int) and not isinstance(value, bool)) or (isinstance(value, float) and math.isfinite(value)),
        }.get(kind, True)
        if not correct:
            errors.append(f"{key} must be {kind}")
            continue
        if "enum" in spec and value not in spec["enum"]:
            errors.append(f"{key} is not supported")
        if kind in ("integer", "number"):
            if "minimum" in spec and value < spec["minimum"]:
                errors.append(f"{key} must be >= {spec['minimum']}")
            if "maximum" in spec and value > spec["maximum"]:
                errors.append(f"{key} must be <= {spec['maximum']}")
            if "exclusiveMinimum" in spec and value <= spec["exclusiveMinimum"]:
                errors.append(f"{key} must be > {spec['exclusiveMinimum']}")
        if kind == "string" and len(value) < spec.get("minLength", 0):
            errors.append(f"{key} must not be empty")
        if kind == "array" and spec.get("items", {}).get("type") == "string":
            if any(not isinstance(item, str) or len(item) < spec["items"].get("minLength", 0) for item in value):
                errors.append(f"{key} must contain nonempty strings")
    return errors


def _output_path(arguments: dict[str, Any], suffix: str) -> Path:
    path = Path(arguments["output_path"]).expanduser().resolve()
    if path.suffix.lower() != suffix:
        raise ValueError(f"output_path must end in {suffix}")
    if not path.parent.is_dir():
        raise FileNotFoundError(f"Output directory does not exist: {path.parent}")
    if path.exists() and not arguments.get("overwrite", False):
        raise FileExistsError(f"File already exists: {path}")
    return path


def handle_call_tool(name: str, arguments: Any) -> dict[str, Any]:
    tool = TOOL_BY_NAME.get(name)
    if tool is None:
        return _tool_result({"code": "unknown_tool", "message": f"Unknown tool: {name}"}, error=True)
    errors = _argument_errors(arguments, tool["inputSchema"])
    if errors:
        return _tool_result({"code": "invalid_arguments", "errors": errors}, error=True)
    try:
        if name == "get_pipeline_capabilities":
            value = {
                "mode": "offline", "live_daw_connected": False,
                "contract_versions": ["2.0.0", "2.1.0"],
                "outputs": ["smf_type_1_midi", "ableton_als_structure", "maxpat_osc_telemetry"],
                "midi_timing_unit": "quarter_note_beats",
                "unsupported_midi_features": ["microtone_cents", "non_440_hz_tuning"],
            }
        elif name == "validate_music_project":
            value = validate_project(arguments["project_data"])
        elif name == "render_project_midi":
            value = render_project_midi(
                arguments["project_data"], arguments["output_path"],
                dry_run=arguments.get("dry_run", False), overwrite=arguments.get("overwrite", False),
            )
        elif name == "convert_visual_score":
            res = CrossModalEngine.visual_score_to_music(
                arguments["score_data"], bpm=arguments.get("bpm", 120), total_bars=arguments.get("total_bars", 4),
            )
            value = {"status": res["status"], "total_notes": res["total_notes"],
                     "loss_metrics": res["loss_metrics"], "duration_sec": res["total_duration_sec"]}
        elif name == "generate_ableton_als":
            path = _output_path(arguments, ".als")
            tempo = arguments.get("tempo", 120)
            builder = AbletonSetBuilder(tempo=tempo)
            for track_name in arguments.get("track_names", ["Drums", "Bass", "Synth", "FX"]):
                builder.add_midi_track(track_name)
            builder.save_als(str(path))
            value = {"status": "created", "path": str(path), "tempo": tempo, "tracks": len(builder.tracks)}
        elif name == "generate_maxpat":
            path = _output_path(arguments, ".maxpat")
            patcher = MaxPatcherBuilder.create_osc_telemetry_patch()
            patcher.save_maxpat(str(path))
            value = {"status": "created", "path": str(path), "patch_type": "osc_telemetry"}
        else:
            span, amp, stroke = (arguments[key] for key in ("band_span", "candidate_amplitude", "stroke_width"))
            budget = arguments.get("budget", 0.42)
            margin_used = span / 2 + stroke / 2
            if margin_used >= budget:
                raise ValueError("Band span and stroke width leave no amplitude headroom")
            clamped = min(amp, budget - margin_used)
            total = margin_used + clamped
            value = {"budget": budget, "candidate_amplitude": amp,
                     "clamped_amplitude": clamped, "final_margin": total, "safe": total <= budget + 1e-9}
        return _tool_result(value)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        return _tool_result({"code": "tool_error", "message": str(exc)}, error=True)


def _response(message_id: Any, *, result: Any = None, error: dict[str, Any] | None = None) -> dict[str, Any]:
    response = {"jsonrpc": "2.0", "id": message_id}
    response["error" if error is not None else "result"] = error if error is not None else result
    return response


def process_message(request: Any) -> dict[str, Any] | None:
    if not isinstance(request, dict) or request.get("jsonrpc") != "2.0" or not isinstance(request.get("method"), str):
        return _response(None, error={"code": -32600, "message": "Invalid Request"})
    method = request["method"]
    if "id" not in request:  # Notifications never receive a response.
        return None
    message_id = request["id"]
    params = request.get("params", {})
    if not isinstance(params, dict):
        return _response(message_id, error={"code": -32602, "message": "Invalid params"})
    if method == "initialize":
        requested = params.get("protocolVersion")
        version = requested if requested in ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05") else PROTOCOL_VERSION
        return _response(message_id, result={"protocolVersion": version, "capabilities": {"tools": {}},
                                             "serverInfo": {"name": "audio-music-pipeline", "version": SERVER_VERSION}})
    if method == "ping":
        return _response(message_id, result={})
    if method == "tools/list":
        return _response(message_id, result={"tools": TOOLS})
    if method == "tools/call":
        if not isinstance(params.get("name"), str):
            return _response(message_id, error={"code": -32602, "message": "Tool name is required"})
        return _response(message_id, result=handle_call_tool(params["name"], params.get("arguments", {})))
    return _response(message_id, error={"code": -32601, "message": "Method not found"})


def run_server() -> None:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            response = _response(None, error={"code": -32700, "message": "Parse error"})
        else:
            response = process_message(request)
        if response is not None:
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        print(json.dumps(TOOLS, indent=2))
    else:
        run_server()
