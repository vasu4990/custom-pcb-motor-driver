#!/usr/bin/env python3
"""Check whether a design is eligible for a declared release stage."""
from __future__ import annotations
import argparse
from pathlib import Path
import yaml

STAGES = {
    "reference": ["reference_profile"],
    "cad-ready": ["schematic_complete", "footprint_verified", "erc_passed"],
    "fab-ready": ["schematic_complete", "footprint_verified", "erc_passed", "pcb_layout_complete", "drc_passed", "gerbers_reviewed"],
    "hardware-validated": ["fabricated", "assembly_inspected", "bench_powerup_passed", "motor_test_passed", "thermal_test_passed", "stall_test_passed"],
}


def evaluate(data: dict, stage: str) -> tuple[bool, list[str]]:
    if stage == "reference":
        missing = [] if data.get("reference_profile") else ["reference_profile"]
        return not missing, missing
    validation = data.get("validation", {})
    missing = [key for key in STAGES[stage] if not validation.get(key, False)]
    return not missing, missing


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("stage", choices=STAGES)
    p.add_argument("--design", type=Path, default=Path("hardware/design_values.yaml"))
    args = p.parse_args()
    data = yaml.safe_load(args.design.read_text(encoding="utf-8"))
    passed, missing = evaluate(data, args.stage)
    print(f"stage={args.stage} passed={str(passed).lower()}")
    if missing:
        print("missing: " + ", ".join(missing))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
