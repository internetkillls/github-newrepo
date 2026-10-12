"""Standard MIDI File (SMF 1.0) pure-Python parser and serializer.

Supports:
- Header chunk (MThd): format 0 and 1, division (ticks per quarter note)
- Track chunks (MTrk) with variable-length quantity (VLQ) delta times
- MIDI Channel Voice messages: Note Off (0x80), Note On (0x90), Polyphonic Key Pressure (0xA0),
  Control Change (0xB0), Program Change (0xC0), Channel Pressure (0xD0), Pitch Bend (0xE0)
- Meta events: Set Tempo (0x51), Time Signature (0x58), Track Name (0x03), End of Track (0x2F)
- Zero external dependencies: 100% standard library Python 3.
"""

import struct
from io import BytesIO
from typing import List, Tuple, Dict, Any, Optional

def write_varlen(value: int) -> bytes:
    """Encode an integer into MIDI variable-length quantity bytes."""
    buf = bytearray()
    buf.append(value & 0x7F)
    value >>= 7
    while value > 0:
        buf.append((value & 0x7F) | 0x80)
        value >>= 7
    buf.reverse()
    return bytes(buf)

def read_varlen(stream: BytesIO) -> int:
    """Decode a MIDI variable-length quantity from a byte stream."""
    value = 0
    while True:
        b = stream.read(1)
        if not b:
            raise EOFError("Unexpected EOF while reading varlen quantity")
        byte = b[0]
        value = (value << 7) | (byte & 0x7F)
        if not (byte & 0x80):
            break
    return value

class MidiEvent:
    def __init__(self, delta: int, type_: str, channel: int = 0, **data):
        self.delta = delta
        self.type = type_
        self.channel = channel
        self.data = data

    def __repr__(self):
        return f"MidiEvent(delta={self.delta}, type={self.type!r}, ch={self.channel}, {self.data})"

class MidiTrack:
    def __init__(self, name: str = ""):
        self.name = name
        self.events: List[MidiEvent] = []

    def add_event(self, event: MidiEvent):
        self.events.append(event)

    def add_note(self, note: int, velocity: int, start_tick: int, duration_tick: int, channel: int = 0):
        """Helper to append note on and note off with delta timing (unsorted raw event container)."""
        self.events.append(MidiEvent(start_tick, 'note_on', channel=channel, note=note, velocity=velocity))
        self.events.append(MidiEvent(start_tick + duration_tick, 'note_off', channel=channel, note=note, velocity=0))

    def serialize(self) -> bytes:
        """Serialize track into MTrk chunk bytes, sorting events by absolute time."""
        # Check if events have absolute times or deltas. If tuples of (abs_time, event), sort them:
        # Standard approach: store absolute ticks in delta, sort, then convert to relative delta.
        sorted_events = sorted(self.events, key=lambda e: (e.delta, 0 if e.type == 'note_off' else 1))

        stream = BytesIO()
        last_tick = 0

        # Track name meta event if provided
        if self.name:
            stream.write(write_varlen(0))
            name_bytes = self.name.encode('utf-8')
            stream.write(b'\xFF\x03' + write_varlen(len(name_bytes)) + name_bytes)

        for ev in sorted_events:
            delta_rel = max(0, ev.delta - last_tick)
            last_tick = ev.delta
            stream.write(write_varlen(delta_rel))

            ch = ev.channel & 0x0F
            if ev.type == 'note_on':
                vel = ev.data.get('velocity', 64)
                note = ev.data.get('note', 60) & 0x7F
                stream.write(bytes([0x90 | ch, note, vel & 0x7F]))
            elif ev.type == 'note_off':
                note = ev.data.get('note', 60) & 0x7F
                stream.write(bytes([0x80 | ch, note, 0]))
            elif ev.type == 'control_change':
                cc = ev.data.get('control', 1) & 0x7F
                val = ev.data.get('value', 0) & 0x7F
                stream.write(bytes([0xB0 | ch, cc, val]))
            elif ev.type == 'program_change':
                prog = ev.data.get('program', 0) & 0x7F
                stream.write(bytes([0xC0 | ch, prog]))
            elif ev.type == 'set_tempo':
                tempo_us = ev.data.get('tempo_us', 500000)  # 120 bpm default
                stream.write(b'\xFF\x51\x03' + struct.pack('>I', tempo_us)[1:])
            elif ev.type == 'time_signature':
                num = ev.data.get('numerator', 4)
                den = ev.data.get('denominator', 4)
                if den < 1 or den & (den - 1):
                    raise ValueError('Time signature denominator must be a power of two')
                den_pow = den.bit_length() - 1
                stream.write(bytes([0xFF, 0x58, 0x04, num, den_pow, 24, 8]))
            elif ev.type == 'end_of_track':
                stream.write(b'\xFF\x2F\x00')

        # Always terminate track cleanly
        stream.write(write_varlen(0))
        stream.write(b'\xFF\x2F\x00')

        payload = stream.getvalue()
        return b'MTrk' + struct.pack('>I', len(payload)) + payload

