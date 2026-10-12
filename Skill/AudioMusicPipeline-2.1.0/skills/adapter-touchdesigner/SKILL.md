---
name: adapter-touchdesigner
description: "Downstream visual adapter for TouchDesigner: audio-reactive baseCOMP engines, 4-sided cube parameter routing, and seamless GLSL loops."
---

# TouchDesigner Visual Adapter

Use this skill to deploy downstream generative visual networks, 4-face cube perimeter ribbons (7200x1080), and audio-reactive engines in Derivative TouchDesigner (2022+ / 2023+).

## Position in AudioMusicPipeline
TouchDesigner is a specialized **visual renderer and adapter**, receiving synchronized musical stems, MIDI events, OSC telemetry, and transport phase from upstream music engines (`ableton-live-integration`, `max-msp-m4l`, `audio-visual-crossmodal`).

## Verified Components Retained from VisualPipeline 1.3.0

1. **`audio_reactive_engine` baseCOMP**:
   - Nyquist-compliant audio-rate filtering (44.1 kHz) before downsampling to video frame rate.
   - Dedicated band splitting: Sub (20-90 Hz), Bass (90-250 Hz), Mid (250-2500 Hz), High (2500-16000 Hz).
   - Dynamic peak auto-gain normalization.
   - Explicit silence safeguard timer ($T = 2.5\text{s}$) crossfading to an autonomous 7-channel fallback generator.
   - Selective cooking null output `audio_drivers`.

2. **`ableton_cube_router` baseCOMP**:
   - Ingests OSC, Ableton Link, and MIDI.
   - Strictly enforces the top/bottom 1080p safe margin rule:
     $$\frac{\text{band\_span}}{2} + \text{amplitude} + \frac{\text{stroke\_width}}{2} \le 0.42$$
   - Quantizes spatial harmonics to integer (`integer='floor'`) to guarantee $C^0/C^1$ seamless corner continuity across the 4 cube faces.

3. **`glsl_visual_loop_builder` & Multi-TOP**:
   - Deploys 7200x1080 fragment shaders (`cube_audio_ribbons.frag` / `audio_reactive_loop.frag`) with standard `TDOutputSwizzle` and antialiasing via `uTDOutputInfo.res.zw`.

## Runtime Testing Status
- TouchDesigner is **not installed** on this packaging host machine.
- All Python builders, AST structures, operator class mappings, and shader closure equations pass offline mathematical and mock verification.
- Live in-app runtime verification is marked as **PENDING / TERTUNDA** until opened on a machine with active TouchDesigner.
