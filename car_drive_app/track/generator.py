import random

from car_drive_app.cartesians import Vector
from car_drive_app.track.track import Track


def random_points(dimensions: Vector) -> list[Vector]:
    """Return a list of random points in the 2D plane.
    
    The number of points will have average density of approximately 1 point 
    per 60x60 square.
    Raises a value error if the dimensions are too small.
    """

    # Calculate the number of points to generate
    area = dimensions.x * dimensions.y
    min_points = area // 80 ** 2
    if min_points < 10:
        raise ValueError(f'Dimensions {dimensions} is too small to generate a track on.')
    max_points = area // 50 ** 2
    num_points = random.randint(min_points, max_points)

    # Generate the points
    points = [Vector(random.randint(1,dimensions.x-1), random.randint(1,dimensions.y-1)) for _ in range(num_points)]
    
    return points


def generator(dimensions: Vector) -> Track:
    """Return a Track that fits on the plane of given dimensions."""

    # Generate random points
    # Get the convex hull using gift wrapping algorithm
    # Compute midpoints and randomly displace them
    # Push apart and fix angles
    # Add splines