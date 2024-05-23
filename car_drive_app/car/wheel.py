import math

from car_drive_app.cartesians import Vector, dot


class Wheel:

    RADIUS = 5
    INERTIA = 1
    FRICTION_COEFFICIENT = 0.9

    def __init__(self) -> None:
        self.rotation_speed: float

    def reset(self) -> None:
        """Return the Wheel to the stationary."""
        
        self.rotation_speed = 0
        self.turn_angle = 0

    @property
    def turn_angle(self) -> float:
        """Return the value of the Wheel relative to the Chassis."""
        return self._turn_angle
    
    @turn_angle.setter
    def turn_angle(self, value: float):
        """Set the Wheels angle relative to the Chassis.
        
        Also sets the forward and side axes (in the frame of the Car)."""

        self._turn_angle = value
        self.forward_axis = Vector.unit_from_angle(value)
        self.side_axis = Vector.unit_from_angle(value + math.pi/2)

    def friction_magnitude(self, relative_ground_velocity: Vector, axis: Vector, weight: float) -> float:
        """Return the magnitude of the frictional force that is acting along the given axis."""

        speed = dot(relative_ground_velocity, axis)

        if math.isclose(speed, 0, rel_tol=1e-07):
            return 0

        if speed > 0:
            return self.FRICTION_COEFFICIENT * weight
        else:
            return - self.FRICTION_COEFFICIENT * weight

    def force_exerted(self, ground_velocity: Vector, weight: float) -> Vector:
        """Return the force the Wheel is exerting on the Chassis given the ground velocity and weight
        that is distributed over the Wheel."""

        resultant_force = Vector(0,0)
        torque = 0

        # Sideways friction
        resultant_force += self.friction_magnitude(ground_velocity, self.side_axis, weight) * self.side_axis

        # Forwards friction
        tyre_velocity = - self.RADIUS * self.rotation_speed * self.forward_axis
        forward_magnitude = self.friction_magnitude(ground_velocity + tyre_velocity, self.forward_axis, weight)
        resultant_force += forward_magnitude * self.forward_axis
        torque += forward_magnitude * self.RADIUS
        
        self.rotation_speed += torque/self.INERTIA
        return resultant_force

        

