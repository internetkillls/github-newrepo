#!/usr/bin/env python3
"""Example demonstration: Visual Score -> Music (MIDI + Audio)."""

import os, sys, json
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from tools.crossmodal_engine import CrossModalEngine

def main():
    score_path = os.path.join(ROOT_DIR, 'contracts', 'visual_score.example.json')
    with open(score_path, 'r', encoding='utf-8') as f:
        score_data = json.load(f)

    print(f"[Direction 1] Converting Visual Score: '{score_data['title']}' to Music...")
    result = CrossModalEngine.visual_score_to_music(
        score_data, bpm=124.0, total_bars=4, scale_root="D", scale_mode="dorian"
    )

    out_midi = os.path.join(SCRIPT_DIR, 'output_score.mid')
    out_wav = os.path.join(SCRIPT_DIR, 'output_score.wav')

    with open(out_midi, 'wb') as f:
        f.write(result['midi_bytes'])
    with open(out_wav, 'wb') as f:
        f.write(result['wav_bytes'])

    print(f"Generated MIDI: {out_midi} ({len(result['midi_bytes'])} bytes)")
    print(f"Generated WAV:  {out_wav} ({len(result['wav_bytes'])} bytes)")
    print(f"Total Notes Synthesized: {result['total_notes']}")
    print(f"Loss Metrics & Irreversibility Report:")
    print(json.dumps(result['loss_metrics'], indent=2))

if __name__ == '__main__':
    main()
