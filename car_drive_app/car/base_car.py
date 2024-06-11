import math

from car_drive_app.car.rigid_body import RigidBody
from car_drive_app.car.wheel import BaseWheel, FrontWheel, BackWheel
from car_drive_app.cartesians import Vector
from car_drive_app.car.acceleration import Acceleration


class BaseCar(RigidBody):
    """The underlying class for the Car that drives around the Track."""

    LENGTH = 80
    WIDTH = 40
    MASS = 200
    POWER = 600
    DRAG_COEFFICIENT = 0.8

    def __init__(self) -> None:

        # Set up the Wheels
        length_offset, width_offset = 0.4 * self.LENGTH, 0.5 * self.WIDTH
        self.fr_wheel = FrontWheel(Vector(length_offset,width_offset))
        self.fl_wheel = FrontWheel(Vector(length_offset,-width_offset))
        self.br_wheel = BackWheel(Vector(-length_offset,width_offset))
        self.bl_wheel = BackWheel(Vector(-length_offset,-width_offset))

        # Set up the RigidBody
        super().__init__(Vector(80,40), self.MASS + 4 * self.wheels[0].MASS)

    def reset(self, position: Vector = Vector(100,100), angle: float = 0) -> None:
        """Return the Car to the given start point."""

        super().reset(position, angle)
        for wheel in self.wheels:
            wheel.reset()

    @property
    def direction(self) -> Vector:
        """Return the unit vector in direction self.angle."""
        return Vector.unit_from_angle(self.angle)
    
    @property
    def front_wheels(self) -> list[FrontWheel]:
        """Return the front Wheels of the Car."""
        return [self.fr_wheel, self.fl_wheel]
    
    @property
    def back_wheels(self) -> list[BackWheel]:
        """Return the back Wheels of the Car."""
        return [self.br_wheel, self.bl_wheel]
    
    @property
    def wheels(self) -> list[BaseWheel]:
        """Return the Wheels of the Car."""
        return self.front_wheels + self.back_wheels

    def move(self, turn_angle: float, acceleration: Acceleration) -> None:
        """Advance the Car one frame."""

        torque_applied = self.POWER * acceleration.value
        for wheel in self.front_wheels:
            wheel.turn_angle = turn_angle
            world_wheel_offset = self.relative_to_world(wheel.offset)
            world_wheel_velocity = self.point_velocity(world_wheel_offset)            
            relative_wheel_velocity = self.world_to_relative(world_wheel_velocity)
            relative_wheel_force = wheel.force_exerted(-1 * relative_wheel_velocity, 0)
            world_wheel_force = self.relative_to_world(relative_wheel_force)
            self.add_force(world_wheel_force, world_wheel_offset)
        for wheel in self.back_wheels:
            world_wheel_offset = self.relative_to_world(wheel.offset)
            world_wheel_velocity = self.point_velocity(world_wheel_offset)           
            relative_wheel_velocity = self.world_to_relative(world_wheel_velocity)
            relative_wheel_force = wheel.force_exerted(-1 * relative_wheel_velocity, torque_applied)
            world_wheel_force = self.relative_to_world(relative_wheel_force)
            self.add_force(world_wheel_force, world_wheel_offset)

        drag = - self.DRAG_COEFFICIENT * self.velocity.magnitude * self.velocity
        self.add_force(drag, Vector(0,0))

        super().update()

        for wheel in self.front_wheels:
            wheel.turn_angle *= 0.95

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