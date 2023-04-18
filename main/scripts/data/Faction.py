import re
from scripts.items.Color import *


# Faction
# |
# |--- Region []


class Faction:

    def __init__(self, is_horde=False):
        self.dictionary = {}
        self.dictionary['faction'] = ""
        self.dictionary['culture'] = ""
        self.dictionary['religion'] = ""
        self.dictionary['primary_colour'] = Color(0, 0, 0)
        self.dictionary['secondary_colour'] = Color(0, 0, 0)
        self.dictionary['symbol'] = ""
        self.dictionary['rebel_symbol'] = ""
        self.dictionary['loading_logo'] = ""
        self.dictionary['standard_index'] = 0
        self.dictionary['logo_index'] = ""
        self.dictionary['small_logo_index'] = ""
        self.dictionary['triumph_value'] = 0
        self.dictionary['custom_battle_availability'] = ""
        self.dictionary['can_sap'] = ""
        self.dictionary['prefers_naval_invasions'] = ""
        self.dictionary['can_have_princess'] = ""
        self.dictionary['has_family_tree'] = ""

        self.is_horde = is_horde
        self.dictionary_horde = {}
        if is_horde:
            self.dictionary_horde['horde_min_units'] = 0
            self.dictionary_horde['horde_max_units'] = 0
            self.dictionary_horde['horde_max_units_reduction_every_horde'] = 0
            self.dictionary_horde['horde_unit_per_settlement_population'] = 0
            self.dictionary_horde['horde_min_named_characters'] = 0
            self.dictionary_horde['horde_max_percent_army_stack'] = 0
            self.dictionary_horde['horde_disband_percent_on_settlement_capture'] = 0
            self.dictionary_horde['horde_unit'] = []

    def __repr__(self):
        return "{}: {}, {}".format(self.dictionary['name'], self.dictionary['culture'], self.dictionary['religion'])
