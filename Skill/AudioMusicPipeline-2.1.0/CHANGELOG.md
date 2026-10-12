# Changelog: AudioMusicPipeline

## 2.1.0

- Added a DAW-neutral project validator with field-path diagnostics and cross-field checks for duplicate tracks, note boundaries, and ordered spectral bands. The contract now defines note time in quarter-note beats and accepts both 2.0.0 and 2.1.0 projects.
- Added offline SMF Type 1 export from validated project tracks, with dry-run preview, no-overwrite default, and explicit rejection of microtones and non-440 Hz tuning that this exporter cannot encode.
- Added portable `mcp.json` discovery, capability reporting, typed tool arguments and structured results, and the 2025-11-25 stdio MCP lifecycle. Corrected the Max tool to advertise only its implemented OSC patch type.
- Added behavioral tests for 6/8 timing, MIDI round trip, invalid contracts, file side effects, and MCP handshake. Documented decisions from the seven supplied projects in `docs/inspiration-review.md`.

## 2.0.0 (Major Architectural Evolution from VisualPipeline 1.3.0)

### 1. Paradigm Shift & Scope Expansion
- **Bidirectional Architecture**: Evolved from a unidirectional, TouchDesigner-centric visual pipeline into a comprehensive, end-to-end music and audio pipeline with bidirectional cross-modal translation (*Visual Score <-> Music/Audio*).
- **First-Class Music Composition**: Added dedicated skills and engines for songwriting ideation, modal harmony theory, voice leading, rhythmic grids, Euclidean patterns, groove swing, and multi-track MIDI arrangement.
- **TouchDesigner Decentered**: TouchDesigner is no longer the center of the system; it is positioned as a downstream visual adapter alongside Resolume Arena.

### 2. Verified Tooling & Real Implementation
- **Pure-Python Standard MIDI 1.0 Engine (`smf_midi.py`)**: Zero-dependency Type 0/1 SMF parser and serializer supporting Note On/Off, CC, Pitch Bend, Tempo, and Time Signature.
- **Ableton Live 12 Suite Bridge (`ableton_als_builder.py`)**: Gzip-compressed XML generator and parser compliant with host Ableton Live 12.4.6 schema (`MinorVersion="12.0_12402"`). Verified against `/Applications/Ableton Live 12 Suite.app`.
- **Cycling '74 Max 8.6 Engine (`maxpat_builder.py`)**: JSON patcher builder and validator producing clean, loadable `.maxpat` files with verified patch cord wiring and OSC telemetry routing. Verified against `/Applications/Max.app`.
- **JUCE C++ DSP Plugin Architecture (`juce_scaffold/`)**:
  - Implemented real-time safe C++17 State-Variable Filter (SVF) with hyperbolic tangent saturation drive and envelope follower in `DSPCore.h`.
  - Implemented standard APVTS parameter layout in `PluginProcessor.cpp` and modern CMake target in `CMakeLists.txt`.
  - Added headless C++ unit test runner (`test_dsp_headless.cpp`) compiled and verified via host Apple Clang 15.0.
- **Model Context Protocol (MCP) Server (`mcp_audio_server.py`)**: Executable stdio JSON-RPC tool server exposing project validation, visual score translation, ALS generation, and safe margin calculations.
- **Audio DSP Analyzer & QA (`audio_dsp_analyzer.py`)**: Extracted RMS envelopes, spectral centroid, onsets, and 4-band energies; audited True Peak, clipping events, and DC offset.

### 3. Bidirectional Cross-Modal Contracts
- Defined typed JSON schemas: `contracts/crossmodal_contract.schema.json` and `contracts/visual_score_schema.json`.
- Implemented `tools/crossmodal_engine.py` translating graphic visual scores to MIDI/audio and audio streams back to 4-face cube ribbons.
- Documented explicit loss metrics: cents quantization error, audio phase erasure in RMS/FFT magnitudes, and 2D spatial dimensional collapse.

### 4. Verification & Testing Rigor
- Created `verify_audio_music_pipeline.py` running 11 distinct evaluation phases.
- Results cleanly categorized into `LULUS` (9 runnable offline/local phases), `GAGAL` (0 errors), and `BELUM DIUJI (PENDING)` (TouchDesigner in-app runtime and physical multi-display LED wall, honestly deferred without mock inflation).

---

## 1.3.0 (Upstream VisualPipeline Archive)
- Fixed TouchDesigner operator class names (`abletonlinkCHOP`, `audiodeviceinCHOP`, `mathCHOP`).
- Added `studio-audio-reactive` skill, 4-band Nyquist-compliant audio filtering, explicit silence timer, and 4-face cube ribbon GLSL shaders.
- Included reference audio loop `assets/audio_reference_loop.wav` (CC0).
