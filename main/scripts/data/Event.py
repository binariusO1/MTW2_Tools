from scripts.items.Coordinates import *


# Event
# |
# |--- Region []


class Event:
    def __init__(self):
        self.descr_events = {}
        self.descr_events["date_start"] = 0
        self.descr_events["date_end"] = 0
        self.descr_events["event_type"] = ""
        self.descr_events["event_name"] = ""
        self.descr_events["description"] = ""
        self.descr_events["movie"] = ""
        self.descr_events["position"] = Coordinates(0, 0)
        self.descr_events["regions"] = []

    def __repr__(self):
        return "{} ".format(self.descr_events['event_name'])
