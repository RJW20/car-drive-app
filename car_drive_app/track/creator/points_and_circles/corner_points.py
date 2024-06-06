from car_drive_app.cartesians import Vector
from car_drive_app.track.creator.points_and_circles.control_point import ControlPoint


def corner_points(dimensions: Vector, offset: int) -> list[ControlPoint]:
    """Return a list of ControlPoints that are near the 4 corners of the 2D plane with given 
    dimensions.
    
    All points will be at offset distance away from the nearest walls.
    Returns the points in anti-clockwise order (clockwise on the regular cartesian plane).
    The point closest to (0,0) is first.
    """

    offset = ControlPoint(offset, offset)
    return [
        offset,
        ControlPoint(offset.x, dimensions.y - offset.y),
        ControlPoint(dimensions.x - offset.x, dimensions.y - offset.y),
        ControlPoint(dimensions.x - offset.x, offset.y)
    ]