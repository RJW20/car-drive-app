import math

from car_drive_app.car.wheel.base_wheel import BaseWheel
from car_drive_app.cartesians import Vector, dot


class FrontWheel(BaseWheel):
    """Front Wheel of the Car."""

    SIDE_FRICTION = 8

    def __init__(self, offset: Vector) -> None:
        super().__init__(offset)
        self._turn_angle = 0

    def reset(self) -> None:
        """Return the Wheel to stationary and pointing forward."""
        
        super().reset()
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