import sys
from pathlib import Path
import yaml
sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))
from release_gate import evaluate

ROOT = Path(__file__).parents[1]


def test_reference_stage_passes_but_fab_ready_does_not():
    data = yaml.safe_load((ROOT / "hardware/design_values.yaml").read_text())
    assert evaluate(data, "reference")[0] is True
    assert evaluate(data, "fab-ready")[0] is False
