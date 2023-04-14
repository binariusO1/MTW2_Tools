import os
from scripts.utils.logger import *
from scripts.utils.filestamp import *


def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


class RegionsExport:
    TEMPLATE_NAME = "descr_regions.txt"
    TEMPLATE_NAME_INFO = "descr_regions_INFO.txt"
    data_path = ""
    dir_templates = ""
    regions = []

    def __init__(self, data_path, dir_templates, regions):
        LOG_INFO("Run factions export script")
        self.data_path = data_path
        os.makedirs(self.data_path, exist_ok=True)
        self.dir_templates = dir_templates
        self.regions = regions

        self.__write_file()

    def __write_file(self):
        # print(self.data_path)
        file = open(self.data_path + self.TEMPLATE_NAME, "w", encoding="utf8")

        self.__write_filestamp(file)
        self.__write_regions(file)

        file.close()

    def __write_regions(self, file):
        for region in self.regions[0:len(self.regions)]:
            template_region = self.__get_empty_template_region()
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
                    print(region.descr_regions[key])
                    text = ""
                    for resource in region.descr_regions[key]:
                        text = text + resource + ", "
                    file.write('\t'+text[0:-1]+'\n')
                elif i == 8:
                    catholic = region.descr_regions[key].catholic
                    orthodox = region.descr_regions[key].orthodox
                    islam = region.descr_regions[key].islam
                    pagan = region.descr_regions[key].pagan
                    heretic = region.descr_regions[key].heretic
                    religions = "religions { catholic " + str(int(catholic)) + " orthodox " + str(int(orthodox)) \
                                + " islam " + str(int(islam)) + " pagan " + str(int(pagan)) + " heretic " + str(int(heretic)) + " }"
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

            file.write('\n\n')
            file.write(get_separator() + '\n')

    def __write_filestamp(self, file):
        for line in get_filestamp():
            self.__get_empty_template_region()
            file.write(line + '\n')

    def __get_empty_template_region(self):
        template_region = []
        file = open(self.dir_templates + self.TEMPLATE_NAME, "r", encoding="utf8")
        for line in file:
            template_region.append(line)
        # print(self.template_faction)
        file.close()
        return template_region
