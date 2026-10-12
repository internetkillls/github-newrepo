---
name: music-project-orchestration
description: "Master DAG planner, contract validation, cue calculation, and multi-target compilation for musical and audiovisual projects."
---

# Music Project Orchestration

Use this skill as the entry point to plan, schedule, validate, and orchestrate complex music and audiovisual projects. It enforces contract compliance across songwriting, harmony, rhythm, sound design, DAW integration, and visual adapters.

## Workflow DAG

```
[ Project Brief & Aesthetic Seeds ]
         │
         ▼
[ music-ideation ] (Concept, Scale, Tempo, Visual Score Seed)
         │
         ▼
[ harmony-theory ] & [ rhythm-groove ] (Progression, Metric Grid, Euclidean Grooves)
         │
         ▼
[ midi-arrangement ] (Voice Allocation, Multi-Track SMF Sequences)
         │
         ▼
[ sound-design-dsp ] (Synthesis Architecture, Timbre Palette)
         │
         ▼
[ multi-target-compilation ]
   ├── ableton-live-integration (Generates .als Live 12 Sets)
   ├── max-msp-m4l (Generates .maxpat / .amxd Patchers)
   ├── juce-plugin-dev (Generates C++ DSP Plugins & CMake)
   └── audio-visual-crossmodal (Generates TouchDesigner / Resolume Controls)
         │
         ▼
[ audio-qa-verification ] (True Peak, LUFS, Clipping, Invariants)
         │
         ▼
[ live-performance-rig ] (Stage Execution, Clock Sync, Failover)
```

## Core Procedures

1. **Contract Initialization**:
   - Create or load `project_music_contract.json` conforming to `contracts/crossmodal_contract.schema.json`.
   - Specify master transport: BPM, meter, total bars, ticks per quarter (default: 480).
   - Specify harmonic system: scale root, mode, chord progression table.

2. **Validation & Integrity Verification**:
   - Run offline validator:
     ```bash
     python3 tools/crossmodal_engine.py validate path/to/project.json
     ```
   - Verify analytic closure and bar boundary integrity (all track note start ticks must be within `total_bars * meter_num * ticks_per_quarter`).

3. **Multi-Target Compilation**:
   - Export Standard MIDI File (`.mid`) via `smf_midi.py`.
   - Export Ableton Live 12 Set (`.als`) via `ableton_als_builder.py`.
   - Export Cycling '74 Max 8.6 patcher (`.maxpat`) via `maxpat_builder.py`.
   - Export visual cube ribbon parameters via `crossmodal_engine.py`.

## Capability Boundaries

- **What this skill DOES**: Coordinates dependencies, validates structural contracts, schedules cues, and orchestrates export pipelines.
- **What this skill DOES NOT do**: Does not write individual synth patches or compile C++ code directly (delegates to `sound-design-dsp` and `juce-plugin-dev`).
