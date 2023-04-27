from scripts.utils.logger import *
from scripts.utils.filestamp import *


class MusicTypeExport:
    TEMPLATE_NAME = "descr_sounds_music_types.txt"
    data_path = ""
    dir_templates = ""
    musicTypes = []

    def __init__(self, data_path, dir_templates, musicTypes):
        LOG_INFO("Run music export script")
        self.data_path = data_path
        self.dir_templates = dir_templates
        self.musicTypes = musicTypes

        self.__write_file()

    def __write_file(self):
        # print(self.data_path)
        file = open(self.data_path + self.TEMPLATE_NAME, "w", encoding="utf8")

        self.__write_filestamp(file)
        self.__write_music_types(file)

        file.close()

    def __write_filestamp(self, file):
        for line in get_filestamp():
            self.__get_empty_template_music_type()
            file.write(line + '\n')

    def __write_music_types(self, file):
        for musicType in self.musicTypes[0:len(self.musicTypes)]:
            # print(musicType)
            template_music_type = self.__get_empty_template_music_type()
            file.write('\n')

            for line in template_music_type:
                all_words = line.split()
                lineTitle = all_words[0]
                if lineTitle == 'regions':
                    regionsToWrite = ""
                    j = 0;
                    for i, region in enumerate(musicType.descr_sound_music_types['regions']):
                        j = i
                        regionsToWrite = regionsToWrite + region + ' '
                        if (i + 1) % 5 == 0:
                            newLine = line.replace("TEXT", regionsToWrite[:-1])
                            file.write(newLine)
                            regionsToWrite = ""
                    if not (j + 1) % 5 == 0:
                        newLine = line.replace("TEXT", regionsToWrite[:-1])
                        file.write(newLine)
                    file.write('\n')
                elif lineTitle == 'factions':
                    factionsToWrite = ""
                    for i, faction in enumerate(musicType.descr_sound_music_types['factions']):
                        factionsToWrite = factionsToWrite + faction + ' '
                    factionsToWrite = factionsToWrite + '\n'
                    newLine = line.replace("TEXT", factionsToWrite[:-1])
                    file.write(newLine)
                else:
                    textToWrite = str(musicType.descr_sound_music_types[lineTitle]) + '\n'
                    newLine = line.replace("TEXT", textToWrite)
                    file.write(newLine)
                # print(newLine)
            file.write('\n\n')
            file.write(get_separator() + '\n')
        return

    def __get_empty_template_music_type(self):
        template_music_type = []
        file = open(self.dir_templates + self.TEMPLATE_NAME, "r", encoding="utf8")
        for line in file:
            template_music_type.append(line)
        # print(self.template_faction)
        file.close()
        return template_music_type
