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
    POWER = 200
    DRAG_COEFFICIENT = 0.8

    def __init__(self) -> None:
        # Set up the Wheels
        length_offset, width_offset = 0.4 * self.LENGTH, 0.5 * self.WIDTH
        fr_wheel = Wheel(Vector(length_offset,width_offset))
        fl_wheel = Wheel(Vector(length_offset,-width_offset))
        br_wheel = Wheel(Vector(-length_offset,width_offset))
        bl_wheel = Wheel(Vector(-length_offset,-width_offset))
        self.wheels: list[Wheel] = [fr_wheel, fl_wheel, br_wheel, bl_wheel]

        super().__init__(Vector(80,40), self.MASS + 4 * self.wheels[0].MASS)

    def reset(self, position: Vector = Vector(0,0), angle: float = 0) -> None:
        """Return the Car to the start point."""

        super().reset(position, angle)
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

        torque_applied = - self.POWER / 2  if accelerate else 0
        for wheel in self.front_wheels:
            wheel.turn_angle = max(min(wheel.turn_angle + turn.value, math.pi/3), -math.pi/3)
            world_wheel_velocity = self.point_velocity(wheel.offset)            
            relative_wheel_velocity = self.world_to_relative(world_wheel_velocity)
            relative_wheel_force = wheel.force_exerted(-1 * relative_wheel_velocity, 0)
            world_wheel_force = self.relative_to_world(relative_wheel_force)
            world_wheel_offset = self.relative_to_world(wheel.offset)
            self.add_force(world_wheel_force, world_wheel_offset)
        for wheel in self.back_wheels:
            world_wheel_velocity = self.point_velocity(wheel.offset)            
            relative_wheel_velocity = self.world_to_relative(world_wheel_velocity)
            relative_wheel_force = wheel.force_exerted(-1 * relative_wheel_velocity, torque_applied)
            world_wheel_force = self.relative_to_world(relative_wheel_force)
            world_wheel_offset = self.relative_to_world(wheel.offset)
            self.add_force(world_wheel_force, world_wheel_offset)

        drag = - self.DRAG_COEFFICIENT * self.velocity.magnitude * self.velocity
        self.add_force(drag, Vector(0,0))

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