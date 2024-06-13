import math

from car_drive_app.cartesians import Vector, dot, cross


def fix_angles(points: list[Vector]) -> bool:
    """Widen the angle created by any 3 consecutive points in the given list that
    currently form an angle less than 90 degrees.
    
    Returns True if any points were altered.
    Increases the angle between points by rotating the vector from the 2nd to the 3rd 
    point enough to make 1-2-3 form a right angle.
    points should not be a closed loop.
    """

    altered = False

    N = len(points)
    for i, point in enumerate(points):
        previous_point = points[i-1]
        next_point = points[(i+1)%N]
        previous_offset = previous_point - point
        next_offset = next_point - point
        angle_between = math.atan2(cross(previous_offset, next_offset), dot(previous_offset, next_offset))
        if abs(angle_between) > math.pi/2:
            continue
        angle_to_rotate_by = 1.05 * (math.copysign(math.pi/2, angle_between) - angle_between)
        new_next_offset = next_offset.rotate_by(angle_to_rotate_by)
        points[(i+1)%N] = point + new_next_offset
        altered = True

    return altered