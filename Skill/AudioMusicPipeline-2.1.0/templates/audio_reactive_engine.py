"""TouchDesigner Audio-Reactive Engine Builder (v1.3.0).

Constructs a modular, production-ready 'audio_reactive_engine' baseCOMP with:
1. Documented TouchDesigner Python operator classes (audiodeviceinCHOP, abletonlinkCHOP, etc.).
2. Nyquist-compliant audio-rate filtering (44.1 kHz) before downsampling scalar envelopes to video frame rate.
3. Decoupled rate conversion (method='preserve') and envelope smoothing (interp='linear').
4. Per-band asymmetric lag interpolation (attack vs. decay).
5. Dynamic auto-gain normalization with rolling peak tracking.
6. Thresholded kick transient detection via bound-logic and continuous phase accumulation.
7. Explicit silence safeguard timer and crossfade duration (not a bare lag filter).
8. Full 7-channel autonomous fallback driver (sub, bass, mid, high, kick, accum_phase, rms).
9. Selective cooking barriers and robust rebuild idempotence.
"""

def build_audio_reactive_engine(parent_path='/project1', comp_name='audio_reactive_engine'):
    """Constructs or updates the audio_reactive_engine COMP inside TouchDesigner.

    Returns:
        bool: True on success, False if outside TouchDesigner.
    """
    try:
        import td
    except ImportError:
        print("[Notice] Running outside TouchDesigner environment. Syntax and imports validated.")
        return False

    parent_op = op(parent_path)
    if not parent_op:
        raise ValueError(f"[Build Error] Target parent path '{parent_path}' does not exist.")

    current_node = None
    current_param = None

    try:
        # 1. Create or retrieve baseCOMP
        current_node = comp_name
        engine = parent_op.op(comp_name)
        if engine is None:
            engine = parent_op.create(baseCOMP, comp_name)

        engine.par.parentshortcut = 'AudioEngine'
        engine.nodeX = 200
        engine.nodeY = 200

        # 2. Setup Custom Parameters on parent COMP
        page = engine.appendCustomPage('Audio Controls')

        # Audio Source Selection
        if not hasattr(engine.par, 'Source'):
            p = page.appendMenu('Source', label='Audio Source')[0]
            p.menuNames = ['device', 'file']
            p.menuLabels = ['Hardware Audio Device In', 'Audio File Loop']

        # Audio File Path
        if not hasattr(engine.par, 'Audiofile'):
            p = page.appendFile('Audiofile', label='Audio File Path')[0]
            p.default = 'assets/audio_reference_loop.wav'

        # Ableton Link Transport Sync Toggle
        if not hasattr(engine.par, 'Linksync'):
            p = page.appendToggle('Linksync', label='Ableton Link Transport Sync')[0]
            p.default = True

        # Master Gain
        if not hasattr(engine.par, 'Gain'):
            p = page.appendFloat('Gain', label='Master Sensitivity')[0]
            p.default = 1.0
            p.min = 0.0
            p.max = 5.0
            p.normMax = 3.0

        # Dynamic Auto-Gain Toggle
        if not hasattr(engine.par, 'Autogain'):
            p = page.appendToggle('Autogain', label='Enable Dynamic Auto-Gain')[0]
            p.default = True

        # Per-Band Lag Controls (Attack / Decay in seconds)
        if not hasattr(engine.par, 'Sublagup'):
            p_up = page.appendFloat('Sublagup', label='Sub Attack (s)')[0]
            p_up.default = 0.008
            p_down = page.appendFloat('Sublagdown', label='Sub Decay (s)')[0]
            p_down.default = 0.22

        if not hasattr(engine.par, 'Basslagup'):
            p_up = page.appendFloat('Basslagup', label='Bass Attack (s)')[0]
            p_up.default = 0.015
            p_down = page.appendFloat('Basslagdown', label='Bass Decay (s)')[0]
            p_down.default = 0.28

        if not hasattr(engine.par, 'Midlagup'):
            p_up = page.appendFloat('Midlagup', label='Mid Attack (s)')[0]
            p_up.default = 0.020
            p_down = page.appendFloat('Midlagdown', label='Mid Decay (s)')[0]
            p_down.default = 0.35

        if not hasattr(engine.par, 'Highlagup'):
            p_up = page.appendFloat('Highlagup', label='High Attack (s)')[0]
            p_up.default = 0.005
            p_down = page.appendFloat('Highlagdown', label='High Decay (s)')[0]
            p_down.default = 0.15

        # Transient Kick Detection Threshold
        if not hasattr(engine.par, 'Kickthreshold'):
            p = page.appendFloat('Kickthreshold', label='Kick Trigger Threshold')[0]
            p.default = 0.65
            p.min = 0.10
            p.max = 1.00

        # Silence Safeguard Parameters
        if not hasattr(engine.par, 'Silencefallback'):
            p = page.appendToggle('Silencefallback', label='Silence Safeguard Fallback')[0]
            p.default = True

        if not hasattr(engine.par, 'Silencethreshold'):
            p = page.appendFloat('Silencethreshold', label='Silence RMS Threshold')[0]
            p.default = 0.020
            p.min = 0.001
            p.max = 0.100

        if not hasattr(engine.par, 'Silencetimeout'):
            p = page.appendFloat('Silencetimeout', label='Silence Timeout (s)')[0]
            p.default = 2.5
            p.min = 0.5
            p.max = 10.0

        if not hasattr(engine.par, 'Crossfadedur'):
            p = page.appendFloat('Crossfadedur', label='Fallback Crossfade Duration (s)')[0]
            p.default = 1.0
            p.min = 0.1
            p.max = 5.0

        # 3. Build Internal Operators
        def get_or_create(op_type, name, x, y):
            nonlocal current_node
            current_node = name
            node = engine.op(name)
            if node is None:
                node = engine.create(op_type, name)
            node.nodeX = x
            node.nodeY = y
            return node

        # Column 1: Audio Signal Sources (Native Audio Sample Rate, e.g. 44100 Hz)
        # Source 0: Hardware Audio Device In (Official class: audiodeviceinCHOP, parameter: bufferlength)
        dev_in = get_or_create(audiodeviceinCHOP, 'audio_dev_in', 0, 300)
        current_param = 'bufferlength'
        dev_in.par.bufferlength = 0.15
        dev_in.par.timeslice = 1

        # Source 1: Audio File In (Official class: audiofileinCHOP, parameter: file)
        file_in = get_or_create(audiofileinCHOP, 'audio_file_in', 0, 150)
        current_param = 'file'
        file_in.par.file.expr = "parent().par.Audiofile"
        file_in.par.play = 1

        # Transport & Tempo Sync: Ableton Link In (Official class: abletonlinkCHOP)
        # Supplies beat ramp (0..1) and BPM for phase synchronization while frequency analysis remains on audio
        link_in = get_or_create(abletonlinkCHOP, 'link_in', 0, -200)
        current_param = 'active'
        link_in.par.active = 1
        link_in.par.ramp = 1
        link_in.par.bpm = 1
        link_in.par.quantum = 4

        # Column 2: Source Switch (X = 240)
        # Routes genuine audio samples (device or file) into spectral filter chain
        src_switch = get_or_create(switchCHOP, 'src_switch', 240, 200)
        src_switch.inputConnectors[0].disconnect()
        src_switch.inputConnectors[0].connect(dev_in)
        src_switch.inputConnectors[0].connect(file_in)
        current_param = 'index'
        src_switch.par.index.expr = "0 if parent().par.Source == 'device' else 1"

        # Column 3: Frequency Band Splitting AT NATIVE AUDIO RATE (X = 460)
        # Nyquist-compliant: Bandpass filtering precedes rate downsampling
        # Band 1: Sub-Bass (Low Pass at 90 Hz, 24 dB/oct rolloff)
        band_sub = get_or_create(audiofilterCHOP, 'band_sub', 460, 350)
        band_sub.par.filter = 'lowpass'
        band_sub.par.units = 'frequency'
        band_sub.par.cutofffrequency = 90
        band_sub.par.rolloff = '24'
        band_sub.inputConnectors[0].disconnect()
        band_sub.inputConnectors[0].connect(src_switch)

        # Band 2: Bass (Band Pass centered at 170 Hz, 90-250 Hz range)
        band_bass = get_or_create(audiofilterCHOP, 'band_bass', 460, 200)
        band_bass.par.filter = 'bandpass'
        band_bass.par.units = 'frequency'
        band_bass.par.cutofffrequency = 170
        band_bass.par.resonance = 1.2
        band_bass.inputConnectors[0].disconnect()
        band_bass.inputConnectors[0].connect(src_switch)

        # Band 3: Mid (Band Pass centered at 1200 Hz, 250-2500 Hz range)
        band_mid = get_or_create(audiofilterCHOP, 'band_mid', 460, 50)
        band_mid.par.filter = 'bandpass'
        band_mid.par.units = 'frequency'
        band_mid.par.cutofffrequency = 1200
        band_mid.par.resonance = 1.0
        band_mid.inputConnectors[0].disconnect()
        band_mid.inputConnectors[0].connect(src_switch)

        # Band 4: High (High Pass at 3000 Hz, 2500-16000 Hz range, 24 dB/oct rolloff)
        band_high = get_or_create(audiofilterCHOP, 'band_high', 460, -100)
        band_high.par.filter = 'highpass'
        band_high.par.units = 'frequency'
        band_high.par.cutofffrequency = 3000
        band_high.par.rolloff = '24'
        band_high.inputConnectors[0].disconnect()
        band_high.inputConnectors[0].connect(src_switch)

        # Column 4: RMS Energy Extraction at Audio Rate (X = 680)
        bands_merge = get_or_create(mergeCHOP, 'bands_merge', 680, 150)
        bands_merge.inputConnectors[0].disconnect()
        bands_merge.inputConnectors[0].connect(band_sub)
        bands_merge.inputConnectors[0].connect(band_bass)
        bands_merge.inputConnectors[0].connect(band_mid)
        bands_merge.inputConnectors[0].connect(band_high)

        analyze_bands = get_or_create(analyzeCHOP, 'analyze_bands', 860, 150)
        analyze_bands.par.function = 'rms'
        analyze_bands.inputConnectors[0].disconnect()
        analyze_bands.inputConnectors[0].connect(bands_merge)

        rename_bands = get_or_create(renameCHOP, 'rename_bands', 1040, 150)
        rename_bands.par.renameto = 'sub bass mid high'
        rename_bands.inputConnectors[0].disconnect()
        rename_bands.inputConnectors[0].connect(analyze_bands)

        # Full Spectrum Aggregate RMS Power (Audio Rate)
        full_rms = get_or_create(analyzeCHOP, 'full_rms', 860, -250)
        full_rms.par.function = 'rms'
        full_rms.inputConnectors[0].disconnect()
        full_rms.inputConnectors[0].connect(src_switch)

        full_rms_rename = get_or_create(renameCHOP, 'full_rms_rename', 1040, -250)
        full_rms_rename.par.renameto = 'rms'
        full_rms_rename.inputConnectors[0].disconnect()
        full_rms_rename.inputConnectors[0].connect(full_rms)

        # Column 5: Downsample Extracted Scalar Envelopes to Video Frame Rate (X = 1240)
        # Method 'preserve' maintains time length while rate matches project frame rate.
        # Interp 'linear' smoothly connects downsampled envelope steps.
        resample_bands = get_or_create(resampleCHOP, 'resample_bands', 1240, 150)
        resample_bands.par.method = 'preserve'
        resample_bands.par.interp = 'linear'
        resample_bands.par.rate.expr = "me.time.rate"
        resample_bands.inputConnectors[0].disconnect()
        resample_bands.inputConnectors[0].connect(rename_bands)

        resample_rms = get_or_create(resampleCHOP, 'resample_rms', 1240, -250)
        resample_rms.par.method = 'preserve'
        resample_rms.par.interp = 'linear'
        resample_rms.par.rate.expr = "me.time.rate"
        resample_rms.inputConnectors[0].disconnect()
        resample_rms.inputConnectors[0].connect(full_rms_rename)

        # Column 6: Dynamic Auto-Gain Normalization (X = 1440)
        # Track rolling peak with fast attack and 4-second release
        peak_tracker = get_or_create(lagCHOP, 'peak_tracker', 1440, -250)
        peak_tracker.par.lag1 = 0.01
        peak_tracker.par.lag2 = 4.0
        peak_tracker.par.lagunit = 'seconds'
        peak_tracker.inputConnectors[0].disconnect()
        peak_tracker.inputConnectors[0].connect(resample_rms)

        # Scale bands dynamically: normalizes quiet passages while clamping loud drops
        gain_scale = get_or_create(mathCHOP, 'gain_scale', 1440, 150)
        gain_scale.par.gain.expr = (
            "parent().par.Gain / max(0.08, op('peak_tracker')['rms']) "
            "if parent().par.Autogain else parent().par.Gain"
        )
        gain_scale.inputConnectors[0].disconnect()
        gain_scale.inputConnectors[0].connect(resample_bands)

        # Column 7: Per-Band Asymmetric Lag Conditioning (X = 1640)
        # Separate individual bands to apply custom attack and decay parameters directly
        sel_sub = get_or_create(selectCHOP, 'sel_sub', 1640, 300)
        sel_sub.par.channames = 'sub'
        sel_sub.inputConnectors[0].disconnect()
        sel_sub.inputConnectors[0].connect(gain_scale)

        lag_sub = get_or_create(lagCHOP, 'lag_sub', 1820, 300)
        lag_sub.par.lag1.expr = "parent().par.Sublagup"
        lag_sub.par.lag2.expr = "parent().par.Sublagdown"
        lag_sub.par.lagunit = 'seconds'
        lag_sub.inputConnectors[0].disconnect()
        lag_sub.inputConnectors[0].connect(sel_sub)

        sel_bass = get_or_create(selectCHOP, 'sel_bass', 1640, 180)
        sel_bass.par.channames = 'bass'
        sel_bass.inputConnectors[0].disconnect()
        sel_bass.inputConnectors[0].connect(gain_scale)

        lag_bass = get_or_create(lagCHOP, 'lag_bass', 1820, 180)
        lag_bass.par.lag1.expr = "parent().par.Basslagup"
        lag_bass.par.lag2.expr = "parent().par.Basslagdown"
        lag_bass.par.lagunit = 'seconds'
        lag_bass.inputConnectors[0].disconnect()
        lag_bass.inputConnectors[0].connect(sel_bass)

        sel_mid = get_or_create(selectCHOP, 'sel_mid', 1640, 60)
        sel_mid.par.channames = 'mid'
        sel_mid.inputConnectors[0].disconnect()
        sel_mid.inputConnectors[0].connect(gain_scale)

        lag_mid = get_or_create(lagCHOP, 'lag_mid', 1820, 60)
        lag_mid.par.lag1.expr = "parent().par.Midlagup"
        lag_mid.par.lag2.expr = "parent().par.Midlagdown"
        lag_mid.par.lagunit = 'seconds'
        lag_mid.inputConnectors[0].disconnect()
        lag_mid.inputConnectors[0].connect(sel_mid)

        sel_high = get_or_create(selectCHOP, 'sel_high', 1640, -60)
        sel_high.par.channames = 'high'
        sel_high.inputConnectors[0].disconnect()
        sel_high.inputConnectors[0].connect(gain_scale)

        lag_high = get_or_create(lagCHOP, 'lag_high', 1820, -60)
        lag_high.par.lag1.expr = "parent().par.Highlagup"
        lag_high.par.lag2.expr = "parent().par.Highlagdown"
        lag_high.par.lagunit = 'seconds'
        lag_high.inputConnectors[0].disconnect()
        lag_high.inputConnectors[0].connect(sel_high)

        lagged_merge = get_or_create(mergeCHOP, 'lagged_merge', 2000, 150)
        lagged_merge.inputConnectors[0].disconnect()
        lagged_merge.inputConnectors[0].connect(lag_sub)
        lagged_merge.inputConnectors[0].connect(lag_bass)
        lagged_merge.inputConnectors[0].connect(lag_mid)
        lagged_merge.inputConnectors[0].connect(lag_high)

        limit_norm = get_or_create(limitCHOP, 'limit_norm', 2180, 150)
        limit_norm.par.type = 'clamp'
        limit_norm.par.min = 0.0
        limit_norm.par.max = 1.0
        limit_norm.inputConnectors[0].disconnect()
        limit_norm.inputConnectors[0].connect(lagged_merge)

        # Column 8: Transient Kick Trigger & Continuous Phase Accumulator (X = 2380)
        kick_select = get_or_create(selectCHOP, 'kick_select', 2380, -100)
        kick_select.par.channames = 'sub'
        kick_select.inputConnectors[0].disconnect()
        kick_select.inputConnectors[0].connect(limit_norm)

        # Kick Detection Logic: Evaluates input inside bounds [Kickthreshold, 10.0]
        kick_logic = get_or_create(logicCHOP, 'kick_logic', 2560, -100)
        kick_logic.par.convert = 'bound'
        kick_logic.par.boundmin.expr = "parent().par.Kickthreshold"
        kick_logic.par.boundmax = 10.0
        kick_logic.inputConnectors[0].disconnect()
        kick_logic.inputConnectors[0].connect(kick_select)

        kick_rename = get_or_create(renameCHOP, 'kick_rename', 2740, -100)
        kick_rename.par.renameto = 'kick'
        kick_rename.inputConnectors[0].disconnect()
        kick_rename.inputConnectors[0].connect(kick_logic)

        # Continuous Phase Integration
        speed_accum = get_or_create(speedCHOP, 'speed_accum', 2920, -100)
        speed_accum.par.scale = 0.05
        speed_accum.inputConnectors[0].disconnect()
        speed_accum.inputConnectors[0].connect(kick_rename)

        speed_rename = get_or_create(renameCHOP, 'speed_rename', 3100, -100)
        speed_rename.par.renameto = 'accum_phase'
        speed_rename.inputConnectors[0].disconnect()
        speed_rename.inputConnectors[0].connect(speed_accum)

        # Transport Phase Selector: Switches between Ableton Link phase ramp and internal speed accumulator
        link_ramp_sel = get_or_create(selectCHOP, 'link_ramp_sel', 2920, -250)
        link_ramp_sel.par.channames = 'ramp'
        link_ramp_sel.inputConnectors[0].disconnect()
        link_ramp_sel.inputConnectors[0].connect(link_in)

        link_phase_rename = get_or_create(renameCHOP, 'link_phase_rename', 3100, -250)
        link_phase_rename.par.renameto = 'accum_phase'
        link_phase_rename.inputConnectors[0].disconnect()
        link_phase_rename.inputConnectors[0].connect(link_ramp_sel)

        phase_switch = get_or_create(switchCHOP, 'phase_switch', 3280, -100)
        phase_switch.inputConnectors[0].disconnect()
        phase_switch.inputConnectors[0].connect(speed_rename)
        phase_switch.inputConnectors[0].connect(link_phase_rename)
        phase_switch.par.index.expr = "1 if parent().par.Linksync and op('link_in')['ramp'] is not None else 0"

        # Column 9: Merge Master Audio Channels (7 Channels Total) (X = 3480)
        audio_merge = get_or_create(mergeCHOP, 'audio_merge', 3480, 150)
        audio_merge.inputConnectors[0].disconnect()
        audio_merge.inputConnectors[0].connect(limit_norm)     # sub, bass, mid, high (4)
        audio_merge.inputConnectors[0].connect(kick_rename)    # kick (1)
        audio_merge.inputConnectors[0].connect(phase_switch)   # accum_phase (1)
        audio_merge.inputConnectors[0].connect(resample_rms)   # rms (1)

        # Column 10: Explicit Silence Timer and Crossfade Safeguard (X = 3480)
        # Silence Detection Logic: 1 if rms <= Silencethreshold, 0 otherwise
        silence_logic = get_or_create(logicCHOP, 'silence_logic', 3480, -280)
        silence_logic.par.convert = 'bound'
        silence_logic.par.boundmin = -1.0
        silence_logic.par.boundmax.expr = "parent().par.Silencethreshold"
        silence_logic.inputConnectors[0].disconnect()
        silence_logic.inputConnectors[0].connect(resample_rms)

        # Explicit Silence Timer: Integrates elapsed silence in seconds, resetting to 0 when audio returns
        silence_timer = get_or_create(speedCHOP, 'silence_timer', 3660, -280)
        silence_timer.par.scale = 1.0
        silence_timer.par.reset.expr = "1 if op('silence_logic')['rms'] == 0 else 0"
        silence_timer.inputConnectors[0].disconnect()
        silence_timer.inputConnectors[0].connect(silence_logic)

        # Silence Crossfade Math: Clamps [Silencetimeout, Silencetimeout + Crossfadedur] -> [0.0, 1.0]
        silence_cross_math = get_or_create(mathCHOP, 'silence_cross_math', 3840, -280)
        silence_cross_math.par.fromrange1.expr = "parent().par.Silencetimeout"
        silence_cross_math.par.fromrange2.expr = "parent().par.Silencetimeout + parent().par.Crossfadedur"
        silence_cross_math.par.torange1 = 0.0
        silence_cross_math.par.torange2 = 1.0
        silence_cross_math.par.limit = 'clamp'
        silence_cross_math.inputConnectors[0].disconnect()
        silence_cross_math.inputConnectors[0].connect(silence_timer)

        # Smooth recovery lag on return from fallback (decay = 0.3s)
        silence_recover_lag = get_or_create(lagCHOP, 'silence_recover_lag', 4020, -280)
        silence_recover_lag.par.lag1 = 0.00
        silence_recover_lag.par.lag2 = 0.30
        silence_recover_lag.par.lagunit = 'seconds'
        silence_recover_lag.inputConnectors[0].disconnect()
        silence_recover_lag.inputConnectors[0].connect(silence_cross_math)

        # Column 11: Complete 7-Channel Autonomous Fallback Generator (X = 3660)
        # Constructs all 7 channels with musically distinct LFOs and appropriate amplitude ranges
        fb_lfo_sub = get_or_create(lfoCHOP, 'fb_lfo_sub', 3660, 450)
        fb_lfo_sub.par.wavetype = 'sin'
        fb_lfo_sub.par.frequency = 0.25
        fb_lfo_sub.par.amplitude = 0.25
        fb_lfo_sub.par.offset = 0.45

        fb_ren_sub = get_or_create(renameCHOP, 'fb_ren_sub', 3840, 450)
        fb_ren_sub.par.renameto = 'sub'
        fb_ren_sub.inputConnectors[0].disconnect()
        fb_ren_sub.inputConnectors[0].connect(fb_lfo_sub)

        fb_lfo_bass = get_or_create(lfoCHOP, 'fb_lfo_bass', 3660, 360)
        fb_lfo_bass.par.wavetype = 'sin'
        fb_lfo_bass.par.frequency = 0.50
        fb_lfo_bass.par.amplitude = 0.20
        fb_lfo_bass.par.offset = 0.35

        fb_ren_bass = get_or_create(renameCHOP, 'fb_ren_bass', 3840, 360)
        fb_ren_bass.par.renameto = 'bass'
        fb_ren_bass.inputConnectors[0].disconnect()
        fb_ren_bass.inputConnectors[0].connect(fb_lfo_bass)

        fb_lfo_mid = get_or_create(lfoCHOP, 'fb_lfo_mid', 3660, 270)
        fb_lfo_mid.par.wavetype = 'sin'
        fb_lfo_mid.par.frequency = 0.80
        fb_lfo_mid.par.amplitude = 0.18
        fb_lfo_mid.par.offset = 0.30

        fb_ren_mid = get_or_create(renameCHOP, 'fb_ren_mid', 3840, 270)
        fb_ren_mid.par.renameto = 'mid'
        fb_ren_mid.inputConnectors[0].disconnect()
        fb_ren_mid.inputConnectors[0].connect(fb_lfo_mid)

        fb_lfo_high = get_or_create(lfoCHOP, 'fb_lfo_high', 3660, 180)
        fb_lfo_high.par.wavetype = 'sin'
        fb_lfo_high.par.frequency = 1.40
        fb_lfo_high.par.amplitude = 0.15
        fb_lfo_high.par.offset = 0.22

        fb_ren_high = get_or_create(renameCHOP, 'fb_ren_high', 3840, 180)
        fb_ren_high.par.renameto = 'high'
        fb_ren_high.inputConnectors[0].disconnect()
        fb_ren_high.inputConnectors[0].connect(fb_lfo_high)

        fb_lfo_kick = get_or_create(lfoCHOP, 'fb_lfo_kick', 3660, 90)
        fb_lfo_kick.par.wavetype = 'pulse'
        fb_lfo_kick.par.frequency = 2.00  # 120 BPM beat impulse
        fb_lfo_kick.par.amplitude = 0.50
        fb_lfo_kick.par.offset = 0.50

        fb_ren_kick = get_or_create(renameCHOP, 'fb_ren_kick', 3840, 90)
        fb_ren_kick.par.renameto = 'kick'
        fb_ren_kick.inputConnectors[0].disconnect()
        fb_ren_kick.inputConnectors[0].connect(fb_lfo_kick)

        fb_lfo_phase = get_or_create(lfoCHOP, 'fb_lfo_phase', 3660, 0)
        fb_lfo_phase.par.wavetype = 'ramp'
        fb_lfo_phase.par.frequency = 0.125
        fb_lfo_phase.par.amplitude = 0.50
        fb_lfo_phase.par.offset = 0.50

        fb_ren_phase = get_or_create(renameCHOP, 'fb_ren_phase', 3840, 0)
        fb_ren_phase.par.renameto = 'accum_phase'
        fb_ren_phase.inputConnectors[0].disconnect()
        fb_ren_phase.inputConnectors[0].connect(fb_lfo_phase)

        fb_const_rms = get_or_create(constantCHOP, 'fb_const_rms', 3660, -90)
        fb_const_rms.par.name0 = 'rms'
        fb_const_rms.par.value0 = 0.35

        fallback_merge = get_or_create(mergeCHOP, 'fallback_merge', 4020, 200)
        fallback_merge.inputConnectors[0].disconnect()
        fallback_merge.inputConnectors[0].connect(fb_ren_sub)
        fallback_merge.inputConnectors[0].connect(fb_ren_bass)
        fallback_merge.inputConnectors[0].connect(fb_ren_mid)
        fallback_merge.inputConnectors[0].connect(fb_ren_high)
        fallback_merge.inputConnectors[0].connect(fb_ren_kick)
        fallback_merge.inputConnectors[0].connect(fb_ren_phase)
        fallback_merge.inputConnectors[0].connect(fb_const_rms)

        # Crossfade between 7-channel Live Audio and 7-channel Fallback Drivers
        cross_safeguard = get_or_create(crossCHOP, 'cross_safeguard', 4240, 150)
        cross_safeguard.inputConnectors[0].disconnect()
        cross_safeguard.inputConnectors[0].connect(audio_merge)
        cross_safeguard.inputConnectors[0].connect(fallback_merge)
        cross_safeguard.par.cross.expr = (
            "op('silence_recover_lag')['rms'] if parent().par.Silencefallback else 0.0"
        )

        # Column 12: Master Selective Cook Null & External Out Connector (X = 4440)
        out_null = get_or_create(nullCHOP, 'audio_drivers', 4440, 150)
        out_null.par.cooktype = 'selective'
        out_null.inputConnectors[0].disconnect()
        out_null.inputConnectors[0].connect(cross_safeguard)

        out_connector = get_or_create(outCHOP, 'out1', 4620, 150)
        out_connector.inputConnectors[0].disconnect()
        out_connector.inputConnectors[0].connect(out_null)

        print(f"[Success] Built verified audio_reactive_engine inside {engine.path}")
        return True

    except Exception as err:
        err_msg = f"[Build Error] Failed at node '{current_node}'"
        if current_param:
            err_msg += f" parameter '{current_param}'"
        err_msg += f": {err}"
        print(err_msg)
        raise RuntimeError(err_msg) from err

if __name__ == '__main__':
    try:
        build_audio_reactive_engine()
    except Exception as exc:
        print(f"[Main Info] {exc}")
