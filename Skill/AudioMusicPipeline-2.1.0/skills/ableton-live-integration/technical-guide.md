# Technical Guide: Ableton Live 12 Integration

## Live Object Model (LOM) Python 3 Architecture
In Ableton Live 12, Remote Scripts inherit from `_Framework` or newer `ableton.v3` base classes:
```python
from ableton.v3.control_surface import ControlSurface

class AudioMusicPipelineRemoteScript(ControlSurface):
    def __init__(self, c_instance=None):
        super().__init__(c_instance=c_instance)
        self.show_message("AudioMusicPipeline Live 12 Bridge Active")
```
- Remote scripts run in Live's dedicated Python thread.
- Avoid blocking I/O calls directly in listener callbacks.
