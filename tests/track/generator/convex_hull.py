from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points
from car_drive_app.track.generator.convex_hull import convex_hull

def main() -> None:

    dimensions = Vector(250,250)
    points = random_points(dimensions)
    for point in points:
        print(point, end=', ')
    print('\n')
    c_hull = convex_hull(points)
    for point in c_hull:
        print(point, end=', ')


if __name__ == '__main__':
    main()