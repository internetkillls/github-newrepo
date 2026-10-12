---
name: audio-qa-verification
description: "Verify audio delivery quality: integrated loudness (LUFS), True Peak headroom, digital clipping detection, DC offset, and stereo phase correlation."
---

# Audio Quality Assurance & Verification

Use this skill to audit audio renders, stems, and project files before delivery, live performance, or client presentation.

## Core QA Checklist

1. **Digital Clipping & Intersample Peak (ISP)**:
   - Peak level must be $\le -0.5 \text{ dBFS}$ for uncompressed delivery; $\le -1.0 \text{ dBFS}$ for lossy codecs (MP3/AAC).
   - Zero consecutive clipped samples ($s \ge 0.999$).

2. **Integrated Loudness Standards**:
   - Streaming Target: $-14.0 \text{ LUFS} \pm 1.0$ (Spotify, Apple Music, YouTube).
   - Club / Live PA Master: $-9.0 \text{ to } -6.0 \text{ LUFS}$ with controlled dynamic range.

3. **DC Offset & Sub-Sonic Rumble**:
   - Mean amplitude across track: $|\mu_{\text{sample}}| < 0.005$ ($< -46 \text{ dBFS}$).
   - High-pass filtering at 20-30 Hz (24 dB/oct) to prevent amplifier DC saturation.

4. **Stereo Phase Correlation**:
   - Pearson correlation coefficient between Left and Right channels:
     $$r = \frac{\sum (L - \bar{L})(R - \bar{R})}{\sqrt{\sum (L - \bar{L})^2 \sum (R - \bar{R})^2}} \in [0.0, 1.0]$$
   - $r > 0.5$: Safe mono compatibility.
   - $r < 0.0$: Severe phase cancellation in mono playback (e.g. phone speakers, club PA systems).

5. **Automated Verification**:
   - Run verification via `tools/audio_dsp_analyzer.py`:
     ```python
     from tools.audio_dsp_analyzer import AudioDspAnalyzer
     samples, rate, _ = AudioDspAnalyzer.load_wav("my_render.wav")
     report = AudioDspAnalyzer.run_qa_checks(samples, rate)
     assert report["qa_pass"] is True
     ```
