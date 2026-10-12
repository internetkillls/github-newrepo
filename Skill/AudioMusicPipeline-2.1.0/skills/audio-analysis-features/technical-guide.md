# Technical Guide: Audio Feature Extraction

## Execution Recipe via `tools/audio_dsp_analyzer.py`
```python
from tools.audio_dsp_analyzer import AudioDspAnalyzer

samples, rate, channels = AudioDspAnalyzer.load_wav("path/to/audio.wav")
features = AudioDspAnalyzer.analyze_features(samples, sample_rate=rate)
print(f"Mean Spectral Centroid: {features['spectral_centroid_mean']:.1f} Hz")
print(f"Detected Onsets: {features['detected_onsets_count']}")
```
