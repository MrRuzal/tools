import pytest
from geometry.triangle import Triangle


def test_area():
    triangle = Triangle(a=3, b=4, c=5)
    assert pytest.approx(triangle.area(), 1e-6) == 6.0


def test_is_right_triangle():
    triangle = Triangle(a=3, b=4, c=5)
    assert triangle.is_right_triangle()

    triangle = Triangle(a=2, b=3, c=4)
    assert not triangle.is_right_triangle()


def test_perimeter():
    triangle = Triangle(a=3, b=4, c=5)
    assert triangle.perimeter() == 12.0


def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(a=1, b=2, c=10)


def test_negative_sides():
    with pytest.raises(ValueError):
        Triangle(a=-1, b=2, c=3)


def test_repr():
    triangle = Triangle(a=3, b=4, c=5)
    assert repr(triangle) == "Triangle(a=3, b=4, c=5)"


def test_str():
    triangle = Triangle(a=3, b=4, c=5)
    assert str(triangle) == "Triangle with sides 3, 4, 5"
