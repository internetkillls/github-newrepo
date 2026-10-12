---
name: mcp-audio-bridge
description: Use the local AudioMusicPipeline MCP server for contract validation, offline MIDI export, visual-score conversion, and structural Ableton/Max file generation. Check capabilities before assuming live DAW control.
---

# MCP Audio Bridge

The plugin's `mcp.json` starts `tools/mcp_audio_server.py` through stdio. It supports the MCP `2025-11-25` tool lifecycle with JSON tool results. The server works offline and does not control a running DAW.

## Choose the smallest tool

| Tool | Use |
| --- | --- |
| `get_pipeline_capabilities` | Check formats, contract versions, and live-DAW status. |
| `validate_music_project` | Validate a complete `crossmodal_contract.schema.json` project; inspect `errors` paths. |
| `render_project_midi` | Compile validated project notes to SMF Type 1. Use `dry_run: true` to preview; existing files require `overwrite: true`. |
| `convert_visual_score` | Calculate a visual-score translation summary in memory; it does not save MIDI or WAV. |
| `generate_ableton_als` | Create a structural `.als` set with empty named MIDI tracks; opening it in Live is a separate verification step. |
| `generate_maxpat` | Create the supported OSC telemetry `.maxpat` patch. |
| `calculate_safe_margin` | Clamp visual ribbon amplitude to its specified margin budget. |

## Contract and loss rules

- `start_beat` and `duration_beats` are quarter-note beats. In 6/8, one bar spans three quarter-note beats.
- Project `version` 2.0.0 and 2.1.0 are accepted. The validator checks required fields, ranges, unique track IDs, note boundaries, and spectral-band ordering.
- Standard MIDI export rejects nonzero `microtone_cents`, non-440 Hz A4 tuning, and note timing finer than the selected ticks-per-quarter resolution instead of silently changing them.
- All project-to-MIDI writes are explicit; `dry_run` has no file side effects.

## Local check

From the plugin root:

```bash
python3 tools/mcp_audio_server.py --list
python3 -m unittest discover -s tests -v
```
