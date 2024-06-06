import pygame

from car_drive_app.track import Track
from car_drive_app.car import Car, Turn, Acceleration


class Game:
    """Controller of all game objects."""

    def __init__(self) -> None:

        # Load the Track
        self.track = Track.load()

        # Start the Car
        self.car = Car()
        self.track.place_car_at_start(self.car)
        
        # Pygame set up
        self.dimensions = self.track.dimensions
        pygame.init()
        self.screen = pygame.display.set_mode((self.dimensions.x, self.dimensions.y))
        pygame.display.set_caption("Car Drive")
        self.clock = pygame.time.Clock()

    def check_move(self) -> tuple[Turn, Acceleration]:
        """Check for new user input and convert to valid move."""
 
        # Allow quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

        # Check for key input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] != keys[pygame.K_LEFT]:
            if keys[pygame.K_RIGHT]:
                turn = Turn.RIGHT
            else:
                turn = Turn.LEFT
        else:
            turn = Turn.STRAIGHT

        accelerate = keys[pygame.K_s]
        brake = keys[pygame.K_a]
        if accelerate:
            acceleration = Acceleration.FORWARD
        elif brake:
            acceleration = Acceleration.REVERSE
        else:
            acceleration = Acceleration.NONE

        return turn, acceleration

    def advance(self, turn: Turn, acceleration: Acceleration) -> None:
        """Advance to the next frame."""

        self.car.move(turn, acceleration)
        self.track.update_gate(self.car)
        if self.track.check_in_bounds(self.car.outline):
            self.track.place_car_at_start(self.car)

    def update_screen(self) -> None:
        """Draw the current frame to the screen."""

        # Wipe the last frame
        self.screen.fill('green')

        # Draw the Track
        self.track.draw(self.screen)

        # Draw the Car
        pygame.draw.circle(self.screen, 'red', (self.car.position.x, self.car.position.y), 5)
        for point in self.car.outline:
            pygame.draw.circle(self.screen, 'black', (point.x, point.y), 1)

        # Draw the Car's Wheels
        for w_cen, w_dir in self.car.wheel_rects:
            start_pos = w_cen + w_dir * 10
            end_pos = w_cen - w_dir * 10
            pygame.draw.line(self.screen, 'black', (start_pos.x, start_pos.y), (end_pos.x, end_pos.y), width=10)

        # Show the changes
        pygame.display.flip()

    def run(self) -> None:
        """Run the main game loop."""

        while True:
            self.advance(*self.check_move())
            self.update_screen()

            self.clock.tick(60)