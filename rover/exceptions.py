class CollisionDetectedError(Exception):
    def __init__(self, coord):
        self.coord = coord

    def __str__(self):
        msg = 'CollisionDetectedError: {} is not within the grid bounds'
        return msg.format(self.coord)

    def __repr__(self):
        return f'CollisionDetectedError({self.coord:s})'
