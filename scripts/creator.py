import sys

from car_drive_app.cartesians import Vector
from car_drive_app.track.creator.points_and_circles import Creator


def creator(args: list=sys.argv) -> None:
    """Starts and runs new instance of points_and_circles.Creator with dimensions
    and save name specified in args."""

    dimensions = Vector(int(args[1]), int(args[2]))
    track_save_name = args[3]
    cr = Creator(dimensions, track_save_name)
    cr.run()