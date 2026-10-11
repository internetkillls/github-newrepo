---
name: studio-resolume-show
description: "Package seamless four-face visual loops and opening/warming/peak/farewell cues for Resolume Arena, including shows crossing midnight. Use for mapping, codecs, cue manifests or operator handoff."
---

# Resolume delivery and show operation

Use the actual project spec; read [references/delivery.md](references/delivery.md). This user's requirement is four continuous cube faces at 1800x1080, daily themes and 22:00-04:00. Session boundary times remain proposals until chosen. Record venue timezone explicitly; chat/computer timezone is not evidence of venue timezone.

1. Choose one master transport with logical face order/orientation. Proposed layouts: linear atlas 7200x1080 or packed grid 3600x2160. Physical processor routing is a separate calibration; record faces, clockwise order, rotations/mirroring, slices and physical destinations.
2. Render short loop banks by theme/session, not a six-hour single render by default. Supply preview, source/manifest, encoded master, face map and cue sheet. Keep a known accepted fallback.
3. Verify supported codecs against the installed Arena/Alley build. Prefer a tested DXV MOV delivery when appropriate; H.264 MP4 may serve as preview. Inspect conversion color/range and banding instead of assuming identical output.
4. Calibrate actual Advanced Output mapping in Arena; shared media phase does not establish hardware frame lock. A software atlas is not a count of physical video cables.
5. Use operator-controlled cues for the pilot. Autopilot relative duration is not a daily wall-clock schedule. An optional future controller must compute show-day identity across midnight, explicit timezone/session boundaries, restart recovery, manual override and fallback before live deployment.
6. Discover actual REST/MCP version and capabilities before automation. Do not assume an MCP can render clips, modify Advanced Output slices or configure mapping. If unavailable, produce a cue package and manual checklist.

The pipeline `cue` helper is a read-only calculation and rejects unknown timezone; it does not trigger Arena or install a scheduler. Preserve the session/theme from the preceding evening through 04:00 next day. Test before/at/after boundaries and outside-show behavior.
