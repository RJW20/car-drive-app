from car_drive_app.cartesians import Vector


def convex_hull(points: list[Vector]) -> list[Vector]:
    """Return the convex hull of the given points.
    
    Uses the gift wrapping algorithm.
    Returns the points in anti-clockwise order (clockwise on the regular cartesian plane).
    """

    hull = []

    # Pick the rightmost point (highest x value)
    start = points[0]
    for point in points[1:]:
        if point.x > start.x:
            start = point
    hull.append(start)
    points.rem

    # Choose a random point and then take the 2D cross product with all others and whenever it is negative we know
    # that point is 'more left' so to switch to it and then continue
    



    # Repeat until back at the start