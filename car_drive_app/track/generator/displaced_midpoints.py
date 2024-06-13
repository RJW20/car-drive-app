import random
import math

from car_drive_app.cartesians import Vector


def midpoint(vec1: Vector, vec2: Vector) -> Vector:
    """Return the midpoint of two Vectors."""
    return (vec1 + vec2) / 2


def separation(vec1: Vector, vec2: Vector) -> Vector:
    """Return the separation length between two Vectors."""
    return (vec1 - vec2).magnitude


def displacement_vector(direction: Vector, severity: float, max_length: float) -> Vector:
    """Return a displacement Vector with given severity.
    
    Points in a direction -60 to -120 degrees from the given direction Vector (always
    points left).
    Length tends towards max_length given as severity gets closer to 0.
    """

    orientation = direction.angle - random.uniform(math.pi/3, 2 * math.pi/3)
    length = max_length * random.random() ** severity
    return Vector.unit_from_angle(orientation) * length


def displaced_midpoints(
    points: list[Vector],
    severity: float,
    required_separation: float,
) -> list[Vector]:
    """Return a list of points containing the input points as well as points that
    are the result of finding the midpoint between consecutive points and randomly
    displacing it.
    
    points should form a closed loop, but the returned points won't (last point will
    be omitted).
    The displacement lengths tend to increase as the severity gets closer to 0, always
    having the value of 1/3 the separation between the consecutive points there.
    If the distance between two consecutive points is not greater than the required_separtion,
    no midpoint will be added between them.
    """

    points_and_disp_mids = []

    N = len(points)
    for i, point in enumerate(points[:-1]):
        next_point = points[(i+1)%N]
        m_p = midpoint(point, next_point)
        if (sep := separation(point, next_point)) > required_separation:
            displacement = displacement_vector(next_point - point, severity, sep / 3)
            points_and_disp_mids.extend([point, m_p + displacement])
        else:
            points_and_disp_mids.append(point)

    return points_and_disp_mids