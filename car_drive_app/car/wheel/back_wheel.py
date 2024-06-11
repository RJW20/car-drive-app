import math

from car_drive_app.car.wheel.base_wheel import BaseWheel
from car_drive_app.cartesians import Vector, dot


class BackWheel(BaseWheel):
    """Back Wheel of the Car."""

    SIDE_FRICTION = 15

    def side_friction(self, slip_velocity: Vector) -> float:
        """Return the magnitude of the frictional force that is acting along self.side_axis.
        
        Modelled as self.SIDE_FRICTION times the cube root of the slipping speed in the side
        direction acting in the opposide direction.
        """

        speed = dot(slip_velocity, self.side_axis)
        
        if speed > 0:
            return - self.SIDE_FRICTION * math.sqrt(speed)
        else:
            return self.SIDE_FRICTION * math.cbrt(-1 * speed)