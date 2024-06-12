import pygame

from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points
from car_drive_app.track.generator.convex_hull import convex_hull
from car_drive_app.track.generator.displaced_midpoints import displaced_midpoints
from car_drive_app.track.creator.points_and_splines.catmull_rom import catmull_rom

def main() -> None:

    # Create the points
    dimensions = Vector(1800,1000)
    TRACK_WIDTH = 150
    points = random_points(dimensions, TRACK_WIDTH)
    c_hull = convex_hull(points)
    points_and_mps = displaced_midpoints(c_hull, 1)
    full_curve = catmull_rom(points_and_mps)

    # Draw the original convex hull points, midpoints and the points in the full curve
    pygame.init()
    screen = pygame.display.set_mode((dimensions.x, dimensions.y))
    pygame.display.set_caption("Catmull-Rom")
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

        screen.fill((37,255,0))

        for point in full_curve:
            pygame.draw.circle(screen, 'purple', (point.x, point.y), 2)

        for point in points_and_mps:
            pygame.draw.circle(screen, 'blue', (point.x, point.y), 10)

        for point in c_hull:
            pygame.draw.circle(screen, 'white', (point.x, point.y), 10)
            
        pygame.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    main()