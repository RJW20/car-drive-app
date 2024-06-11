import sys
import math

import pygame

from car_drive_app.track.track import Track
from car_drive_app.car.car import Car
from car_drive_app.car import Acceleration


class Game:
    """Game controller but all parts used in calculations are drawn on the screen."""

    def __init__(self, track_save_name: str) -> None:

        # Load the Track
        self.track = Track.load(track_save_name)

        # Start the Car
        self.car = Car()
        self.track.place_car_at_start(self.car)
        
        # Pygame set up
        self.dimensions = self.track.dimensions
        pygame.init()
        self.screen = pygame.display.set_mode((self.dimensions.x, self.dimensions.y))
        pygame.display.set_caption("Car Drive")
        self.clock = pygame.time.Clock()
        try:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        except pygame.error:
            raise Exception('No Controller found')

    def check_move(self) -> tuple[float, Acceleration]:
        """Check for new user input and convert to valid move."""
 
        # Allow quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

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
        self.track.update_gate(self.car)
        if not self.track.check_in_bounds(self.car.outline):
            self.track.place_car_at_start(self.car)

    def update_screen(self) -> None:
        """Draw the current frame to the screen."""

        # Wipe the last frame
        self.screen.fill((37,255,0))

        # Draw the Track
        self.track.draw(self.screen)

        # Draw the points we're currently tracking collisions using
        for point in self.track.enclosed_center_line:
            pygame.draw.circle(self.screen, 'purple', (point.x, point.y), 5)

        # Draw the track gates
        for gate in self.track.gates:
            center = self.track.center_line[gate.index]
            direction = gate.direction.rotate_by(math.pi/2)
            start_pos = center - direction * self.track.radius * 1.2
            end_pos = center + direction * self.track.radius * 1.2
            pygame.draw.line(self.screen, 'blue', (start_pos.x, start_pos.y), (end_pos.x, end_pos.y), width=4)

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
    track_save_name = sys.argv[1]
    game = Game(track_save_name)
    game.run()