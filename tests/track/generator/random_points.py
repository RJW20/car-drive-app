import pygame

from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points

def main() -> None:

    # Create the points
    dimensions = Vector(1800,1000)
    TRACK_WIDTH = 150
    points = random_points(dimensions, TRACK_WIDTH)

    # Draw the points
    pygame.init()
    screen = pygame.display.set_mode((dimensions.x, dimensions.y))
    pygame.display.set_caption("Random Points")
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

        screen.fill((37,255,0))

        for point in points:
            pygame.draw.circle(screen, 'white', (point.x, point.y), 10)
        
        pygame.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    main()