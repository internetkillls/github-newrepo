---
name: audio-analysis-features
description: "Extract spectral features, FFT frequency band energies, RMS envelopes, spectral centroids, and transient onsets from audio signals."
---

# Audio Feature Extraction & DSP Analysis

Use this skill to extract perceptual and physical features from audio files and live streams to drive visual parameters, monitor mix balances, or trigger cross-modal cues.

## Core Procedures

1. **RMS & Peak Envelope Following**:
   - Extract frame-by-frame energy with configurable attack and decay smoothing.
   - Separate transient peaks from sustained RMS loudness.

2. **Nyquist-Compliant 4-Band Spectral Splitting**:
   - Always filter at the native audio rate (44.1 kHz / 48 kHz) before downsampling to video frame rates.
   - Frequency band definitions:
     - Sub-Bass: 20 Hz - 90 Hz
     - Bass: 90 Hz - 250 Hz
     - Mid: 250 Hz - 2500 Hz
     - High: 2500 Hz - 16000 Hz

3. **Spectral Centroid (Perceptual Brightness)**:
   $$C = \frac{\sum_{k=0}^{N/2} f_k |X[k]|}{\sum_{k=0}^{N/2} |X[k]|}$$
   - Maps directly to visual color temperature, spatial frequency, and shader particle dispersion.

4. **Transient & Onset Detection**:
   - Compute spectral flux or positive energy difference ($\Delta E = \max(0, E_t - E_{t-1})$).
   - Generate discrete pulse triggers (e.g. for kick drum visual impacts).
