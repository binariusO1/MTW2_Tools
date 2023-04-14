from scripts.Color import *
from scripts.Religion import *


class Region:

    def __init__(self):
        self.descr_regions = {}
        self.descr_regions['region_name'] = ""
        self.descr_regions['settlement_name'] = ""
        self.descr_regions['faction_creator'] = ""
        self.descr_regions['rebel_type'] = ""
        self.descr_regions['color_code'] = Color(0, 0, 0)
        self.descr_regions['hidden_resources'] = []
        self.descr_regions['triumph_value'] = 5
        self.descr_regions['fertility'] = 1
        self.descr_regions['religions'] = Religion(100, 0, 0, 0, 0)

    def __repr__(self):
        return "{}:".format(self.descr_regions['region_name'])
