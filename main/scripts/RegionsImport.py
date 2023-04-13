import xlrd
from scripts.utils.logger import *
from scripts.Region import Region, Color
from scripts.read_excel import *
from scripts.utils.constants import *


class RegionsImport:
    RANGE_START = Cell("B", 5)
    RANGE_END = Cell("AW", 7)
    REGION_SHEET_INDEX = 0
    dir_path_script = ""

    def __init__(self, dir_path_script):
        LOG_INFO("Run regions import script")
        self.dir_path_script = dir_path_script
        self.regionsList = []
        self.__run()

    def get_list(self):
        return self.regionsList

    def __run(self):
        workbook = xlrd.open_workbook(INPUT_XML_REGIONS)
        worksheet_name = workbook.sheet_by_index(self.REGION_SHEET_INDEX)

        titlesList = collect_first_row_as_titles(worksheet_name, self.RANGE_START, self.RANGE_END)
        self.regionsList = self.__fill_region_list(worksheet_name, self.RANGE_START, self.RANGE_END, titlesList)
        # assert len(self.factionsList) == MAX_NUM_FACTIONS, f"Number of factions different than: {MAX_NUM_FACTIONS}"

    def __fill_region_list(self, worksheet_name, range_start, range_end, titles_list):
        regionsList = []
        for row in range(range_start.row, range_end.row):
            attrList = collect_data_from_row(worksheet_name, range_start.col, range_end.col, row)
            region = Region()

            is_hidden_resource = False
            hidden_resource = []
            for i, attr in enumerate(titles_list):
                value = attrList[i]
                if attr == "r1":
                    region.descr_regions['color_code'].r = int(float(value))
                elif attr == "g1":
                    region.descr_regions['color_code'].g = int(float(value))
                elif attr == "b1":
                    region.descr_regions['color_code'].b = int(float(value))
                elif attr == "catholic":
                    region.descr_regions['religions'].catholic = int(float(value))
                elif attr == "orthodox":
                    region.descr_regions['religions'].orthodox = int(float(value))
                elif attr == "islam":
                    region.descr_regions['religions'].islam = int(float(value))
                elif attr == "pagan":
                    region.descr_regions['religions'].pagan = int(float(value))
                elif attr == "heretic":
                    region.descr_regions['religions'].heretic = int(float(value))
                elif attr == "hidden_resources_start":
                    is_hidden_resource = True
                elif attr == "hidden_resources_end":
                    is_hidden_resource = False
                    region.descr_regions['hidden_resource'] = hidden_resource
                elif is_hidden_resource:
                    if value == "yes":
                        hidden_resource.append(attr)
                    else:
                        hidden_resource.append(value)
                elif attr == '':
                    continue
                else:
                    region.descr_regions[attr] = attrList[i]

            regionsList.append(region)
        return regionsList
