from rover import parse
from rover.enums import RotationCommand


def main():
    grid = parse.parse_grid(input('Please enter grid size: '))

    while (rover := parse.parse_rover(input('Please enter rover start: '))):
        commands = input('Please enter rover commands: ')
        commands = parse.parse_rover_commands(commands)

        for command in commands:
            if isinstance(command, RotationCommand):
                rover.rotate(command)
            else:
                rover.move(command, grid)

        print_position(rover)


def print_position(rover):
    print(f'{rover.coord.x} {rover.coord.y} {rover.cardinal_direction.name}')


if __name__ == '__main__':
    main()
