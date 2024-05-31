import pygame

from car_drive_app.cartesians import Vector
from car_drive_app.track.creator.corner_points import corner_points
from car_drive_app.track.creator.catmull_rom import catmull_rom


class Creator:
    """Class for creating Tracks."""

    def __init__(self, dimensions: Vector) -> None:

        # Pygame set up
        self.screen = pygame.display.set_mode((dimensions.x, dimensions.y))
        pygame.display.set_caption("Track Creator")
        self.clock = pygame.time.Clock()

        # Set up initial basic loop
        self.points = corner_points(dimensions)
        self.full_curve = catmull_rom(self.points, 100)

    def check_events(self) -> None:
        """Check for mouse clicks for quitting, dragging and new points."""

        # Allow quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos = Vector(pos[0], pos[1])
                for i, point in enumerate(self.points):
                    if point.contains(pos):
                        print(i)

    def draw_track(self) -> None:
        """Draw self.full_curve and self.points."""

        self.screen.fill('green')

        # Draw the curve
        for point in self.full_curve:
            pygame.draw.circle(self.screen, 'grey', (point.x, point.y), 20)

        # Draw all the control points
        for point in self.points:
            point.draw(self.screen)

        pygame.display.flip()

    def run(self) -> None:
        """Run the main loop."""

        while True:
            self.check_events()
            self.draw_track()
            self.clock.tick(60)


if __name__ == '__main__':
    cr = Creator(Vector(1200, 800))
    cr.run()