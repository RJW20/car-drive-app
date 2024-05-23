from car_drive_app.cartesians import Vector
from car_drive_app.car.turn import Turn


class BaseCar:
    """The underlying class for the Car that drives around the Track."""

    LENGTH = 80
    WIDTH = 40
    MASS = 1
    POWER = 10
    DRAG_COEFFICIENT = 0.002
    ROLLING_COEFFICIENT = 0.06

    def __init__(self) -> None:
        self.position: Vector
        self.velocity: Vector
        self.angle: float
        self.angular_velocity: float

    def reset(self) -> None:
        """Return the Car to the start point."""

        self.position = Vector(100,400)
        self.velocity = Vector(0,0)
        self.angle = 0
        self.angular_velocity = 0

    @property
    def direction(self) -> Vector:
        """Return the unit vector in direction self.angle."""
        return Vector.unit_from_angle(self.angle)

    def move(self, turn: Turn, accelerate: bool) -> None:
        """Advance the Car one frame."""

        # Longitudinal forces
        traction = self.POWER * self.direction if accelerate else Vector(0,0)
        drag = - self.DRAG_COEFFICIENT * self.velocity.magnitude * self.velocity
        rolling = - self.ROLLING_COEFFICIENT * self.velocity

        # Adjust the position
        acceleration = (traction + drag + rolling) / self.MASS
        self.velocity += acceleration
        self.position += self.velocity

    @property
    def outline(self) -> list[Vector]:
        """Return 2D points that make up the outline of the Car."""

        length_ways = self.direction * (self.LENGTH // 20)
        width_ways = Vector.unit_from_angle(self.angle + 90) * (self.WIDTH // 10)

        front_center = self.position + 10 *  length_ways
        front = [front_center + i * width_ways for i in range(-5,6)]

        back_center = self.position - 10 * length_ways
        back = [back_center + i * width_ways for i in range(-5,6)]

        right_center = self.position + 5 * width_ways
        right = [right_center + i * length_ways for i in range(-10,11)]

        left_center = self.position - 5 * width_ways
        left = [left_center + i * length_ways for i in range(-10,11)]

        return front + back + right + left