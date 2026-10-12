"""Bidirectional Cross-Modal Engine for AudioMusicPipeline.

Provides mathematically verified bidirectional translations:
1. Visual Score -> Music (MIDI sequence, Harmonic progression, Audio synthesis)
2. Music/Audio -> Visual Control Data (4-face Cube Ribbons, OSC Telemetry, Visual Score reconstruction)

Also computes explicit information loss & irreversibility metrics.
"""

import math, json, struct, wave
from io import BytesIO
from typing import Dict, Any, List, Tuple, Optional

# Import local pure-Python SMF tool
try:
    from .smf_midi import MidiFile, MidiTrack, MidiEvent
except (ImportError, ValueError):
    from smf_midi import MidiFile, MidiTrack, MidiEvent

SCALE_INTERVALS = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "natural_minor": [0, 2, 3, 5, 7, 8, 10],
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "phrygian": [0, 1, 3, 5, 7, 8, 10],
    "lydian": [0, 2, 4, 6, 7, 9, 11],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "locrian": [0, 1, 3, 5, 6, 8, 10],
    "pentatonic_minor": [0, 3, 5, 7, 10],
    "chromatic": list(range(12))
}

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def note_name_to_midi(name: str, octave: int = 4) -> int:
    name_clean = name.strip().upper()
    idx = NOTE_NAMES.index(name_clean) if name_clean in NOTE_NAMES else 0
    return 12 * (octave + 1) + idx

def quantize_pitch_to_scale(midi_pitch: float, root_name: str = "D", mode: str = "natural_minor") -> Tuple[int, float]:
    """Snap a continuous pitch value to the closest scale pitch.

    Returns:
        (quantized_midi_pitch, detune_cents_lost)
    """
    root_idx = NOTE_NAMES.index(root_name)
    scale = [(root_idx + iv) % 12 for iv in SCALE_INTERVALS.get(mode, SCALE_INTERVALS["natural_minor"])]

    rounded = int(round(midi_pitch))
    pitch_class = rounded % 12
    octave = rounded // 12

    # Find closest scale pitch class
    closest_pc = min(scale, key=lambda pc: min(abs(pc - pitch_class), 12 - abs(pc - pitch_class)))
    quantized_note = octave * 12 + closest_pc

    # Calculate difference in cents (1 semitone = 100 cents)
    cents_lost = (midi_pitch - quantized_note) * 100.0
    return quantized_note, cents_lost

