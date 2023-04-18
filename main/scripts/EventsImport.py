import xlrd
from scripts.utils.logger import *
from scripts.data.Event import *
from scripts.utils.read_excel import *
from scripts.utils.constants import *


class EventsImport:
    REGIONS_SHEET_INDEX = 0
    EVENTS_SHEET_INDEX = 0
    dir_path_script = ""

    def __init__(self, dir_path_script, p_regionsData):
        LOG_INFO("Run events import script")
        self.dir_path_script = dir_path_script
        self.eventsList = []

        self.__run(p_regionsData)

    def get_list(self):
        return self.eventsList

    def __run(self, p_regionsData):
        workbook = xlrd.open_workbook(INPUT_XML_EVENTS)
        worksheet_name = workbook.sheet_by_index(self.EVENTS_SHEET_INDEX)
        range_start = get_tables_size(worksheet_name)[0]
        range_end = get_tables_size(worksheet_name)[1]
        titlesList = collect_first_row_as_titles(worksheet_name, range_start, range_end)
        self.eventsList = self.__fill_events_list(worksheet_name, range_start, range_end, titlesList)

        worksheet_name = workbook.sheet_by_index(self.REGIONS_SHEET_INDEX)
        range_start = get_tables_size(worksheet_name)[0]
        range_end = get_tables_size(worksheet_name)[1]
        titlesList = collect_first_row_as_titles(worksheet_name, range_start, range_end)
        self.__fill_events_list_by_regions(worksheet_name, range_start, range_end, titlesList, self.eventsList, p_regionsData)


    def __fill_events_list(self, p_worksheet_name, p_range_start, p_range_end, p_titles_list):
        l_eventsList = []
        for row in range(p_range_start.row, p_range_end.row):
            attrList = collect_data_from_row(p_worksheet_name, p_range_start.col, p_range_end.col, row)
            event = Event()

            x = 0
            regions = []
            for i, title in enumerate(p_titles_list):
                value = attrList[i]
                if title == 'x':
                    if value == "":
                        continue
                elif title == 'y':
                    if value == "":
                        continue
                    event.descr_events['position'] = Coordinates(x, value)
                    x = 0
                elif title == "region_name" and not value == '':
                    regions.append(value)
                else:
                    event.descr_events[title] = value
            if len(regions) > 0:
                event.descr_events['regions'] = regions
            l_eventsList.append(event)
        return l_eventsList

    def __fill_events_list_by_regions(self, worksheet_name, range_start, range_end, titles_list, p_eventsList, p_regionsData):
        regions = []
        for event in p_eventsList:
            if not event.descr_events['regions'] == []:
                for region in p_regionsData:
                    for eventRegion in event.descr_events['regions']:
                        if region.descr_regions['region_name'] == eventRegion:
                            regions.append(region)
                            # print(":", region.descr_strat['coordinates'])
                # print(event.descr_events['regions'])
            if len(regions) > 0:
                event.descr_events['regions'] = regions
                regions = []
        return p_eventsList