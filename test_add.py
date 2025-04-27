import pytest
import math
from MyLib.add import add


def test_add_normal_cases():
    assert add(2, 3) == 5
    assert add(-4, 5) == 1
    assert add(0, 100) == 100
    assert add(2.5, 4) == 6.5
    assert add(1.1, 2.2) == pytest.approx(3.3)


def test_add_extreme_cases():
    assert add(1e100, 1e100) == 2e100
    assert add(-1e308, 1) == -1e308
    assert add(1e-100, 1e-100) == 2e-100
    assert add(1e308, 1e308) == float("inf")


def test_add_nan_and_inf():
    assert math.isnan(add(float("nan"), 5))
    assert add(float("inf"), 2) == float("inf")
    assert add(-float("inf"), 2) == -float("inf")


def test_add_commutativity():
    a, b = 7, 3.5
    assert add(a, b) == add(b, a)


def test_add_boolean_values():
    assert add(True, 5) == 6
    assert add(False, 10) == 10


def test_add_invalid_inputs():
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(2, None)
    with pytest.raises(TypeError):
        add([1, 2], 3)
    with pytest.raises(TypeError):
        add({}, 3)
    with pytest.raises(TypeError):
        add(3, "a")

