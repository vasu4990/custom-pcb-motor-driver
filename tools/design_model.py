"""Pure calculation helpers for the motor-driver reference design.

These functions are intentionally transparent and unit-testable. They are
engineering sanity checks, not a substitute for the semiconductor datasheet,
PCB field solver, or bench measurements.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class ThermalEstimate:
    power_w: float
    rise_c: float
    junction_c: float


def require_positive(name: str, value: float) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be > 0")


def hbridge_path_resistance(high_side_ohm: float, low_side_ohm: float) -> float:
    require_positive("high_side_ohm", high_side_ohm)
    require_positive("low_side_ohm", low_side_ohm)
    return high_side_ohm + low_side_ohm


def conduction_loss_w(current_rms_a: float, path_resistance_ohm: float, active_bridges: int = 1) -> float:
    if current_rms_a < 0:
        raise ValueError("current_rms_a must be >= 0")
    require_positive("path_resistance_ohm", path_resistance_ohm)
    if active_bridges < 1:
        raise ValueError("active_bridges must be >= 1")
    return current_rms_a**2 * path_resistance_ohm * active_bridges


def sense_resistor_ohm(vref_v: float, regulated_current_a: float, gain: float = 6.6) -> float:
    require_positive("vref_v", vref_v)
    require_positive("regulated_current_a", regulated_current_a)
    require_positive("gain", gain)
    return vref_v / (gain * regulated_current_a)


def regulated_current_a(vref_v: float, sense_resistor_ohm_value: float, gain: float = 6.6) -> float:
    require_positive("vref_v", vref_v)
    require_positive("sense_resistor_ohm", sense_resistor_ohm_value)
    require_positive("gain", gain)
    return vref_v / (gain * sense_resistor_ohm_value)


def resistor_dissipation_w(current_rms_a: float, resistance_ohm: float) -> float:
    if current_rms_a < 0:
        raise ValueError("current_rms_a must be >= 0")
    require_positive("resistance_ohm", resistance_ohm)
    return current_rms_a**2 * resistance_ohm


def thermal_estimate(power_w: float, ambient_c: float, theta_ja_c_per_w: float) -> ThermalEstimate:
    if power_w < 0:
        raise ValueError("power_w must be >= 0")
    require_positive("theta_ja_c_per_w", theta_ja_c_per_w)
    rise = power_w * theta_ja_c_per_w
    return ThermalEstimate(power_w=power_w, rise_c=rise, junction_c=ambient_c + rise)


def operating_voltage_margin_percent(max_application_v: float, recommended_max_v: float) -> float:
    require_positive("max_application_v", max_application_v)
    require_positive("recommended_max_v", recommended_max_v)
    return (recommended_max_v - max_application_v) / recommended_max_v * 100.0


def sense_resistor_derating_ratio(power_dissipation_w: float, resistor_rating_w: float) -> float:
    if power_dissipation_w < 0:
        raise ValueError("power_dissipation_w must be >= 0")
    require_positive("resistor_rating_w", resistor_rating_w)
    return power_dissipation_w / resistor_rating_w


def regulated_current_range_a(vref_min_v: float, vref_max_v: float, resistor_nom_ohm: float, resistor_tolerance_percent: float, gain: float = 6.6) -> tuple[float, float]:
    require_positive("vref_min_v", vref_min_v)
    require_positive("vref_max_v", vref_max_v)
    require_positive("resistor_nom_ohm", resistor_nom_ohm)
    if vref_max_v < vref_min_v:
        raise ValueError("vref_max_v must be >= vref_min_v")
    if not 0 <= resistor_tolerance_percent < 100:
        raise ValueError("resistor_tolerance_percent must be in [0, 100)")
    tol = resistor_tolerance_percent / 100.0
    r_min = resistor_nom_ohm * (1.0 - tol)
    r_max = resistor_nom_ohm * (1.0 + tol)
    return (
        regulated_current_a(vref_min_v, r_max, gain),
        regulated_current_a(vref_max_v, r_min, gain),
    )


def capacitor_droop_v(delta_current_a: float, duration_s: float, capacitance_f: float) -> float:
    if delta_current_a < 0 or duration_s < 0:
        raise ValueError("delta_current_a and duration_s must be >= 0")
    require_positive("capacitance_f", capacitance_f)
    return delta_current_a * duration_s / capacitance_f
