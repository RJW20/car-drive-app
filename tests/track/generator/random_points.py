from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points

def main() -> None:

    dimensions = Vector(250,250)
    points = random_points(dimensions)
    for point in points:
        print(point)


if __name__ == '__main__':
    main()