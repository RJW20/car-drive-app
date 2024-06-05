from car_drive_app.cartesians import Vector


class Gate:
    """Gates that section the Track.
    
    index is the index of the point in Track.center_line.
    direction is a Vector pointing towards the next point in Track.center_line."""

    def __init__(self, index: int, direction: Vector) -> None:
        self.index: int = index
        self.direction: Vector = direction/direction.magnitude