from __future__ import annotations
from functools import lru_cache
import math


@lru_cache
def cached_sine(theta: float) -> float:
    return math.sin(theta)


@lru_cache
def cached_cosine(theta: float) -> float:
    return math.cos(theta)


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

    @property
    def magnitude(self) -> float:
        """Return the Euclidean length of the Vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def rotate(self, angle: float) -> None:
        """Rotate the Vector in place clockwise by the given angle."""

        # Put the angle in the range 0-360 to maximise efficiency in cached trig functions
        angle = angle % 360

        x = cached_cosine(angle) * self.x - cached_sine(angle) * self.y
        y = cached_sine(angle) * self.x + cached_cosine(angle) * self.y
        self.x, self.y = x, y