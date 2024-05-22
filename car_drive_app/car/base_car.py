from car_drive_app.cartesians import Vector
from car_drive_app.car.turn import Turn


class BaseCar:
    """The underlying class for the Car that drives around the Track."""

    LENGTH = 40
    WIDTH = 20

    def __init__(self) -> None:
        self.position: Vector
        self.speed: float
        self.angle: float
        self.angular_velocity: float

    def reset(self) -> None:
        """Return the Car to the start point."""

        self.position = Vector(30,30)
        self.speed = 0
        self.angle = 0
        self.angular_velocity = 0

    @property
    def velocity(self) -> Vector:
        return Vector.unit_from_angle(self.angle) * self.speed

    def move(self, turn: Turn, accelerate: bool) -> None:
        """Advance the Car one frame.
        
        Rotates the Car's direction by the angle in turn and increases or 
        decreases the Car's speed according to accelerate.
        Adds the new velocity to the Car's position.
        """

        if self.speed != 0:
            self.angle += turn.value

        if accelerate:
            self.speed = min(self.speed + 0.6, 12)
        else:
            self.speed = max(self.speed - 0.4, 0)

        self.position += self.velocity

    @property
    def outline(self) -> list[Vector]:
        """Return 2D points that make up the outline of the Car."""

        length_ways = Vector.unit_from_angle(self.angle) * (self.LENGTH // 20)
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