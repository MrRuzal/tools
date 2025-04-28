import pytest
from geometry.rectangle import Rectangle


def test_area():
    rectangle = Rectangle(width=4, height=6)
    assert rectangle.area() == 24.0


def test_perimeter():
    rectangle = Rectangle(width=4, height=6)
    assert rectangle.perimeter() == 20.0


def test_invalid_dimensions():
    with pytest.raises(ValueError):
        Rectangle(width=-1, height=5)

    with pytest.raises(ValueError):
        Rectangle(width=5, height=-1)


def test_repr():
    rectangle = Rectangle(width=4, height=6)
    assert repr(rectangle) == "Rectangle(width=4, height=6)"


def test_str():
    rectangle = Rectangle(width=4, height=6)
    assert str(rectangle) == "Rectangle with width 4 and height 6"
