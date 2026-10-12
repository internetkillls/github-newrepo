---
name: adapter-resolume
description: "Downstream output adapter for Resolume Arena: multi-slice 4-face cube routing, OSC cue synchronization, and DXV3 video playback."
---

# Resolume Arena Show Adapter

Use this skill to package visual loops, configure multi-slice screen routing, and synchronize live show cues in Resolume Arena (7.0+).

## Core Procedures

1. **Advanced Output 4-Sided Cube Slicing**:
   - Master Canvas: $7200 \times 1080$ (or $3600 \times 540$ preview).
   - Slice 1 (North Face): Input $[0, 1800] \times [0, 1080]$.
   - Slice 2 (East Face):  Input $[1800, 3600] \times [0, 1080]$.
   - Slice 3 (South Face): Input $[3600, 5400] \times [0, 1080]$.
   - Slice 4 (West Face):  Input $[5400, 7200] \times [0, 1080]$.

2. **OSC Cue Synchronization**:
   - Ingest cues from Ableton Live / Max:
     - `/composition/layers/1/clips/1/connect 1` (Trigger Loop A)
     - `/composition/bpm <float>`
     - `/composition/master <float>`

3. **Timekeeping Crossing Midnight**:
   - For evening venue sessions running from 22:00 to 04:00, use absolute elapsed second offsets rather than naive wall-clock comparisons to prevent negative duration errors when passing 00:00.
