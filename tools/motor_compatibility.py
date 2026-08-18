#!/usr/bin/env python3
"""Screen a motor profile against the reference application's voltage/current envelope."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import yaml


def load(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a mapping")
    return data


def evaluate(motor: dict, design: dict) -> dict:
    app = design["application"]
    nominal_v = float(motor["nominal_voltage_v"])
    running_a = float(motor["representative_running_current_a"])
    stall_a = float(motor["raw_stall_current_a"])
    limit_a = float(app["current_limit_a_per_channel"])
    checks = {
        "motor_nominal_voltage_within_application_envelope": float(app["supply_min_v"]) <= nominal_v <= float(app["supply_max_v"]),
        "representative_running_current_below_current_limit": running_a <= limit_a,
        "positive_stall_current": stall_a > 0,
    }
    warnings = []
    if stall_a > limit_a:
        warnings.append("Raw motor stall current exceeds the configured chopping limit; current regulation is expected to engage during stall/high-load events.")
    if running_a > 0.85 * limit_a:
        warnings.append("Representative running current is close to the configured chopping limit; validate torque margin and thermal behavior on hardware.")
    return {
        "motor": motor.get("name", "unnamed"),
        "passed": all(checks.values()),
        "checks": checks,
        "metrics": {
            "nominal_voltage_v": nominal_v,
            "representative_running_current_a": running_a,
            "raw_stall_current_a": stall_a,
            "configured_current_limit_a": limit_a,
            "stall_to_limit_ratio": stall_a / limit_a,
            "running_to_limit_ratio": running_a / limit_a,
        },
        "warnings": warnings,
        "disclaimer": "Compatibility screening is based on supplied profile values and does not replace motor/load measurement or hardware thermal validation.",
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("motor", type=Path)
    p.add_argument("--design", type=Path, default=Path("hardware/design_values.yaml"))
    args = p.parse_args()
    report = evaluate(load(args.motor), load(args.design))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
