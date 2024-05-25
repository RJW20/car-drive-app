from car_drive_app.car.rigid_body import RigidBody
from car_drive_app.cartesians import Vector


def consant_forward() -> None:
    """Tests that a RigidBody set in forward motion never stops."""

    rb = RigidBody(Vector(20,20), 100)
    rb.reset()

    # Add one push
    rb.add_force(Vector(0,10), Vector(5,0))

    for i in range(10):

        rb.update()
        print(rb.velocity, rb.angular_velocity)


if __name__ == '__main__':
    consant_forward()