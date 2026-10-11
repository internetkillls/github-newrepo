# Studio cube perimeter ribbons v1
Independently authored neutral analytic recipe. For face i, u in[0,1], alpha=2*pi*(i+u)/4. For frame f, theta=2*pi*f/N.
For ribbon j in0..R-1:
v_j=0.5+band_span*((j+0.5)/R-0.5)+amplitude*sin(spatial_harmonic*alpha+temporal_cycles*theta+2*pi*j/R).
Stroke is centered on v_j with thickness stroke_width measured as a fraction of face height. Draw ribbons in increasing j, source-over, opaque background=palette[0], ribbon color=palette[1+j%(len(palette)-1)].
Integer spatial_harmonic/temporal_cycles close spatial/temporal periods. Endpoint invariants are analytical; crop/packing/orientation and rasterization still need rendered checks. Top/bottom safe margin0.08 requires band_span/2+amplitude+stroke_width/2<=0.42.
Pilot bounds: R3..12, band_span0.2..0.6, amplitude0.01..0.08, stroke_width0.002..0.02, spatial_harmonic2..8 integer, temporal_cycles1..3 integer. Stylization such as bloom/3D lighting/feedback creates a declared rendition/revision.
No simulation warmup or random inputs for this recipe; seed is recorded for future variants but does not affect this v1 field. Export f=0..N-1, test f=N against0 without exporting the duplicate endpoint. Spatial phase samples at exact joins must agree including D->A. A visual loop still needs playback QA.
