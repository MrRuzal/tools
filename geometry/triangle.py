import math
from .base import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = sorted([a, b, c])
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("The sides do not form a valid triangle.")
        if min(sides) <= 0:
            raise ValueError("All sides must be positive.")
        self.a, self.b, self.c = sides

    def area(self) -> float:
        """Calculate the area of the triangle using Heron's formula."""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self) -> bool:
        """Check if the triangle is a right triangle."""
        return math.isclose(self.a**2 + self.b**2, self.c**2)

    def perimeter(self) -> float:
        """Calculate the perimeter of the triangle."""
        return self.a + self.b + self.c

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

    def __str__(self):
        return f"Triangle with sides {self.a}, {self.b}, {self.c}"
