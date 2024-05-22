


class Track:
    """The Track the Car drives on."""

    def __init__(self) -> None:
        pass

    def check_collision(self, outline: list[tuple[int,int]]) -> bool:
        """Return True if the outline given has any points not on the driveable section
        of the Track."""