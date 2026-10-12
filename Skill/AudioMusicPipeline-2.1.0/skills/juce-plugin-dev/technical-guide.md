# Technical Guide: JUCE Audio Plugin Development

## State-Variable Filter (SVF) Mathematics
The continuous-time state-variable filter:
$$\frac{d^2 y}{dt^2} + 2 R \omega_0 \frac{dy}{dt} + \omega_0^2 y = \omega_0^2 x(t)$$
Bilinear transform with frequency pre-warping:
$$\omega_a = \frac{2}{T} \tan\left(\frac{\omega_d T}{2}\right), \quad g = \frac{\omega_a T}{2}$$
Outputs:
- Low-Pass: $y_{\text{LP}} = g \cdot y_{\text{BP}} + s_2$
- Band-Pass: $y_{\text{BP}} = g \cdot y_{\text{HP}} + s_1$
- High-Pass: $y_{\text{HP}} = \frac{x - (2R + g)s_1 - s_2}{1 + 2Rg + g^2}$
All implemented with zero allocations in `juce_scaffold/Source/DSPCore.h`.
