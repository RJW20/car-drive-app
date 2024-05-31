import pygame

from car_drive_app.cartesians import Vector
from car_drive_app.track.generator.random_points import random_points
from car_drive_app.track.generator.convex_hull import convex_hull
from car_drive_app.track.generator.displaced_midpoints import displaced_midpoints
from car_drive_app.track.generator.catmull_rom import catmull_rom


def draw_track_generation() -> None:

    dimensions = Vector(1200,800)

    # Pygame set up
    screen = pygame.display.set_mode((dimensions.x, dimensions.y))
    pygame.display.set_caption("Track")
    clock = pygame.time.Clock()


    car_scale_length = min(dimensions.x,dimensions.y) // 20

    points = random_points(dimensions, 3 * car_scale_length)
    c_hull = convex_hull(points)
    points_and_mps = displaced_midpoints(c_hull, 1, 2 * car_scale_length)
    full_curve = catmull_rom(points_and_mps, car_scale_length)

    while True:

        # Allow quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

        screen.fill('green')

        # Draw the curve
        for point in full_curve:
            pygame.draw.circle(screen, 'grey', (point.x, point.y), 20)

        # Draw lines between points and midpoints
        pygame.draw.lines(screen, 'blue', True, [(point.x, point.y) for point in points_and_mps], 2)

        # Draw convex hull
        pygame.draw.lines(screen, 'red', True, [(point.x, point.y) for point in c_hull], 2)

        # Draw all the original points
        for point in points:
            pygame.draw.circle(screen, 'white', (point.x, point.y), 5)

        pygame.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    draw_track_generation()