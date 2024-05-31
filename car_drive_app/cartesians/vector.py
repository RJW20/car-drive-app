from __future__ import annotations
import math


class Vector:
    """2D Vector."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: float) -> Vector:
        return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other: float) -> Vector:
        return Vector(self.x * other, self.y * other)
    
    def __truediv__(self, other: float) -> Vector:
        return Vector(self.x / other, self.y / other)
    
    def __rtruediv__(self, other: float) -> Vector:
        return Vector(self.x / other, self.y / other)
    
    def __floordiv__(self, other: float) -> Vector:
        return Vector(self.x // other, self.y // other)
    
    def __rfloordiv__(self, other: float) -> Vector:
        return Vector(self.x // other, self.y // other)
    
    def __eq__(self, other: Vector) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    @property
    def magnitude(self) -> float:
        """Return the Euclidean length of the Vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    @classmethod
    def unit_from_angle(cls, angle: float) -> Vector:
        """Return the unit Vector pointing along the given angle."""
        return cls(math.cos(angle), math.sin(angle))
    
    def rotate_by(self, angle: float) -> Vector:
        """Return the Vector that is produced by the clockwise rotation by the given angle."""

        x = math.cos(angle) * self.x - math.sin(angle) * self.y
        y = math.sin(angle) * self.x + math.cos(angle) * self.y
        return Vector(x, y)


def dot(vec1: Vector, vec2: Vector) -> float:
    """Compute the standard dot product between the two given Vectors."""
    return vec1.x * vec2.x + vec1.y * vec2.y

def cross(vec1: Vector, vec2: Vector) -> float:
    """Compute the 2D cross product between the two given Vectors."""
    return vec1.x * vec2.y - vec1.y * vec2.x