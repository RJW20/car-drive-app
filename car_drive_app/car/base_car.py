from car_drive_app.cartesians import Vector


class BaseCar:
    """The underlying class for the Car that drives around the Track."""

    def __init__(self) -> None:
        self.position = Vector(0,0)
        self.angle = 0

    def outline(self) -> list[tuple[int,int]]:
        """Return 2d points that make up the outline of the Car."""

    def move(self) -> None:
        """Advance the Car one frame."""