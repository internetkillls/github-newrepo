# AudioMusicPipeline (v2.1.0)

A modular music, DAW-file, audio DSP, and bidirectional audiovisual pipeline. It guides creative and technical projects from musical songwriting, modal harmony, and rhythm composition to implementation in **Ableton Live 12 Suite**, **Cycling '74 Max/MSP 8.6**, **Max for Live**, **JUCE C++ audio plugins**, and downstream visual rendering in **TouchDesigner** and **Resolume Arena**. Runtime support varies by target and is described in the verification section.

## 2.1 portable project contract

The DAW-neutral `contracts/crossmodal_contract.schema.json` project is the canonical input for offline MIDI export. Its note positions and durations are **quarter-note beats**: a 6/8 bar occupies 3 quarter-note beats. The validator reports exact field paths and checks note boundaries, unique track IDs, and frequency-band order. Contracts labeled 2.0.0 remain accepted; new examples use 2.1.0.

`mcp.json` exposes the local stdio bridge. `get_pipeline_capabilities` states what is actually available; `validate_music_project` checks the full contract; `render_project_midi` creates SMF Type 1 with a dry-run option and preserves existing files by default. MIDI export rejects unsupported microtonal offsets and non-440 Hz tuning explicitly. This bridge generates files offline; it does not control a running DAW.

The seven supplied MCP projects informed the narrow interface: capability discovery, typed parameters, DAW-neutral note coordinates, and clear file-side-effect rules. See `docs/inspiration-review.md` for the source-to-decision mapping.

---

## 1. Architectural Overview & Workflow DAG

```
                      [ Project Brief / Visual Score Seed ]
                                       │
                                       ▼
                   ┌──────────────────────────────────────┐
                   │        music-project-orchestration   │
                   └──────────────────┬───────────────────┘
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            ▼                                                   ▼
 ┌──────────────────────┐                           ┌───────────────────────┐
 │   music-ideation     │                           │ audio-visual-crossmodal│
 └──────────┬───────────┘                           └───────────┬───────────┘
            │                                                   │
 ┌──────────┴───────────┐                                       │ (Bidirectional)
 │    harmony-theory    │◄──────────────────────────────────────┤  - Visual Score -> Music
 │    rhythm-groove     │                                       │  - Audio -> Visual Data
 │   midi-arrangement   │──────────────────────────────────────►│
 └──────────┬───────────┘                                       │
            │                                                   ▼
 ┌──────────┴───────────┐                           ┌───────────────────────┐
 │   sound-design-dsp   │                           │  Downstream Adapters  │
 │ audio-analysis-feat. │                           │  - adapter-touchdesign│
 └──────────┬───────────┘                           │  - adapter-resolume   │
            │                                       └───────────────────────┘
            ▼
 ┌──────────────────────────────────────────────────────────────┐
 │                    Target Platform Compilers                 │
 │  ├── ableton-live-integration (Live 12 Suite .als Gzip XML)  │
 │  ├── max-msp-m4l              (Max 8.6 .maxpat JSON)         │
 │  ├── juce-plugin-dev          (C++17 SVF DSP Core + CMake)   │
 │  └── mcp-audio-bridge         (Stdio JSON-RPC MCP Server)    │
 └──────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
                   ┌───────────────────────────┐
                   │   audio-qa-verification   │ (True Peak, LUFS, Invariants)
                   └────────────┬──────────────┘
                                │
                                ▼
                   ┌───────────────────────────┐
                   │    live-performance-rig   │ (Low Latency, Clock Sync)
                   └───────────────────────────┘
```

---

## 2. Skills Inventory (16 Modular Skills)

