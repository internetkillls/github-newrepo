# Acceptance record
Each check: check_id, stage, expected value/tolerance, actual result, tool/build, artifact path/hash, timestamp, status(pass/fail/pending), limitations.
Contract: 4 faces1800x1080; exact fps/N; explicit coordinates/phase; parameter ranges; session intervals; null unknowns preserved. Offline helper also probes analytic seams/periodicity.
Source: repeated build has no owned duplicates; assets relocate; no runtime errors; same declared inputs/versions.
Render: real dimensions/fps/frame count; opaque alpha unless requested; codec/container; color/range; visible first/last transition; A-B/B-C/C-D/D-A continuity, same transport phase, calibration orientation; output quality at native resolution.
Player: decode/storage/GPU headroom on actual hardware, output routing, manual override/fallback, actual intended-duration operation. Record a short test as short, not a six-hour acceptance test.
Brand/design: approved palette/shape/motion, legibility at viewing distance, daily-theme continuity and session variation. Human visual judgment is not replaced by file hashes.
If optional tools such as ffprobe are installed, use actual media metadata. If no tool/render/player exists, keep these checks pending and return a useful handoff.
