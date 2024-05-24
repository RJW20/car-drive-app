from car_drive_app.cartesians import Vector, cross


class RigidBody:
    """Represents a rectangle for which the distance between points making up
    the rectangle does not change."""

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
    
    def point_velocity(self, offset: Vector) -> Vector:
        """Return the velocity of the point at Vector offset from self.position."""
        return self.velocity + self.angular_velocity * Vector(-offset.y, offset.x)
    
    def add_force(self, force: Vector, offset: Vector) -> None:
        """Update self.forces and self.torque for a force acting at Vector offset
        from self.position."""

        self.forces += force
        self.torque += cross(offset, force)
        
    def update(self) -> None:
        """Update position and angle using self.forces and self.torque."""

        # Linear
        acceleration = self.forces / self.mass
        self.velocity += acceleration
        self.position += self.velocity
        self.forces = Vector(0,0)

        # Angular
        angular_acceleration = self.torque / self.interia
        self.angular_velocity += angular_acceleration
        self.angle += self.angular_velocity
        self.torque = 0