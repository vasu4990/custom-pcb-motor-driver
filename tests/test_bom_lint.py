import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))
from bom_lint import lint


def test_bom_is_structurally_valid():
    assert lint(Path(__file__).parents[1] / "hardware/BOM.csv") == []
