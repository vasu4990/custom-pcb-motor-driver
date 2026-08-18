#!/usr/bin/env python3
"""Validate the EDA-independent connectivity contract before/after CAD capture."""
from __future__ import annotations
import argparse
from pathlib import Path
import yaml

REQUIRED_NETS = {
    "VM", "GND", "AIN1", "AIN2", "BIN1", "BIN2", "nSLEEP", "nFAULT", "VREF",
    "AOUT1", "AOUT2", "BOUT1", "BOUT2", "AISEN", "BISEN", "VINT"
}


def lint(path: Path) -> list[str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    nets = data.get("nets", {})
    missing = REQUIRED_NETS - set(nets)
    if missing:
        errors.append("missing nets: " + ", ".join(sorted(missing)))
    for net, cfg in nets.items():
        endpoints = cfg.get("endpoints", []) if isinstance(cfg, dict) else []
        if len(endpoints) < 2 and net not in {"nFAULT"}:
            errors.append(f"{net}: expected >=2 endpoints")
    return errors


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("path", nargs="?", type=Path, default=Path("hardware/cad/netlist_spec.yaml"))
    args = p.parse_args()
    errors = lint(args.path)
    if errors:
        for e in errors:
            print(e)
        raise SystemExit(1)
    print("netlist contract passed")


if __name__ == "__main__":
    main()
