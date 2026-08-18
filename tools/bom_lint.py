#!/usr/bin/env python3
"""Lint the engineering BOM for missing selection and traceability fields."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path

REQUIRED = {"Reference", "Category", "Description", "Qty", "Selection_Status", "Notes", "MPN", "Manufacturer", "Critical"}
ALLOWED_STATUS = {"Selected", "Reference", "Application-specific", "DNP", "TBD"}


def lint(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return ["BOM is empty"]
    missing = REQUIRED - set(rows[0])
    if missing:
        return [f"missing columns: {', '.join(sorted(missing))}"]
    seen = set()
    for i, row in enumerate(rows, start=2):
        ref = row["Reference"].strip()
        if not ref:
            errors.append(f"line {i}: empty Reference")
        if ref in seen:
            errors.append(f"line {i}: duplicate Reference {ref}")
        seen.add(ref)
        if row["Selection_Status"].strip() not in ALLOWED_STATUS:
            errors.append(f"line {i}: invalid Selection_Status")
        if row["Critical"].strip().lower() not in {"yes", "no"}:
            errors.append(f"line {i}: Critical must be yes/no")
        if row["Selection_Status"].strip() == "Selected" and not row["MPN"].strip():
            errors.append(f"line {i}: selected component {ref} has no MPN")
    return errors


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("path", nargs="?", type=Path, default=Path("hardware/BOM.csv"))
    args = p.parse_args()
    errors = lint(args.path)
    if errors:
        print("BOM lint failed:")
        for e in errors:
            print(f"- {e}")
        raise SystemExit(1)
    print("BOM lint passed")


if __name__ == "__main__":
    main()
