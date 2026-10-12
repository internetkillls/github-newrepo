cmake_minimum_required(VERSION 3.22)
project(AudioMusicPipelinePlugin VERSION 2.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Option to fetch JUCE via FetchContent if online, or point to local JUCE
option(AMP_BUILD_JUCE_PLUGIN "Build full VST3/AU targets with JUCE" OFF)

if(AMP_BUILD_JUCE_PLUGIN)
    include(FetchContent)
    FetchContent_Declare(
        JUCE
        GIT_REPOSITORY https://github.com/juce-framework/JUCE.git
        GIT_TAG 8.0.4
    )
    FetchContent_MakeAvailable(JUCE)

    juce_add_plugin(AudioMusicPipeline
        PLUGIN_MANUFACTURER_CODE AMP1
        PLUGIN_CODE AmpF
        FORMATS VST3 AU Standalone
        PRODUCT_NAME "AudioMusicPipeline Filter"
        IS_SYNTH FALSE
        NEEDS_MIDI_INPUT TRUE
        NEEDS_MIDI_OUTPUT TRUE
        IS_MIDI_EFFECT FALSE
    )

    target_sources(AudioMusicPipeline PRIVATE
        Source/PluginProcessor.cpp
        Source/PluginProcessor.h
        Source/DSPCore.h
    )

    target_link_libraries(AudioMusicPipeline PRIVATE
        juce::juce_audio_utils
        juce::juce_audio_processors
        juce::juce_dsp
    )
else()
    # Standalone verification executable
    add_executable(test_dsp_headless tests/test_dsp_headless.cpp)
    target_include_directories(test_dsp_headless PRIVATE Source)
endif()