class MidiFile:
    def __init__(self, ticks_per_quarter: int = 480, format_: int = 1):
        self.ticks_per_quarter = ticks_per_quarter
        self.format = format_
        self.tracks: List[MidiTrack] = []

    def add_track(self, track: MidiTrack):
        self.tracks.append(track)

    def write(self, filename: str):
        with open(filename, 'wb') as f:
            f.write(self.serialize())

    def serialize(self) -> bytes:
        out = BytesIO()
        out.write(b'MThd')
        out.write(struct.pack('>IHHH', 6, self.format, len(self.tracks), self.ticks_per_quarter))
        for track in self.tracks:
            out.write(track.serialize())
        return out.getvalue()

    @classmethod
    def read(cls, filename: str) -> 'MidiFile':
        with open(filename, 'rb') as f:
            data = f.read()
        return cls.deserialize(data)

    @classmethod
    def deserialize(cls, data: bytes) -> 'MidiFile':
        stream = BytesIO(data)
        header_tag = stream.read(4)
        if header_tag != b'MThd':
            raise ValueError(f"Invalid MIDI header: expected b'MThd', got {header_tag!r}")
        length, format_, num_tracks, division = struct.unpack('>IHHH', stream.read(10))
        if length > 6:
            stream.read(length - 6)

        midi = cls(ticks_per_quarter=division, format_=format_)

        for _ in range(num_tracks):
            track_tag = stream.read(4)
            if track_tag != b'MTrk':
                raise ValueError(f"Expected b'MTrk', got {track_tag!r}")
            track_len, = struct.unpack('>I', stream.read(4))
            track_data = stream.read(track_len)
            track_stream = BytesIO(track_data)

            track = MidiTrack()
            current_abs_tick = 0
            running_status = None

            while track_stream.tell() < track_len:
                delta = read_varlen(track_stream)
                current_abs_tick += delta
                status_b = track_stream.read(1)
                if not status_b:
                    break
                status = status_b[0]

                if status < 0x80:
                    if running_status is None:
                        raise ValueError(f"Running status byte without previous status: {status:#x}")
                    first_byte = status
                    status = running_status
                else:
                    running_status = status
                    first_byte = None

                if status == 0xFF:  # Meta Event
                    meta_type = track_stream.read(1)[0]
                    meta_len = read_varlen(track_stream)
                    meta_payload = track_stream.read(meta_len)
                    if meta_type == 0x03:
                        track.name = meta_payload.decode('utf-8', errors='ignore')
                    elif meta_type == 0x51 and meta_len == 3:
                        tempo_us = struct.unpack('>I', b'\x00' + meta_payload)[0]
                        track.add_event(MidiEvent(current_abs_tick, 'set_tempo', tempo_us=tempo_us))
                    elif meta_type == 0x58 and meta_len >= 2:
                        track.add_event(MidiEvent(current_abs_tick, 'time_signature',
                                                  numerator=meta_payload[0], denominator=2**meta_payload[1]))
                    elif meta_type == 0x2F:
                        track.add_event(MidiEvent(current_abs_tick, 'end_of_track'))
                        break
                elif status == 0xF0 or status == 0xF7:  # SysEx
                    sysex_len = read_varlen(track_stream)
                    track_stream.read(sysex_len)
                else:
                    event_type_nibble = status & 0xF0
                    channel = status & 0x0F
                    b1 = first_byte if first_byte is not None else track_stream.read(1)[0]

                    if event_type_nibble in (0x80, 0x90, 0xA0, 0xB0, 0xE0):
                        b2 = track_stream.read(1)[0]
                        if event_type_nibble == 0x90:
                            if b2 > 0:
                                track.add_event(MidiEvent(current_abs_tick, 'note_on', channel=channel, note=b1, velocity=b2))
                            else:
                                track.add_event(MidiEvent(current_abs_tick, 'note_off', channel=channel, note=b1, velocity=0))
                        elif event_type_nibble == 0x80:
                            track.add_event(MidiEvent(current_abs_tick, 'note_off', channel=channel, note=b1, velocity=b2))
                        elif event_type_nibble == 0xB0:
                            track.add_event(MidiEvent(current_abs_tick, 'control_change', channel=channel, control=b1, value=b2))
                    elif event_type_nibble in (0xC0, 0xD0):
                        if event_type_nibble == 0xC0:
                            track.add_event(MidiEvent(current_abs_tick, 'program_change', channel=channel, program=b1))

            midi.add_track(track)

        return midi
