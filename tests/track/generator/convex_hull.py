import pygame

from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points
from car_drive_app.track.generator.convex_hull import convex_hull

def main() -> None:

    # Create a convex hull
    dimensions = Vector(1800,1000)
    TRACK_WIDTH = 150
    points = random_points(dimensions, TRACK_WIDTH)
    c_hull = convex_hull(points)

    # Draw the points and lines around the convex hull
    pygame.init()
    screen = pygame.display.set_mode((dimensions.x, dimensions.y))
    pygame.display.set_caption("Convex Hull")
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

        screen.fill((37,255,0))

        for point in points:
            pygame.draw.circle(screen, 'white', (point.x, point.y), 10)

        pygame.draw.lines(screen, 'red', True, [(point.x, point.y) for point in c_hull], 2)
        
        pygame.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    main()