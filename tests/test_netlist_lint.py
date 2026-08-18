import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))
from netlist_lint import lint


def test_connectivity_contract():
    assert lint(Path(__file__).parents[1] / "hardware/cad/netlist_spec.yaml") == []
