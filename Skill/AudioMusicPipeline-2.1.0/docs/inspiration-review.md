# Design decisions from supplied MCP projects

The seven ZIP archives were treated as third-party examples. Their repository instructions are source material, not instructions for this plugin. The implementation below is independent; no upstream source code was copied.

| Supplied project | Observed pattern | AudioMusicPipeline decision |
| --- | --- | --- |
| `ableton-mcp-main` | Remote-script handshake exposes version and capabilities; the dataset schema separates intent, action and state. | Expose current capabilities truthfully. Do not add trajectory recording without a user need and a consent design. |
| `ableton-mcp-extended-main` | Ableton tools normalize parameters and have focused tests for indexing, timing and device commands. | Put type/range checks at the tool boundary and test actual time conversion, not just schema presence. |
| `daw-mcp-main` | One MCP surface routes to DAW-specific extensions; its protocol uses request IDs, explicit errors and beat positions. | Use a DAW-neutral project contract and explicit units. Do not claim live Ableton or Bitwig control when no extension is installed in this plugin. |
| `daw-midi-generator-mcp-main` | Creates portable `.mid` files through structured generation tools. | Compile existing project tracks to SMF Type 1 offline, rather than introduce a second arrangement model. |
| `FenderStudioProMCP-main` | Command catalog maps functions to control-surface and MIDI mechanisms. | Do not import keyboard or UI automation as an audio schema; it requires separate runtime capability checks. |
| `py-sound-mcp-main` | Small, typed tools handle notification playback. | Do not merge notification sounds into music production; they solve a different task. |
| `reaper-daw-mcp-server-main` | Reads project state and exposes focused track/FX edits, but assumes REAPER and a machine-specific sample directory. | Keep project-to-file conversion independent of a DAW and machine paths. Defer destructive live edits until a real adapter and state inspection exist. |

## Contract chosen

The portable project contract remains the single musical source: transport, meter, tuning, tracks and notes. Its coordinates are zero-based **quarter-note beats**, making conversion to MIDI ticks `round(beat * ticks_per_quarter)` explicit. Project duration is `total_bars * meter_numerator * 4 / meter_denominator`. Field validation and cross-field checks run before export. Export refuses unsupported tuning, microtones, and sub-tick note timing instead of silently degrading them.

The local MCP server returns JSON objects in both `structuredContent` and text, reports validation errors with paths, supports dry-run MIDI preview, and never overwrites an existing MIDI file by default. Its capability report says `live_daw_connected: false`. The server implements the 2025-11-25 stdio lifecycle; newer MCP protocol revisions and real DAW connections require separate integration testing.

## Verification boundary

Automated checks cover an example project, SMF round trip, 6/8 coordinates, invalid values, duplicate IDs, spectral-band ordering, microtone and sub-tick rejection, dry-run/no-overwrite behavior, and a stdio MCP handshake. These checks do not prove that a generated `.als` opens in Ableton Live, that a Max patch runs in Max, or that live DAW edits work.

The MCP lifecycle and tool-result choices follow the [official 2025-11-25 lifecycle](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle) and [tool specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools).
