#!/usr/bin/env python3
"""Simple conduction-loss sanity checker for a motor-driver concept.

This is intentionally conservative and incomplete: it does not model switching
loss, thermal impedance, current recirculation, PCB heating, or transient load.
Use the selected driver's datasheet for final design work.
"""

import argparse


def conduction_loss(current_a: float, rds_on_ohm: float, channels: int = 1) -> float:
    if current_a < 0 or rds_on_ohm < 0 or channels < 1:
        raise ValueError("current and resistance must be non-negative; channels >= 1")
    return (current_a ** 2) * rds_on_ohm * channels


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--current", type=float, required=True, help="RMS/representative channel current in A")
    parser.add_argument("--rds-on", type=float, required=True, help="Effective conduction resistance in ohms")
    parser.add_argument("--channels", type=int, default=1, help="Simultaneously active channels")
    args = parser.parse_args()
    watts = conduction_loss(args.current, args.rds_on, args.channels)
    print(f"Estimated conduction loss: {watts:.3f} W")
    print("Not included: switching loss, transient/stall behavior, PCB thermal resistance, ambient temperature.")


if __name__ == "__main__":
    main()
