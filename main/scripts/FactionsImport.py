import xlrd
from scripts.utils.logger import *
from scripts.Faction import Faction, Color
from scripts.read_excel import *
from scripts.utils.constants import *


class FactionsImport:
    RANGE_START = Cell("B", 4)
    RANGE_END = Cell("AJ", 35)
    FACTION_SHEET_INDEX = 0
    dir_path_script = ""

    def __init__(self, dir_path_script):
        LOG_INFO("Run factions import script")
        self.dir_path_script = dir_path_script
        self.factionsList = []
        self.__run()

    def get_list(self):
        return self.factionsList

    def __run(self):
        workbook = xlrd.open_workbook(INPUT_XML_FACTIONS)
        worksheet_name = workbook.sheet_by_index(self.FACTION_SHEET_INDEX)

        titlesList = collect_first_row_as_titles(worksheet_name, self.RANGE_START, self.RANGE_END)
        self.factionsList = self.__fill_faction_list(worksheet_name, self.RANGE_START, self.RANGE_END, titlesList)
        assert len(self.factionsList) == MAX_NUM_FACTIONS, f"Number of factions different than: {MAX_NUM_FACTIONS}"

    def __fill_faction_list(self, worksheet_name, range_start, range_end, titles_list):
        factionsList = []
        for row in range(range_start.row, range_end.row):
            attrList = collect_data_from_row(worksheet_name, range_start.col, range_end.col, row)
            faction = Faction()
            is_horde = False
            horde_unit = []

            for i, attr in enumerate(titles_list):
                if attr == "r1":
                    faction.dictionary['primary_colour'].r = int(float(attrList[i]))
                elif attr == "g1":
                    faction.dictionary['primary_colour'].g = int(float(attrList[i]))
                elif attr == "b1":
                    faction.dictionary['primary_colour'].b = int(float(attrList[i]))
                elif attr == "r2":
                    faction.dictionary['secondary_colour'].r = int(float(attrList[i]))
                elif attr == "g2":
                    faction.dictionary['secondary_colour'].g = int(float(attrList[i]))
                elif attr == "b2":
                    faction.dictionary['secondary_colour'].b = int(float(attrList[i]))
                elif attr == "is_horde" and attrList[i] == "yes":
                    faction.is_horde = True
                    is_horde = True
                elif is_horde:
                    if attr == "horde_min_units":
                        faction.dictionary['horde_min_units'] = int(float(attrList[i]))
                    elif attr == "horde_max_units":
                        faction.dictionary['horde_max_units'] = int(float(attrList[i]))
                    elif attr == "horde_max_units_reduction_every_horde":
                        faction.dictionary['horde_max_units_reduction_every_horde'] = int(float(attrList[i]))
                    elif attr == "horde_unit_per_settlement_population":
                        faction.dictionary['horde_unit_per_settlement_population'] = int(float(attrList[i]))
                    elif attr == "horde_min_named_characters":
                        faction.dictionary['horde_min_named_characters'] = int(float(attrList[i]))
                    elif attr == "horde_max_percent_army_stack":
                        faction.dictionary['horde_max_percent_army_stack'] = int(float(attrList[i]))
                    elif attr == "horde_disband_percent_on_settlement_capture":
                        faction.dictionary['horde_disband_percent_on_settlement_capture'] = int(float(attrList[i]))
                    elif attr == "horde_unit":
                        horde_unit.append(attrList[i])
                    else:
                        faction.dictionary_horde['horde_unit'] = horde_unit
                        faction.dictionary[attr] = attrList[i]
                        is_horde = False
                elif attr == '':
                    continue
                else:
                    faction.dictionary[attr] = attrList[i]
            factionsList.append(faction)
        return factionsList
