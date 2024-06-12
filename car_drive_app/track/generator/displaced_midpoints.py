
import random
import math

from car_drive_app.cartesians import Vector


def midpoint(vec1: Vector, vec2: Vector) -> Vector:
    """Return the midpoint of two Vectors."""
    return (vec1 + vec2) / 2


def displacement_vector(
    severity: float,
    max_length: float,
) -> Vector:
    """Return a displacement Vector with given severity.
    
    Points in a random direction.
    Length tends towards max_length given as as severity gets closer to 0.
    """

    orientation = random.uniform(-math.pi/2, math.pi/2)
    length = max_length * random.random() ** severity
    return Vector.unit_from_angle(orientation) * length


def displaced_midpoints(
    points: list[Vector],
    severity: float,
    max_displacement: float,
) -> list[Vector]:
    """Return a list of points containing the input points as well as points that
    are the result of finding the midpoint between consecutive points and randomly
    displacing it.
    
    points should form a closed loop, but the returned points won't do (last point 
    will be omitted).
    The displacement length increases as the severity gets closer to 0, always having 
    the value max_displacement there.
    """

    points_and_disp_mids = []

    N = len(points)
    for i, point in enumerate(points[:-1]):
        next_point = points[(i+1)%N]
        m_p = midpoint(point, next_point)
        displacement = displacement_vector(severity, max_displacement)
        points_and_disp_mids.extend([point, m_p + displacement])

    return points_and_disp_mids