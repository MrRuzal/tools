from abc import ABC, abstractmethod
from typing import TypeVar

ShapeType = TypeVar('ShapeType', bound='Shape')


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @staticmethod
    def calculate_area(shape: 'Shape') -> float:
        """
        Calculate the area of a shape without knowing its type at compile-time.

        Args:
            shape (Shape): Any object implementing the Shape interface.

        Returns:
            float: The area of the shape.
        """
        return shape.area()

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return f"Shape with unknown properties"
