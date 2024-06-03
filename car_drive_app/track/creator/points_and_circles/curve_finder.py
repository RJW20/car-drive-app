import math

from car_drive_app.cartesians import Vector, cross, dot
from car_drive_app.track.creator.points_and_circles.control_point import ControlPoint


def connection_angles(p1: ControlPoint, p2: ControlPoint) -> tuple[float,float]:
    """Return the angles at which the given ControlPoints connect at.
    
    The angle is found such that the tangents to both circles around the ControlPoints 
    and the line connecting the points the tangents start from all have the same gradient 
    in 2D space and point from p1 to p2.
    """

    for theta in range(0,720):
        theta_1 = math.pi/360 * theta
        direction = p1.tangent_at(theta_1)
        theta_2 = (theta_1 + math.pi) % (2 * math.pi) if not p1.orientation == p2.orientation else theta_1  # Ensures tangents point in the same direction
        vec_between = p2.turning_point_at(theta_2) - p1.turning_point_at(theta_1)

        if not math.isclose(cross(vec_between/vec_between.magnitude, direction), 0, abs_tol=10e-2):
            continue

        if dot(vec_between, direction) > 0:
            return theta_1, theta_2
        

def points_around(point: ControlPoint, in_angle: float, out_angle: float) -> list[Vector]:
    """Return the points on the circle around the given point at distance point.turn_radius.
    
    Only the points between the given angles are included, the direction around the circle is 
    determined by point.orientation.
    The point at out_angle is not included.
    """

    sector_arc = []

    current_angle = in_angle
    if point.orientation == -1:
        if out_angle > in_angle:
            out_angle -= 2 * math.pi
        while current_angle > out_angle:
            sector_arc.append(point.turning_point_at(current_angle))
            current_angle -= math.pi/180
    else:
        if out_angle < in_angle:
            out_angle += 2 * math.pi
        while current_angle < out_angle:
            sector_arc.append(point.turning_point_at(current_angle))
            current_angle += math.pi/180

    return sector_arc


def interpolate(p1: Vector, p2: Vector) -> list[Vector]:
    """Return the points that make up the linear interpolation between p1 and p2.
    
    The density is approximately 1 point per 2 pixels travelled.
    p1 is included, p2 is not.
    """

    vec_between = p2 - p1
    step = 2 * vec_between/vec_between.magnitude
    return [p1 + t * step for t in range(0,int(vec_between.magnitude//2))]
    

def curve_finder(points: list[ControlPoint]) -> list[Vector]:
    """Return the list of Vectors that make up the points and circles interpolation curve of the 
    given points.
    
    points should not form a closed loop, but the resultant curve will be.
    """

    curve = []
    
    # Find the angle to connect at first two points
    p0_out_angle, p1_in_angle = connection_angles(points[0], points[1])
    # Linearly interpolate between the connection points at reasonable density
    curve.extend(interpolate(points[0].turning_point_at(p0_out_angle), points[1].turning_point_at(p1_in_angle)))

    current_in_angle = p1_in_angle
    for i, current_point in enumerate(points[1:-1]):
        next_point = points[i+2]

        # Find the angle to connect at current and next points
        current_out_angle, next_in_angle = connection_angles(current_point, next_point)
        # Draw around the current point from the angle it was connected at previously
        curve.extend(points_around(current_point, current_in_angle, current_out_angle))
        # Linearly interpolate between the connection points at reasonable density
        curve.extend(interpolate(current_point.turning_point_at(current_out_angle), next_point.turning_point_at(next_in_angle)))

        current_in_angle = next_in_angle

    # Find the angle to connect at last and first points
    pn_out_angle, p0_in_angle = connection_angles(points[-1], points[0])
    # Draw around the last point from the angle it was connected at previously
    curve.extend(points_around(points[-1], next_in_angle, pn_out_angle))
    # Linearly interpolate between the connection points at reasonable density
    curve.extend(interpolate(points[-1].turning_point_at(pn_out_angle), points[0].turning_point_at(p0_in_angle)))
    # Draw around the first point using the very first angle
    curve.extend(points_around(points[0], p0_in_angle, p0_out_angle))

    return curve