class Coordinates:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def is_set(self):
        return self.x != 0 or self.y != 0

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)
