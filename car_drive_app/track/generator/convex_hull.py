from car_drive_app.cartesians import Vector, cross


def find_start(points: list[Vector]) -> Vector:
    """Return the right-most point (highest x-value)."""
    return sorted(points, key=lambda point: point.x, reverse=True)[0]


def next_most_left(start: Vector, others: list[Vector]) -> Vector:
    """Return the point in others that is the most left of the start Vector (and hence all others
    must be to the right).
    
    Sets a pointer at the first point in others, then iterates through points in others and calculates 
    the 2D cross product of the Vectors start->pointer and start->current_point and whenever it is
    negative switches the pointer to current_point then continues.
    """

    choice = others[0]
    choice_offset = choice - start
    for point in others[1:]:
        point_offset = point - start
        if cross(choice_offset, point_offset) < 0:
            choice = point
            choice_offset = choice - start

    return choice


def convex_hull(points: list[Vector]) -> list[Vector]:
    """Return the convex hull of the given points.
    
    Uses the gift wrapping algorithm.
    Returns the points in anti-clockwise order (clockwise on the regular cartesian plane).
    """

    hull = []

    # Get start
    start = find_start(points)
    hull.append(start)

    # Choose first
    possible_next = points[:]
    possible_next.remove(start)
    choice = next_most_left(start, possible_next)
    hull.append(choice)

    # Iterate throught till back at the start
    while not choice == start:
        possible_next = points[:]
        possible_next.remove(choice)
        choice = next_most_left(start, possible_next)
        hull.append(choice)
    
    return hull