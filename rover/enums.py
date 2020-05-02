import enum


class CardinalDirection(enum.Enum):
    N = 90
    E = 0
    S = 270
    W = 180

    def __str__(self):
        return self.name


class RelativeDirection(enum.Enum):
    L = -90
    R = 90


class MovementCommand(enum.Enum):
    M = 1
