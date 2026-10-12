# Technical Guide: MIDI & Multi-Track Arrangement

## Standard MIDI File (SMF 1.0) Architecture
- **Division**: 480 PPQ (ticks per quarter note) is industry standard for Ableton Live and Logic Pro.
- **Delta-Time Rules**: Always calculate delta relative to previous event tick. Note Off must precede simultaneous Note On.
- **Running Status**: Permitted in SMF streams, but explicit status bytes are preferred for robust DAW import.
