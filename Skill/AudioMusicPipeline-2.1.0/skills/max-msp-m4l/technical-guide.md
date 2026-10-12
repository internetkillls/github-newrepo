# Technical Guide: Max/MSP & Max for Live

## JSON Patcher Format Specifications
- Root dictionary MUST contain `"patcher"` object.
- Patcher version: `"fileversion": 1`.
- Box coordinates: `"patching_rect": [x, y, width, height]`.
- Max class names must match Cycling '74 object dictionary.
