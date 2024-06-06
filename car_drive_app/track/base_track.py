from __future__ import annotations
from collections import deque
from itertools import islice
import pickle
from pathlib import Path

from car_drive_app.cartesians import Vector, dot
from car_drive_app.track.gate import Gate
from car_drive_app.car.base_car import BaseCar


class BaseTrack:
    """The underlying attributes of the Track the Car drives on."""

    def __init__(self, dimensions: Vector, center_line: deque[Vector], width: int) -> None:
        self.dimensions: Vector = dimensions
        self.center_line: deque[Vector] = center_line
        self.radius: int = width // 2

        # Create a list of Gates around the Track
        self.gates: list[Gate] = []
        for i in range(0, len(self.center_line) - self.radius//2 + 1, self.radius//2):
            direction = self.center_line[i+1] - self.center_line[i]
            self.gates.append(Gate(i, direction))
        self.total_gates = len(self.gates)
        self.current_gate_index: int

    def car_start_position(self, car: BaseCar) -> Vector:
        """Return the position the Car should start at."""
        return self.center_line[0] - self.gates[0].direction * car.LENGTH * 0.5
    
    @property
    def car_start_direction(self) -> float:
        """Return the angle the Car should start pointing in."""
        return self.gates[0].direction.angle
    
    def place_car_at_start(self, car: BaseCar) -> Vector:
        """Reset the Car just behind the startline."""

        car.reset(position=self.car_start_position(car), angle=self.car_start_direction)
        self.current_gate_index = 0

    @property
    def current_gate(self) -> Gate:
        return self.gates[self.current_gate_index]

    def update_gate(self, car: BaseCar) -> None:
        """Update self.current_gate_index depending on if the Car has passed through self.current_gate
        forwards or the gate before that backwards."""

        # Advancing through Gate in front
        # Advance if one point is through the Gate
        gate_center = self.center_line[self.current_gate.index]
        gate_direction = self.current_gate.direction
        for point in car.outline:
            offset = point - gate_center
            if dot(offset, gate_direction) > 0:
                self.current_gate_index = (self.current_gate_index + 1) % self.total_gates
                return
            
        # Advancing through Gate behind
        # Advance us all points are through the Gate
        gate = self.gates[self.current_gate_index - 1]
        gate_center = self.center_line[gate.index]
        gate_direction = gate.direction
        for point in car.outline:
            offset = point - gate_center
            if dot(offset, gate_direction) > 0:
                return
        self.current_gate_index = (self.current_gate_index - 1) % self.total_gates

    @property
    def behind_gate(self) -> Gate:
        """Return the second Gate behind the Car."""
        return self.gates[self.current_gate_index - 2]
    
    @property
    def in_front_gate(self) -> Gate:
        """Return the second Gate in front of the Car."""
        return self.gates[(self.current_gate_index + 1) % self.total_gates]

    @property
    def enclosed_center_line(self) -> list[Vector]:
        """Return the points in self.center_line that are enclosed between the current
        behind and in front gates."""
        
        if self.behind_gate.index < self.in_front_gate.index:
            return list(islice(self.center_line, self.behind_gate.index, self.in_front_gate.index))
        else:
            return list(islice(self.center_line, self.behind_gate.index, None)) + list(islice(self.center_line, 0, self.in_front_gate.index))

    def check_in_bounds(self, points: list[Vector]) -> bool:
        """Return False if the points given has any point not on the driveable section
        of the Track."""

        enclosed_center_line = self.enclosed_center_line
        for point in points:
            if min([(point - center_point).magnitude for center_point in enclosed_center_line]) > self.radius:
                return False

        return True

    def save(self, name: str) -> None:
        """Save the constituents needed to reload this Track to 'tracks/{name}.pickle'."""

        destination = Path(f'tracks/{name}.pickle')
        with destination.open('wb') as dest:
            pickle.dump(self.dimensions, dest)
            pickle.dump(self.center_line, dest)
            pickle.dump(self.radius * 2, dest)

    @classmethod
    def load(cls, name: str) -> BaseTrack:
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