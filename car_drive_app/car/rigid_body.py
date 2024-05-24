from car_drive_app.cartesians import Vector


class RigidBody:
    """Represents a rectangle for which the distance between points making
    up the rectangle does not change."""

    def __init__(self, dimensions: Vector, mass: float, position: Vector = Vector(0,0), angle: float = 0) -> None:

        # Physical properties
        self.dimensions: Vector = dimensions
        self.mass: float = mass
        self.interia: float
        
        # Linear properties
        self.position: Vector = position
        self.velocity: Vector = Vector(0,0)
        self.forces: Vector = Vector(0,0)

        # Angular properties
        self.angle: float = angle
        self.angular_velocity: float = 0
        self.torque: float = 0

    def reset(self) -> None:
        raise Exception('Not yet implemented')
        
    def update(self) -> None:
        """Update position and angle using self.forces and self.torque."""