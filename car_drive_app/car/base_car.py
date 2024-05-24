import math

from car_drive_app.car.rigid_body import RigidBody
from car_drive_app.car.wheel import Wheel
from car_drive_app.cartesians import Vector
from car_drive_app.car.turn import Turn


class BaseCar(RigidBody):
    """The underlying class for the Car that drives around the Track."""

    LENGTH = 80
    WIDTH = 40
    MASS = 200
    POWER = 0.5
    DRAG_COEFFICIENT = 0.002

    def __init__(self) -> None:
        # Set up the Wheels
        length_offset, width_offset = 0.4 * self.LENGTH, 0.5 * self.WIDTH
        fr_wheel = Wheel(Vector(length_offset,width_offset))
        fl_wheel = Wheel(Vector(length_offset,-width_offset))
        br_wheel = Wheel(Vector(-length_offset,width_offset))
        bl_wheel = Wheel(Vector(-length_offset,-width_offset))
        self.wheels: list[Wheel] = [fr_wheel, fl_wheel, br_wheel, bl_wheel]

        super().__init__(Vector(80,40), self.MASS + 4 * self.wheels[0].MASS)

    def reset(self) -> None:
        """Return the Car to the start point."""

        super().reset()
        for wheel in self.wheels:
            wheel.reset()

    @property
    def direction(self) -> Vector:
        """Return the unit vector in direction self.angle."""
        return Vector.unit_from_angle(self.angle)
    
    @property
    def front_wheels(self) -> list[Wheel]:
        """Return the front Wheels of the Car."""
        return self.wheels[:2]
    
    @property
    def back_wheels(self) -> list[Wheel]:
        """Return the back Wheels of the Car."""
        return self.wheels[2:]

    def move(self, turn: Turn, accelerate: bool) -> None:
        """Advance the Car one frame."""

        torque_applied = 1 if accelerate else 0
        for wheel in self.front_wheels:
            self.add_force(wheel.force_exerted(-self.velocity, 0))
        for wheel in self.back_wheels:
            self.add_force(wheel.force_exerted(-self.velocity, torque_applied))

        super().update()

    @property
    def outline(self) -> list[Vector]:
        """Return 2D points that make up the outline of the Car."""

        length_ways = self.direction * (self.LENGTH // 20)
        width_ways = Vector.unit_from_angle(self.angle + math.pi/2) * (self.WIDTH // 10)

        front_center = self.position + 10 *  length_ways
        front = [front_center + i * width_ways for i in range(-5,6)]

        back_center = self.position - 10 * length_ways
        back = [back_center + i * width_ways for i in range(-5,6)]

        right_center = self.position + 5 * width_ways
        right = [right_center + i * length_ways for i in range(-10,11)]

        left_center = self.position - 5 * width_ways
        left = [left_center + i * length_ways for i in range(-10,11)]

        return front + back + right + left