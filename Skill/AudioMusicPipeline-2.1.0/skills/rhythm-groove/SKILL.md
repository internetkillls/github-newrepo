---
name: rhythm-groove
description: "Generate metric grids, Euclidean rhythms, polyrhythmic cycles, syncopation templates, and groove swing quantization."
---

# Rhythm & Groove Architecture

Use this skill to construct drum patterns, rhythmic grids, Euclidean distribution algorithms, polyrhythms, and groove timing offsets.

## Core Procedures

1. **Euclidean Rhythm Generation ($E(k, n)$)**:
   - Distribute $k$ active pulses across $n$ time steps as evenly as possible using Bjorklund's algorithm:
     - $E(4, 16)$: Standard four-on-the-floor kick `[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]`.
     - $E(5, 16)$: Bossa-nova / Afro-Cuban clave variant `[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]`.
     - $E(7, 16)$: West African bell pattern.

2. **Polyrhythms & Polymeters**:
   - Polyrhythm: Two different subdivisions occupying the same time span (e.g., 3 against 2, 4 against 3).
   - Polymeter: Different bar lengths running concurrently with the same subdivision pulse (e.g., 5/4 bassline against 4/4 drums).

3. **Groove & Swing Quantization**:
   - Roger Linn style 16th-note swing: Delay even-numbered 16th notes by percentage $S \in [50\%, 75\%]$:
     $$\Delta t = \text{step\_duration} \times \left(\frac{S - 50}{50}\right)$$
   - Humanization: Micro-timing jitter ($[-4, +4]$ ticks) and velocity randomization ($[-6, +6]$) applied to avoid robotic static playback.

4. **MIDI Mapping**:
   - Note 36: Kick
   - Note 38/40: Snare / Clap
   - Note 42: Closed Hi-Hat
   - Note 46: Open Hi-Hat
   - Note 49: Crash / Splash
