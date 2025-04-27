import pytest
import math
from MyLib.multiply import multiply

def test_multiply_normal_cases():
    assert multiply(2, 3) == 6
    assert multiply(-4, 5) == -20
    assert multiply(0, 100) == 0
    assert multiply(2.5, 4) == 10.0
    assert multiply(1.1, 2.2) == pytest.approx(2.42)


def test_multiply_extreme_cases():
    assert multiply(1e100, 1e100) == 1e200
    assert multiply(-1e308, 1) == -1e308
    assert multiply(1e-100, 1e-100) == 1e-200
    assert multiply(1e308, 10) == float("inf")


def test_multiply_nan_and_inf():
    assert math.isnan(multiply(float("nan"), 5))
    assert multiply(float("inf"), 2) == float("inf")
    assert multiply(-0.0, 5) == -0.0


def test_multiply_commutativity():
    a, b = 7, 3.5
    assert multiply(a, b) == multiply(b, a)


def test_multiply_boolean_values():
    assert multiply(True, 5) == 5
    assert multiply(False, 10) == 0


def test_multiply_invalid_inputs():
    with pytest.raises(TypeError):
        multiply("2", 3)
    with pytest.raises(TypeError):
        multiply(2, None)
    with pytest.raises(TypeError):
        multiply([1, 2], 3)
    with pytest.raises(TypeError):
        multiply({}, 3)
    with pytest.raises(TypeError):
        multiply(3, "a")

