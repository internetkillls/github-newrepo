// Audio-Reactive Visual Loop Fragment Shader for TouchDesigner GLSL TOP (v1.3.0)
// Real-time frequency response, seamless circle-phase looping, and 4-face cube continuity.
// Complies strictly with TouchDesigner GLSL TOP standards (TDOutputSwizzle, uTDOutputInfo).

uniform vec4 uAudioBands;      // x: Sub-Bass, y: Bass, z: Mid, w: High/Treble (normalized 0.0 - 1.0)
uniform float uKick;           // Discrete transient punch [0.0 - 1.0]
uniform float uPhase;          // Continuous temporal loop phase [0.0 - 1.0] (from Ableton Link / Clock)
uniform float uEnergy;         // Aggregate track energy / moving average [0.0 - 1.0]
uniform float uIsCube;         // 1.0 = 4-face 7200x1080 cube mode; 0.0 = standard 16:9 canvas

out vec4 fragColor;

#define PI 3.14159265358979323846
#define TWO_PI 6.28318530717958647692

// Cosine-based procedural palette interpolation (Inigo Quilez formula)
// Returns smooth, vibrant color gradients without expensive texture lookups.
vec3 CosinePalette(float t, vec3 a, vec3 b, vec3 c, vec3 d) {
    return a + b * cos(TWO_PI * (c * t + d));
}

// 2D Rotation Matrix
mat2 Rot(float angle) {
    float s = sin(angle), c = cos(angle);
    return mat2(c, -s, s, c);
}

// Seamless Cylinder & Circle-Time Noise for 100% Analytic Seam & Loop Closure
float SeamlessCylinderNoise(float alpha, float vNorm, float phaseAngle, float freq) {
    // 1. Spatial cylindrical coordinates around the 4-sided cube: (cos(alpha), sin(alpha), vNorm)
    // Ensures alpha=0 and alpha=2*PI are identical to machine precision.
    vec3 cylPos = vec3(cos(alpha) * freq, sin(alpha) * freq, vNorm * freq);

    // 2. Temporal circle embedding: (cos(phaseAngle), sin(phaseAngle))
    // Ensures phaseAngle=0 and phaseAngle=2*PI are identical to machine precision.
    vec3 p1 = cylPos + vec3(cos(phaseAngle) * 0.8, sin(phaseAngle) * 0.8, 0.0);
    vec3 p2 = cylPos + vec3(sin(phaseAngle) * 0.8, -cos(phaseAngle) * 0.8, 0.5);
    return (TDSimplexNoise(p1) + TDSimplexNoise(p2)) * 0.5;
}

// Seamless 2D Planar Noise (used for standard 16:9 canvas mode)
float SeamlessPlanarNoise(vec2 st, float phaseAngle, float freq) {
    vec3 p1 = vec3(st * freq, cos(phaseAngle) * 0.8);
    vec3 p2 = vec3(st * freq, sin(phaseAngle) * 0.8);
    return (TDSimplexNoise(p1) + TDSimplexNoise(p2)) * 0.5;
}

