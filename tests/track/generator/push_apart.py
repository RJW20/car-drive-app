import pygame

from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points
from car_drive_app.track.generator.convex_hull import convex_hull
from car_drive_app.track.generator.displaced_midpoints import displaced_midpoints
from car_drive_app.track.generator.push_apart import push_apart

def main() -> None:

    # Create the points
    dimensions = Vector(1800,1000)
    TRACK_WIDTH = 150
    points = random_points(dimensions, TRACK_WIDTH)
    c_hull = convex_hull(points)
    points_and_mps = displaced_midpoints(c_hull, 1, 2 * TRACK_WIDTH)

    # Draw the original convex hull points and midpoints as well as lines around
    pygame.init()
    screen = pygame.display.set_mode((dimensions.x, dimensions.y))
    pygame.display.set_caption("Push Apart")
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

        screen.fill((37,255,0))

        for point in points_and_mps:
            pygame.draw.circle(screen, 'white', (point.x, point.y), 10)
            
        pygame.draw.lines(screen, 'blue', True, [(point.x, point.y) for point in points_and_mps], 2)
        
        pygame.display.flip()

        clock.tick(1)

        push_apart(points_and_mps, TRACK_WIDTH)


if __name__ == '__main__':
    main()