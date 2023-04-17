class MusicType:
    def __init__(self):
        self.descr_sound_music_types = {}
        self.descr_sound_music_types["music_type"] = ""
        self.descr_sound_music_types["regions"] = []
        self.descr_sound_music_types["factions"] = []

    def __repr__(self):
        return "{}: {}: {}".format(self.descr_sound_music_types['music_type'], self.descr_sound_music_types['factions'],   self.descr_sound_music_types["regions"])

class MusicTypeData:
    def __init__(self, musicTypeDataList):
        self.musicTypeDataList = musicTypeDataList