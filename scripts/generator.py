import sys

from car_drive_app.cartesians import Vector
from car_drive_app.track.generator import generator as ge


def generator(args: list=sys.argv) -> None:
    """Run a new track generation with dimensions and save name specified in args."""

    dimensions = Vector(int(args[1]), int(args[2]))
    track_save_name = args[3]
    ge(dimensions, track_save_name)