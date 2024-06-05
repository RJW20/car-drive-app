from __future__ import annotations
from collections import deque
import pickle
from pathlib import Path

from car_drive_app.cartesians import Vector
from car_drive_app.track.gate import Gate
from car_drive_app.car.base_car import BaseCar


class BaseTrack:
    """The underlying attributes of the Track the Car drives on."""

    def __init__(self, dimensions: Vector, center_line: deque[Vector], width: int) -> None:
        self.dimensions: Vector = dimensions
        self.center_line: deque[Vector] = center_line
        self.radius: int = width // 2

        self.gates: list[Gate] = []
        for i in range(0, len(self.center_line) - self.radius + 1, self.radius):
            direction = self.center_line[i+1] - self.center_line[i]
            self.gates.append(Gate(i, direction))

    def car_start_position(self, car: BaseCar) -> Vector:
        """Return the position the Car should start at."""
        return self.center_line[0] - self.gates[0].direction * car.LENGTH * 0.5

    def check_collision(self, outline: list[Vector]) -> bool:
        """Return True if the outline given has any points not on the driveable section
        of the Track."""

        return False

    def save(self) -> None:

        destination = Path('track.pickle')
        with destination.open('wb') as dest:
            pickle.dump(self.dimensions, dest)
            pickle.dump(self.center_line, dest)
            pickle.dump(self.radius * 2, dest)

    @classmethod
    def load(cls) -> BaseTrack:

        source = Path('track.pickle')

        try:
            with source.open('rb') as src:
                dimensions = pickle.load(src)
                center_line = pickle.load(src)
                width = pickle.load(src)
                return cls(dimensions, center_line, width)
        except OSError:
            raise OSError(f'Unable to open Track save \'{source}\'.')