class CrossModalEngine:
    """Core processor for bidirectional cross-modal translation."""

    @staticmethod
    def visual_score_to_music(
        score_data: Dict[str, Any],
        bpm: float = 120.0,
        total_bars: int = 4,
        scale_root: str = "D",
        scale_mode: str = "dorian",
        ticks_per_quarter: int = 480
    ) -> Dict[str, Any]:
        """Convert Visual Score graphical notation into MIDI sequence & audio synthesis.

        Direction: Visual Score -> Music/Audio
        """
        beats_per_bar = 4
        total_beats = total_bars * beats_per_bar
        midi = MidiFile(ticks_per_quarter=ticks_per_quarter, format_=1)

        # Track 0: Conductor (Tempo & Time Signature)
        conductor = MidiTrack(name="Conductor")
        tempo_us = int(60_000_000.0 / bpm)
        conductor.add_event(MidiEvent(0, 'set_tempo', tempo_us=tempo_us))
        conductor.add_event(MidiEvent(0, 'time_signature', numerator=4, denominator=4))
        midi.add_track(conductor)

        elements = score_data.get("elements", [])

        # Segregate voices by role
        roles = {}
        for el in elements:
            r = el.get("voice_role", "melody")
            roles.setdefault(r, []).append(el)

        role_channel_map = {
            "melody": 0,
            "harmony": 1,
            "bass": 2,
            "percussion": 9,
            "texture": 3
        }

        min_pitch = 36  # C2
        max_pitch = 84  # C6

        loss_metrics = {
            "pitch_quantization_max_cents": 0.0,
            "pitch_quantization_mean_cents": 0.0,
            "total_notes": 0,
            "spatial_degrees_of_freedom_collapsed": "2D (X, Y) -> 1D timeline"
        }
        total_cents_error = 0.0

        all_generated_notes = []

        for role, el_list in roles.items():
            track = MidiTrack(name=f"Role_{role}")
            ch = role_channel_map.get(role, 0)

            for el in el_list:
                pts = el.get("points", [])
                if not pts:
                    continue

                stroke = el.get("stroke_width", 0.01)
                # Map stroke width to velocity: [0.002, 0.040] -> [40, 120]
                base_vel = int(40 + min(80, max(0, (stroke - 0.002) / (0.038) * 80)))

                # If single point or point event
                if el.get("type") == "point_event" or len(pts) == 1:
                    x, y = pts[0][:2]
                    raw_pitch = min_pitch + y * (max_pitch - min_pitch)
                    quant_pitch, cents_lost = quantize_pitch_to_scale(raw_pitch, scale_root, scale_mode)

                    beat_pos = x * total_beats
                    # Quantize to 16th notes (0.25 beats)
                    beat_quant = round(beat_pos / 0.25) * 0.25
                    start_tick = int(beat_quant * ticks_per_quarter)
                    duration_tick = int(0.5 * ticks_per_quarter) # 8th note duration

                    track.add_note(quant_pitch, base_vel, start_tick, duration_tick, channel=ch)
                    all_generated_notes.append({
                        "pitch": quant_pitch, "velocity": base_vel,
                        "start_tick": start_tick, "duration_tick": duration_tick, "channel": ch
                    })

                    total_cents_error += abs(cents_lost)
                    loss_metrics["pitch_quantization_max_cents"] = max(loss_metrics["pitch_quantization_max_cents"], abs(cents_lost))
                    loss_metrics["total_notes"] += 1

                # Trajectory curve
                elif el.get("type") in ("trajectory_curve", "harmonic_ribbon"):
                    for i in range(len(pts) - 1):
                        p1 = pts[i]
                        p2 = pts[i+1]
                        x1, y1 = p1[:2]
                        x2, y2 = p2[:2]

                        raw_pitch = min_pitch + y1 * (max_pitch - min_pitch)
                        quant_pitch, cents_lost = quantize_pitch_to_scale(raw_pitch, scale_root, scale_mode)

                        start_beat = round((x1 * total_beats) / 0.25) * 0.25
                        end_beat = round((x2 * total_beats) / 0.25) * 0.25
                        dur_beats = max(0.25, end_beat - start_beat)

                        start_tick = int(start_beat * ticks_per_quarter)
                        duration_tick = int(dur_beats * ticks_per_quarter)

                        track.add_note(quant_pitch, base_vel, start_tick, duration_tick, channel=ch)
                        all_generated_notes.append({
                            "pitch": quant_pitch, "velocity": base_vel,
                            "start_tick": start_tick, "duration_tick": duration_tick, "channel": ch
                        })

                        total_cents_error += abs(cents_lost)
                        loss_metrics["pitch_quantization_max_cents"] = max(loss_metrics["pitch_quantization_max_cents"], abs(cents_lost))
                        loss_metrics["total_notes"] += 1

            midi.add_track(track)

        if loss_metrics["total_notes"] > 0:
            loss_metrics["pitch_quantization_mean_cents"] = total_cents_error / loss_metrics["total_notes"]

        midi_bytes = midi.serialize()

        # Synthesize simple offline PCM preview audio
        sample_rate = 44100
        total_seconds = (total_beats / bpm) * 60.0
        num_samples = int(total_seconds * sample_rate)
        audio_buffer = [0.0] * num_samples

        for n in all_generated_notes:
            freq = 440.0 * (2.0 ** ((n["pitch"] - 69) / 12.0))
            start_sec = (n["start_tick"] / (ticks_per_quarter * (bpm / 60.0)))
            dur_sec = (n["duration_tick"] / (ticks_per_quarter * (bpm / 60.0)))
            start_smp = int(start_sec * sample_rate)
            dur_smp = int(dur_sec * sample_rate)
            amp = (n["velocity"] / 127.0) * 0.25

            for s in range(min(dur_smp, num_samples - start_smp)):
                t = s / sample_rate
                # Decay envelope
                env = math.exp(-3.0 * (s / dur_smp))
                val = amp * env * math.sin(2.0 * math.pi * freq * t)
                audio_buffer[start_smp + s] += val

        # Normalize audio buffer to prevent clipping
        max_amp = max([abs(x) for x in audio_buffer] or [1.0])
        if max_amp > 0.95:
            audio_buffer = [x * (0.95 / max_amp) for x in audio_buffer]

        wav_bytes = CrossModalEngine._write_wav_bytes(audio_buffer, sample_rate)

        return {
            "status": "success",
            "direction": "visual_score_to_music",
            "midi_bytes": midi_bytes,
            "wav_bytes": wav_bytes,
            "total_notes": loss_metrics["total_notes"],
            "loss_metrics": loss_metrics,
            "total_duration_sec": total_seconds
        }

    @staticmethod
    def music_to_visual_control(
        midi_notes: List[Dict[str, Any]],
        audio_rms: List[float],
        total_bars: int = 4,
        safe_margin_budget: float = 0.42
    ) -> Dict[str, Any]:
        """Convert musical notes & audio telemetry into 4-sided cube visual parameters.

        Direction: Music/Audio -> Visual Control Data
        """
        # Dynamic parameter calculation conforming to VisualPipeline 1.3.0 & AudioMusicPipeline
        # Drums RMS -> Amplitude (0.015 - 0.075)
        avg_rms = sum(audio_rms) / len(audio_rms) if audio_rms else 0.1
        amp_candidate = 0.015 + min(0.060, avg_rms * 0.15)

        # Bass notes / register -> Stroke Width (0.003 - 0.018)
        bass_notes = [n for n in midi_notes if n.get("pitch", 60) < 48]
        if bass_notes:
            stroke_width = 0.003 + min(0.015, len(bass_notes) * 0.002)
        else:
            stroke_width = 0.008

        # Lead notes -> Spatial Harmonic (2 to 8, strictly quantized to integer)
        lead_notes = [n for n in midi_notes if n.get("pitch", 60) >= 60]
        if lead_notes:
            avg_pitch = sum(n["pitch"] for n in lead_notes) / len(lead_notes)
            # Map pitch [60, 84] -> [2, 8]
            harmonic_raw = 2.0 + (avg_pitch - 60) / 24.0 * 6.0
            spatial_harmonic = max(2, min(8, int(math.floor(harmonic_raw))))
        else:
            spatial_harmonic = 4

        # FX / Energy -> Band Span (0.25 - 0.48)
        band_span = 0.25 + min(0.23, avg_rms * 0.5)

        # Enforce Safe Margin Rule: band_span / 2 + amplitude + stroke_width / 2 <= 0.42
        margin_used = (band_span / 2.0) + (stroke_width / 2.0)
        allowed_headroom = max(0.005, safe_margin_budget - margin_used)
        amplitude_clamped = min(amp_candidate, allowed_headroom)

        # Verify strict mathematical invariant
        actual_margin = (band_span / 2.0) + amplitude_clamped + (stroke_width / 2.0)
        margin_compliant = actual_margin <= (safe_margin_budget + 1e-9)

        # Reverse Visual Score Reconstruction
        reconstructed_elements = []
        for i, n in enumerate(midi_notes[:16]):
            x = (n.get("start_tick", 0) / (480.0 * 4.0 * total_bars)) % 1.0
            y = (n.get("pitch", 60) - 36) / 48.0
            reconstructed_elements.append({
                "element_id": f"rev_point_{i}",
                "type": "point_event",
                "voice_role": "melody" if n.get("pitch", 60) >= 60 else "bass",
                "points": [[round(x, 4), round(y, 4)]],
                "stroke_width": round(stroke_width, 4)
            })

        loss_metrics = {
            "audio_phase_information_loss": "100% (RMS is magnitude scalar, audio phase discarded)",
            "polyphonic_spatial_ambiguity": "Collapsed chords into harmonic ribbon spatial harmonic",
            "safe_margin_throttling_applied": amp_candidate > allowed_headroom
        }

        return {
            "status": "success",
            "direction": "music_to_visual_control",
            "cube_parameters": {
                "amplitude": round(amplitude_clamped, 4),
                "stroke_width": round(stroke_width, 4),
                "spatial_harmonic": spatial_harmonic,
                "band_span": round(band_span, 4),
                "margin_actual": round(actual_margin, 4),
                "margin_budget": safe_margin_budget,
                "margin_compliant": margin_compliant
            },
            "reconstructed_visual_score": {
                "score_id": "auto_reconstructed_score",
                "elements": reconstructed_elements
            },
            "loss_metrics": loss_metrics
        }

    @staticmethod
    def _write_wav_bytes(samples: List[float], sample_rate: int = 44100) -> bytes:
        out = BytesIO()
        with wave.open(out, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            frames = bytearray()
            for s in samples:
                val = max(-32767, min(32767, int(s * 32767.0)))
                frames.extend(struct.pack('<h', val))
            wf.writeframes(bytes(frames))
        return out.getvalue()
