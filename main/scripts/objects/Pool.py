

# Pool
# |
# |--- Region [] as string


class Mercenary:

    def __init__(self):
        self.unit = {}
        self.unit['unit'] = ""
        self.unit['unit_type'] = ""
        self.unit['exp'] = 0
        self.unit['cost'] = 0
        self.unit['replenish_min'] = 0.0
        self.unit['replenish_max'] = 0.0
        self.unit['max'] = 0
        self.unit['initial'] = 0
        self.unit['start_year'] = 0
        self.unit['end_year'] = 0
        self.unit['catholic'] = ""
        self.unit['islam'] = ""
        self.unit['orthodox'] = ""
        self.unit['crusading'] = ""
        self.unit['event_1'] = ""
        self.unit['event_2'] = ""

    def __repr__(self):
        return "{}".format(self.unit['unit'])


class Pool:

    def __init__(self):
        self.pool = {}
        self.pool['pool_name'] = ""
        self.pool['regions'] = []
        self.pool['units'] = []

    def __repr__(self):
        return "{}: {}".format(self.pool['pool_name'], self.pool['regions'])
