from car_drive_app.cartesians import Vector
from car_drive_app.track.base_track import BaseTrack


def generator(dimensions: Vector) -> BaseTrack:
    """Return a BaseTrack that fits on the plane of given dimensions."""

    # Generate random points
    # Get the convex hull using gift wrapping algorithm
    # Compute midpoints and randomly displace them
    # Push apart and fix angles
    # Add splines