from __future__ import annotations
import math
from functools import cached_property
import pickle
from pathlib import Path

import pygame

from car_drive_app.track.base_track import BaseTrack
from car_drive_app.cartesians.vector import Vector


class Track(BaseTrack):
    """The Track the Car drives on."""

    @cached_property
    def start_line_lines(self) -> list[tuple[Vector]]:
        """Return pairs of Vectors that when connected form the lines that when
        drawn make up the start line."""

        start_point = self.center_line[0]
        start_direction = self.gates[0].direction
        line_direction = start_direction.rotate_by(math.pi/2)
        return [(start_point + i * start_direction - line_direction * self.radius, 
                 start_point + i * start_direction + line_direction * self.radius)
                 for i in range(30)]

    def draw(self, screen: pygame.Surface) -> None:
        """Draw a grey circle at point.x, point.y with radius self.radius
        for every point in self.center_line.
        
        Also draws the start/finish line."""

        for point in self.center_line:
            pygame.draw.circle(screen, 'grey', (point.x, point.y), self.radius)

        # Start/finish line
        for line in self.start_line_lines:
            start_pos, end_pos = line[0], line[1]
            pygame.draw.line(screen, (232, 237, 115), (start_pos.x, start_pos.y), (end_pos.x, end_pos.y), width=2)

    @classmethod
    def load(cls, name: str) -> Track:
        """Return the Track saved at 'tracks/{name}.pickle'."""

        source = Path(f'tracks/{name}.pickle')
        try:
            with source.open('rb') as src:
                dimensions = pickle.load(src)
                center_line = pickle.load(src)
                width = pickle.load(src)
                return cls(dimensions, center_line, width)
        except OSError:
            raise OSError(f'Unable to open Track save \'{source}\'.')