import random

from car_drive_app.track.base_track import BaseTrack
from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points
from car_drive_app.track.generator.convex_hull import convex_hull
from car_drive_app.track.generator.displaced_midpoints import displaced_midpoints
from car_drive_app.track.creator.points_and_splines.catmull_rom import catmull_rom


def generator(dimensions: Vector, track_save_name: str) -> BaseTrack:
    """Save a randomly generated BaseTrack that fits on the plane of given dimensions 
    to the file 'tracks/{track_save_name}.pickle'."""

    TRACK_WIDTH = 150

    points = random_points(dimensions, 2 * TRACK_WIDTH)
    c_hull = convex_hull(points)
    points_and_mps = displaced_midpoints(c_hull, 1, TRACK_WIDTH)
    # Push apart and fix angles
    full_curve = catmull_rom(points_and_mps)
    full_curve.rotate(random.randint(0, len(full_curve) - 1))
    track = BaseTrack(dimensions, full_curve, TRACK_WIDTH)
    track.save(track_save_name)