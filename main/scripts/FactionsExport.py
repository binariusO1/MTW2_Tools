import logger
from scripts.filestamp import *


class FactionsExport:
    FILE_NAME = "descr_sm_factions.txt"
    FILE_NAME_HORDE = "descr_sm_factions_horde.txt"
    data_path = ""
    dir_templates = ""
    factions = []

    def __init__(self, data_path, dir_templates, factions):
        logger.INFO("Run factions export script")
        self.data_path = data_path
        self.dir_templates = dir_templates
        self.factions = factions

        self.__write_file()

    def __write_file(self):
        # print(self.data_path)
        file = open(self.data_path + self.FILE_NAME, "w", encoding="utf8")

        self.__write_filestamp(file)
        self.__write_factions(file)

        file.close()

    def __write_filestamp(self, file):
        for line in get_filestamp():
            self.__get_empty_template_faction()
            file.write(line + '\n')

    def __write_factions(self, file):
        is_horde = False
        horde_fill = False

        for faction in self.factions[0:len(self.factions)]:
            if faction.is_horde:
                is_horde = True
                template_faction = self.__get_empty_template_horde_faction()
            else:
                is_horde = False
                template_faction = self.__get_empty_template_faction()

            file.write('\n')

            for line in template_faction:
                all_words = line.split()
                lineTitle = all_words[0]

                if lineTitle == "primary_colour" or lineTitle == "secondary_colour":
                    r = faction.dictionary[lineTitle].r
                    g = faction.dictionary[lineTitle].g
                    b = faction.dictionary[lineTitle].b
                    colour = "red " + str(r) + ", green " + str(g) + ", blue " + str(b)
                    newLine = line.replace("TEXT", colour)
                    file.write(newLine)
                else:
                    try:
                        if lineTitle == "horde_unit":
                            for unit in faction.dictionary_horde['horde_unit']:
                                newLine = line.replace("TEXT", unit)
                                file.write(newLine)
                        else:
                            newLine = line.replace("TEXT", str(int(faction.dictionary[lineTitle])))
                            file.write(newLine)
                    except ValueError:
                        textToWrite = str(faction.dictionary[lineTitle])
                        if is_horde and lineTitle == "faction":
                            textToWrite = textToWrite + ", spawned_on_event"
                        newLine = line.replace("TEXT", textToWrite)
                        file.write(newLine)
            file.write('\n')
            file.write('\n')
            file.write(get_separator() + '\n')

    def __get_empty_template_faction(self):
        template_faction = []
        file = open(self.dir_templates + self.FILE_NAME, "r", encoding="utf8")
        for line in file:
            template_faction.append(line)
        # print(self.template_faction)
        file.close()
        return template_faction

    def __get_empty_template_horde_faction(self):
        template_faction = []
        file = open(self.dir_templates + self.FILE_NAME_HORDE, "r", encoding="utf8")
        for line in file:
            template_faction.append(line)
        # print(self.template_faction)
        file.close()
        return template_faction