void main() {
    vec2 st = vUV.st;
    // Built-in TouchDesigner resolution query
    vec2 aspect = (uTDOutputInfo.res.w > 0.0) ? uTDOutputInfo.res.zw : vec2(1920.0, 1080.0);

    // Temporal Loop Angle: 0 to 2*PI over 1 loop period
    float loopAngle = fract(uPhase) * TWO_PI;

    // Audio Frequency Decomposition
    float subBass = uAudioBands.x;
    float bass    = uAudioBands.y;
    float mid     = uAudioBands.z;
    float treble  = uAudioBands.w;

    float warpField = 0.0;
    float warpFieldR = 0.0;
    float warpFieldB = 0.0;
    float contourPattern = 0.0;
    float centerGlow = 0.0;

    bool isCube = (uIsCube > 0.5);

    if (isCube) {
        // --- 4-FACE CUBE MODE (7200x1080) ---
        // Decode face index [0..3] and local face coordinate u [0..1]
        float scaledX = st.s * 4.0;
        float face = floor(scaledX);
        float u = fract(scaledX);
        float v = st.t; // Normalized height [0..1]
        float vNorm = (v - 0.5) * 2.0; // [-1.0 bottom, +1.0 top]

        // Continuous perimeter angle around the cube: 0 to 2*PI
        // At left edge (face 0, u=0): alpha = 0
        // At right edge (face 3, u=1): alpha = 2*PI
        float alpha = TWO_PI * (face + u) / 4.0;

        // Domain warping with strictly periodic cylinder coordinates
        float q1 = SeamlessCylinderNoise(alpha, vNorm, loopAngle, 2.0);
        float q2 = SeamlessCylinderNoise(alpha + PI * 0.5, vNorm, loopAngle + 1.0, 2.0);

        // Sub-bass modulates macro coordinate warping; mid modulates micro turbulence
        float alphaWarp = alpha + (subBass * 0.35) * q1;
        float vWarp = vNorm + (mid * 0.25) * q2;

        warpField = SeamlessCylinderNoise(alphaWarp, vWarp, loopAngle, 3.0);

        // Chromatic dispersion (RGB split on treble transients)
        float disp = 0.02 * treble + 0.002;
        warpFieldR = SeamlessCylinderNoise(alphaWarp + disp, vWarp, loopAngle, 3.0);
        warpFieldB = SeamlessCylinderNoise(alphaWarp - disp, vWarp, loopAngle, 3.0);

        // Harmonic Contour Rings: Integer harmonic count guarantees exact seam closure across corners
        float harmonicCount = 4.0 + floor(mid * 8.0); // Strict integer
        float wave = sin(harmonicCount * alpha + warpField * 5.0 - loopAngle * 2.0);
        float ringSharpness = 0.15 + bass * 0.45;
        contourPattern = smoothstep(-ringSharpness, ringSharpness, wave);

        // Center Equator Glow: depends only on vertical distance from equator |vNorm|,
        // completely invariant along alpha -> Identical at alpha=0 and alpha=2*PI!
        float vDist = abs(vNorm);
        centerGlow = exp(-vDist * 3.5) * (0.3 + subBass * 0.8 + uKick * 1.2);

    } else {
        // --- STANDARD ASPECT-CORRECTED 2D CANVAS ---
        vec2 p = (st - 0.5) * vec2(aspect.x / max(1.0, aspect.y), 1.0);
        p = Rot(sin(loopAngle) * 0.2 + uKick * 0.15) * p;

        float q1 = SeamlessPlanarNoise(p, loopAngle, 2.0);
        float q2 = SeamlessPlanarNoise(p + vec2(4.3, 1.2), loopAngle + 1.0, 2.0);

        vec2 pWarp = p + (subBass * 0.35) * vec2(q1, q2);
        warpField = SeamlessPlanarNoise(pWarp, loopAngle, 3.0);

        float disp = 0.015 * treble + 0.002;
        warpFieldR = SeamlessPlanarNoise(pWarp + vec2(disp, 0.0), loopAngle, 3.0);
        warpFieldB = SeamlessPlanarNoise(pWarp - vec2(disp, 0.0), loopAngle, 3.0);

        float dist = length(p);
        float wave = sin(dist * (8.0 + floor(mid * 8.0)) + warpField * 5.0 - loopAngle * 2.0);
        float ringSharpness = 0.15 + bass * 0.45;
        contourPattern = smoothstep(-ringSharpness, ringSharpness, wave);

        centerGlow = exp(-dist * 3.0) * (0.3 + subBass * 0.8 + uKick * 1.2);
    }

    // Dynamic Cosine Palette Generation
    // Energy level blends from cool dusk atmosphere to intense radiant peak
    vec3 palA = mix(vec3(0.08, 0.09, 0.14), vec3(0.20, 0.12, 0.28), uEnergy);
    vec3 palB = mix(vec3(0.40, 0.35, 0.50), vec3(0.80, 0.45, 0.60), uEnergy);
    vec3 palC = vec3(1.0, 1.0, 1.0);

    // FIXED PERIODICITY: Multiply uPhase by 1.0 (integer) inside TWO_PI so cos(... + 2*PI*1.0) == cos(...)
    // Guarantees Frame 0 (uPhase=0.0) matches Frame N (uPhase=1.0) exactly!
    vec3 palD = vec3(0.00, 0.33, 0.67) + vec3(fract(uPhase) * 1.0);

    vec3 colR = CosinePalette(warpFieldR + contourPattern * 0.2, palA, palB, palC, palD);
    vec3 colG = CosinePalette(warpField  + contourPattern * 0.2, palA, palB, palC, palD);
    vec3 colB = CosinePalette(warpFieldB + contourPattern * 0.2, palA, palB, palC, palD);
    vec3 finalColor = vec3(colR.r, colG.g, colB.b);

    // Add Transient Core Glow
    finalColor += vec3(1.0, 0.85, 0.6) * centerGlow;

    // Treble Edge Shimmer
    float edgeShimmer = pow(abs(warpField), 4.0) * treble * 1.5;
    finalColor += vec3(0.7, 0.9, 1.0) * edgeShimmer;

    // Soft-Knee Dynamic Range Compression (Reinhard Tone-Mapping)
    finalColor = finalColor / (finalColor + vec3(1.0));

    // TouchDesigner standard output swizzle is strictly required
    fragColor = TDOutputSwizzle(vec4(finalColor, 1.0));
}
