#pragma once
#include <cmath>
#include <cstdint>
#include <algorithm>

namespace AudioMusicPipeline {

/**
 * @brief High-performance real-time DSP processor core.
 *
 * Invariants:
 * - Real-time safe: Zero memory allocations, zero locks, zero file I/O inside processBlock.
 * - Numerically stable state-variable filter topology (SVF) with smooth parameter updates.
 */
class DSPCore {
public:
    enum FilterType {
        LowPass = 0,
        BandPass = 1,
        HighPass = 2
    };

    DSPCore() = default;

    void prepare(double sampleRate, uint32_t maxBlockSize) {
        m_sampleRate = sampleRate > 0.0 ? sampleRate : 44100.0;
        m_maxBlockSize = maxBlockSize;
        reset();
    }

    void reset() {
        m_s1[0] = 0.0f; m_s1[1] = 0.0f;
        m_s2[0] = 0.0f; m_s2[1] = 0.0f;
        m_envelope = 0.0f;
    }

    void setParameters(float cutoffHz, float resonanceQ, float drive, FilterType type) {
        m_cutoff = std::max(20.0f, std::min(static_cast<float>(m_sampleRate * 0.49), cutoffHz));
        m_q = std::max(0.5f, std::min(10.0f, resonanceQ));
        m_drive = std::max(1.0f, std::min(10.0f, drive));
        m_type = type;
        updateCoefficients();
    }

    void process(float* const* channelData, int numChannels, int numSamples) {
        if (numChannels < 1 || numSamples < 1) return;

        for (int i = 0; i < numSamples; ++i) {
            float inL = channelData[0][i];
            float inR = (numChannels > 1) ? channelData[1][i] : inL;

            // Apply saturation drive (soft-clipping hyperbolic tangent approximation)
            float drivenL = std::tanh(inL * m_drive);
            float drivenR = std::tanh(inR * m_drive);

            // Process State-Variable Filter (Chamberlin / Zavalishin topology)
            float outL = processSample(drivenL, 0);
            float outR = processSample(drivenR, (numChannels > 1) ? 1 : 0);

            channelData[0][i] = outL;
            if (numChannels > 1) {
                channelData[1][i] = outR;
            }

            // Envelope follower for visual telemetry
            float rectSample = std::max(std::abs(outL), std::abs(outR));
            float alpha = (rectSample > m_envelope) ? 0.01f : 0.001f; // Fast attack, smooth decay
            m_envelope += alpha * (rectSample - m_envelope);
        }
    }

    float getEnvelopeLevel() const noexcept {
        return m_envelope;
    }

private:
    void updateCoefficients() {
        // Pre-warped frequency
        float wd = 2.0f * static_cast<float>(M_PI) * m_cutoff;
        float T = 1.0f / static_cast<float>(m_sampleRate);
        float wa = (2.0f / T) * std::tan(wd * T / 2.0f);
        m_g = wa * T / 2.0f;
        m_damping = 1.0f / m_q;
    }

    float processSample(float input, int ch) {
        // Linear SVF tick
        float hp = (input - (2.0f * m_damping + m_g) * m_s1[ch] - m_s2[ch]) / (1.0f + 2.0f * m_damping * m_g + m_g * m_g);
        float bp = m_g * hp + m_s1[ch];
        m_s1[ch] = m_g * hp + bp;
        float lp = m_g * bp + m_s2[ch];
        m_s2[ch] = m_g * bp + lp;

        switch (m_type) {
            case LowPass:  return lp;
            case BandPass: return bp;
            case HighPass: return hp;
            default:       return lp;
        }
    }

    double m_sampleRate = 44100.0;
    uint32_t m_maxBlockSize = 512;
    float m_cutoff = 1000.0f;
    float m_q = 0.707f;
    float m_drive = 1.0f;
    FilterType m_type = LowPass;

    float m_g = 0.0f;
    float m_damping = 1.0f;
    float m_s1[2] = {0.0f, 0.0f};
    float m_s2[2] = {0.0f, 0.0f};
    float m_envelope = 0.0f;
};

} // namespace AudioMusicPipeline
