import math

from car_drive_app.cartesians import Vector, dot


class Wheel:

    RADIUS = 5
    MASS = 10
    INERTIA = MASS * RADIUS ** 2 / 2
    SIDE_FRICTION = 2
    FORWARD_FRICTION = 1

    def __init__(self, offset: Vector) -> None:
        self.offset: Vector = offset
        self.rotation_speed: float

    def reset(self) -> None:
        """Return the Wheel to stationary."""
        
        self.rotation_speed = 0
        self.turn_angle = 0

    @property
    def turn_angle(self) -> float:
        """Return the value of the Wheel relative to the Chassis."""
        return self._turn_angle
    
    @turn_angle.setter
    def turn_angle(self, value: float):
        """Set the Wheels angle relative to the Chassis.
        
        Also sets the forward and side axes (in the frame of the Car).
        """

        self._turn_angle = value
        self.forward_axis = Vector.unit_from_angle(value)
        self.side_axis = Vector.unit_from_angle(value + math.pi/2)

    def side_friction(self, slip_velocity: Vector) -> float:
        """Return the magnitude of the frictional force that is acting along self.side_axis.
        
        Modelled as self.SIDE_FRICTION times the slipping speed in the side direction acting
        in the opposide direction.
        """
        return - self.SIDE_FRICTION * dot(slip_velocity, self.side_axis)
    
    def forward_friction(self, slip_velocity: Vector) -> float:
        """Return the magnitude of the frictional force that is acting along self.forward_axis.
        
        Modelled as self.FORWARD_FRICTION times the slipping speed in the forward direction
        acting in the opposite direction.
        """

        return - self.FORWARD_FRICTION * dot(slip_velocity, self.forward_axis)

    def force_exerted(self, ground_velocity: Vector, torque_applied: float) -> Vector:
        """Return the force the Wheel is exerting on the Chassis given the ground velocity and the 
        torque applied (braking or accelerating)."""

        resultant_force = Vector(0,0)
        torque = torque_applied

        # Calculate which way the tyre is slipping
        tyre_surface_velocity = self.RADIUS * self.rotation_speed * self.forward_axis
        slip_velocity = tyre_surface_velocity - ground_velocity

        # Sideways friction
        resultant_force += self.side_friction(slip_velocity) * self.side_axis

        # Forwards friction
        forward_magnitude = self.forward_friction(slip_velocity)
        resultant_force += forward_magnitude * self.forward_axis
        torque += forward_magnitude * self.RADIUS
        
        self.rotation_speed += torque/self.INERTIA
        return resultant_force

        