| Skill Name | Role & Core Function | Primary Targets |
| :--- | :--- | :--- |
| **`music-project-orchestration`** | Master DAG planner, contract validator, cue scheduler, and multi-engine compiler. | Pipeline CLI, `project_music_contract.json` |
| **`music-ideation`** | Songwriting concept generation, stylistic parameters, tempo constraints, visual score seeds. | Composition Brief, Cue Cards |
| **`harmony-theory`** | Chord progressions, modal mixture, voice leading rules, microtonality. | Progression Tables, Voicings |
| **`rhythm-groove`** | Metric grids, Euclidean rhythms, polyrhythms, syncopation, Linn-style swing quantization. | Drum Patterns, Groove Templates |
| **`midi-arrangement`** | Multi-track MIDI orchestration, voice allocation, velocity curves, SMF 1.0 export. | `.mid` Type 1 files |
| **`sound-design-dsp`** | Subtractive, FM, wavetable, granular synthesis architectures, signal chains. | Synths, Samplers, Effect Racks |
| **`audio-analysis-features`** | Nyquist 4-band splitting, RMS envelopes, spectral centroid, onsets. | Audio Telemetry, Analysis Graphs |
| **`ableton-live-integration`** | Live 12 Set `.als` generator/parser (schema `12.0_12402`), OSC bridge, LOM scripts. | Ableton Live 12 Suite |
| **`max-msp-m4l`** | Max 8.6 `.maxpat` JSON patcher generator, signal `~` vs control flow, M4L `live.*` UI. | Cycling '74 Max 8.6, Max for Live |
| **`mcp-audio-bridge`** | Local stdio MCP server with capability discovery, contract validation, and offline MIDI export. | Codex and compatible MCP hosts |
| **`juce-plugin-dev`** | Real-time safe C++17 SVF filter with saturation drive, APVTS, headless Clang tests. | VST3, AU, CMake |
| **`audio-qa-verification`** | Quality assurance: integrated LUFS, True Peak, clipping detection, DC offset. | QA Reports, Audio Masters |
| **`live-performance-rig`** | Buffer latency management, redundant audio failover, Ableton Link master clock. | Stage Hardware, Live Sets |
| **`audio-visual-crossmodal`**| Bidirectional translation: *visual score -> music* and *audio -> visual parameters*. | Cross-Modal Engine, Loss Metrics |
| **`adapter-touchdesigner`** | Downstream 7200x1080 4-face cube ribbons, audio-reactive engines, GLSL shaders. | Derivative TouchDesigner 2022+ |
| **`adapter-resolume`** | 4-slice Advanced Output routing, DXV3 playback, OSC show cue triggers. | Resolume Arena 7.0+ |

---

## 3. Bidirectional Cross-Modal Workflow

### Direction 1: Visual Score $\to$ Music / Audio
- **Definition of Visual Score**: A graphical or parametric score (not standard sheet music notation) mapping continuous spatial curves, point events, and color hues to sound.
- **Translation**:
  - $X$-axis $[0.0, 1.0] \to$ Time in musical beats (quantized to 16th-note grid).
  - $Y$-axis $[0.0, 1.0] \to$ Pitch register, snapped to scale degrees (e.g. D Dorian).
  - Stroke Width $[0.002, 0.040] \to$ Note velocity $[40, 120]$.
  - Element Type $\to$ Voice role (`melody`, `harmony`, `bass`, `percussion`).
- **Lossy Analysis**: Continuous curve interpolation to discrete 12-TET semitones incurs quantization error (reported in mean cents lost).

### Direction 2: Music / Audio $\to$ Visual Control
- **Translation**:
  - Drums RMS $\to$ Ribbon Amplitude ($[0.015, 0.075]$).
  - Bass RMS $\to$ Stroke Width ($[0.003, 0.018]$).
  - Lead pitch $\to$ Spatial Harmonic ($[2, 8]$ integer quantized for $C^0/C^1$ seam closure).
  - FX energy $\to$ Band Span ($[0.25, 0.48]$).
  - Transport ramp $\to$ Phase ($[0.0, 1.0]$).
- **Safe Margin Rule**: Strictly limits amplitude such that $\frac{\text{band\_span}}{2} + \text{amplitude} + \frac{\text{stroke\_width}}{2} \le 0.42$.

