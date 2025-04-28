import pytest
from geometry.base import Shape
from geometry.circle import Circle
from geometry.triangle import Triangle


def test_calculate_area():
    circle = Circle(radius=5)
    triangle = Triangle(a=3, b=4, c=5)

    assert (
        pytest.approx(Shape.calculate_area(circle), 1e-6) == 78.53981633974483
    )
    assert pytest.approx(Shape.calculate_area(triangle), 1e-6) == 6.0


def test_abstract_class():
    with pytest.raises(TypeError):
        Shape()
