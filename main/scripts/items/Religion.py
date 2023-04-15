class Religion:

    def __init__(self, catholic, orthodox, islam, pagan, heretic):
        self.catholic = int(catholic)
        self.orthodox = int(orthodox)
        self.islam = int(islam)
        self.pagan = int(pagan)
        self.heretic = int(heretic)
        assert (self.catholic + self.orthodox + self.islam + self.pagan + self.heretic) == 100, f"Sum of religions are not equal to 100!"
