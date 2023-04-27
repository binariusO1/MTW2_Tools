

# CharacterType
# |
# |
# |--- Character []


class CharacterType:

    def __init__(self):
        self.character = {}
        self.character['role'] = ""
        self.character['wage_base'] = 0
        self.character['starting_action_points'] = 0
        self.charactersList = []

    def __repr__(self):
        return "{}".format(self.character['role'])


class Character:

    def __init__(self):
        self.faction = ""
        self.model_strat = []
        self.battle_model = ""

    def __repr__(self):
        return "{}".format(self.faction)
