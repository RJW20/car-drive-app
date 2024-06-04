from __future__ import annotations
from functools import cached_property
import math
import pickle
from pathlib import Path

from car_drive_app.cartesians import Vector


class BaseTrack:
    """The underlying attributes of the Track the Car drives on."""

    def __init__(self, dimensions: Vector, center_line: list[Vector], width: int) -> None:
        self.dimensions: Vector = dimensions
        self.center_line: list[Vector] = center_line
        self.radius: int = width // 2

    @cached_property
    def driveable_area(self) -> set[Vector]:
        """Return a set of all the positions on the driveable track as Vectors."""

        d_a = set()

        for point in self.center_line:
            for y in range(-1 * self.radius, self.radius + 1):
                x_range = math.ceil(math.sqrt(self.radius ** 2 - y ** 2))
                for x in range(-1 * x_range, x_range + 1):
                    d_a.add(point + Vector(x,y))

        return d_a

    def check_collision(self, outline: list[Vector]) -> bool:
        """Return True if the outline given has any points not on the driveable section
        of the Track."""

        for point in outline:
            if point not in self.driveable_area:
                return True
            
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