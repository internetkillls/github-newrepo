# Technical Guide: Audio Quality Assurance

## BS.1770 / EBU R128 Loudness Filter Topology
- Stage 1: High-shelf filter boosting high frequencies (modeling head acoustic diffraction).
- Stage 2: High-pass filter cutting sub-rumble below 38 Hz.
- Mean square energy calculated with 400ms gating blocks.
Implemented in `tools/audio_dsp_analyzer.py`.
