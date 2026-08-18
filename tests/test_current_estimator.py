import math
import pytest

from tools.current_estimator import conduction_loss


def test_conduction_loss():
    assert math.isclose(conduction_loss(2.0, 0.1, 2), 0.8)


def test_zero_current():
    assert conduction_loss(0.0, 0.5) == 0.0


def test_invalid_values():
    with pytest.raises(ValueError):
        conduction_loss(-1.0, 0.1)
