import os
import sys
from scripts.utils.constants import *

PATH_ROOT = os.path.dirname(os.path.realpath(__file__))
DIR_PATH_MAIN = os.path.dirname(os.path.realpath(__file__)) + "\\"
MAIN_FOLDER_NAME = os.path.basename(PATH_ROOT)
DATA_NUM = -1 * len(MAIN_FOLDER_NAME)
DATA_PATH = PATH_ROOT[0:DATA_NUM]
PATH_SCRIPTS = DIR_PATH_MAIN + DIR_SCRIPTS
PATH_TEMPLATES = DIR_PATH_MAIN + DIR_TEMPLATES
PATH_UTILS = PATH_SCRIPTS + DIR_UTILS
sys.path.insert(1, PATH_UTILS)

from scripts.utils.logger import *
from scripts.FactionsData import *
from scripts.FactionsImport import *
from scripts.FactionsExport import *
from scripts.RegionsData import *
from scripts.RegionsImport import *
from scripts.RegionsExport import *

def run_scripts():
    # for filename in os.listdir(PATH_SCRIPTS):
    # f = os.path.join(PATH_SCRIPTS, filename)
    # if os.path.isfile(f):
    #    print(f)
    factionsData = FactionsData(FactionsImport(DIR_PATH_MAIN).get_list())
    FactionsExport(DATA_PATH + DIR_DATA, DIR_TEMPLATES, factionsData.factionsDataList)

    regionsData = RegionsData(RegionsImport(DIR_PATH_MAIN).get_list())
    RegionsExport(DATA_PATH + DIR_BASE, DIR_TEMPLATES, regionsData.regionsDataList)

if __name__ == '__main__':
    LOG_INFO("Run main")
    run_scripts()
    LOG_INFO("End main")
