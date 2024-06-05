from __future__ import annotations
from collections import deque
import pickle
from pathlib import Path

from car_drive_app.cartesians import Vector


class BaseTrack:
    """The underlying attributes of the Track the Car drives on."""

    def __init__(self, dimensions: Vector, center_line: deque[Vector], width: int) -> None:
        self.dimensions: Vector = dimensions
        self.center_line: deque[Vector] = center_line
        self.radius: int = width // 2

    def check_collision(self, outline: list[Vector]) -> bool:
        """Return True if the outline given has any points not on the driveable section
        of the Track."""

        return False

    def save(self) -> None:

        destination = Path('track.pickle')
        with destination.open('wb') as dest:
            pickle.dump(self.dimensions, dest)
            pickle.dump(self.center_line, dest)
            pickle.dump(self.radius, dest)

    @classmethod
    def load(cls) -> BaseTrack:

        source = Path('track.pickle')

        try:
            with source.open('rb') as src:
                dimensions = pickle.load(src)
                center_line = pickle.load(src)
                radius = pickle.load(src)
                return cls(dimensions, center_line, radius)
        except OSError:
            raise OSError(f'Unable to open Track save \'{source}\'.')