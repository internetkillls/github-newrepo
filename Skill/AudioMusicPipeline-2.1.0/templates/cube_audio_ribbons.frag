// TouchDesigner GLSL Fragment Shader: 4-Sided Cube Perimeter Ribbons (v1.3.0)
// Renders continuous, mathematically closed multi-ribbon visual waves across a 7200x1080 atlas (4 faces).
// Guarantees zero corner seams (C0/C1) and 100% seamless temporal loop closure.
// Complies strictly with TouchDesigner GLSL TOP standards (TDOutputSwizzle, uTDOutputInfo).

// Canvas and loop uniforms (fed from ableton_cube_router nullCHOP 'cube_parameters')
uniform vec2 uResolution;         // Canvas resolution (e.g. 7200.0, 1080.0)
uniform float uPhase;            // Continuous phase from Ableton Link / transport [0.0 - 1.0]
uniform float uAmplitude;        // Dynamic wave height [0.005 - 0.080]
uniform float uStrokeWidth;      // Ribbon line thickness [0.002 - 0.020]
uniform float uSpatialHarmonic;  // Integer wave harmonic around 4 faces [2 - 8]
uniform float uTemporalCycles;   // Temporal bar cycles (default: 1)
uniform float uBandSpan;         // Vertical ribbon band spread [0.20 - 0.50]
uniform float uRibbonCount;      // Number of ribbons R (default: 8, bounds: 3 - 12)

// Project Color Palette: [0] = background, [1..3] = ribbon colors
uniform vec4 uPalette[4];

out vec4 fragColor;

#define PI 3.14159265358979323846
#define TWO_PI 6.28318530717958647692

void main() {
    // 1. Normalized canvas coordinates [0.0, 1.0]
    vec2 st = vUV.st;

    // 2. Linear Atlas 4-face decoding:
    // Canvas is horizontally packed: Face 0 [0..0.25], Face 1 [0.25..0.5], Face 2 [0.5..0.75], Face 3 [0.75..1.0]
    float scaledX = st.s * 4.0;
    float face = floor(scaledX);
    float u = fract(scaledX);
    float v = st.t; // Normalized vertical height [0.0 bottom, 1.0 top]

    // 3. Continuous perimeter angle around the 4-sided cube: alpha in [0, 2*PI)
    // Ensures seamless C0 and C1 continuity across all physical cube corners:
    // Face 0->1, 1->2, 2->3, and wrapping 3->0 (alpha=2*PI == alpha=0)
    float alpha = TWO_PI * (face + u) / 4.0;

    // 4. Time phase derived from Ableton Link / Clock: theta in [0, 2*PI)
    float theta = TWO_PI * fract(uPhase);

    // 5. Initialize background color
    vec3 color = (uPalette[0].a > 0.0) ? uPalette[0].rgb : vec3(0.06, 0.07, 0.10);

    float R = max(1.0, floor(uRibbonCount + 0.5));
    float harmonic = max(1.0, floor(uSpatialHarmonic + 0.5));
    float cycles = max(1.0, floor(uTemporalCycles + 0.5));
    float halfWidth = max(0.001, uStrokeWidth * 0.5);

    // Resolution determination for antialiasing:
    // Prefer TouchDesigner built-in uTDOutputInfo, fallback to uniform uResolution, fallback to 1080.0
    float resY = (uTDOutputInfo.res.w > 0.0) ? uTDOutputInfo.res.w : ((uResolution.y > 0.0) ? uResolution.y : 1080.0);
    float pixelAAStep = 1.0 / resY;

    // 6. Draw ribbons in increasing index j (source-over composite)
    int maxRibbons = int(min(R, 12.0));
    for (int j = 0; j < 12; j++) {
        if (j >= maxRibbons) break;

        float j_f = float(j);

        // Analytic Ribbon Centerline Formula:
        // v_j = 0.5 + band_span * ((j + 0.5)/R - 0.5) + amplitude * sin(harmonic * alpha + cycles * theta + 2*PI*j/R)
        float baseline = 0.5 + uBandSpan * ((j_f + 0.5) / R - 0.5);
        float wave = uAmplitude * sin(harmonic * alpha + cycles * theta + TWO_PI * j_f / R);
        float v_j = baseline + wave;

        // Anti-aliased ribbon stroke distance
        float dist = abs(v - v_j);
        float alphaMask = 1.0 - smoothstep(halfWidth - pixelAAStep, halfWidth + pixelAAStep, dist);

        // Pick ribbon color from palette cycle [1..3]
        int colorIdx = 1 + (j % 3);
        vec3 ribbonColor = (uPalette[colorIdx].a > 0.0) ? uPalette[colorIdx].rgb : vec3(0.3, 0.6, 0.9);

        // Source-over blend
        color = mix(color, ribbonColor, alphaMask);
    }

    // TouchDesigner standard output swizzle is strictly required
    fragColor = TDOutputSwizzle(vec4(color, 1.0));
}
