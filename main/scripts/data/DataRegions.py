import os

from scripts.data.IData import *
from scripts.objects.Pool import *
from scripts.objects.Region import *
from scripts.utils.Constants import *
from scripts.utils.custom import *
from scripts.utils.read_excel import *
from scripts.utils.write_data import *


class DataRegions(IData):

    def __init__(self, p_mainPath, p_dataPath):
        IData.__init__(self, p_mainPath)
        self.dataPath = p_dataPath
        self.regionsList = []
        self.mercenariesList = []

    def load_all_data(self):
        IData.load_all_data(self)

        self.__load_regions_data()
        self.__load_mercenaries_data()

    def get_regions_list(self):
        return self.regionsList

    def create_all(self):
        IData.create_all(self)
        self.create_descr_regions()
        self.create_descr_mercenaries()

    def create_descr_regions(self):
        LOG_INFO("Creating descr_regions.txt file")

        os.makedirs(self.dataPath + DIR_BASE, exist_ok=True)
        self.__write_descr_regions(self.dataPath + DIR_BASE)

    def create_descr_mercenaries(self):
        LOG_INFO("Creating descr_mercenaries.txt file")
        os.makedirs(self.dataPath + DIR_IMPERIAL_CAMPAIGN, exist_ok=True)
        self.__write_descr_mercenaries(self.dataPath + DIR_IMPERIAL_CAMPAIGN)

    # private

    def __load_regions_data(self):
        LOG_INFO("Load regions data")
        self.__fill_regions_list(REGIONS_DATA_INPUT, REGIONS_SHEET_INDEX, 0)

    def __load_mercenaries_data(self):
        LOG_INFO("Load mercenaries data")
        self.__fill_mercenaries_list(REGIONS_DATA_INPUT, MERCENARIES_SHEET_INDEX, 0)

    def __fill_regions_list(self, p_workbook_name, p_worksheet_index, p_table_index):
        titles = get_titles_from_first_row(p_workbook_name, p_worksheet_index, p_table_index)
        regionsList = []
        for row in get_rows(p_workbook_name, p_worksheet_index, p_table_index):
            region = Region()

            is_hidden_resource = False
            hidden_resources = []
            coordinates = Coordinates(0, 0)
            for i, attr in enumerate(titles):
                value = row[i]
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
                    region.descr_regions['hidden_resources'] = hidden_resources
                elif attr == "x":
                    coordinates.x = int(value)
                elif attr == "y":
                    coordinates.y = int(value)
                    region.descr_strat['coordinates'] = coordinates
                elif is_hidden_resource:
                    if value == "yes":
                        hidden_resources.append(attr)
                    elif value == "":
                        continue
                    else:
                        hidden_resources.append(value)
                elif attr == '':
                    continue
                else:
                    region.descr_regions[attr] = row[i]
            regionsList.append(region)
        self.regionsList = regionsList

    def __fill_mercenaries_list(self, p_workbook_name, p_worksheet_index, p_table_index=0):
        titles = get_titles_from_first_row(p_workbook_name, p_worksheet_index, p_table_index)
        poolsList = []
        pool = Pool()
        actualPoolName = ""
        for row in get_rows(p_workbook_name, p_worksheet_index, p_table_index):
            mercenary = Mercenary()
            for i, title in enumerate(titles):
                value = row[i]
                if title == "pool_name":
                    if not actualPoolName == value:
                        poolsList.append(pool)
                        actualPoolName = value
                        pool = Pool()
                        pool.pool['pool_name'] = value
                        # print(pool)
                    else:
                        continue
                mercenary.unit[title] = value;
            pool.pool['units'].append(mercenary)

        poolsList.append(pool)
        # print(poolsList)

        self.mercenariesList = poolsList

        # get regions
        for region in self.regionsList:
            for pool in self.mercenariesList:
                if region.descr_regions['pool_name'] == pool.pool['pool_name']:
                    pool.pool['regions'].append(region.descr_regions['region_name'])
                # print(region.descr_regions['pool_name'])

    def __write_descr_regions(self, p_creationPath):
        TEMPLATE_NAME = "descr_regions.txt"
        TEMPLATE_NAME_INFO = "descr_regions_INFO.txt"

        file = open(p_creationPath + TEMPLATE_NAME, "w", encoding="utf8")

        write_filestamp(file)
        write_info(file, TEMPLATE_NAME_INFO)
        self.__write_regions_data(file, TEMPLATE_NAME)

        file.close()

    def __write_descr_mercenaries(self, p_creationPath):
        TEMPLATE_NAME = "descr_mercenaries.txt"
        TEMPLATE_NAME_INFO = "descr_mercenaries_INFO.txt"

        file = open(p_creationPath + TEMPLATE_NAME, "w", encoding="utf8")

        write_filestamp(file)
        write_info(file, TEMPLATE_NAME_INFO)
        self.__write_mercenaries_data(file, TEMPLATE_NAME)

        file.close()

    def __write_regions_data(self, file, p_template_name):
        for region in self.regionsList[0:len(self.regionsList)]:
            template_region = get_empty_template(p_template_name)
            file.write('\n')

            for i, line in enumerate(template_region):
                key = get_nth_key(region.descr_regions, i)
                if i == 4:
                    r = region.descr_regions[key].r
                    g = region.descr_regions[key].g
                    b = region.descr_regions[key].b
                    colour = str(r) + " " + str(g) + " " + str(b)
                    newLine = line.replace("NUMS", colour)
                    file.write(newLine)
                elif i == 5:
                    # print(region.descr_regions[key])
                    text = ""
                    for resource in region.descr_regions[key]:
                        text = text + resource + ", "
                    file.write('\t' + text[0:-2] + '\n')
                elif i == 8:
                    catholic = region.descr_regions[key].catholic
                    orthodox = region.descr_regions[key].orthodox
                    islam = region.descr_regions[key].islam
                    pagan = region.descr_regions[key].pagan
                    heretic = region.descr_regions[key].heretic
                    religions = "religions { catholic " + str(int(catholic)) + " orthodox " + str(int(orthodox)) \
                                + " islam " + str(int(islam)) + " pagan " + str(int(pagan)) + " heretic " + str(
                        int(heretic)) + " }"
                    newLine = line.replace("TEXT", religions)
                    file.write(newLine)
                else:
                    try:
                        newLine = line.replace("NUM", str(int(region.descr_regions[key])))
                        file.write(newLine)
                    except ValueError:
                        textToWrite = str(region.descr_regions[key])
                        newLine = line.replace("TEXT", textToWrite)
                        file.write(newLine)

    def __write_mercenaries_data(self, file, p_template_name):
        for pool in self.mercenariesList[0:len(self.mercenariesList)]:
            template = get_empty_template(p_template_name)
            file.write('\n')

            for line in template:
                all_words = line.split()
                lineTitle = all_words[0]
                if lineTitle == "pool":
                    file.write(line.replace("TEXT", pool.pool['pool_name']))
                elif lineTitle == "regions":
                    allRegions = ""
                    for region in pool.pool['regions']:
                        allRegions += region + ' '
                        # print(allRegions)
                    file.write(line.replace("TEXT", allRegions[:-1]))
                elif lineTitle == "unit":
                    # actualUnitType = ""
                    for unit in pool.pool['units']:
                        # if not actualUnitType == unit.unit['unit_type']:
                        #     actualUnitType = unit.unit['unit_type']
                        #     file.write('\n' + "; " + unit.unit['unit_type'] +'\n\n')
                        unitLine = unit.unit['unit'] + get_tabs(unit.unit['unit'], 6) \
                                   + "exp" + ' ' + str(int(unit.unit['exp'])) + ' ' \
                                   + "cost" + ' ' + self.__add_cost(unit.unit['cost']) + ' ' \
                                   + "replenish" + ' ' + str(unit.unit['replenish_min']) + ' - ' + str(unit.unit['replenish_min']) + ' ' \
                                   + "max" + ' ' + str(int(unit.unit['max'])) + ' ' \
                                   + "initial" + ' ' + str(int(unit.unit['initial'])) + ' '
                        if unit.unit['start_year'] > 0:
                            unitLine += "start_year" + ' ' + str(int(unit.unit['start_year'])) + ' '
                        if unit.unit['end_year'] > 0:
                            unitLine += "end_year" + ' ' + str(int(unit.unit['end_year'])) + ' '
                        if unit.unit['catholic'] == 'yes' or unit.unit['islam'] == 'yes' or unit.unit['orthodox'] == 'yes':
                            unitLine += "religions { "
                        if unit.unit['catholic'] == 'yes':
                            unitLine += "catholic" + ' '
                        if unit.unit['islam'] == 'yes':
                            unitLine += "islam" + ' '
                        if unit.unit['orthodox'] == 'yes':
                            unitLine += "orthodox" + ' '
                        if unit.unit['catholic'] == 'yes' or unit.unit['islam'] == 'yes' or unit.unit['orthodox'] == 'yes':
                            unitLine += '} '
                        if unit.unit['crusading'] == 'yes':
                            unitLine += "crusading" + ' '
                        if not unit.unit['event_1'] == "":
                            unitLine += 'events { ' + unit.unit['event_1'] + ' '
                        if not unit.unit['event_2'] == "":
                            unitLine += unit.unit['event_2'] + ' '
                        if not unit.unit['event_1'] == "" or not unit.unit['event_2'] == "":
                            unitLine += '} '
                        unitLine += '\n'
                        # print(unitLine)
                        file.write(line.replace("TEXT", unitLine))
            file.write('\n' + get_separator() + '\n')

    def __add_cost(self, p_cost):
        if len(str(int(p_cost))) == 3:
            return str(int(p_cost)) + ' '
        return str(int(p_cost))
