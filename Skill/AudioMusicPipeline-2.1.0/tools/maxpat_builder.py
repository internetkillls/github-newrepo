"""Cycling '74 Max/MSP 8.6 & Max for Live (.maxpat) JSON patcher builder and validator.

Constructs valid, loadable JSON patchers for Max 8.6.2 with:
- Strict JSON structure: {"patcher": {"boxes": [...], "lines": [...]}}
- Accurate inlet/outlet indices and execution coordinates
- Support for DSP objects (~), Max for Live UI objects (live.dial, live.gain~),
  and OSC/networking objects (udpreceive, oscparse)
- Validation of patch cord integrity (no dangling lines or missing box IDs)
"""

import json
from typing import Dict, Any, List, Optional, Tuple

class MaxPatcherBuilder:
    """Builder for generating Cycling '74 Max/MSP and Max for Live .maxpat files."""

    def __init__(self, title: str = "AudioMusicPipeline_Bridge"):
        self.title = title
        self.boxes: List[Dict[str, Any]] = []
        self.lines: List[Dict[str, Any]] = []
        self._box_id_counter = 1

    def add_box(
        self,
        text: str,
        maxclass: str = "newobj",
        rect: Optional[List[int]] = None,
        numinlets: int = 1,
        numoutlets: int = 1,
        varname: Optional[str] = None,
        extra_props: Optional[Dict[str, Any]] = None
    ) -> str:
        """Add an object box and return its unique ID."""
        box_id = f"obj-{self._box_id_counter}"
        self._box_id_counter += 1

        if rect is None:
            # Default staggered placement
            rect = [50, 40 * self._box_id_counter, 150, 22]

        box_def = {
            "box": {
                "id": box_id,
                "maxclass": maxclass,
                "text": text,
                "numinlets": numinlets,
                "numoutlets": numoutlets,
                "patching_rect": rect
            }
        }
        if varname:
            box_def["box"]["varname"] = varname
        if extra_props:
            box_def["box"].update(extra_props)

        self.boxes.append(box_def)
        return box_id

    def add_line(self, src_id: str, src_outlet: int, dst_id: str, dst_inlet: int):
        """Connect an outlet to an inlet via a patch cord."""
        self.lines.append({
            "patchline": {
                "source": [src_id, src_outlet],
                "destination": [dst_id, dst_inlet]
            }
        })

    def build_patcher_dict(self) -> Dict[str, Any]:
        """Construct the full Max 8 JSON dictionary."""
        return {
            "patcher": {
                "fileversion": 1,
                "appversion": {
                    "major": 8,
                    "minor": 6,
                    "revision": 2,
                    "architecture": "x64",
                    "modern": 1
                },
                "classnamespace": "box",
                "rect": [100.0, 100.0, 850.0, 650.0],
                "bglocked": 0,
                "openinpresentation": 0,
                "default_fontsize": 12.0,
                "default_fontname": "Arial",
                "gridonopen": 1,
                "gridsize": [15.0, 15.0],
                "gridsnaponopen": 1,
                "boxes": self.boxes,
                "lines": self.lines
            }
        }

    def export_json(self) -> str:
        return json.dumps(self.build_patcher_dict(), indent=2)

    def save_maxpat(self, filepath: str):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.export_json())

    @staticmethod
    def validate_maxpat(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate structural integrity of a Max patcher dictionary."""
        errors = []
        if "patcher" not in data:
            return False, ["Missing top-level 'patcher' key."]

        p = data["patcher"]
        boxes = p.get("boxes", [])
        lines = p.get("lines", [])

        box_ids = set()
        for b in boxes:
            box_obj = b.get("box", {})
            bid = box_obj.get("id")
            if not bid:
                errors.append("Box missing 'id'")
            elif bid in box_ids:
                errors.append(f"Duplicate box ID '{bid}'")
            else:
                box_ids.add(bid)

        for l in lines:
            pline = l.get("patchline", {})
            src = pline.get("source", [])
            dst = pline.get("destination", [])
            if len(src) != 2 or len(dst) != 2:
                errors.append(f"Malformed patchline: {pline}")
                continue
            if src[0] not in box_ids:
                errors.append(f"Patchline source '{src[0]}' not in boxes")
            if dst[0] not in box_ids:
                errors.append(f"Patchline destination '{dst[0]}' not in boxes")

        return len(errors) == 0, errors

    @classmethod
    def create_osc_telemetry_patch(cls, port: int = 7000) -> 'MaxPatcherBuilder':
        """Factory creating a standard OSC receiver patch for Ableton <-> TouchDesigner bridging."""
        builder = cls(title="OSC_Telemetry_Bridge")
        # 1. udpreceive
        udp = builder.add_box(f"udpreceive {port}", "newobj", [50, 40, 120, 22], numinlets=1, numoutlets=1)
        # 2. OSC route
        route = builder.add_box("route /drums /bass /synth /fx", "newobj", [50, 90, 220, 22], numinlets=1, numoutlets=5)
        builder.add_line(udp, 0, route, 0)
        # 3. Flonum monitors
        for i, name in enumerate(["drums", "bass", "synth", "fx"]):
            flonum = builder.add_box(f"flonum", "flonum", [50 + i * 80, 150, 60, 22], numinlets=1, numoutlets=2, varname=f"val_{name}")
            builder.add_line(route, i, flonum, 0)
        return builder
