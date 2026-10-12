---
name: live-performance-rig
description: "Design and operate low-latency live performance rigs: buffer safety, redundant audio failover, MIDI controller mapping, and master clock synchronization."
---

# Live Performance Rig Architecture

Use this skill to design, configure, and operate live stage rigs connecting Ableton Live, Max/MSP, TouchDesigner, hardware synthesizers, and audio interfaces.

## Core Procedures

1. **Latency & Buffer Sizing**:
   - Audio buffer size:
     - 64 samples at 48 kHz: $1.33 \text{ ms}$ output latency (tight for live finger drumming / vocal monitoring).
     - 128 samples at 48 kHz: $2.67 \text{ ms}$ output latency (industry sweet spot for live electronics).
     - 256 samples at 48 kHz: $5.33 \text{ ms}$ output latency (maximum acceptable for live sync).
   - Video buffer size:
     - 60 fps frame budget: $16.6 \text{ ms}$ per frame.

2. **Redundant Failover Switching**:
   - Use automated audio switchers (e.g., Radial SW8 or dual interface Dante networks).
   - In TouchDesigner & Max: Maintain an autonomous 7-channel fallback generator with silence watchdog timers ($T_{\text{silence}} = 2.5 \text{ s}$) that automatically fades into backup loops if DAW transport dies.

3. **Master Clock & Transport Synchronization**:
   - Use Ableton Link as peer-to-peer network master.
   - Fallback to MIDI Clock / DIN Sync for vintage analog drum machines.
   - Broadcast OSC scene cue triggers on track changes: `/scene/launch <int>`.
