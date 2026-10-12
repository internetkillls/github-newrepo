---
name: ableton-live-integration
description: "Integrate with Ableton Live 12 Suite: parse and generate .als project files, configure OSC telemetry, and scaffold Python Remote Scripts."
---

# Ableton Live 12 Integration Engine

Use this skill to interface directly with Ableton Live 12 Suite. It builds genuine Live Set projects (`.als`), controls transport via Ableton Link or OSC, and scaffolds Python 3 MIDI Remote Scripts.

## Verified Environment on Host
- **Application**: Ableton Live 12 Suite (`12.4.6 (2026-09-10_0de5c8fa9a)`)
- **Location**: `/Applications/Ableton Live 12 Suite.app`
- **Internal Python**: Python 3 (located in `App-Resources/Python`)
- **Schema Reference**: `App-Resources/Schema/12.0_12402.txt`

## Core Procedures

1. **Generating Live 12 Projects (`.als`)**:
   - Use `tools/ableton_als_builder.py` to compile musical tracks and clips into a valid gzip XML project:
     ```python
     from tools.ableton_als_builder import AbletonSetBuilder
     builder = AbletonSetBuilder(tempo=124.0)
     builder.add_midi_track("Drums", color_index=12)
     builder.add_midi_track("Bass", color_index=24)
     builder.add_midi_track("Melody", color_index=48)
     builder.save_als("output_project.als")
     ```
   - Test round-trip decompression and XML validity:
     ```python
     info = AbletonSetBuilder.parse_als("output_project.als")
     assert info["status"] == "valid"
     ```

2. **OSC Telemetry Bridge**:
   - Send track volume, macro parameter, and cue telemetry over UDP (e.g. port 7000 or 8000) using OSC address patterns:
     - `/drums/rms <float>`
     - `/bass/width <float>`
     - `/synth/harmonic <int>`
     - `/master/tempo <float>`
     - `/transport/play <int>`

3. **Ableton Link Transport Sync**:
   - Synchronizes tempo and bar phase across local devices (peer-to-peer UDP).
   - In TouchDesigner: `abletonlinkCHOP` (`ramp=1`, `quantum=4`).
   - In Max: `link.beat~` or `link.phasor~`.

4. **Python Remote Script Scaffolding**:
   - Scaffolds MIDI Remote Scripts placed in `~/Music/Ableton/User Library/Remote Scripts/` for deep Live Object Model (LOM) automation (`Song`, `Track`, `ClipSlot`, `Device`).
