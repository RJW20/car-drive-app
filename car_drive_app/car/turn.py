from enum import Enum
import math

class Turn(Enum):
    """Class containing Car turns and the angle to turn by."""

    STRAIGHT = 0
    RIGHT = math.pi/120
    LEFT = -math.pi/120