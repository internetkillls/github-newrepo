# Technical Guide: Live Performance Rig Architecture

## Latency Budget Equation
$$T_{\text{total}} = T_{\text{in\_buffer}} + T_{\text{dsp\_process}} + T_{\text{out\_buffer}} + T_{\text{da\_converter}}$$
For a 128-sample buffer at 48 kHz:
$$T_{\text{buffer}} = \frac{128}{48000} \approx 2.67 \text{ ms}$$
Total round-trip latency typically reaches $5.5 - 7.0 \text{ ms}$, safely under the $10 \text{ ms}$ psychoacoustic threshold.
