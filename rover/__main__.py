import functools

from rover import parse, exceptions
from rover.enums import RotationCommand


def main():
    grid = get_grid()

    while (rover := get_rover()):
        commands = get_rover_commands()

        for command in commands:
            if isinstance(command, RotationCommand):
                rover.rotate(command)
            else:
                rover.move(command, grid)

        print_position(rover)


def red(str_):
    return f'\033[31m{str_}\033[0m'


def green(str_):
    return f'\033[32m{str_}\033[0m'


def get_grid():
    return parse.parse_grid(input('Please enter grid size: '))


def get_rover():
    return parse.parse_rover(input('Please enter rover start: '))


def get_rover_commands():
    return parse.parse_rover_commands(input('Please enter rover commands: '))


def print_position(rover):
    msg = f'{rover.coord.x} {rover.coord.y} {rover.cardinal_direction.name}'
    print(green(msg))


if __name__ == '__main__':
    main()
