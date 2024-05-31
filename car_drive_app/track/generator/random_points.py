import random

from car_drive_app.cartesians import Vector


def random_points(dimensions: Vector, dist_from_edges: int = 0) -> list[Vector]:
    """Return a list of random points in the 2D plane.
    
    The number of points will have average density of approximately 1 point 
    per 60x60 square.
    No point will be closer than dist_from_edges to the outside of the dimensions.
    Raises a value error if the dimensions are too small.
    """

    # Calculate the number of points to generate
    offset = Vector(dist_from_edges, dist_from_edges)
    available_dimensions = dimensions - 2 * offset
    area = available_dimensions.x * available_dimensions.y
    min_points = area // 80 ** 2
    if min_points < 9:
        raise ValueError(f'Dimensions {dimensions} is too small to generate a track on.')
    max_points = area // 50 ** 2
    num_points = random.randint(min_points, max_points)

    # Generate the points
    points = [offset + Vector(random.randint(1,available_dimensions.x-1), random.randint(1,available_dimensions.y-1)) for _ in range(num_points)]
    
    return points