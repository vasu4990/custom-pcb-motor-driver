#!/usr/bin/env python3
"""Lint requirements traceability for unique IDs and valid evidence states."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path

REQUIRED = {"ID", "Category", "Requirement", "Verification", "Status", "Evidence"}
ALLOWED_STATUS = {"planned", "verified-by-model", "verified-by-contract", "verified-by-policy", "verified-by-hardware"}


def lint(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return ["requirements matrix is empty"]
    missing = REQUIRED - set(rows[0])
    if missing:
        return ["missing columns: " + ", ".join(sorted(missing))]
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        rid = row["ID"].strip()
        if not rid:
            errors.append(f"line {line}: empty requirement ID")
        elif rid in seen:
            errors.append(f"line {line}: duplicate requirement ID {rid}")
        seen.add(rid)
        if row["Status"].strip() not in ALLOWED_STATUS:
            errors.append(f"line {line}: invalid status {row['Status']!r}")
        if not row["Verification"].strip():
            errors.append(f"line {line}: missing verification method")
        if not row["Evidence"].strip():
            errors.append(f"line {line}: missing evidence/reference path")
    return errors


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("path", nargs="?", type=Path, default=Path("hardware/requirements.csv"))
    args = p.parse_args()
    errors = lint(args.path)
    if errors:
        print("requirements lint failed:")
        for error in errors:
            print("-", error)
        raise SystemExit(1)
    print("requirements traceability passed")


if __name__ == "__main__":
    main()
