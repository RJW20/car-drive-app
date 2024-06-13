from car_drive_app.cartesians import Vector


def push_apart(points: list[Vector], min_distance: int) -> bool:
    """Push apart any consecutive points in the given list that have less than min_distance
    separation between them.
    
    Returns True if any points were altered.
    Pushes both points further away in line with the original vector between them.
    """

    altered = False

    N = len(points)
    for i, point in enumerate(points):
        next_point = points[(i+1)%N]
        separation = next_point - point
        if (sep_length := separation.magnitude) < min_distance:
            length_change = (min_distance - sep_length) / 1.5
            change_vec = length_change * separation/sep_length
            points[i] = point - change_vec
            points[(i+1)%N] = point + change_vec
            altered = True

    return altered