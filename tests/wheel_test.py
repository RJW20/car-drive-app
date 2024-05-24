from car_drive_app.car.wheel import Wheel
from car_drive_app.cartesians import Vector


def consant_forward() -> None:
    """Tests that a Wheel set in forward motion never stops."""

    wheel = Wheel()
    wheel.reset()

    wheel.rotation_speed = 1  # Moving forwards is negative
    tyre_surface_speed = wheel.rotation_speed * wheel.RADIUS
    wheel_speed = - tyre_surface_speed  # Tyre is moving backwards at the surface

    for i in range(20):

        wheel.force_exerted(Vector(-wheel_speed,0))
        tyre_surface_speed = wheel.rotation_speed * wheel.RADIUS
        wheel_speed = - tyre_surface_speed
        print(wheel_speed, wheel.rotation_speed)


def match_floor() -> None:
    """Tests that a Wheel with fixed axle with surface on a moving floor (moving in the 
    direction of the Wheel's forward axis) tends towards the rotation speed which gives 
    its surface the same speed as the floor."""

    wheel = Wheel()
    wheel.reset()

    floor_velocity = Vector(-1,0)
    wheel.rotation_speed = 0.2  # Moving forwards is negative
    tyre_surface_speed = wheel.rotation_speed * wheel.RADIUS

    for i in range(20):

        wheel.force_exerted(floor_velocity)
        tyre_surface_speed = wheel.rotation_speed * wheel.RADIUS
        print(tyre_surface_speed)


if __name__ == '__main__':
    match_floor()