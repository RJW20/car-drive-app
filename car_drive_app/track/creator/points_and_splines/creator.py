import pygame

from car_drive_app.track.base_track import BaseTrack
from car_drive_app.cartesians import Vector
from car_drive_app.track.creator.points_and_splines.control_point import ControlPoint
from car_drive_app.track.creator.corner_points import corner_points
from car_drive_app.track.creator.points_and_splines.catmull_rom import catmull_rom


class Creator:
    """Class for creating Tracks using points and splines."""

    TRACK_WIDTH = 150

    def __init__(self, dimensions: Vector, track_save_name: str) -> None:

        self.dimensions = dimensions
        self.track_save_name = track_save_name

        # Pygame set up
        self.screen = pygame.display.set_mode((dimensions.x, dimensions.y))
        pygame.display.set_caption("Track Creator")
        self.clock = pygame.time.Clock()

        # Set up initial basic loop
        self.points = corner_points(dimensions, int(self.TRACK_WIDTH * 1.55), ControlPoint)
        self.full_curve = catmull_rom(self.points)

    def check_events(self) -> None:
        """Check for mouse clicks for quitting, dragging and new points.
        
        Returns True if the return key is pressed.
        """

        for event in pygame.event.get():

            # Allow quitting
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            # Dragging
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos = Vector(pos[0], pos[1])
                for point in self.points:
                    if point.contains(pos):
                        point.dragging = True
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                for point in self.points:
                    point.dragging = False

            elif event.type == pygame.KEYDOWN:

                # New ControlPoint
                if event.key == pygame.K_SPACE:
                    self.points.append(ControlPoint(self.dimensions.x // 2, self.dimensions.y // 2))
                    self.full_curve = catmull_rom(self.points)

                # Conclude Track drawing
                elif event.key == pygame.K_RETURN:
                    return True
                
        return False

    def update(self) -> None:
        """Update to the next frame.
        
        Move any control points being dragged.
        """

        for point in self.points:
            if point.dragging:
                pos = pygame.mouse.get_pos()
                point.x, point.y = pos
                self.full_curve = catmull_rom(self.points)
                
    def draw_track(self) -> None:
        """Draw self.full_curve and self.points."""

        self.screen.fill((37,255,0))

        # Draw the curve
        for point in self.full_curve:
            pygame.draw.circle(self.screen, 'grey', (point.x, point.y), self.TRACK_WIDTH // 2)

        # Draw all the control points
        for point in self.points:
            point.draw(self.screen)

        pygame.display.flip()

    def create_track(self) -> None:
        """Allow the user to create the Track in self.full_curve."""

        while not self.check_events():
            self.update()
            self.draw_track()
            self.clock.tick(60)

    def check_mouse_click(self) -> tuple[int,int] | None:
        """Return the coordinates of a mouse click if applicable."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                return pygame.mouse.get_pos()
            
        return None
    
    def set_start_point(self) -> None:
        """Allow the user to select the start point location.
        
        Rotates self.full_curve so that the chosen start point is the first one.
        """

        # Await a mouse click
        while not (pos := self.check_mouse_click()):
            self.clock.tick(60)

        # Find the point on the curve closest to the position clicked
        pos = Vector(pos[0], pos[1])
        distance = self.dimensions.magnitude
        closest = None
        for i, point in enumerate(self.full_curve):
            if (pos - point).magnitude < distance:
                distance = (pos - point).magnitude
                closest = i

        # Roate the deque
        self.full_curve.rotate(-1 * closest)

    def run(self) -> None:
        """Run the main loop."""

        self.create_track()
        self.set_start_point()

        # Create/save a Track
        track = BaseTrack(self.dimensions, self.full_curve, self.TRACK_WIDTH)
        track.save(self.track_save_name)