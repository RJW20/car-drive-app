from __future__ import annotations
from functools import lru_cache
import math


@lru_cache
def cached_sine(theta: float) -> float:
    return math.sin(math.radians(theta))


@lru_cache
def cached_cosine(theta: float) -> float:
    return math.cos(math.radians(theta))


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
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    @property
    def magnitude(self) -> float:
        """Return the Euclidean length of the Vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    @classmethod
    def unit_from_angle(cls, angle: float) -> Vector:
        """Return the unit Vector pointing along the given angle."""
        return cls(cached_cosine(angle), cached_sine(angle))