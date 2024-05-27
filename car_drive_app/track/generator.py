from car_drive_app.cartesians import Vector
from car_drive_app.track.track import Track


def generator(dimensions: Vector) -> Track:
    """Return a Track that fits on the plane of given dimensions."""

    # Generate random points
    # Get the convex hull using gift wrapping algorithm
    # Compute midpoints and randomly displace them
    # Push apart and fix angles
    # Add splines