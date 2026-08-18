#!/usr/bin/env python3
"""Evaluate the reference design against the selected motor-driver profile."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import yaml
from design_model import (
    conduction_loss_w,
    hbridge_path_resistance,
    operating_voltage_margin_percent,
    regulated_current_a,
    regulated_current_range_a,
    resistor_dissipation_w,
    sense_resistor_derating_ratio,
    thermal_estimate,
)


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a mapping")
    return data


def evaluate(design: dict, profile: dict, ambient_c: float = 25.0) -> dict:
    app = design["application"]
    cs = design["current_sense"]
    resistance = profile["resistance"]
    thermal = profile["thermal"]
    supply = profile["supply"]
    motor = profile["motor"]
    regulation = profile["current_regulation"]

    path25 = hbridge_path_resistance(resistance["high_side_typ_25c_ohm"], resistance["low_side_typ_25c_ohm"])
    path85 = hbridge_path_resistance(resistance["high_side_typ_85c_ohm"], resistance["low_side_typ_85c_ohm"])
    active = int(app["simultaneous_channels"])
    expected_i = float(app["expected_continuous_current_a_per_channel"])
    limit_i = regulated_current_a(float(cs["vref_v"]), float(cs["resistor_ohm"]), float(regulation["sense_gain"]))
    limit_min_i, limit_max_i = regulated_current_range_a(float(regulation["vint_min_v"]), float(regulation["vint_max_v"]), float(cs["resistor_ohm"]), float(cs["tolerance_percent"]), float(regulation["sense_gain"]))
    expected_loss25 = conduction_loss_w(expected_i, path25, active)
    top_loss25 = conduction_loss_w(float(app["current_limit_a_per_channel"]), path25, active)
    top_loss85 = conduction_loss_w(float(app["current_limit_a_per_channel"]), path85, active)
    top_thermal25 = thermal_estimate(top_loss25, ambient_c, float(thermal["theta_ja_c_per_w"]))
    design_ambient = float(app["ambient_design_max_c"])
    hot_loss_at_limit = conduction_loss_w(limit_max_i, path85, active)
    hot_thermal = thermal_estimate(hot_loss_at_limit, design_ambient, float(thermal["theta_ja_c_per_w"]))
    sense_power = resistor_dissipation_w(float(app["current_limit_a_per_channel"]), float(cs["resistor_ohm"]))
    derating = sense_resistor_derating_ratio(sense_power, float(cs["resistor_power_rating_w"]))
    margin = operating_voltage_margin_percent(float(app["supply_max_v"]), float(supply["operating_max_v"]))

    checks = {
        "application_supply_within_profile": float(app["supply_max_v"]) <= float(supply["operating_max_v"]),
        "application_supply_below_absolute_max": float(app["supply_max_v"]) < float(supply["absolute_max_v"]),
        "pwm_within_profile": float(app["pwm_target_hz"]) <= float(profile["control"]["input_max_pwm_hz"]),
        "nominal_current_limit_within_rms_rating": limit_i <= float(motor["rms_current_per_bridge_a"]),
        "worst_case_current_limit_within_rms_rating": limit_max_i <= float(motor["rms_current_per_bridge_a"]),
        "current_limit_below_ocp_typ": limit_max_i < float(motor["overcurrent_trip_typ_a"]),
        "sense_resistor_derated_to_50_percent_or_less": derating <= 0.50,
        "rough_25c_junction_below_150c": top_thermal25.junction_c < float(thermal["junction_max_operating_c"]),
        "rough_hot_corner_junction_below_150c": hot_thermal.junction_c < float(thermal["junction_max_operating_c"]),
        "local_vm_cap_meets_datasheet_min": float(design["input_power"]["local_ceramic_uf"]) >= float(profile["external_components"]["vm_bypass_min_uf"]),
    }

    return {
        "profile": profile["profile"],
        "design_revision": design["design_revision"],
        "checks": checks,
        "passed": all(checks.values()),
        "metrics": {
            "hbridge_path_resistance_25c_ohm": path25,
            "hbridge_path_resistance_85c_ohm": path85,
            "configured_current_limit_a": limit_i,
            "worst_case_current_limit_min_a": limit_min_i,
            "worst_case_current_limit_max_a": limit_max_i,
            "expected_total_conduction_loss_25c_w": expected_loss25,
            "two_bridge_loss_at_current_limit_25c_w": top_loss25,
            "two_bridge_loss_at_current_limit_85c_w": top_loss85,
            "rough_junction_at_limit_ambient_c": ambient_c,
            "rough_junction_at_limit_c": top_thermal25.junction_c,
            "rough_hot_corner_junction_c": hot_thermal.junction_c,
            "sense_resistor_power_at_limit_w_each": sense_power,
            "sense_resistor_rating_utilization": derating,
            "operating_voltage_headroom_percent": margin,
        },
        "disclaimer": "Thermal estimate uses a datasheet JEDEC theta-JA metric and is only a screening calculation; validate on the actual PCB.",
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--design", type=Path, default=Path("hardware/design_values.yaml"))
    p.add_argument("--profile", type=Path, default=Path("hardware/reference_profiles/drv8848.yaml"))
    p.add_argument("--ambient", type=float, default=25.0)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    report = evaluate(load_yaml(args.design), load_yaml(args.profile), args.ambient)
    text = json.dumps(report, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
