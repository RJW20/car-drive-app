from enum import Enum


class Turn(Enum):
    """Class containing Car turns and the angle to turn by."""

    STRAIGHT = 0
    RIGHT = 5
    LEFT = -5