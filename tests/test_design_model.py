import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))
from design_model import *


def test_drv8848_reference_sense_resistor():
    assert math.isclose(sense_resistor_ohm(3.3, 1.0), 0.5, rel_tol=1e-9)
    assert math.isclose(regulated_current_a(3.3, 0.56), 0.8928571428571428, rel_tol=1e-9)
    lo, hi = regulated_current_range_a(3.13, 3.47, 0.56, 1.0)
    assert lo < 0.85 and hi < 0.95


def test_conduction_loss_two_bridges():
    assert math.isclose(conduction_loss_w(1.0, 0.9, 2), 1.8)


def test_thermal_screen():
    result = thermal_estimate(1.8, 25.0, 40.3)
    assert math.isclose(result.rise_c, 72.54)
    assert math.isclose(result.junction_c, 97.54)


def test_derating():
    assert sense_resistor_derating_ratio(0.5, 1.0) == 0.5
