class CollisionDetectedError(Exception):
    def __init__(self, coordinate):
        self.coordinate = coordinate

    def __str__(self):
        msg = '{} is not within the grid bounds'
        return msg.format(self.position)

    def __repr__(self):
        return f'CollisionDetectedError({self.coordinate:s})'


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
