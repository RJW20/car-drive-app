import math

from car_drive_app.cartesians import Vector
from car_drive_app.car.turn import Turn


class BaseCar:
    """The underlying class for the Car that drives around the Track."""

    LENGTH = 80
    WIDTH = 40
    MASS = 1
    POWER = 0.5
    DRAG_COEFFICIENT = 0.002
    ROLLING_COEFFICIENT = 0.06
    WHEELS_OFFSET = 0.4 * LENGTH

    def __init__(self) -> None:
        self.position: Vector
        self.velocity: Vector
        self.orientation: float
        self.turning_angle: float
        self.turning_angular_velocity: float

    def reset(self) -> None:
        """Return the Car to the start point."""

        self.position = Vector(100,400)
        self.velocity = Vector(0,0)
        self.orientation = 0
        self.turning_angle = 0
        self.turning_angular_velocity = 0

    @property
    def direction(self) -> Vector:
        """Return the unit vector in direction self.orientation."""
        return Vector.unit_from_angle(self.orientation)

    def move(self, turn: Turn, accelerate: bool) -> None:
        """Advance the Car one frame."""

        # Acceleration
        traction = self.POWER * self.direction if accelerate else Vector(0,0)
        drag = - self.DRAG_COEFFICIENT * self.velocity.magnitude * self.velocity
        rolling = - self.ROLLING_COEFFICIENT * self.velocity
        acceleration = (traction + drag + rolling) / self.MASS
        self.velocity += acceleration

        # Turning
        self.turning_angle = max(min(self.turning_angle + turn.value, math.pi/3), -math.pi/3)
        if not self.turning_angle == 0:
            turning_radius = 2 * self.WHEELS_OFFSET / math.sin(self.turning_angle)
            self.turning_angular_velocity = self.velocity.magnitude/turning_radius
            self.velocity.rotate_by(self.turning_angular_velocity) 

        # Adjust the position and orientation
        self.position += self.velocity + self.WHEELS_OFFSET * (Vector.unit_from_angle(self.orientation + self.turning_angular_velocity) - self.direction)
        self.orientation += self.turning_angular_velocity

    @property
    def outline(self) -> list[Vector]:
        """Return 2D points that make up the outline of the Car."""

        length_ways = self.direction * (self.LENGTH // 20)
        width_ways = Vector.unit_from_angle(self.orientation + math.pi/2) * (self.WIDTH // 10)

        front_center = self.position + 10 *  length_ways
        front = [front_center + i * width_ways for i in range(-5,6)]

        back_center = self.position - 10 * length_ways
        back = [back_center + i * width_ways for i in range(-5,6)]

        right_center = self.position + 5 * width_ways
        right = [right_center + i * length_ways for i in range(-10,11)]

        left_center = self.position - 5 * width_ways
        left = [left_center + i * length_ways for i in range(-10,11)]

        return front + back + right + left