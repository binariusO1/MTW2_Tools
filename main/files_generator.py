import os
import sys
from scripts.utils.Constants import *

PATH_ROOT = os.path.dirname(os.path.realpath(__file__))
DIR_PATH_MAIN = os.path.dirname(os.path.realpath(__file__)) + "\\"
MAIN_FOLDER_NAME = os.path.basename(PATH_ROOT)
DATA_NUM = -1 * len(MAIN_FOLDER_NAME)
DATA_PATH = PATH_ROOT[0:DATA_NUM]
PATH_SCRIPTS = DIR_PATH_MAIN + DIR_SCRIPTS
PATH_TEMPLATES = DIR_PATH_MAIN + DIR_TEMPLATES
PATH_UTILS = PATH_SCRIPTS + DIR_UTILS
sys.path.insert(1, PATH_UTILS)

from scripts.data.DataFactions import *
from scripts.data.DataRegions import *
from scripts.utils.logger import *
from scripts.EventsImport import *
from scripts.EventsExport import *
from scripts.MusicTypeImport import *
from scripts.MusicTypeExport import *


def run_scripts():
    # an order of imports is important
    factions = DataFactions(DIR_PATH_MAIN, DATA_PATH)
    factions.load_all_data()
    regions = DataRegions(DIR_PATH_MAIN, DATA_PATH)
    regions.load_all_data()

    # to refactor:
    dataRegions = regions.get_regions_list()
    eventsData = load_data_events(dataRegions)
    musicTypeData = load_data_music(dataRegions)
    # end

    regions.create_all()
    factions.create_all()

    # to refactor:
    EventsExport(DATA_PATH + DIR_IMPERIAL_CAMPAIGN, DIR_TEMPLATES, eventsData)
    MusicTypeExport(DATA_PATH + DIR_BASE, DIR_TEMPLATES, musicTypeData)
    # end

    # TODO
    # add recource checker (compare exported files with gfx files inside dir)

def load_data_events(p_regionsData):
    return EventsImport(DIR_PATH_MAIN, p_regionsData).get_list()


def load_data_music(p_regionsData):
    return MusicTypeImport(DIR_PATH_MAIN, p_regionsData).get_list()


if __name__ == '__main__':
    LOG_INFO("Run main")
    run_scripts()
    LOG_INFO("End main")
