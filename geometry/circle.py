import math
from .base import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __str__(self):
        return f"Circle with radius {self.radius}"
