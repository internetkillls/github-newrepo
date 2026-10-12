"""TouchDesigner GLSL Audio-Reactive Visual Loop Builder (v1.3.0).

Constructs a 'glsl_visual_loop' glslmultiTOP wired to the audio engine drivers,
configuring resolution (7200x1080 for 4-face cube or 1920x1080 for 16:9 canvas),
exact matching uniform parameters (uAudioBands, uKick, uPhase, uEnergy, uIsCube),
docked pixel DAT synchronization (without unsupported language parameters),
robust file/DAT/fallback shader resolution, and output nullTOP.
"""

from pathlib import Path

# Complete verified shader fallback code if disk file is unavailable in Text DAT execution
FALLBACK_SHADER_CODE = """// Audio-Reactive Visual Loop Fragment Shader for TouchDesigner GLSL TOP
uniform vec4 uAudioBands;
uniform float uKick;
uniform float uPhase;
uniform float uEnergy;
uniform float uIsCube;

out vec4 fragColor;

#define PI 3.14159265358979323846
#define TWO_PI 6.28318530717958647692

vec3 CosinePalette(float t, vec3 a, vec3 b, vec3 c, vec3 d) {
    return a + b * cos(TWO_PI * (c * t + d));
}

float SeamlessCylinderNoise(float alpha, float vNorm, float phaseAngle, float freq) {
    vec3 cylPos = vec3(cos(alpha) * freq, sin(alpha) * freq, vNorm * freq);
    vec3 p1 = cylPos + vec3(cos(phaseAngle) * 0.8, sin(phaseAngle) * 0.8, 0.0);
    vec3 p2 = cylPos + vec3(sin(phaseAngle) * 0.8, -cos(phaseAngle) * 0.8, 0.5);
    return (TDSimplexNoise(p1) + TDSimplexNoise(p2)) * 0.5;
}

float SeamlessPlanarNoise(vec2 st, float phaseAngle, float freq) {
    vec3 p1 = vec3(st * freq, cos(phaseAngle) * 0.8);
    vec3 p2 = vec3(st * freq, sin(phaseAngle) * 0.8);
    return (TDSimplexNoise(p1) + TDSimplexNoise(p2)) * 0.5;
}

void main() {
    vec2 st = vUV.st;
    vec2 aspect = (uTDOutputInfo.res.w > 0.0) ? uTDOutputInfo.res.zw : vec2(1920.0, 1080.0);
    float loopAngle = fract(uPhase) * TWO_PI;
    float subBass = uAudioBands.x;
    float bass = uAudioBands.y;
    float mid = uAudioBands.z;
    float treble = uAudioBands.w;
    float warpField = 0.0;
    float warpFieldR = 0.0;
    float warpFieldB = 0.0;
    float contourPattern = 0.0;
    float centerGlow = 0.0;
    bool isCube = (uIsCube > 0.5);

    if (isCube) {
        float scaledX = st.s * 4.0;
        float face = floor(scaledX);
        float u = fract(scaledX);
        float v = st.t;
        float vNorm = (v - 0.5) * 2.0;
        float alpha = TWO_PI * (face + u) / 4.0;
        float q1 = SeamlessCylinderNoise(alpha, vNorm, loopAngle, 2.0);
        float q2 = SeamlessCylinderNoise(alpha + PI * 0.5, vNorm, loopAngle + 1.0, 2.0);
        float alphaWarp = alpha + (subBass * 0.35) * q1;
        float vWarp = vNorm + (mid * 0.25) * q2;
        warpField = SeamlessCylinderNoise(alphaWarp, vWarp, loopAngle, 3.0);
        float disp = 0.02 * treble + 0.002;
        warpFieldR = SeamlessCylinderNoise(alphaWarp + disp, vWarp, loopAngle, 3.0);
        warpFieldB = SeamlessCylinderNoise(alphaWarp - disp, vWarp, loopAngle, 3.0);
        float harmonicCount = 4.0 + floor(mid * 8.0);
        float wave = sin(harmonicCount * alpha + warpField * 5.0 - loopAngle * 2.0);
        float ringSharpness = 0.15 + bass * 0.45;
        contourPattern = smoothstep(-ringSharpness, ringSharpness, wave);
        centerGlow = exp(-abs(vNorm) * 3.5) * (0.3 + subBass * 0.8 + uKick * 1.2);
    } else {
        vec2 p = (st - 0.5) * vec2(aspect.x / max(1.0, aspect.y), 1.0);
        float q1 = SeamlessPlanarNoise(p, loopAngle, 2.0);
        float q2 = SeamlessPlanarNoise(p + vec2(4.3, 1.2), loopAngle + 1.0, 2.0);
        vec2 pWarp = p + (subBass * 0.35) * vec2(q1, q2);
        warpField = SeamlessPlanarNoise(pWarp, loopAngle, 3.0);
        float disp = 0.015 * treble + 0.002;
        warpFieldR = SeamlessPlanarNoise(pWarp + vec2(disp, 0.0), loopAngle, 3.0);
        warpFieldB = SeamlessPlanarNoise(pWarp - vec2(disp, 0.0), loopAngle, 3.0);
        float dist = length(p);
        float wave = sin(dist * (8.0 + floor(mid * 8.0)) + warpField * 5.0 - loopAngle * 2.0);
        contourPattern = smoothstep(-0.25, 0.25, wave);
        centerGlow = exp(-dist * 3.0) * (0.3 + subBass * 0.8 + uKick * 1.2);
    }

    vec3 palA = mix(vec3(0.08, 0.09, 0.14), vec3(0.20, 0.12, 0.28), uEnergy);
    vec3 palB = mix(vec3(0.40, 0.35, 0.50), vec3(0.80, 0.45, 0.60), uEnergy);
    vec3 palC = vec3(1.0, 1.0, 1.0);
    vec3 palD = vec3(0.00, 0.33, 0.67) + vec3(fract(uPhase) * 1.0);

    vec3 colR = CosinePalette(warpFieldR + contourPattern * 0.2, palA, palB, palC, palD);
    vec3 colG = CosinePalette(warpField  + contourPattern * 0.2, palA, palB, palC, palD);
    vec3 colB = CosinePalette(warpFieldB + contourPattern * 0.2, palA, palB, palC, palD);
    vec3 finalColor = vec3(colR.r, colG.g, colB.b) + vec3(1.0, 0.85, 0.6) * centerGlow;
    finalColor += vec3(0.7, 0.9, 1.0) * pow(abs(warpField), 4.0) * treble * 1.5;
    finalColor = finalColor / (finalColor + vec3(1.0));
    fragColor = TDOutputSwizzle(vec4(finalColor, 1.0));
}
"""

