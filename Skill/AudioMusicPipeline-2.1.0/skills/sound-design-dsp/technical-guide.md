# Technical Guide: Sound Design & Synthesis

## FM Synthesis Modulation Index Formula
$$y(t) = A \sin\left(\omega_c t + I \cdot \sin(\omega_m t)\right)$$
where:
- $\omega_c = 2\pi f_c$ is carrier angular frequency
- $\omega_m = 2\pi f_m$ is modulator angular frequency
- $I = \frac{\Delta f}{f_m}$ is the modulation index controlling spectral bandwidth and sideband spread.
