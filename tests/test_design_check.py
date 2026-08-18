import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))
from design_check import load_yaml, evaluate

ROOT = Path(__file__).parents[1]


def test_reference_design_passes_screening_checks():
    d = load_yaml(ROOT / "hardware/design_values.yaml")
    p = load_yaml(ROOT / "hardware/reference_profiles/drv8848.yaml")
    report = evaluate(d, p)
    assert report["passed"] is True
    assert 0.89 < report["metrics"]["configured_current_limit_a"] < 0.90
    assert report["metrics"]["worst_case_current_limit_max_a"] < 1.0
