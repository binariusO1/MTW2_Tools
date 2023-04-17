import xlrd
from scripts.utils.logger import *
from scripts.data.MusicType import *
from scripts.utils.read_excel import *
from scripts.utils.constants import *


class MusicTypeImport:
    REGIONS_SHEET_INDEX = 0
    MUSIC_SHEET_INDEX = 1
    dir_path_script = ""

    def __init__(self, dir_path_script):
        LOG_INFO("Run music import script")
        self.dir_path_script = dir_path_script
        self.musicTypesList = []

        self.__run()

    def get_list(self):
        return self.musicTypesList

    def __run(self):
        workbook = xlrd.open_workbook(INPUT_XML_REGIONS)
        worksheet_name = workbook.sheet_by_index(self.MUSIC_SHEET_INDEX)
        range_start = get_tables_size(worksheet_name)[0]
        range_end = get_tables_size(worksheet_name)[1]
        titlesList = collect_first_row_as_titles(worksheet_name, range_start, range_end)
        self.musicTypesList = self.__fill_music_list(worksheet_name, range_start, range_end, titlesList)

        worksheet_name = workbook.sheet_by_index(self.REGIONS_SHEET_INDEX)
        range_start = get_tables_size(worksheet_name)[0]
        range_end = get_tables_size(worksheet_name)[1]
        titlesList = collect_first_row_as_titles(worksheet_name, range_start, range_end)
        self.__fill_music_list_by_regions(worksheet_name, range_start, range_end, titlesList, self.musicTypesList)

    def __fill_music_list(self, worksheet_name, range_start, range_end, titles_list):
        musicList = []
        factions = []
        for row in range(range_start.row, range_end.row):
            attrList = collect_data_from_row(worksheet_name, range_start.col, range_end.col, row)
            musicType = MusicType()

            for i, title in enumerate(titles_list):
                value = attrList[i]
                if title == "faction":
                    factions.append(value)
                else:
                    musicType.descr_sound_music_types[title] = value
            factions = sorted(factions)
            factions = [x for x in factions if x != '']
            musicType.descr_sound_music_types['factions'] = factions
            factions = []
            musicList.append(musicType)
        return musicList

    def __fill_music_list_by_regions(self, worksheet_name, range_start, range_end, titles_list, musicList):
        region_name = ""
        for row in range(range_start.row, range_end.row):
            attrList = collect_data_from_row(worksheet_name, range_start.col, range_end.col, row)
            for i, title in enumerate(titles_list):
                value = attrList[i]
                # print(title, "] ", i, " ", region_name, ": ", value)
                if title == "region_name":
                    # print(title, "] ", i, " ", region_name, ": ", value)
                    region_name = value
                elif title == "music_type":
                    # print(title, "] ", i, " ", region_name, ": ", value)
                    for music_type in musicList:
                        if value == music_type.descr_sound_music_types[title]:
                            music_type.descr_sound_music_types["regions"].append(region_name)
                        music_type.descr_sound_music_types["regions"] = sorted(music_type.descr_sound_music_types["regions"])
        return musicList
