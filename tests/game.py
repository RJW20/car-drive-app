import sys
import math

import pygame

from car_drive_app.game import Game


class GameVisual(Game):
    """Game controller but all parts used in calculations are drawn on the screen."""

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


if __name__ == '__main__':
    track_save_name = sys.argv[1]
    game = GameVisual(track_save_name)
    game.run()