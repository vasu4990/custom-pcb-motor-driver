import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))
from motor_compatibility import load, evaluate

ROOT = Path(__file__).parents[1]


def test_example_motor_profile_screens_cleanly_with_current_limit_warning():
    report = evaluate(
        load(ROOT / "examples/motor_profile_small_gearmotor.yaml"),
        load(ROOT / "hardware/design_values.yaml"),
    )
    assert report["passed"] is True
    assert report["metrics"]["stall_to_limit_ratio"] > 1.0
    assert report["warnings"]
