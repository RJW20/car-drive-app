import pygame

from car_drive_app.car.base_car import BaseCar
from car_drive_app.car import Turn


class Game:
    """Controller of all game objects."""

    def __init__(self, settings: dict) -> None:
        
        # Pygame set up
        self.screen = pygame.display.set_mode(settings['dimensions'])
        pygame.display.set_caption("Car Drive")
        self.clock = pygame.time.Clock()

        # Start the Car
        self.car = BaseCar()

    def check_move(self) -> tuple[Turn, bool]:
        """Check for new user input and convert to valid move."""

        # Check for a Turn
        for event in pygame.event.get():

            # Allow quitting
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            # Check key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move = Turn.RIGHT
                elif event.key == pygame.K_LEFT:
                    move = Turn.LEFT

        # Check for acceleration
        keys = pygame.key.get_pressed()
        accelerate =  keys[pygame.K_SPACE]

        return move, accelerate if move else Turn.STRAIGHT, accelerate

    def advance(self, turn: Turn, accelerate: bool) -> None:
        """Advance to the next frame."""

        self.car.move(turn, accelerate)

    def update_screen(self) -> None:
        """Draw the current frame to the screen."""

        # Wipe the last frame
        self.screen.fill('white')

        # Draw the Car
        pygame.draw.circle(self.screen, 'red', self.car.position, 5)

        # Show the changes
        pygame.display.flip()

    def run(self) -> None:
        """Run the main game loop."""

        while True:
            self.advance(*self.check_move)
            self.update_screen()

            self.clock.tick(60)