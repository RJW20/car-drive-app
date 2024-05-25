from car_drive_app.cartesians import Vector, cross


class RigidBody:
    """Represents a rectangle for which the distance between points making up
    the rectangle does not change."""

    def __init__(self, dimensions: Vector, mass: float) -> None:

        # Physical properties
        self.dimensions: Vector = dimensions
        self.mass: float = mass
        self.interia: float = mass * (dimensions.x ** 2 + dimensions.y ** 2) / 12
        
        # Linear properties
        self.position: Vector
        self.velocity: Vector
        self.forces: Vector

        # Angular properties
        self.angle: float
        self.angular_velocity: float
        self.torque: float

        self.force_pairs: list[tuple[Vector, Vector]] = []

    def reset(self, position: Vector = Vector(0,0), angle: float = 0) -> None:
        """Return the RigidBody to stationary."""
            
        self.position: Vector = position
        self.velocity: Vector = Vector(0,0)
        self.forces: Vector = Vector(0,0)

        self.angle: float = angle
        self.angular_velocity: float = 0
        self.torque: float = 0
    
    def point_velocity(self, offset: Vector) -> Vector:
        """Return the velocity of the point at relative Vector offset from self.position."""
        return self.velocity + self.angular_velocity * Vector(-offset.y, offset.x)
    
    def relative_to_world(self, vector: Vector) -> Vector:
        """Convert the given Vector in the frame of the RigidBody to a Vector in the world frame."""
        return vector.rotate_by(self.angle)
    
    def world_to_relative(self, vector: Vector) -> Vector:
        """Convert the given Vector in the world frame to a Vector in the frame of the RigidBody."""
        return vector.rotate_by(-self.angle)
    
    def add_force(self, world_force: Vector, world_offset: Vector) -> None:
        """Update self.forces and self.torque for a force acting at Vector offset
        from self.position."""

        self.forces += world_force
        self.torque += cross(world_offset, world_force)

        self.force_pairs.append((world_force, self.position + world_offset))
        
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