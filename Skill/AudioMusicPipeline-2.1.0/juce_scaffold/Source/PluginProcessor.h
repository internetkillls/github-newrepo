#pragma once
#include "DSPCore.h"

// If JUCE is available via CMake, include juce_audio_processors
#if __has_include(<juce_audio_processors/juce_audio_processors.h>)
 #include <juce_audio_processors/juce_audio_processors.h>
 #define HAS_JUCE_FRAMEWORK 1
#else
 #define HAS_JUCE_FRAMEWORK 0
#endif

#if HAS_JUCE_FRAMEWORK
class AudioMusicPipelineAudioProcessor : public juce::AudioProcessor {
public:
    AudioMusicPipelineAudioProcessor();
    ~AudioMusicPipelineAudioProcessor() override = default;

    void prepareToPlay(double sampleRate, int samplesPerBlock) override;
    void releaseResources() override;
    void processBlock(juce::AudioBuffer<float>&, juce::MidiBuffer&) override;

    juce::AudioProcessorEditor* createEditor() override;
    bool hasEditor() const override { return true; }

    const juce::String getName() const override { return "AudioMusicPipeline"; }
    bool acceptsMidi() const override { return true; }
    bool producesMidi() const override { return true; }
    double getTailLengthSeconds() const override { return 0.0; }

    int getNumPrograms() override { return 1; }
    int getCurrentProgram() override { return 0; }
    void setCurrentProgram(int) override {}
    const juce::String getProgramName(int) override { return {}; }
    void changeProgramName(int, const juce::String&) override {}

    void getStateInformation(juce::MemoryBlock& destData) override;
    void setStateInformation(const void* data, int sizeInBytes) override;

private:
    AudioMusicPipeline::DSPCore m_dspCore;
    juce::AudioProcessorValueTreeState m_parameters;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR(AudioMusicPipelineAudioProcessor)
};
#else
// Fallback declaration when building headless without JUCE SDK
namespace AudioMusicPipeline {
    class AudioProcessorStub {
    public:
        DSPCore dsp;
    };
}
#endif
