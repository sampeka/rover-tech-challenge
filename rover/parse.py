from typing import List, Union, Generator

from rover import exceptions
from rover.models import Grid, Rover, Coordinate
from rover.enums import MovementCommand, RelativeDirection, CardinalDirection


def parse_grid(str_: str) -> Grid:
    parts = str_.split(' ')

    if len(parts) > 2:
        msg = f'Too many arguments to initialise Grid from input {str_!r}'
        raise exceptions.InvalidGridInputError(msg)
    elif len(parts) < 2:
        msg = f'Too few arguments to initialise Grid from input {str_!r}'
        raise exceptions.InvalidGridInputError(msg)

    x_max, y_max = parts

    try:
        x_max = parse_int(x_max)
        y_max = parse_int(y_max)
    except exceptions.InvalidInputError as e:
        msg = f'Failed to parse grid from input {str_!r}'
        raise exceptions.InvalidGridInputError(msg) from e

    return Grid(
        x_max=x_max,
        y_max=y_max
    )


def parse_rover(str_: str) -> Rover:
    parts = str_.upper().split(' ')

    if len(parts) > 3:
        msg = f'Too many arguments to initialise Rover from input {str_!r}'
        raise exceptions.InvalidRoverInputError(msg)
    elif len(parts) < 3:
        msg = f'Too few arguments to initialise Rover from input {str_!r}'
        raise exceptions.InvalidRoverInputError(msg)

    x, y, direction = parts

    try:
        x = parse_int(x)
        y = parse_int(y)
        direction = parse_cardinal_direction(direction)
    except exceptions.InvalidInputError as e:
        msg = f'Failed to parse Rover from input {str_!r}'
        raise exceptions.InvalidRoverInputError(msg) from e

    return Rover(
        coord=Coordinate(x=x, y=y),
        angle=direction.value
    )


def parse_int(str_: str) -> int:
    try:
        return int(str_)
    except ValueError:
        raise exceptions.InvalidInputError(f'Invalid integer {str_!r}')


def parse_cardinal_direction(str_: str) -> CardinalDirection:
    str_ = str_.upper()

    if str_ == 'N':
        return CardinalDirection.N
    elif str_ == 'E':
        return CardinalDirection.E
    elif str_ == 'S':
        return CardinalDirection.S
    elif str_ == 'W':
        return CardinalDirection.W
    else:
        msg = f'{str_!r} is not a valid CardinalDirection'
        raise exceptions.InvalidCardinalDirectionInputError(msg)


RoverCommand = Union[MovementCommand, RelativeDirection]


def parse_rover_commands(str_: str) -> List[RoverCommand]:
    return list(_parse_rover_commands(str_))


def _parse_rover_commands(str_: str) -> Generator[RoverCommand, None, None]:
    for char in str_.upper():
        if char == 'L':
            yield RelativeDirection.L
        elif char == 'R':
            yield RelativeDirection.R
        elif char == 'M':
            yield MovementCommand.M
        else:
            msg = f'{char!r} in {str!r} is not a valid RoverCommand'
            raise exceptions.InvalidCommandInputError(msg)
