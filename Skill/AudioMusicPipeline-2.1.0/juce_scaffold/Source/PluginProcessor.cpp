#include "PluginProcessor.h"

#if HAS_JUCE_FRAMEWORK
AudioMusicPipelineAudioProcessor::AudioMusicPipelineAudioProcessor()
    : AudioProcessor(BusesProperties()
                     .withInput("Input", juce::AudioChannelSet::stereo(), true)
                     .withOutput("Output", juce::AudioChannelSet::stereo(), true)),
      m_parameters(*this, nullptr, "Parameters", {
          std::make_unique<juce::AudioParameterFloat>("cutoff", "Cutoff", 20.0f, 20000.0f, 1000.0f),
          std::make_unique<juce::AudioParameterFloat>("resonance", "Resonance", 0.5f, 10.0f, 0.707f),
          std::make_unique<juce::AudioParameterFloat>("drive", "Drive", 1.0f, 10.0f, 1.0f),
          std::make_unique<juce::AudioParameterChoice>("type", "Type", juce::StringArray{"LowPass", "BandPass", "HighPass"}, 0)
      })
{
}

void AudioMusicPipelineAudioProcessor::prepareToPlay(double sampleRate, int samplesPerBlock) {
    m_dspCore.prepare(sampleRate, static_cast<uint32_t>(samplesPerBlock));
}

void AudioMusicPipelineAudioProcessor::releaseResources() {
    m_dspCore.reset();
}

void AudioMusicPipelineAudioProcessor::processBlock(juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midiMessages) {
    juce::ignoreUnused(midiMessages);
    juce::ScopedNoDenormals noDenormals;

    const auto cutoff = m_parameters.getRawParameterValue("cutoff")->load();
    const auto resonance = m_parameters.getRawParameterValue("resonance")->load();
    const auto drive = m_parameters.getRawParameterValue("drive")->load();
    const auto typeIdx = static_cast<int>(m_parameters.getRawParameterValue("type")->load());

    m_dspCore.setParameters(cutoff, resonance, drive, static_cast<AudioMusicPipeline::DSPCore::FilterType>(typeIdx));

    auto* channelData = buffer.getArrayOfWritePointers();
    m_dspCore.process(channelData, buffer.getNumChannels(), buffer.getNumSamples());
}

juce::AudioProcessorEditor* AudioMusicPipelineAudioProcessor::createEditor() {
    return new juce::GenericAudioProcessorEditor(*this);
}

void AudioMusicPipelineAudioProcessor::getStateInformation(juce::MemoryBlock& destData) {
    auto state = m_parameters.copyState();
    std::unique_ptr<juce::XmlElement> xml(state.createXml());
    copyXmlToBinary(*xml, destData);
}

void AudioMusicPipelineAudioProcessor::setStateInformation(const void* data, int sizeInBytes) {
    std::unique_ptr<juce::XmlElement> xmlState(getXmlFromBinary(data, sizeInBytes));
    if (xmlState.get() != nullptr && xmlState->hasTagName(m_parameters.state.getType())) {
        m_parameters.replaceState(juce::ValueTree::fromXml(*xmlState));
    }
}

juce::AudioProcessor* JUCE_CALLTYPE createPluginFilter() {
    return new AudioMusicPipelineAudioProcessor();
}
#endif
