---
name: sound-design-dsp
description: "Design synthesis architectures (subtractive, FM, wavetable, granular, physical modelling), effect chains, and sound design recipes."
---

# Sound Design & Synthesis Architectures

Use this skill to design synthesizer patches, signal flow chains, modulation routings, and timbral sound design recipes across native DAW devices, Max/MSP, and JUCE DSP.

## Synthesis Paradigms

1. **Subtractive Synthesis**:
   - Oscillators (Saw, Pulse/PWM, Triangle) -> Saturation Drive -> Multi-mode 24dB/oct Filter -> VCA Envelope.
   - Envelopes: Fast attack punch for bass/leads; slow exponential attack for ambient pads.

2. **Frequency Modulation (FM) Synthesis**:
   - 2 to 6 Operator algorithms (Carrier + Modulators).
   - Non-integer frequency ratios (e.g. 1 : 2.718) produce metallic, bell-like, inharmonic bells and industrial textures.
   - Integer ratios (1:1, 1:2, 1:3) produce rich brass, reed, and harmonic leads.

3. **Wavetable & Granular Synthesis**:
   - Wavetable position modulation via sync'd LFOs.
   - Granular: Grain size ($20 - 100 \text{ ms}$), density (10-50 grains/sec), spray/jitter, pitch transposition.

4. **Effects Chain Architecture**:
   - Utility / Gain Staging -> Corrective Subtractive EQ -> Saturation / Distortion -> Modulation (Chorus/Phaser) -> Time-based FX (Stereo Delay / Algorithmic Reverb) -> Limiter.
