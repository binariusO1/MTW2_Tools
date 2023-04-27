import xlrd
from scripts.utils.logger import *
from scripts.objects.MusicType import *
from scripts.utils.read_excel import *
from scripts.utils.Constants import *


class MusicTypeImport:
    REGIONS_SHEET_INDEX = 0
    MUSIC_SHEET_INDEX = 0
    dir_path_script = ""

    def __init__(self, dir_path_script, p_regionsData):
        LOG_INFO("Run music import script")
        self.dir_path_script = dir_path_script
        self.musicTypesList = []

        self.__run(p_regionsData)

    def get_list(self):
        return self.musicTypesList

    def __run(self, p_regionsData):
        workbook = xlrd.open_workbook(INPUT_XML_MUSIC)
        worksheet_name = workbook.sheet_by_index(self.MUSIC_SHEET_INDEX)
        range_start = get_tables_size(worksheet_name)[0]
        range_end = get_tables_size(worksheet_name)[1]
        titlesList = collect_first_row_as_titles(worksheet_name, range_start, range_end)
        self.musicTypesList = self.__fill_music_list(worksheet_name, range_start, range_end, titlesList)

        self.__fill_music_list_by_regions(p_regionsData, self.musicTypesList)

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

    def __fill_music_list_by_regions(self, p_regionsData, p_musicList):
        regionCounter = 0
        for region in p_regionsData:
            mType = region.descr_regions['music_type']
            for music_type in p_musicList:
                if mType == music_type.descr_sound_music_types['music_type']:
                    music_type.descr_sound_music_types["regions"].append(region.descr_regions['region_name'])
                    regionCounter += 1
                music_type.descr_sound_music_types["regions"] = sorted(music_type.descr_sound_music_types["regions"])
        assert regionCounter == MAX_NUM_REGIONS, "Number of regions for music_type.txt is different than MAX_NUM_REGIONS"
        return p_musicList
