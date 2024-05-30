from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points
from car_drive_app.track.generator.convex_hull import convex_hull
from car_drive_app.track.generator.displaced_midpoints import displaced_midpoints
from car_drive_app.track.generator.catmull_rom import catmull_rom

def main() -> None:

    dimensions = Vector(250,250)
    points = random_points(dimensions)
    c_hull = convex_hull(points)
    points_and_mps = displaced_midpoints(c_hull, 1, 10)
    full_curve = catmull_rom(points_and_mps, 10)
    for point in full_curve:
        print(point, end=', ')

if __name__ == '__main__':
    main()