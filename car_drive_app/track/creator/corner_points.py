from car_drive_app.cartesians import Vector
from car_drive_app.track.creator.control_point import ControlPoint


def corner_points(dimensions: Vector) -> list[ControlPoint]:
    """Return a list of ControlPoints that are near the 4 corners of the 2D plane with given 
    dimensions.
    
    Returns the points in anti-clockwise order (clockwise on the regular cartesian plane).
    The point closest to (0,0) is first.
    """

    offset = ControlPoint(dimensions.x // 5, dimensions.y // 5)
    return [
        offset,
        ControlPoint(offset.x, dimensions.y - offset.y),
        ControlPoint(dimensions.x - offset.x, dimensions.y - offset.y),
        ControlPoint(dimensions.x - offset.x, offset.y)
    ]