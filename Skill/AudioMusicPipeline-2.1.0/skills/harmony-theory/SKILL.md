---
name: harmony-theory
description: "Construct chord progressions, voice leading, modal interchange, microtonal tunings, and harmonic tension curves."
---

# Harmony & Music Theory Engine

Use this skill to design, analyze, and verify harmonic progressions, chord voicings, voice-leading smoothness, and microtonal systems.

## Core Procedures

1. **Modal & Scale Definition**:
   - Supported modes: Major, Natural Minor, Harmonic Minor, Melodic Minor, Dorian, Phrygian, Lydian, Mixolydian, Locrian, Pentatonic.
   - Microtonal tunings: Custom frequency tables, Just Intonation, 24-EDO quarter-tone pitch bends.

2. **Progression Synthesis**:
   - Build harmonic tables with degree, Roman numeral, chord symbol, bass note, and concrete MIDI note voicings:
     - Example (D Dorian):
       * Bar 1: `i` -> `Dm7` [D3, A3, C4, F4, A4]
       * Bar 2: `IV` -> `G7` [G2, G3, B3, D4, F4]
       * Bar 3: `bVII` -> `Cmaj7` [C3, G3, B3, E4, G4]
       * Bar 4: `v` -> `Am7` [A2, E3, G3, C4, E4]

3. **Smooth Voice Leading Verification**:
   - Enforce minimal voice movement between adjacent chords:
     $$\Delta_{\text{voice}} = \sum_{v=1}^{V} |p_{v, t} - p_{v, t-1}| \le 8 \text{ semitones}$$
   - Avoid parallel octaves and fifths between outer voices where stylistic purity is desired.
   - Retain common tones across chord transitions.

4. **Output Format**:
   - Exports directly to `harmonic_system` in `contracts/crossmodal_contract.schema.json`.
