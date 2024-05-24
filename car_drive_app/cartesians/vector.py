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
    
    def rotate_by(self, angle: float) -> Vector:
        """Return the Vector that is produced by the clockwise rotation by the given angle."""

        # Put the angle in the range 0-2pi to maximise efficiency in cached trig functions
        angle = angle % (2 * math.pi)

        x = cached_cosine(angle) * self.x - cached_sine(angle) * self.y
        y = cached_sine(angle) * self.x + cached_cosine(angle) * self.y
        return Vector(self.x, self.y)


def dot(vec1: Vector, vec2: Vector) -> float:
    """Compute the standard dot product between the two given Vectors."""
    return vec1.x * vec2.x + vec1.y * vec2.y

def cross(vec1: Vector, vec2: Vector) -> float:
    """Compute the 2D cross product between the two given Vectors."""
    return vec1.x * vec2.y - vec1.y * vec2.x