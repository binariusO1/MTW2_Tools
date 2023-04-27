import sys
from scripts.data.IData import *
from scripts.objects.Faction import *
from scripts.objects.Character import *
from scripts.objects.ModelStrat import *
from scripts.utils.Constants import *
from scripts.utils.custom import *
from scripts.utils.error_handling import *
from scripts.utils.read_excel import *
from scripts.utils.write_data import *


class DataFactions(IData):

    def __init__(self, p_mainPath, p_dataPath):
        IData.__init__(self, p_mainPath)
        self.dataPath = p_dataPath
        self.characterTypesList = []
        self.modelsStratList = []
        self.factionsList = []
        self.rebelFactionsList = []

    def load_all_data(self):
        IData.load_all_data(self)

        try:
            self.__load_factions_data()
            self.__load_characters_data()
            self.__load_rebel_factions_data()
        except FaultExcelData:
            LOG_ERROR("Exception occurred: FaultExcelData")
            finish_prgram()

    def get_factions_list(self):
        return self.factionsList

    def create_all(self):
        IData.create_all(self)
        self.create_descr_character()
        self.create_descr_model_strat()
        self.create_descr_sm_factions()
        self.create_descr_rebel_factions()

    def create_descr_sm_factions(self):
        LOG_INFO("Creating descr_sm_factions.txt file")

        l_dir = self.dataPath + DIR_DATA
        os.makedirs(l_dir, exist_ok=True)
        self.__write_descr_sm_factions(l_dir)

    def create_descr_rebel_factions(self):
        LOG_INFO("Creating descr_rebel_factions.txt file")

        l_dir = self.dataPath + DIR_DATA
        os.makedirs(l_dir, exist_ok=True)
        LOG_WARNING("empty function")
        # self.__write_descr_rebel_factions(l_dir)

    def create_descr_character(self):
        LOG_INFO("Creating descr_character.txt file")

        l_dir = self.dataPath + DIR_DATA
        os.makedirs(l_dir, exist_ok=True)
        self.__write_descr_character(l_dir)

    def create_descr_model_strat(self):
        LOG_INFO("Creating descr_model_strat.txt file")
        assert self.modelsStratList != [], "Models start list cannot be empty! Load models strat first."

        l_dir = self.dataPath + DIR_DATA
        os.makedirs(l_dir, exist_ok=True)
        self.__write_descr_model_strat(l_dir)

    # private

    # load

    def __load_characters_data(self):
        LOG_INFO("Load characters data")
        self.__load_models_strat_data()
        assert self.factionsList != [], "Factions list cannot be empty before load models strat data! Load factions first."
        assert self.modelsStratList != [], "Models start list cannot be empty before load characters data! Load models strat first."
        self.__fill_characters_list(FACTIONS_DATA_INPUT, MODELS_STRAT_SHEET_INDEX, 0, 1)

    def __load_factions_data(self):
        LOG_INFO("Load factions data")
        self.__fill_factions_list(FACTIONS_DATA_INPUT, FACTIONS_SHEET_INDEX, 0)

    def __load_rebel_factions_data(self):
        LOG_INFO("Load rebel factions data")
        LOG_WARNING("empty function")

    def __load_models_strat_data(self):
        LOG_INFO("Load models strat data")
        self.__fill_models_strat_list(FACTIONS_DATA_INPUT, MODELS_STRAT_SHEET_INDEX, 2)

    # fill

    def __fill_factions_list(self, p_workbook_name, p_worksheet_index, p_table_index):
        titles = get_titles_from_first_row(p_workbook_name, p_worksheet_index, p_table_index)
        factionsList = []
        for row in get_rows(p_workbook_name, p_worksheet_index, p_table_index):
            faction = Faction()
            is_horde = False
            horde_unit = []

            for i, title in enumerate(titles):
                value = row[i]
                if title == "r1":
                    faction.dictionary['primary_colour'].r = int(float(value))
                elif title == "g1":
                    faction.dictionary['primary_colour'].g = int(float(value))
                elif title == "b1":
                    faction.dictionary['primary_colour'].b = int(float(value))
                elif title == "r2":
                    faction.dictionary['secondary_colour'].r = int(float(value))
                elif title == "g2":
                    faction.dictionary['secondary_colour'].g = int(float(value))
                elif title == "b2":
                    faction.dictionary['secondary_colour'].b = int(float(value))
                elif title == "is_horde" and value == "yes":
                    faction.is_horde = True
                    is_horde = True
                elif is_horde:
                    if title == "horde_min_units":
                        faction.dictionary['horde_min_units'] = int(float(value))
                    elif title == "horde_max_units":
                        faction.dictionary['horde_max_units'] = int(float(value))
                    elif title == "horde_max_units_reduction_every_horde":
                        faction.dictionary['horde_max_units_reduction_every_horde'] = int(float(value))
                    elif title == "horde_unit_per_settlement_population":
                        faction.dictionary['horde_unit_per_settlement_population'] = int(float(value))
                    elif title == "horde_min_named_characters":
                        faction.dictionary['horde_min_named_characters'] = int(float(value))
                    elif title == "horde_max_percent_army_stack":
                        faction.dictionary['horde_max_percent_army_stack'] = int(float(value))
                    elif title == "horde_disband_percent_on_settlement_capture":
                        faction.dictionary['horde_disband_percent_on_settlement_capture'] = int(float(value))
                    elif title == "horde_unit":
                        horde_unit.append(value)
                    else:
                        faction.dictionary_horde['horde_unit'] = horde_unit
                        faction.dictionary[title] = value
                        is_horde = False
                elif title == '':
                    continue
                else:
                    faction.dictionary[title] = value
            factionsList.append(faction)
        self.factionsList = factionsList

    def __fill_characters_list(self, p_workbook_name, p_worksheet_index, p_table_wages_index, p_table_characters_index):

        # table 1

        titles = get_titles_from_first_row(p_workbook_name, p_worksheet_index, p_table_wages_index)
        characterTypesList = []
        for row in get_rows(p_workbook_name, p_worksheet_index, p_table_wages_index):
            characterType = CharacterType()
            for i, title in enumerate(titles):
                value = row[i]
                characterType.character[title] = value
            characterTypesList.append(characterType)
        self.characterTypesList = characterTypesList

        # table 2

        titles = get_titles_from_first_row(p_workbook_name, p_worksheet_index, p_table_characters_index)
        charactersList = []
        for row in get_rows(p_workbook_name, p_worksheet_index, p_table_characters_index):
            actualFaction = ""
            for i, title in enumerate(titles):
                # print(row)
                value = row[i]
                if title == "faction":
                    actualFaction = value
                else:
                    for characterType in self.characterTypesList:
                        if title == characterType.character['role']:
                            character = Character()
                            character.faction = actualFaction
                            # print(character.faction, ': ', title, value)
                            character.model_strat.append(value)
                            characterType.charactersList.append(character)

        self.__verify_models_strat_and_characters()

    def __fill_models_strat_list(self, p_workbook_name, p_worksheet_index, p_table_descr_models_index):
        titles = get_titles_from_first_row(p_workbook_name, p_worksheet_index, p_table_descr_models_index)
        modelStratList = []
        for row in get_rows(p_workbook_name, p_worksheet_index, p_table_descr_models_index):
            modelStrat = ModelStrat()
            for i, title in enumerate(titles):
                value = row[i]
                modelStrat.model_strat[title] = value
                # print(title)
            modelStratList.append(modelStrat)
        self.modelsStratList = modelStratList

    # write

    def __write_descr_sm_factions(self, p_creationPath):
        TEMPLATE_NAME = "descr_sm_factions.txt"
        TEMPLATE_NAME_HORDE = "descr_sm_factions_horde.txt"

        file = open(p_creationPath + TEMPLATE_NAME, "w", encoding="utf8")

        write_filestamp(file)
        self.__write_factions_data(file, TEMPLATE_NAME, TEMPLATE_NAME_HORDE)

        file.close()

    def __write_descr_model_strat(self, p_creationPath):
        TEMPLATE_NAME = "descr_model_strat.txt"
        TEMPLATE_NAME_INFO = "descr_model_strat_INFO.txt"

        file = open(p_creationPath + TEMPLATE_NAME, "w", encoding="utf8")

        write_filestamp(file)
        write_info(file, TEMPLATE_NAME_INFO)

        self.__write_descr_models_data(file, TEMPLATE_NAME)

        file.close()

    def __write_descr_character(self, p_creationPath):
        TEMPLATE_NAME = "descr_character.txt"
        TEMPLATE_NAME_INFO = "descr_character_INFO.txt"
        TEMPLATE_NAME_CHARACTERS = ["descr_character_named_character.txt",
                                    "descr_character_general.txt",
                                    "descr_character_admiral.txt",
                                    "descr_character_assassin.txt",
                                    "descr_character_diplomat.txt",
                                    "descr_character_merchant.txt",
                                    "descr_character_priest.txt",
                                    "descr_character_princess.txt",
                                    "descr_character_spy.txt",
                                    "descr_character_heretic.txt",
                                    "descr_character_witch.txt",
                                    "descr_character_inquisitor.txt" ]

        file = open(p_creationPath + TEMPLATE_NAME, "w", encoding="utf8")

        write_filestamp(file)
        write_info(file, TEMPLATE_NAME_INFO)
        for templateName in TEMPLATE_NAME_CHARACTERS:
            self.__write_descr_character_data(file, templateName)

        file.close()

    def __write_factions_data(self, file, p_template_name, p_template_name_horde):
        is_horde = False
        horde_fill = False

        for faction in self.factionsList[0:len(self.factionsList)]:
            if faction.is_horde:
                is_horde = True
                template_faction = get_empty_template(p_template_name_horde)
            else:
                is_horde = False
                template_faction = get_empty_template(p_template_name)

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
                        if lineTitle == "horde_unit" and is_horde:
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
            file.write('\n\n')
            file.write(get_separator() + '\n')

    def __write_descr_models_data(self, file, p_template_name):
        for mType in self.modelsStratList[0:len(self.modelsStratList)]:
            # print(mType)
            template = get_empty_template(p_template_name)

            file.write('\n\n')
            file.write(get_separator() + '\n')

            for line in template:
                all_words = line.split()
                lineTitle = all_words[0]
                if lineTitle == "type":
                    newLine = line.replace("TEXT", mType.model_strat['type'])
                    file.write(newLine)
                elif lineTitle == "skeleton":
                    newLine = line.replace("TEXT", mType.model_strat['skeleton'])
                    file.write(newLine)
                elif lineTitle == "scale":
                    newLine = line.replace("FLOAT", str(mType.model_strat['scale']))
                    file.write(newLine)
                elif lineTitle == "indiv_range":
                    newLine = line.replace("INT", str(int(mType.model_strat['indiv_range'])))
                    file.write(newLine)
                elif lineTitle == "texture":
                    for charType in self.characterTypesList:
                            for character in charType.charactersList:
                                for modelStrat in character.model_strat:
                                    if modelStrat ==  mType.model_strat['type']:
                                        if mType.model_strat['texture_format'] == '':
                                            newLine = line.replace("PREFIX_FACTION.FORMAT", mType.model_strat['texture_prefix'])
                                            newLine1 = newLine.replace("FACTION", character.faction)
                                            newLine2 = newLine1.replace("DIR", mType.model_strat['dir'])
                                            file.write(newLine2)
                                        else:
                                            newLine = line.replace("FACTION", character.faction)
                                            newLine1 = newLine.replace("DIR", mType.model_strat['dir'])
                                            newLine2 = newLine1.replace("PREFIX", mType.model_strat['texture_prefix'])
                                            newLine3 = newLine2.replace("FORMAT", mType.model_strat['texture_format'])
                                            file.write(newLine3)
                    # LOG_ERROR("TODO")
                elif lineTitle == "model_flexi_m":
                    newLine = line.replace("DIR", mType.model_strat['dir'])
                    newLine1 = newLine.replace("MODEL", mType.model_strat['model_flexi_m'])
                    file.write(newLine1)
                elif lineTitle == "shadow_model_flexi":
                    newLine = line.replace("DIR", mType.model_strat['dir'])
                    newLine1 = newLine.replace("MODEL", mType.model_strat['shadow_model_flexi'])
                    file.write(newLine1)

    def __write_descr_character_data(self, file, p_template_name):

        LOG_DEBUG("empty")

    def __verify_models_strat_and_characters(self):
        modelStratListToCheck = []
        for modelStrat in self.modelsStratList:
            modelStratListToCheck.append(modelStrat.model_strat['type'])
            # print(modelStrat.model_strat['type'])
        charactersListToCheck = []
        for characterType in self.characterTypesList:
            for character in characterType.charactersList:
                for modelStrat in character.model_strat:
                    charactersListToCheck.append(modelStrat)

        modelStratListToCheck = list(dict.fromkeys(modelStratListToCheck))
        # print(modelStratListToCheck)
        charactersListToCheck = list(dict.fromkeys(charactersListToCheck))
        uniqueElements1, uniqueElements2 = compare_lists(modelStratListToCheck, charactersListToCheck)
        if len(uniqueElements1) > 0:
            LOG_INFO("Models strat which are not assignee to table_2: ")
            print(uniqueElements1)
            LOG_INFO("See workbook: factions.xlsx, sheet: models_strat, table_2 and table_3")
        if len(uniqueElements2) > 0:
            LOG_WARNING("Models strat found in table_2 not defined in model table_3: ")
            print(uniqueElements2)
            LOG_WARNING("See workbook: factions.xlsx, sheet: models_strat, table_2 and table_3")
            raise FaultExcelData('Fault Excel Data')
