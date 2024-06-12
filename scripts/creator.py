import sys

from car_drive_app.cartesians import Vector
import car_drive_app.track.creator.points_and_circles.creator
import car_drive_app.track.creator.points_and_splines.creator


def creator_1(args: list=sys.argv) -> None:
    """Starts and runs new instance of points_and_circles.Creator with dimensions
    and save name specified in args."""

    dimensions = Vector(int(args[1]), int(args[2]))
    track_save_name = args[3]
    cr = car_drive_app.track.creator.points_and_circles.creator.Creator(dimensions, track_save_name)
    cr.run()


def creator_2(args: list=sys.argv) -> None:
    """Starts and runs new instance of points_and_splines.Creator with dimensions
    and save name specified in args."""

    dimensions = Vector(int(args[1]), int(args[2]))
    track_save_name = args[3]
    cr = car_drive_app.track.creator.points_and_splines.creator.Creator(dimensions, track_save_name)
    cr.run()