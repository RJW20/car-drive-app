import math

import pygame

from car_drive_app.cartesians import Vector


class ControlPoint(Vector):
    """A control point for making a Track during creation.

    turn_radius is the distance from the point to the center of the track turning around it.
    orientation is -1 (anti-clockwise) or 1 (clockwise).
    """

    def __init__(self, x: float, y: float, radius: float = 10) -> None:
        super().__init__(x, y)
        self.turn_radius: int = 120
        self.orientation: int = -1

        self.radius: float = radius
        self.dragging: bool = False
        self.selected: bool = False

    def turning_point_at(self, angle: float) -> Vector:
        """Return the point at the polar coordinate (self.turn_radius, angle) from self."""
        return self + self.turn_radius * Vector.unit_from_angle(angle)
    
    def tangent_at(self, angle: float) -> Vector:
        """Return the tangent to the circle at the polar coordinate (self.turn_radius, angle) from self.
        
        The tangent points in the direction corresponding to self.orientation.
        """
        return Vector.unit_from_angle((angle + math.pi/2)) * self.orientation

    def contains(self, coordinate: Vector) -> bool:
        """Return True if the given coordinate is inside the circle this ControlPoint 
        represents."""
        return (coordinate - self).magnitude < self.radius

    def draw(self, screen: pygame.Surface) -> None:
        """Draw a white circle at self.x, self.y with radius self.radius."""

        if not self.selected:
            pygame.draw.circle(screen, 'white', (self.x, self.y), self.radius)
        else:
            pygame.draw.circle(screen, 'black', (self.x, self.y), self.radius)
