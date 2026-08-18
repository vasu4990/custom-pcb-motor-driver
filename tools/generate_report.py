#!/usr/bin/env python3
"""Generate a human-readable Markdown design snapshot."""
from __future__ import annotations
import argparse
from pathlib import Path
from design_check import load_yaml, evaluate


def build_markdown(report: dict) -> str:
    m = report["metrics"]
    rows = "\n".join(f"| `{k}` | {v:.4f} |" if isinstance(v, float) else f"| `{k}` | {v} |" for k, v in m.items())
    checks = "\n".join(f"- [{'x' if ok else ' '}] `{name}`" for name, ok in report["checks"].items())
    return f"""# Automated Design Snapshot\n\n**Profile:** `{report['profile']}`  \n**Design revision:** `{report['design_revision']}`  \n**Screening result:** **{'PASS' if report['passed'] else 'FAIL'}**\n\n## Checks\n\n{checks}\n\n## Calculated metrics\n\n| Metric | Value |\n|---|---:|\n{rows}\n\n> {report['disclaimer']}\n\nThis report is generated from machine-readable design inputs. It is not measured hardware data.\n"""


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--design", type=Path, default=Path("hardware/design_values.yaml"))
    p.add_argument("--profile", type=Path, default=Path("hardware/reference_profiles/drv8848.yaml"))
    p.add_argument("--output", type=Path, default=Path("artifacts/design-report.md"))
    args = p.parse_args()
    report = evaluate(load_yaml(args.design), load_yaml(args.profile))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_markdown(report), encoding="utf-8")
    print(args.output)
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