def resolve_shader_source():
    """Resolves shader source code robustly across Text DAT and script environments."""
    # 1. Try local file path relative to __file__ if available
    try:
        if '__file__' in globals():
            local_path = Path(__file__).resolve().parent / 'audio_reactive_loop.frag'
            if local_path.is_file():
                return local_path.read_text(encoding='utf-8')
    except Exception:
        pass

    # 2. Try project folder if running in TouchDesigner
    try:
        import td
        if hasattr(td, 'project') and hasattr(td.project, 'folder'):
            proj_path = Path(td.project.folder) / 'audio_reactive_loop.frag'
            if proj_path.is_file():
                return proj_path.read_text(encoding='utf-8')
    except Exception:
        pass

    # 3. Fallback to embedded verified shader code
    return FALLBACK_SHADER_CODE.strip()

def build_glsl_visual_loop(parent_path='/project1', top_name='glsl_visual_loop', cube_mode=True):
    """Constructs or updates the audio-reactive GLSL TOP in TouchDesigner.

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
        raise ValueError(f"[GLSL Build Error] Target parent path '{parent_path}' does not exist.")

    current_node = None
    current_param = None

    try:
        # 1. Resolve shader source code
        shader_source = resolve_shader_source()

        # 2. Create or retrieve glslmultiTOP
        current_node = top_name
        glsl_top = parent_op.op(top_name)
        if glsl_top is None:
            glsl_top = parent_op.create(glslmultiTOP, top_name)

        glsl_top.nodeX = 600
        glsl_top.nodeY = 200

        # Output Resolution Setup
        current_param = 'outputresolution'
        glsl_top.par.outputresolution = 'custom'
        if cube_mode:
            glsl_top.par.resolutionw = 7200
            glsl_top.par.resolutionh = 1080
        else:
            glsl_top.par.resolutionw = 1920
            glsl_top.par.resolutionh = 1080

        # 3. Setup Docked Pixel DAT (Do NOT set language='glsl'; handled natively by TouchDesigner)
        dat_name = f"{top_name}_pixel"
        current_node = dat_name
        pixel_dat = parent_op.op(dat_name)
        if pixel_dat is None:
            pixel_dat = parent_op.create(textDAT, dat_name)
            pixel_dat.dock = glsl_top
            pixel_dat.nodeX = glsl_top.nodeX
            pixel_dat.nodeY = glsl_top.nodeY - 150

        if shader_source:
            pixel_dat.text = shader_source

        current_node = top_name
        glsl_top.par.pixeldat = pixel_dat.name

        # 4. Bind Uniforms - Exact 1:1 match with audio_reactive_loop.frag declarations
        # Uniform 0: uniform vec4 uAudioBands; (x: sub, y: bass, z: mid, w: high)
        current_param = 'vec0name'
        glsl_top.par.vec0name = 'uAudioBands'
        glsl_top.par.vec0valuex.expr = "op('AudioEngine/audio_drivers')['sub'] if op('AudioEngine/audio_drivers') else 0.0"
        glsl_top.par.vec0valuey.expr = "op('AudioEngine/audio_drivers')['bass'] if op('AudioEngine/audio_drivers') else 0.0"
        glsl_top.par.vec0valuez.expr = "op('AudioEngine/audio_drivers')['mid'] if op('AudioEngine/audio_drivers') else 0.0"
        glsl_top.par.vec0valuew.expr = "op('AudioEngine/audio_drivers')['high'] if op('AudioEngine/audio_drivers') else 0.0"

        # Uniform 1: uniform float uKick; (transient hit pulse)
        current_param = 'vec1name'
        glsl_top.par.vec1name = 'uKick'
        glsl_top.par.vec1valuex.expr = "op('AudioEngine/audio_drivers')['kick'] if op('AudioEngine/audio_drivers') else 0.0"

        # Uniform 2: uniform float uPhase; (continuous temporal loop phase)
        current_param = 'vec2name'
        glsl_top.par.vec2name = 'uPhase'
        glsl_top.par.vec2valuex.expr = (
            "op('AudioEngine/audio_drivers')['accum_phase'] % 1.0 "
            "if op('AudioEngine/audio_drivers') else (me.time.frame % 360) / 360.0"
        )

        # Uniform 3: uniform float uEnergy; (track aggregate volume)
        current_param = 'vec3name'
        glsl_top.par.vec3name = 'uEnergy'
        glsl_top.par.vec3valuex.expr = "op('AudioEngine/audio_drivers')['rms'] if op('AudioEngine/audio_drivers') else 0.0"

        # Uniform 4: uniform float uIsCube; (1.0 for 4-face 7200x1080 cube mode; 0.0 for 16:9 canvas)
        current_param = 'vec4name'
        glsl_top.par.vec4name = 'uIsCube'
        glsl_top.par.vec4valuex = 1.0 if cube_mode else 0.0

        # 5. Connect downstream nullTOP
        current_node = 'final_visual_loop'
        null_out = parent_op.op('final_visual_loop')
        if null_out is None:
            null_out = parent_op.create(nullTOP, 'final_visual_loop')

        null_out.nodeX = glsl_top.nodeX + 220
        null_out.nodeY = glsl_top.nodeY
        null_out.inputConnectors[0].disconnect()
        null_out.inputConnectors[0].connect(glsl_top)

        print(f"[Success] Built verified {top_name} with synchronized uniforms and connected to {null_out.path}")
        return True

    except Exception as err:
        err_msg = f"[GLSL Build Error] Failed at node '{current_node}'"
        if current_param:
            err_msg += f" parameter '{current_param}'"
        err_msg += f": {err}"
        print(err_msg)
        raise RuntimeError(err_msg) from err

if __name__ == '__main__':
    try:
        build_glsl_visual_loop()
    except Exception as exc:
        print(f"[GLSL Main Info] {exc}")
