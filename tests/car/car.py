import math

import pygame

from car_drive_app.car.car import Car
from car_drive_app.car import Acceleration


class CarPhysics:
    """Area for testing the Car's physics."""

    def __init__(self) -> None:

        # Start the Car
        self.car = Car()
        self.car.reset()
        
        # Pygame set up
        pygame.init()
        self.screen = pygame.display.set_mode((1800, 950))
        pygame.display.set_caption("Car Physics Testing")
        self.clock = pygame.time.Clock()
        try:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        except pygame.error:
            raise Exception('No Controller found')

    def check_move(self) -> tuple[float, Acceleration]:
        """Check for new user input and convert to valid move."""
 
        for event in pygame.event.get():

            # Allow quitting
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            # Reset the Car
            if event.type == pygame.JOYBUTTONDOWN:
                if self.joystick.get_button(3):
                    self.car.reset()

        # Check for user input
        turn_angle = self.joystick.get_axis(0) * math.pi / 4

        accelerate = self.joystick.get_button(0)
        brake = self.joystick.get_button(1)
        if accelerate:
            acceleration = Acceleration.FORWARD
        elif brake:
            acceleration = Acceleration.REVERSE
        else:
            acceleration = Acceleration.NONE

        return turn_angle, acceleration

    def advance(self, turn_angle: float, acceleration: Acceleration) -> None:
        """Advance to the next frame."""
        self.car.move(turn_angle, acceleration)

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

        # Show the changes
        pygame.display.flip()

    def run(self) -> None:
        """Run the main game loop."""

        while True:
            self.advance(*self.check_move())
            self.update_screen()

            self.clock.tick(60)


if __name__ == '__main__':
    game = CarPhysics()
    game.run()