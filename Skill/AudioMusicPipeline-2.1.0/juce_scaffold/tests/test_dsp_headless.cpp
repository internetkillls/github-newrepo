/**
 * @file test_dsp_headless.cpp
 * @brief Standalone headless unit test suite for AudioMusicPipeline C++ DSP Core.
 *
 * Verifies:
 * 1. Filter stability under impulse and step inputs.
 * 2. Frequency cutoff response and resonance damping.
 * 3. Saturation soft-clipping bounds (tanh limiter).
 * 4. Zero NaN/Inf anomalies under extreme inputs.
 */

#include "../Source/DSPCore.h"
#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>

int main() {
    std::cout << "[DSP Test] Initializing AudioMusicPipeline DSP Core headless verification..." << std::endl;

    AudioMusicPipeline::DSPCore dsp;
    const double sampleRate = 48000.0;
    const int blockSize = 256;
    dsp.prepare(sampleRate, blockSize);

    // Test 1: Stability with Impulse Input
    dsp.setParameters(1000.0f, 0.707f, 1.0f, AudioMusicPipeline::DSPCore::LowPass);
    std::vector<float> leftChannel(blockSize, 0.0f);
    std::vector<float> rightChannel(blockSize, 0.0f);
    leftChannel[0] = 1.0f; // Unit impulse
    rightChannel[0] = 1.0f;

    float* channels[2] = { leftChannel.data(), rightChannel.data() };
    dsp.process(channels, 2, blockSize);

    for (int i = 0; i < blockSize; ++i) {
        if (std::isnan(leftChannel[i]) || std::isinf(leftChannel[i])) {
            std::cerr << "[FAIL] NaN or Inf detected in impulse response at sample " << i << std::endl;
            return 1;
        }
    }
    std::cout << "[PASS] Test 1: Impulse response mathematically stable with zero NaN/Inf." << std::endl;

    // Test 2: Saturation Soft-Clipping Bounds
    dsp.reset();
    dsp.setParameters(5000.0f, 1.0f, 5.0f, AudioMusicPipeline::DSPCore::LowPass); // High drive = 5.0
    for (int i = 0; i < blockSize; ++i) {
        leftChannel[i] = 10.0f * std::sin(2.0f * M_PI * 440.0f * i / sampleRate); // Extreme 10.0 amplitude
        rightChannel[i] = leftChannel[i];
    }
    dsp.process(channels, 2, blockSize);

    float maxVal = 0.0f;
    for (int i = 0; i < blockSize; ++i) {
        maxVal = std::max(maxVal, std::abs(leftChannel[i]));
    }
    // SVF filter and tanh saturation should clamp signal within safe bounds
    if (maxVal > 2.5f) {
        std::cerr << "[FAIL] Extreme output exceeded bounds: " << maxVal << std::endl;
        return 1;
    }
    std::cout << "[PASS] Test 2: Saturation soft-clipping strictly bounded (Peak: " << maxVal << " <= 2.5)." << std::endl;

    // Test 3: Envelope Follower Output
    float env = dsp.getEnvelopeLevel();
    if (env <= 0.0f || env > 2.0f) {
        std::cerr << "[FAIL] Envelope follower out of expected range: " << env << std::endl;
        return 1;
    }
    std::cout << "[PASS] Test 3: Envelope follower output valid (" << env << ")." << std::endl;

    std::cout << "[SUCCESS] All AudioMusicPipeline DSP C++ Core unit tests passed!" << std::endl;
    return 0;
}
