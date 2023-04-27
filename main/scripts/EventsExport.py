from scripts.utils.logger import *
from scripts.utils.filestamp import *


class EventsExport:
    TEMPLATE_NAME = "descr_events.txt"
    TEMPLATE_NAME_INFO = "descr_events_INFO.txt"
    data_path = ""
    dir_templates = ""
    events = []

    def __init__(self, p_data_path, p_dir_templates, p_events):
        LOG_INFO("Run events export script")
        self.data_path = p_data_path
        self.dir_templates = p_dir_templates
        self.events = p_events

        self.__write_file()

    def __write_file(self):
        file = open(self.data_path + self.TEMPLATE_NAME, "w", encoding="utf8")

        self.__write_filestamp(file)
        self.__write_info(file, self.TEMPLATE_NAME_INFO)
        self.__write_events(file)

        file.close()

    def __write_filestamp(self, file):
        for line in get_filestamp():
            self.__get_empty_template_event()
            file.write(line + '\n')

    def __write_events(self, p_file):
        for event in self.events[0:len(self.events)]:
            template_event = self.__get_empty_template_event()
            p_file.write('\n')

            for line in template_event:
                all_words = line.split()
                lineTitle = all_words[0]
                if lineTitle == 'event':
                    newLine = line.replace("EVENT", event.descr_events["event_type"])
                    event_name = event.descr_events["event_name"]
                    if len(event_name) < 8:
                        event_name = event_name + '\t'
                    if len(event_name) < 16:
                        event_name = event_name + '\t'
                    if len(event_name) < 24:
                        event_name = event_name + '\t'
                    newLine2 = newLine.replace("TEXT", event_name)
                    newLine3 = newLine2.replace("DESC", event.descr_events["description"])
                    p_file.write(newLine3)
                elif lineTitle == 'date':
                    date = str(int(event.descr_events["date_start"]))
                    if event.descr_events["date_end"] != "":
                        date = date + ' ' + str(int(event.descr_events["date_end"]))
                    newLine = line.replace("TEXT", date)
                    p_file.write(newLine)
                elif lineTitle == 'position' and event.descr_events["position"].is_set():
                    position = str(int(event.descr_events["position"].x)) + ", " + str(
                        int(event.descr_events["position"].y))
                    newLine = line.replace("TEXT", position)
                    p_file.write(newLine)
                elif lineTitle == 'position' and not event.descr_events["regions"] == []:
                    for region in event.descr_events["regions"]:
                        # print("Region event: ", region)
                        if not region.descr_regions['region_name'] == '':
                            position = str(int(region.descr_strat['coordinates'].x)) + ", " + str(
                                int(region.descr_strat['coordinates'].y))
                            newLine = line.replace("TEXT", position)
                            p_file.write(newLine)
                elif lineTitle == 'movie' and not event.descr_events["movie"] == '':
                    newLine = line.replace("TEXT", event.descr_events["movie"])
                    p_file.write(newLine + '\n')
            p_file.write('\n')
            p_file.write(get_separator() + '\n')

        return

    def __write_info(self, file, info_file_name):
        info_file = open(self.dir_templates + info_file_name, "r", encoding="utf8")
        file.write('\n')
        for line in info_file:
            file.write(line)
        file.write('\n')
        info_file.close()

    def __get_empty_template_event(self):
        template_faction = []
        file = open(self.dir_templates + self.TEMPLATE_NAME, "r", encoding="utf8")
        for line in file:
            template_faction.append(line)
        # print(self.template_faction)
        file.close()
        return template_faction

    # def __get__coordinates_for_region(self):
    #     return
