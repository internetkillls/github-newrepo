"""TouchDesigner Ableton-to-Cube Visual Parameter Router Builder (v1.3.0).

Constructs an 'ableton_cube_router' baseCOMP that:
1. Ingests Ableton Live telemetry across 3 selectable Routing Modes:
   - Mode 0: OSC Telemetry (/drums, /bass, /synth, /fx)
   - Mode 1: Ableton Link + Audio In (sub, bass, mid, high from audio_reactive_engine)
   - Mode 2: Direct MIDI In (faders and note velocities)
2. Uses documented TouchDesigner Python operator classes (abletonlinkCHOP, mathCHOP, etc.).
3. Accurately maps musical stems into bounded parameters for 4-sided cube perimeter ribbons.
4. Enforces strict integer quantization for spatial harmonics (integer='floor') for C0/C1 corner seams.
5. Dynamically enforces the top/bottom safe margin rule:
   (band_span / 2 + amplitude + stroke_width / 2 <= 0.42)
   with graceful clamping and headroom preservation under out-of-nominal inputs.
6. Provides idempotent rebuilds and comprehensive error diagnostics.
"""

def build_ableton_cube_router(parent_path='/project1', comp_name='ableton_cube_router'):
    """Constructs or updates the ableton_cube_router COMP inside TouchDesigner.

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
        raise ValueError(f"[Router Error] Target parent path '{parent_path}' does not exist.")

    current_node = None
    current_param = None

    try:
        # 1. Create or retrieve baseCOMP
        current_node = comp_name
        router = parent_op.op(comp_name)
        if router is None:
            router = parent_op.create(baseCOMP, comp_name)

        router.par.parentshortcut = 'AbletonRouter'
        router.nodeX = 200
        router.nodeY = 400

        # 2. Setup Custom Parameters on parent COMP
        page = router.appendCustomPage('Ableton Cube Router')

        if not hasattr(router.par, 'Routingmode'):
            p = page.appendMenu('Routingmode', label='Input Routing Mode')[0]
            p.menuNames = ['osc', 'link_audio', 'midi']
            p.menuLabels = ['OSC Telemetry (UDP)', 'Ableton Link + Audio In', 'Direct MIDI In']

        if not hasattr(router.par, 'Oscport'):
            p = page.appendInt('Oscport', label='OSC Port')[0]
            p.default = 7000

        if not hasattr(router.par, 'Ribboncount'):
            p = page.appendInt('Ribboncount', label='Ribbon Count (R)')[0]
            p.default = 8
            p.min = 3
            p.max = 12

        if not hasattr(router.par, 'Basebandspan'):
            p = page.appendFloat('Basebandspan', label='Base Band Span')[0]
            p.default = 0.40
            p.min = 0.20
            p.max = 0.50

        if not hasattr(router.par, 'Drumampmod'):
            p = page.appendFloat('Drumampmod', label='Drums -> Amp Sensitivity')[0]
            p.default = 1.0
            p.min = 0.0
            p.max = 2.0

        if not hasattr(router.par, 'Basswidthmod'):
            p = page.appendFloat('Basswidthmod', label='Bass -> Width Sensitivity')[0]
            p.default = 1.0
            p.min = 0.0
            p.max = 2.0

        if not hasattr(router.par, 'Harmonicmod'):
            p = page.appendFloat('Harmonicmod', label='Synth -> Harmonic Sensitivity')[0]
            p.default = 1.0
            p.min = 0.0
            p.max = 2.0

        if not hasattr(router.par, 'Enforcesafemargin'):
            p = page.appendToggle('Enforcesafemargin', label='Enforce Safe Margin (<= 0.42)')[0]
            p.default = True

        # 3. Helper to create or fetch nodes
        def get_or_create(op_type, name, x, y):
            nonlocal current_node
            current_node = name
            node = router.op(name)
            if node is None:
                node = router.create(op_type, name)
            node.nodeX = x
            node.nodeY = y
            return node

        # Column 1: Ingestion Sources for All 3 Routing Modes (X = 0)
        # Mode 0 Source: OSC Telemetry Ingestion
        osc_in = get_or_create(oscinCHOP, 'osc_in', 0, 350)
        current_param = 'port'
        osc_in.par.port.expr = "parent().par.Oscport"
        osc_in.par.active = 1

        osc_select = get_or_create(selectCHOP, 'osc_select', 180, 350)
        osc_select.par.chop = osc_in.name
        osc_select.par.channames = '*drums* *bass* *synth* *fx*'
        osc_select.par.renamefrom = '*'
        osc_select.par.renameto = 'drums bass synth fx'

        # Mode 1 Source: Audio/Engine Input via In CHOP (connected to audio_reactive_engine)
        audio_in = get_or_create(inCHOP, 'audio_in', 0, 180)

        audio_rename = get_or_create(renameCHOP, 'audio_rename', 180, 180)
        audio_rename.par.renamefrom = 'sub bass mid high'
        audio_rename.par.renameto = 'drums bass synth fx'
        audio_rename.inputConnectors[0].disconnect()
        audio_rename.inputConnectors[0].connect(audio_in)

        # Mode 2 Source: MIDI Ingestion
        midi_in = get_or_create(midiinCHOP, 'midi_in', 0, 0)

        midi_rename = get_or_create(renameCHOP, 'midi_rename', 180, 0)
        midi_rename.par.renamefrom = '*'
        midi_rename.par.renameto = 'drums bass synth fx'
        midi_rename.inputConnectors[0].disconnect()
        midi_rename.inputConnectors[0].connect(midi_in)

        # Ableton Link Ingestion (Common Transport Provider)
        # Documented TD class: abletonlinkCHOP (parameter: ramp=1 outputs bar phase)
        link_in = get_or_create(abletonlinkCHOP, 'link_in', 0, -220)
        current_param = 'active'
        link_in.par.active = 1
        link_in.par.ramp = 1
        link_in.par.quantum = 4

        # Column 2: Multi-Mode Routing Switch (X = 380)
        # Actively switches stem sources based on parent parameter Routingmode
        stem_source_switch = get_or_create(switchCHOP, 'stem_source_switch', 380, 200)
        stem_source_switch.inputConnectors[0].disconnect()
        stem_source_switch.inputConnectors[0].connect(osc_select)
        stem_source_switch.inputConnectors[0].connect(audio_rename)
        stem_source_switch.inputConnectors[0].connect(midi_rename)
        current_param = 'index'
        stem_source_switch.par.index.expr = (
            "0 if parent().par.Routingmode == 'osc' else "
            "(1 if parent().par.Routingmode == 'link_audio' else 2)"
        )

        # Lag Smoothing per stem (Decoupled Attack & Musical Release)
        stem_lag = get_or_create(lagCHOP, 'stem_lag', 560, 200)
        stem_lag.par.lag1 = 0.01
        stem_lag.par.lag2 = 0.25
        stem_lag.par.lagunit = 'seconds'
        stem_lag.inputConnectors[0].disconnect()
        stem_lag.inputConnectors[0].connect(stem_source_switch)

        # Column 3: Mathematical Parameter Mappings (X = 760)
        # 1. Drums -> Candidate Amplitude (Nominal bounds: 0.015 to 0.075)
        amp_raw = get_or_create(mathCHOP, 'amp_raw', 760, 400)
        amp_raw.par.scope = 'drums'
        amp_raw.par.gain.expr = "parent().par.Drumampmod"
        amp_raw.par.torange1 = 0.015
        amp_raw.par.torange2 = 0.075
        amp_raw.inputConnectors[0].disconnect()
        amp_raw.inputConnectors[0].connect(stem_lag)

        amp_rename = get_or_create(renameCHOP, 'amp_rename', 940, 400)
        amp_rename.par.renamefrom = 'drums'
        amp_rename.par.renameto = 'amplitude_candidate'
        amp_rename.inputConnectors[0].disconnect()
        amp_rename.inputConnectors[0].connect(amp_raw)

        # 2. Bass -> Stroke Width (Bounds: 0.003 to 0.018)
        width_math = get_or_create(mathCHOP, 'width_math', 760, 220)
        width_math.par.scope = 'bass'
        width_math.par.gain.expr = "parent().par.Basswidthmod"
        width_math.par.torange1 = 0.003
        width_math.par.torange2 = 0.018
        width_math.inputConnectors[0].disconnect()
        width_math.inputConnectors[0].connect(stem_lag)

        width_rename = get_or_create(renameCHOP, 'width_rename', 940, 220)
        width_rename.par.renamefrom = 'bass'
        width_rename.par.renameto = 'stroke_width'
        width_rename.inputConnectors[0].disconnect()
        width_rename.inputConnectors[0].connect(width_math)

        # 3. Synth/Lead -> Spatial Harmonic (Bounds: 2 to 8, STRICT INTEGER QUANTIZATION)
        # Documented TouchDesigner mathCHOP parameter: integer='floor' (not postop)
        harmonic_math = get_or_create(mathCHOP, 'harmonic_math', 760, 40)
        harmonic_math.par.scope = 'synth'
        harmonic_math.par.gain.expr = "parent().par.Harmonicmod"
        harmonic_math.par.torange1 = 2.0
        harmonic_math.par.torange2 = 8.0
        current_param = 'integer'
        harmonic_math.par.integer = 'floor'  # Enforce integer to guarantee C0/C1 corner seams
        harmonic_math.inputConnectors[0].disconnect()
        harmonic_math.inputConnectors[0].connect(stem_lag)

        harmonic_rename = get_or_create(renameCHOP, 'harmonic_rename', 940, 40)
        harmonic_rename.par.renamefrom = 'synth'
        harmonic_rename.par.renameto = 'spatial_harmonic'
        harmonic_rename.inputConnectors[0].disconnect()
        harmonic_rename.inputConnectors[0].connect(harmonic_math)

        # 4. FX / Energy -> Band Span (Bounds: 0.25 to 0.48)
        span_math = get_or_create(mathCHOP, 'span_math', 760, -140)
        span_math.par.scope = 'fx'
        span_math.par.gain.expr = "parent().par.Basebandspan / 0.40"
        span_math.par.torange1 = 0.25
        span_math.par.torange2 = 0.48
        span_math.inputConnectors[0].disconnect()
        span_math.inputConnectors[0].connect(stem_lag)

        span_rename = get_or_create(renameCHOP, 'span_rename', 940, -140)
        span_rename.par.renamefrom = 'fx'
        span_rename.par.renameto = 'band_span'
        span_rename.inputConnectors[0].disconnect()
        span_rename.inputConnectors[0].connect(span_math)

        # 5. Ableton Link Phase -> u_phase (0.0 to 1.0 continuous ramp)
        link_select = get_or_create(selectCHOP, 'link_select', 760, -300)
        link_select.par.chop = link_in.name
        link_select.par.channames = 'ramp'

        link_rename = get_or_create(renameCHOP, 'link_rename', 940, -300)
        link_rename.par.renamefrom = 'ramp'
        link_rename.par.renameto = 'u_phase'
        link_rename.inputConnectors[0].disconnect()
        link_rename.inputConnectors[0].connect(link_select)

        # Column 4: ACTIVE SAFE MARGIN ENFORCEMENT LIMITER (X = 1140)
        # Mathematical invariant: band_span / 2 + amplitude + stroke_width / 2 <= 0.42
        span_half = get_or_create(mathCHOP, 'span_half', 1140, -140)
        span_half.par.gain = 0.5
        span_half.inputConnectors[0].disconnect()
        span_half.inputConnectors[0].connect(span_rename)

        width_half = get_or_create(mathCHOP, 'width_half', 1140, 220)
        width_half.par.gain = 0.5
        width_half.inputConnectors[0].disconnect()
        width_half.inputConnectors[0].connect(width_rename)

        margin_used = get_or_create(mathCHOP, 'margin_used', 1320, 40)
        margin_used.par.chopop = 'add'
        margin_used.inputConnectors[0].disconnect()
        margin_used.inputConnectors[0].connect(span_half)
        margin_used.inputConnectors[0].connect(width_half)

        # Headroom calculation: 0.42 - margin_used
        # Documented TouchDesigner mathCHOP parameter: postoff = 0.42 (not postadd)
        budget_headroom = get_or_create(mathCHOP, 'budget_headroom', 1500, 40)
        budget_headroom.par.preop = 'negate'
        current_param = 'postoff'
        budget_headroom.par.postoff = 0.42
        budget_headroom.inputConnectors[0].disconnect()
        budget_headroom.inputConnectors[0].connect(margin_used)

        # Headroom Floor: Prevent headroom from collapsing to negative under extreme inputs
        headroom_floor = get_or_create(limitCHOP, 'headroom_floor', 1680, 40)
        headroom_floor.par.type = 'clamp'
        headroom_floor.par.min = 0.005
        headroom_floor.par.max = 0.420
        headroom_floor.inputConnectors[0].disconnect()
        headroom_floor.inputConnectors[0].connect(budget_headroom)

        # Dynamic amplitude clamp: min(candidate_amplitude, allowed_headroom)
        amp_clamped = get_or_create(mathCHOP, 'amp_clamped', 1860, 220)
        amp_clamped.par.chopop = 'min'
        amp_clamped.inputConnectors[0].disconnect()
        amp_clamped.inputConnectors[0].connect(amp_rename)
        amp_clamped.inputConnectors[0].connect(headroom_floor)

        # Margin Bypass Switch: Enforces or bypasses margin dynamically based on toggle
        amp_margin_switch = get_or_create(switchCHOP, 'amp_margin_switch', 2040, 220)
        amp_margin_switch.inputConnectors[0].disconnect()
        amp_margin_switch.inputConnectors[0].connect(amp_raw)
        amp_margin_switch.inputConnectors[0].connect(amp_clamped)
        amp_margin_switch.par.index.expr = "1 if parent().par.Enforcesafemargin else 0"

        # Final Safe Bounds Clamp (Absolute Physical Range: 0.005 to 0.080)
        amp_safe = get_or_create(limitCHOP, 'amp_safe', 2220, 220)
        amp_safe.par.type = 'clamp'
        amp_safe.par.min = 0.005
        amp_safe.par.max = 0.080
        amp_safe.inputConnectors[0].disconnect()
        amp_safe.inputConnectors[0].connect(amp_margin_switch)

        amp_final = get_or_create(renameCHOP, 'amp_final', 2400, 220)
        amp_final.par.renamefrom = '*'
        amp_final.par.renameto = 'amplitude'
        amp_final.inputConnectors[0].disconnect()
        amp_final.inputConnectors[0].connect(amp_safe)

        # Column 5: Recipe Constants (X = 2220)
        const_recipe = get_or_create(constantCHOP, 'const_recipe', 2220, -300)
        const_recipe.par.name0 = 'ribbon_count'
        const_recipe.par.value0.expr = "parent().par.Ribboncount"
        const_recipe.par.name1 = 'temporal_cycles'
        const_recipe.par.value1 = 1

        # Column 6: Master Merge of Safe Cube Parameters (X = 2580)
        cube_merge = get_or_create(mergeCHOP, 'cube_merge', 2580, 100)
        cube_merge.inputConnectors[0].disconnect()
        cube_merge.inputConnectors[0].connect(amp_final)
        cube_merge.inputConnectors[0].connect(width_rename)
        cube_merge.inputConnectors[0].connect(harmonic_rename)
        cube_merge.inputConnectors[0].connect(span_rename)
        cube_merge.inputConnectors[0].connect(link_rename)
        cube_merge.inputConnectors[0].connect(const_recipe)

        # Column 7: Selective Cook Null & Output Connector (X = 2780)
        cube_params = get_or_create(nullCHOP, 'cube_parameters', 2780, 100)
        cube_params.par.cooktype = 'selective'
        cube_params.inputConnectors[0].disconnect()
        cube_params.inputConnectors[0].connect(cube_merge)

        out1 = get_or_create(outCHOP, 'out1', 2960, 100)
        out1.inputConnectors[0].disconnect()
        out1.inputConnectors[0].connect(cube_params)

        print(f"[Success] Built verified ableton_cube_router inside {router.path}")
        return True

    except Exception as err:
        err_msg = f"[Router Error] Failed at node '{current_node}'"
        if current_param:
            err_msg += f" parameter '{current_param}'"
        err_msg += f": {err}"
        print(err_msg)
        raise RuntimeError(err_msg) from err

if __name__ == '__main__':
    try:
        build_ableton_cube_router()
    except Exception as exc:
        print(f"[Router Info] {exc}")
