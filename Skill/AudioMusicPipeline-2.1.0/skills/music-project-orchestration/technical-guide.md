# Technical Guide: Music Project Orchestration

## 1. Mathematical Time Conversions
- **Tick duration in seconds**:
  $$t_{\text{tick}} = \frac{60.0}{\text{BPM} \times \text{PPQ}}$$
- **Bar duration in seconds**:
  $$T_{\text{bar}} = \frac{60.0}{\text{BPM}} \times \text{Numerator} \times \frac{4}{\text{Denominator}}$$
- **Sample count at sample rate $f_s$**:
  $$N_{\text{samples}} = \text{round}(T_{\text{total}} \times f_s)$$

## 2. Multi-Target Compilation CLI Recipe
```bash
# Validate project contract
python3 -c "
import json
from tools.crossmodal_engine import CrossModalEngine
with open('contracts/project_music_contract.example.json') as f:
    data = json.load(f)
assert 'time_transport' in data
print('[Valid] Project contract loaded cleanly.')
"
```
