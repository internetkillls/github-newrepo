#!/usr/bin/env python3
"""Example demonstration: Music/Audio -> Visual Control Data (4-face cube ribbons)."""

import os, sys, json
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from tools.crossmodal_engine import CrossModalEngine
from tools.audio_dsp_analyzer import AudioDspAnalyzer

def main():
    contract_path = os.path.join(ROOT_DIR, 'contracts', 'project_music_contract.example.json')
    with open(contract_path, 'r', encoding='utf-8') as f:
        contract_data = json.load(f)

    print(f"[Direction 2] Mapping Project: '{contract_data['title']}' to 4-Face Cube Visual Controls...")

    # Extract notes from tracks
    all_notes = []
    for trk in contract_data.get('tracks', []):
        all_notes.extend(trk.get('notes', []))

    # Simulate RMS audio stream
    simulated_rms = [0.12, 0.28, 0.45, 0.85, 0.92, 0.35, 0.18, 0.60]

    result = CrossModalEngine.music_to_visual_control(
        midi_notes=all_notes,
        audio_rms=simulated_rms,
        total_bars=4,
        safe_margin_budget=0.42
    )

    print("Calculated 4-Face Cube Parameters:")
    print(json.dumps(result['cube_parameters'], indent=2))
    print(f"Mathematical Invariant Enforced: {result['cube_parameters']['margin_compliant']}")
    print(f"Headroom formula: {result['cube_parameters']['band_span']}/2 + {result['cube_parameters']['amplitude']} + {result['cube_parameters']['stroke_width']}/2 = {result['cube_parameters']['margin_actual']} <= {result['cube_parameters']['margin_budget']}")
    print("\nLoss Metrics & Information Divergence:")
    print(json.dumps(result['loss_metrics'], indent=2))

if __name__ == '__main__':
    main()
