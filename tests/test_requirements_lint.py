import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))
from requirements_lint import lint


def test_requirements_matrix_is_valid():
    assert lint(Path(__file__).parents[1] / "hardware/requirements.csv") == []
