from car_drive_app.cartesians import Vector
from car_drive_app.car.turn import Turn


class BaseCar:
    """The underlying class for the Car that drives around the Track."""

    def __init__(self) -> None:
        self.position = Vector(0,0)
        self.direction = Vector(1,0)
        self.speed = 0

    @property
    def velocity(self) -> Vector:
        return self.direction * self.speed

    def move(self, turn: Turn, accelerate: bool) -> None:
        """Advance the Car one frame.
        
        Rotates the Car's direction by the angle in turn and increases or 
        decreases the Car's speed according to accelerate.
        Adds the new velocity to the Car's position.
        """

        if not turn == Turn.STRAIGHT:
            self.direction.rotate_by(turn.value)

        if accelerate:
            self.speed = min(self.speed + 1, 10)
        else:
            self.speed = max(self.speed - 1, 0)

        self.position += self.velocity

    def outline(self) -> list[tuple[int,int]]:
        """Return 2d points that make up the outline of the Car."""