from __future__ import annotations
import pickle
from pathlib import Path

import pygame

from car_drive_app.track.base_track import BaseTrack


class Track(BaseTrack):
    """The Track the Car drives on."""

    def draw(self, screen: pygame.Surface) -> None:
        """Draw a grey circle at point.x, point.y with radius self.radius
        for every point in self.center_line."""

        for point in self.center_line:
            pygame.draw.circle(screen, 'grey', (point.x, point.y), 60)

    @classmethod
    def load(cls) -> Track:

        source = Path('track.pickle')

        try:
            with source.open('rb') as src:
                dimensions = pickle.load(src)
                center_line = pickle.load(src)
                radius = pickle.load(src)
                return cls(dimensions, center_line, radius)
        except OSError:
            raise OSError(f'Unable to open Track save \'{source}\'.')