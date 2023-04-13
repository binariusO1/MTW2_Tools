class Color:
    r = 0
    g = 0
    b = 0

    def __init__(self, r, g, b):
        try:
            self.r = int(float(r))
        except ValueError:
            self.r = r
        try:
            self.g = int(float(g))
        except ValueError:
            self.g = g
        try:
            self.b = int(float(b))
        except ValueError:
            self.b = b