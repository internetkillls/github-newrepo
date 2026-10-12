# Technical Guide: TouchDesigner Visual Adapter

## Builder Script Execution in TouchDesigner
Inside a TouchDesigner `textDAT`:
```python
import audio_reactive_engine
audio_reactive_engine.build_audio_reactive_engine('/project1', 'audio_reactive_engine')

import ableton_cube_router
ableton_cube_router.build_ableton_cube_router('/project1', 'ableton_cube_router')
```
- Ingests OSC from Max/MSP (`port=7000`) or Ableton Live.
- Preserves 7200x1080 canvas for 4-sided LED cubes.
