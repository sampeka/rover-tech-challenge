import pytest

from rover import parse, exceptions
from rover.enums import CardinalDirection, RotationCommand, MovementCommand
from rover.models import Coordinate, Rover, Grid


class TestParseGrid:
    def test_valid(self):
        input_ = '5 10'
        grid = parse.parse_grid(input_)
        assert grid == Grid(x_max=5, y_max=10)

    def test_too_many_args(self):
        input_ = '5 10 15'

        with pytest.raises(exceptions.InvalidGridInputError):
            parse.parse_grid(input_)

    def test_too_few_args(self):
        input_ = '5'

        with pytest.raises(exceptions.InvalidGridInputError):
            parse.parse_grid(input_)

    @pytest.mark.parametrize('input_', ['5 G', 'V 3'])
    def test_invalid_int(self, input_):
        with pytest.raises(exceptions.InvalidGridInputError):
            parse.parse_grid(input_)


class TestParseRover:
    def test_valid(self):
        input_ = '1 1 E'

        rover = parse.parse_rover(input_)

        assert isinstance(rover, Rover)
        assert rover.angle == 0
        assert rover.coord == Coordinate(1, 1)

    def test_too_many_args(self):
        input_ = '1 1 E 1'

        with pytest.raises(exceptions.InvalidRoverInputError):
            parse.parse_rover(input_)

    def test_too_few_args(self):
        input_ = '1 1'

        with pytest.raises(exceptions.InvalidRoverInputError):
            parse.parse_rover(input_)

    def test_invalid_cardinal_direction(self):
        input_ = '1 1 G'

        with pytest.raises(exceptions.InvalidRoverInputError):
            parse.parse_rover(input_)

    @pytest.mark.parametrize('input_', ['1 B N', 'N 1 N'])
    def test_invalid_int(self, input_):
        with pytest.raises(exceptions.InvalidRoverInputError):
            parse.parse_rover(input_)


class TestParseInt:
    def test_valid(self):
        assert parse.parse_int('1') == 1

    def test_invalid(self):
        with pytest.raises(exceptions.InvalidInputError):
            parse.parse_int('g')


class TestParseCardinalDirection:
    @pytest.mark.parametrize('input_,output', [
        ('n', CardinalDirection.N),
        ('e', CardinalDirection.E),
        ('s', CardinalDirection.S),
        ('w', CardinalDirection.W),
    ])
    def test_valid(self, input_, output):
        # Test lowercase
        cardinal_direction = parse.parse_cardinal_direction(input_)
        assert cardinal_direction == output

        # Test uppercase
        cardinal_direction = parse.parse_cardinal_direction(input_.upper())
        assert cardinal_direction == output

    def test_invalid(self):
        with pytest.raises(exceptions.InvalidCardinalDirectionInputError):
            parse.parse_cardinal_direction('somestring')


class TestParseRoverCommands:
    @pytest.mark.parametrize('input_', [
        'LLMRMMMRMRM',
        'llmrmmmrmrm',
    ])
    def test_valid(self, input_):
        commands = parse.parse_rover_commands(input_)

        assert commands == [
            RotationCommand.L,
            RotationCommand.L,
            MovementCommand.M,
            RotationCommand.R,
            MovementCommand.M,
            MovementCommand.M,
            MovementCommand.M,
            RotationCommand.R,
            MovementCommand.M,
            RotationCommand.R,
            MovementCommand.M,
        ]

    def test_invalid(self):
        input_ = 'LLRMN'

        with pytest.raises(exceptions.InvalidCommandInputError):
            parse.parse_rover_commands(input_)
