---
name: juce-plugin-dev
description: "Develop, scaffold, and verify C++ audio plugins using the JUCE framework: real-time DSP, APVTS parameter layouts, CMake configuration, and headless unit testing."
---

# JUCE Audio Plugin Development

Use this skill to develop, structure, compile, and test low-latency audio plugins (VST3, AU, Standalone) using the JUCE C++ framework and CMake.

## Verified Environment on Host
- **Compiler**: Apple Clang 15.0 (`/usr/bin/clang++`) supporting C++17 and C++20.
- **Build System**: CMake 4.4.4 (`/opt/homebrew/bin/cmake`).
- **Scaffold**: `juce_scaffold/` containing `DSPCore.h`, `PluginProcessor.h`, `PluginProcessor.cpp`, `CMakeLists.txt`, and `tests/test_dsp_headless.cpp`.

## Core Procedures

1. **Real-Time Safety Invariants**:
   - Audio thread (`processBlock`):
     - **NEVER** allocate memory (`new`, `malloc`, `std::vector::push_back`).
     - **NEVER** acquire mutexes or locks that can cause priority inversion.
     - **NEVER** perform disk, network, or console I/O (`std::cout`, file streams).
     - **NEVER** throw or catch C++ exceptions.

2. **Parameter Management (APVTS)**:
   - Use `juce::AudioProcessorValueTreeState` to manage plugin parameters.
   - Decouple GUI parameter changes from audio processing using atomic reads (`std::atomic<float>` or `.load()`).

3. **Headless DSP Unit Testing**:
   - Compile and verify DSP algorithms in isolation using Apple Clang:
     ```bash
     clang++ -std=c++17 -Wall -Wextra -O2 \
       juce_scaffold/tests/test_dsp_headless.cpp \
       -o juce_scaffold/tests/test_dsp_runner
     ./juce_scaffold/tests/test_dsp_runner
     ```
   - Verifies numerical stability (zero NaN/Inf), soft-clipping limits, and filter behavior without requiring a graphical DAW session.

4. **Production Build via CMake**:
   - When building full VST3/AU with JUCE SDK:
     ```bash
     cmake -B build -S juce_scaffold -DAMP_BUILD_JUCE_PLUGIN=ON
     cmake --build build --config Release
     ```
   - (Note: Live DAW plugin scanning in Ableton is marked as **pending** until the full JUCE framework is built locally).
