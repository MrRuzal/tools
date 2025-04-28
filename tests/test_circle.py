import pytest
from geometry.circle import Circle


def test_area():
    circle = Circle(radius=5)
    assert pytest.approx(circle.area(), 1e-6) == 78.53981633974483


def test_perimeter():
    circle = Circle(radius=5)
    assert pytest.approx(circle.perimeter(), 1e-6) == 31.41592653589793


def test_invalid_radius():
    with pytest.raises(ValueError):
        Circle(radius=-1)


def test_repr():
    circle = Circle(radius=5)
    assert repr(circle) == "Circle(radius=5)"


def test_str():
    circle = Circle(radius=5)
    assert str(circle) == "Circle with radius 5"
