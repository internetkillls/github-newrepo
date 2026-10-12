# Technical Guide: Harmony & Music Theory

## Voice-Leading Algorithm Recipe
```python
def check_voice_leading(chord_a, chord_b):
    """Calculate voice-leading distance between two sorted chord voicings."""
    assert len(chord_a) == len(chord_b), "Voicings must have same voice count"
    total_movement = sum(abs(a - b) for a, b in zip(chord_a, chord_b))
    return total_movement
```
