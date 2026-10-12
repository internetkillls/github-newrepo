---
name: max-msp-m4l
description: "Generate and validate Cycling '74 Max/MSP 8.6 patchers (.maxpat) and Max for Live devices (.amxd) with valid JSON structures and signal flow."
---

# Max/MSP & Max for Live Engine

Use this skill to create, inspect, and validate modular patchers for Cycling '74 Max 8.6.2 and Max for Live.

## Verified Environment on Host
- **Application**: Max (`8.6.2 (d076223e34e)`)
- **Location**: `/Applications/Max.app`
- **Architecture**: Modern JSON `.maxpat` format

## Core Procedures

1. **Max Patcher JSON Generation**:
   - Use `tools/maxpat_builder.py` to construct valid `.maxpat` JSON trees:
     ```python
     from tools.maxpat_builder import MaxPatcherBuilder
     builder = MaxPatcherBuilder("Live_OSC_Telemetry")
     udp = builder.add_box("udpreceive 7000", "newobj", [50, 40, 120, 22])
     route = builder.add_box("route /drums /bass /synth /fx", "newobj", [50, 80, 200, 22], numoutlets=5)
     builder.add_line(udp, 0, route, 0)
     builder.save_maxpat("osc_bridge.maxpat")
     ```

2. **Control Rate vs Signal Rate (Tilde `~`) Hygiene**:
   - Objects ending with `~` process audio rate signals (e.g. `cycle~`, `dac~`, `live.gain~`, `snapshot~`).
   - Standard objects process event messages at control rate (e.g. `metro`, `route`, `pack`, `unpack`).
   - Use `snapshot~` or `peakamp~` to bridge audio rate signals into control rate data streams for OSC or visual telemetry without audio-thread blocking.

3. **Max for Live (M4L) UI & Parameter Exposure**:
   - Use dedicated `live.*` UI objects for native Ableton parameter automation:
     - `live.dial`: Continuous floating-point or integer knob.
     - `live.tab`: Multi-option radio switch.
     - `live.numbox`: Number box with musical units (dB, Hz, %).
     - `live.observer`: Observes Live Object Model properties in real-time.

4. **Validation Checklist**:
   - Verify every line connects to valid existing box IDs.
   - Verify outlet and inlet indices exist within box definition.
