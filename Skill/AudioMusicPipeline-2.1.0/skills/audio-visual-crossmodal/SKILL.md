---
name: audio-visual-crossmodal
description: "Bidirectional cross-modal engine: convert visual scores to music/audio and audio/music to visual control parameters, with loss analysis."
---

# Bidirectional Audio-Visual Cross-Modal Engine

Use this skill to translate between visual representations (graphic scores, geometric coordinates, color palettes) and musical structures (MIDI, pitch, harmony, audio features), operating strictly in both directions.

## Direction 1: Visual Score $\to$ Music / Audio
1. **Definition of Visual Score**:
   - A *Visual Score* is NOT traditional Western staff notation. It is a graphical, parametric, or geometric score (pioneered by Xenakis, Cage, Bussotti, and contemporary generative audiovisual artists) where spatial dimensions, trajectories, and colors correspond to sound parameters:
     - $X$-axis: Temporal progression (normalized $[0.0, 1.0]$ mapped to musical beats and bars).
     - $Y$-axis: Pitch trajectory (normalized $[0.0, 1.0]$ mapped to MIDI register, snapped to scale degrees).
     - Stroke Width / Density: Dynamic velocity ($[0.002, 0.040] \to [40, 120]$).
     - Color Hue: Timbral brightness (mapped to synth filter cutoff or MIDI voice role).
2. **Execution**:
   ```python
   from tools.crossmodal_engine import CrossModalEngine
   result = CrossModalEngine.visual_score_to_music(score_data, bpm=124.0, total_bars=4)
   # Writes result['midi_bytes'] and result['wav_bytes']
   ```

## Direction 2: Music / Audio $\to$ Visual Control Data
1. **Feature Extraction & Mapping**:
   - Audio RMS / Stems $\to$ 4-sided cube ribbon parameters:
     - Drums RMS $\to$ `amplitude` ($[0.015, 0.075]$)
     - Bass RMS $\to$ `stroke_width` ($[0.003, 0.018]$)
     - Synth/Lead pitch $\to$ `spatial_harmonic` ($[2, 8]$ integer quantized)
     - FX/Drop energy $\to$ `band_span` ($[0.25, 0.48]$)
     - Master Link ramp $\to$ `u_phase` ($[0.0, 1.0]$)
2. **Safe Margin Enforcement**:
   - Enforce the top/bottom 1080p boundary invariant:
     $$\frac{\text{band\_span}}{2} + \text{amplitude} + \frac{\text{stroke\_width}}{2} \le 0.42$$
   - Throttles candidate amplitude gracefully under extreme inputs.
3. **Execution**:
   ```python
   result = CrossModalEngine.music_to_visual_control(midi_notes, audio_rms, total_bars=4)
   # Returns result['cube_parameters'] and result['reconstructed_visual_score']
   ```

## Lossy & Irreversibility Metrics
- **Phase Erasure**: Converting audio waveforms into RMS envelopes or FFT magnitude discards phase ($100\%$ irreversible).
- **Pitch Quantization**: Snapping continuous graphical curves into 12-TET notes introduces cents error (reported in `loss_metrics['pitch_quantization_mean_cents']`).
- **Dimensional Collapse**: Projecting a 2D spatial drawing onto a 1D timeline collapses simultaneous horizontal overlaps into polyphonic voice chords.