---

## 4. Host Environment & Checked Tooling

| Software / Tool | Host Version | Location | Verification Status |
| :--- | :--- | :--- | :--- |
| **Ableton Live** | `12.4.6 Suite` | `/Applications/Ableton Live 12 Suite.app` | App detected; generated ALS round trip checked offline; opening in Live not checked here. |
| **Cycling '74 Max** | `8.6.2` | `/Applications/Max.app` | App detected; generated patch structure checked offline; opening in Max not checked here. |
| **Apple Clang** | `15.0.0 (C++17)` | `/usr/bin/clang++` | Verified (Compiled & executed headless DSP tests) |
| **CMake** | `4.4.4` | `/opt/homebrew/bin/cmake` | Verified (Build system ready) |
| **Python** | `3.12.0 / 3.15.0` | `/Library/.../3.12` & `/opt/homebrew` | Verified (NumPy, SciPy, Wave, Gzip tested) |
| **Node.js** | `v26.11.1` | `/opt/homebrew/bin/node` | Verified |
| **TouchDesigner** | Not Installed | N/A | Offline mock passed; In-app test **PENDING** |

---

## 5. Quickstart & Usage

### A. Run Automated Verification Suite
```bash
python3 verify_audio_music_pipeline.py
```

### B. Run Bidirectional Translation Demos
```bash
# Direction 1: Visual Score -> MIDI + Audio WAV
python3 examples/visual_score_to_music/run_demo.py

# Direction 2: Music -> 4-Face Cube Visual Parameters
python3 examples/music_to_visual_control/run_demo.py
```

### C. Build Ableton Live 12 Project (.als)
```python
from tools.ableton_als_builder import AbletonSetBuilder

builder = AbletonSetBuilder(tempo=124.0)
builder.add_midi_track("Drums", 12)
builder.add_midi_track("Sub_Bass", 24)
builder.save_als("MyProject.als")
```

### D. Compile Headless C++ DSP Unit Test
```bash
clang++ -std=c++17 -Wall -Wextra -O2 \
  juce_scaffold/tests/test_dsp_headless.cpp \
  -o juce_scaffold/tests/test_dsp_runner
./juce_scaffold/tests/test_dsp_runner
```

### E. Start MCP Stdio Server
```bash
python3 tools/mcp_audio_server.py
```

The plugin's `mcp.json` starts the server automatically in supported local hosts. To check the revised contract and protocol boundary:

```bash
python3 -m unittest discover -s tests -v
```

---

## 6. Verification Status Report

- **Total Phases Evaluated**: 12
- **LULUS (Passed)**: 10
  - Python Syntax & Compilation (100% clean)
  - JSON Schema & File Integrity (100% clean)
  - Bidirectional Cross-Modal Engine (Verified with audio render and safe margin math)
  - Ableton Live 12 file structure (ALS gzip XML generator & parser checked offline)
  - Max/MSP 8.6 file structure (Maxpat JSON generator & wiring verifier checked offline)
  - Audio DSP Analysis & QA (RMS, Centroid, True Peak, Clipping QA verified)
  - JUCE C++ DSP Core Headless Test (Compiled via Clang 15.0; verified stability)
  - Model Context Protocol (MCP) Server (7 tool endpoints; local lifecycle and MIDI contract tests)
  - TouchDesigner Adapter Mock & Math Proofs (Idempotence & $C^0/C^1$ seam math verified)
- **GAGAL (Failed)**: 0
- **BELUM DIUJI (Pending)**: 2
  - *TouchDesigner Live In-App Runtime*: TouchDesigner is not installed on this host machine; in-app rendering deferred to staging bench.
  - *Physical Multi-Display LED Cube Hardware*: No physical 7200x1080 4-sided LED wall attached to this machine.

---

## 7. License & Attribution

- See `ATTRIBUTION.md` and `LICENSE-TDMCP.md` for full upstream notices and credits.
- Authored by J. G. Agathon.
