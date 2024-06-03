import pygame

from car_drive_app.cartesians import Vector
from car_drive_app.track.creator.points_and_circles.control_point import ControlPoint
from car_drive_app.track.creator.points_and_circles.corner_points import corner_points
from car_drive_app.track.creator.points_and_circles.curve_finder import curve_finder


class Creator:
    """Class for creating Tracks using points and circles around them."""

    def __init__(self, dimensions: Vector) -> None:

        self.dimensions = dimensions

        # Pygame set up
        self.screen = pygame.display.set_mode((dimensions.x, dimensions.y))
        pygame.display.set_caption("Track Creator")
        self.clock = pygame.time.Clock()

        # Set up initial basic loop
        self.points = corner_points(dimensions)
        self.full_curve = curve_finder(self.points)

    def check_events(self) -> None:
        """Check for mouse clicks for quitting, dragging, changing orientation/radius and new points."""

        # Allow quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos = Vector(pos[0], pos[1])
                for point in self.points:
                    if point.contains(pos):
                        point.dragging = True
                        point.selected = True
                    else:
                        point.selected = False

            elif event.type == pygame.MOUSEBUTTONUP:
                for point in self.points:
                    point.dragging = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.points.append(ControlPoint(self.dimensions.x // 2, self.dimensions.y // 2))
                    self.full_curve = curve_finder(self.points)

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    try:
                        selected_point =  [point for point in self.points if point.selected][0]
                        selected_point.orientation *= -1
                        self.full_curve = curve_finder(self.points)
                    except IndexError:
                        pass

                elif event.key == pygame.K_UP:
                    try:
                        selected_point =  [point for point in self.points if point.selected][0]
                        selected_point.turn_radius += 1
                        self.full_curve = curve_finder(self.points)
                    except IndexError:
                        pass
                elif event.key == pygame.K_DOWN:
                    try:
                        selected_point =  [point for point in self.points if point.selected][0]
                        selected_point.turn_radius -= 1
                        selected_point.turn_radius = max(selected_point.turn_radius, 1)
                        self.full_curve = curve_finder(self.points)
                    except IndexError:
                        pass
                elif event.key == pygame.K_r:
                    try:
                        selected_point =  [point for point in self.points if point.selected][0]
                        selected_point.turn_radius = 100
                        self.full_curve = curve_finder(self.points)
                    except IndexError:
                        pass

    def update(self) -> None:
        """Update to the next frame.
        
        Move any control points being dragged.
        """

        for point in self.points:
            if point.dragging:
                pos = pygame.mouse.get_pos()
                point.x, point.y = pos
                self.full_curve = curve_finder(self.points)
                

    def draw_track(self) -> None:
        """Draw self.full_curve and self.points."""

        self.screen.fill('green')

        # Draw the curve
        for point in self.full_curve:
            pygame.draw.circle(self.screen, 'grey', (point.x, point.y), 60)

        # Draw all the control points
        for point in self.points:
            point.draw(self.screen)

        pygame.display.flip()

    def run(self) -> None:
        """Run the main loop."""

        while True:
            self.check_events()
            self.update()
            self.draw_track()
            self.clock.tick(60)


if __name__ == '__main__':
    cr = Creator(Vector(1500, 900))
    cr.run()