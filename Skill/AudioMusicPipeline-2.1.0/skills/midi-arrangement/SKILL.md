---
name: midi-arrangement
description: "Orchestrate multi-track MIDI arrangements, voice allocation, clip boundaries, velocity contours, and SMF 1.0 serialization."
---

# MIDI & Multi-Track Arrangement Engine

Use this skill to transform harmonic progressions, melodic lines, and rhythmic grooves into cohesive multi-track MIDI arrangements.

## Core Procedures

1. **Orchestral Role & Voice Allocation**:
   - Assign musical material to standard stems:
     - Channel 0: Lead Melody / Hook (Monophonic or tight duophonic)
     - Channel 1: Harmony Chords / Arpeggiator (Polyphonic pad / keys)
     - Channel 2: Bass / 808 (Monophonic low register C1 - C3)
     - Channel 3: Atmospheric Textures / FX (Stereo wide soundscapes)
     - Channel 9: Drums / Percussion (GM MIDI drum map)

2. **Dynamics & Expression Automation**:
   - Velocity contouring: Accents on downbeats, ghost notes (velocity 30-50).
   - CC Automation: CC 1 (Mod Wheel / Filter Cutoff), CC 11 (Expression), CC 64 (Sustain Pedal), CC 74 (Brightness).

3. **Standard MIDI File Export**:
   - Assemble tracks into `tools/smf_midi.py`:
     ```python
     from tools.smf_midi import MidiFile, MidiTrack
     midi = MidiFile(ticks_per_quarter=480, format_=1)
     # Add conductor and instrument tracks
     midi.write("output.mid")
     ```
   - Verify zero overlap on monophonic tracks (Note Off strictly preceding next Note On for same pitch).
