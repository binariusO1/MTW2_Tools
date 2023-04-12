import sys
import os

DATA_FOLDER_NAME = "data"

DIR_PATH_STRIP = os.path.dirname(os.path.realpath(__file__))
DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\"
MAIN_FOLDER_NAME = os.path.basename(DIR_PATH_STRIP)
DATA_NUM = -1 * len(MAIN_FOLDER_NAME)
DATA_PATH = DIR_PATH_STRIP[0:DATA_NUM] + DATA_FOLDER_NAME + "\\"

DIR_SCRIPTS = "scripts" + "\\"
DIR_UTILS = "utils" + "\\"
DIR_TEMPLATES = "templates" + "\\"

PATH_SCRIPTS = DIR_PATH + DIR_SCRIPTS
PATH_TEMPLATES = DIR_PATH + DIR_TEMPLATES
PATH_UTILS = PATH_SCRIPTS + DIR_UTILS
# print(PATH_UTILS)
sys.path.insert(1, PATH_UTILS)

import logger
from scripts.FactionsImport import *
from scripts.FactionsExport import *

def run_scripts():
    for filename in os.listdir(PATH_SCRIPTS):
        f = os.path.join(PATH_SCRIPTS, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
    factionsImport = FactionsImport(DIR_PATH)
    FactionsExport(DATA_PATH, DIR_TEMPLATES, factionsImport.get_factions())


if __name__ == '__main__':
    logger.INFO("Run main")
    run_scripts()
    logger.INFO("\t end main")
    # input()
