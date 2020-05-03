class CollisionDetectedError(Exception):
    def __init__(self, coord):
        self.coord = coord

    def __str__(self):
        msg = 'CollisionDetectedError: {} is not within the grid bounds'
        return msg.format(self.coord)

    def __repr__(self):
        return f'CollisionDetectedError({self.coord:s})'


class InvalidInputError(Exception):
    pass


class InvalidGridInputError(InvalidInputError):
    pass


class InvalidRoverInputError(InvalidInputError):
    pass


class InvalidCommandInputError(InvalidInputError):
    pass


class InvalidCardinalDirectionInputError(InvalidInputError):
    pass
