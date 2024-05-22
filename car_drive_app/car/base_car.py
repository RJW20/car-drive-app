from car_drive_app.cartesians import Vector
from car_drive_app.car.turn import Turn


class BaseCar:
    """The underlying class for the Car that drives around the Track."""

    def __init__(self) -> None:
        self.position = Vector(30,30)
        self.angle = 0
        self.speed = 0

    @property
    def velocity(self) -> Vector:
        return Vector.unit_from_angle(self.angle) * self.speed

    def move(self, turn: Turn, accelerate: bool) -> None:
        """Advance the Car one frame.
        
        Rotates the Car's direction by the angle in turn and increases or 
        decreases the Car's speed according to accelerate.
        Adds the new velocity to the Car's position.
        """

        self.angle += turn.value

        if accelerate:
            self.speed = min(self.speed + 1, 10)
        else:
            self.speed = max(self.speed - 1, 0)

        self.position += self.velocity

    def outline(self) -> list[tuple[int,int]]:
        """Return 2d points that make up the outline of the Car."""