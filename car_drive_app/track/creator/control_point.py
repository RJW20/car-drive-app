import pygame

from car_drive_app.cartesians import Vector


class ControlPoint(Vector):
    """A control point for the Catmull-Rom spline making up a Track during creation."""

    def __init__(self, x: float, y: float, radius: float = 10) -> None:
        super().__init__(x, y)
        self.radius: float = radius
        self.dragging: bool = False

    def contains(self, coordinate: Vector) -> bool:
        """Return True if the given coordinate is inside the circle this ControlPoint 
        represents."""
        return (coordinate - self).magnitude < self.radius

    def draw(self, screen: pygame.Surface) -> None:
        """Draw a white circle at self.x, self.y with radius self.radius."""
        pygame.draw.circle(screen, 'white', (self.x, self.y), self.radius)
