import pytest

from rover import exceptions
from rover.models import Coordinate, Movement, Grid, Rover
from rover.enums import CardinalDirection, RotationCommand, MovementCommand


class TestCoordinate:
    def test_add_movement(self):
        coord = Coordinate(x=0, y=0)

        coord += Movement(angle=90, delta=1)

        assert coord.y == 1
        assert coord.x == 0

        coord += Movement(angle=270, delta=1)

        assert coord.y == 0
        assert coord.x == 0

        coord += Movement(angle=0, delta=1)

        assert coord.y == 0
        assert coord.x == 1

        coord += Movement(angle=180, delta=1)

        assert coord.y == 0
        assert coord.x == 0

    def test_add_invalid(self):
        coord = Coordinate(x=0, y=0)

        with pytest.raises(TypeError):
            coord += (1, 1)


class TestMovement:
    @pytest.mark.parametrize('angle,delta_x', [
        (0, 1),
        (180, -1),
    ])
    def test_delta_x(self, angle, delta_x):
        movement = Movement(angle=angle, delta=1)
        assert movement.delta_x == delta_x

    @pytest.mark.parametrize('angle,delta_y', [
        (90, 1),
        (270, -1),
    ])
    def test_delta_y(self, angle, delta_y):
        movement = Movement(angle=angle, delta=1)
        assert movement.delta_y == delta_y


class TestGrid:
    @pytest.mark.parametrize('x,y,within_bounds', [
        (0, 0, True),
        (5, 5, True),
        (2, 3, True),
        (0, 5, True),
        (5, 0, True),
        (-1, 0, False),
        (6, 0, False),
        (0, -1, False),
        (0, 6, False),
    ])
    def test_is_within_bounds(self, x, y, within_bounds):
        grid = Grid(x_max=5, y_max=5)
        coord = Coordinate(x=x, y=y)
        assert grid.is_within_bounds(coord) == within_bounds


class TestRover:
    def test_cardinal_direction(self):
        rover = Rover(
            id='1',
            angle=90,
            coord=Coordinate(x=0, y=0)
        )

        assert rover.cardinal_direction == CardinalDirection.N

    def test_invalid_cardinal_direction(self):
        rover = Rover(
            id='1',
            angle=85,
            coord=Coordinate(x=0, y=0)
        )

        with pytest.raises(ValueError):
            rover.cardinal_direction

    @pytest.mark.parametrize('command,angle', [
        (RotationCommand.L, 180),
        (RotationCommand.R, 0),
    ])
    def test_rotate(self, command, angle):
        # Facing north

        rover = Rover(
            id='1',
            angle=90,
            coord=Coordinate(0, 0)
        )

        rover.rotate(command)

        assert rover.angle == angle

    def test_move(self):
        grid = Grid(5, 5)
        rover = Rover(id='1', angle=90, coord=Coordinate(0, 0))
        rover.move(MovementCommand.M, grid=grid)
        assert rover.coord == Coordinate(0, 1)

    def test_move_outside_of_bounds(self):
        grid = Grid(5, 5)
        rover = Rover(id='1', angle=180, coord=Coordinate(0, 0))

        with pytest.raises(exceptions.CollisionDetectedError):
            rover.move(MovementCommand.M, grid=grid)

        assert rover.coord == Coordinate(0, 0)
