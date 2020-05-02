import math
from dataclasses import dataclass

from rover import exceptions
from rover.enums import CardinalDirection, RelativeDirection, MovementCommand


@dataclass
class Coordinate:
    x: int
    y: int

    def __add__(self, other):
        if isinstance(other, Movement):
            return Coordinate(
                x=self.x + other.delta_x,
                y=self.y + other.delta_y
            )

        msg = 'Unsupported operand types for +: {:r} and {:r}'
        raise TypeError(msg.format(type(self), type(other)))

    def __str__(self):
        return f'{self.x} {self.y}'

    def __repr__(self):
        return f'Coordinate({self})'


@dataclass
class Movement:
    angle: int
    delta: int

    @property
    def delta_x(self) -> int:
        return int(self.delta * math.cos(self.angle * (math.pi / 180)))

    @property
    def delta_y(self) -> int:
        return int(self.delta * math.sin(self.angle * (math.pi / 180)))


@dataclass
class Grid:
    x_max: int
    y_max: int
    x_min = 0
    y_min = 0

    def is_within_bounds(self, coordinate: Coordinate):
        return (
            self.x_min <= coordinate.x <= self.x_max and
            self.y_min <= coordinate.y <= self.y_max
        )


@dataclass
class Rover:
    id: str
    angle: int
    coord: Coordinate

    @property
    def cardinal_direction(self) -> CardinalDirection:
        return CardinalDirection(self.angle)

    def rotate(self, direction: RelativeDirection):
        self.angle = (self.angle - direction.value) % 360

    def move(self, command: MovementCommand, grid: Grid):
        movement = Movement(angle=self.angle, delta=command.value)
        new_coord = self.coord + movement

        if not grid.is_within_bounds(new_coord):
            raise exceptions.CollisionDetectedError(new_coord)

        self.coord = new_coord
