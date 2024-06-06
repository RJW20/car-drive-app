from enum import Enum

class Acceleration(Enum):
    """Class containing Car accelerations and the multiplier of its Power to apply."""

    FORWARD = - 0.5
    REVERSE = 0.125
    NONE = 0