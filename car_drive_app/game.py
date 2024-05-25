import math

import pygame

from car_drive_app.car.car import Car
from car_drive_app.cartesians import Vector
from car_drive_app.car import Turn


class Game:
    """Controller of all game objects."""

    def __init__(self, settings: dict) -> None:
        
        # Pygame set up
        self.screen = pygame.display.set_mode(settings['dimensions'])
        pygame.display.set_caption("Car Drive")
        self.clock = pygame.time.Clock()

        # Start the Car
        self.car = Car()
        self.car.reset(position=Vector(200,200), angle=0)

    def check_move(self) -> tuple[Turn, bool]:
        """Check for new user input and convert to valid move."""
 
        # Allow quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.car.reset(position=Vector(200,200))

        # Check for key input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] != keys[pygame.K_LEFT]:
            if keys[pygame.K_RIGHT]:
                turn = Turn.RIGHT
            else:
                turn = Turn.LEFT
        else:
            turn = Turn.STRAIGHT

        accelerate =  keys[pygame.K_SPACE]

        return turn, accelerate

    def advance(self, turn: Turn, accelerate: bool) -> None:
        """Advance to the next frame."""

        self.car.move(turn, accelerate)

    def update_screen(self) -> None:
        """Draw the current frame to the screen."""

        # Wipe the last frame
        self.screen.fill('white')

        # Draw the Car
        pygame.draw.circle(self.screen, 'red', (self.car.position.x, self.car.position.y), 5)
        for point in self.car.outline:
            pygame.draw.circle(self.screen, 'black', (point.x, point.y), 1)

        # Draw the Car's Wheels
        for w_cen, w_dir in self.car.wheel_rects:
            start_pos = w_cen + w_dir * 10
            end_pos = w_cen - w_dir * 10
            pygame.draw.line(self.screen, 'black', (start_pos.x, start_pos.y), (end_pos.x, end_pos.y), width=10)

        # Draw the forces acting on the car
        for force, origin in self.car.force_pairs:
            start_pos = origin
            end_pos = origin + force * 20
            pygame.draw.line(self.screen, 'green', (start_pos.x, start_pos.y), (end_pos.x, end_pos.y), width=2)
        self.car.force_pairs = []

        # Show the changes
        pygame.display.flip()

    def run(self) -> None:
        """Run the main game loop."""

        while True:
            self.advance(*self.check_move())
            self.update_screen()

            self.clock.tick(60)