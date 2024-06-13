import random

from car_drive_app.cartesians import Vector


def random_points(dimensions: Vector, offset: int) -> list[Vector]:
    """Return a list of random points in the 2D plane.
    
    All points will be at offset distance away from the nearest walls.
    The number of points will have average density of approximately 1 point 
    per 240x240 square.
    Raises a value error if the dimensions are too small.
    """

    # Calculate the number of points to generate
    offset = Vector(offset, offset)
    available_dimensions = dimensions - 2 * offset
    area = available_dimensions.x * available_dimensions.y
    min_points = area // 320 ** 2
    if min_points < 9:
        raise ValueError(f'Dimensions {dimensions} is too small to generate a track on.')
    max_points = area // 200 ** 2
    num_points = random.randint(min_points, max_points)

    # Generate the points
    points = [offset + Vector(random.randint(0,available_dimensions.x), random.randint(0,available_dimensions.y)) for _ in range(num_points)]
    
    return points