

# ModelStrat
# |
# |


class ModelStrat:

    def __init__(self):


        self.model_strat = {}
        self.model_strat['type'] = ""
        self.model_strat['role'] = ""
        self.model_strat['skeleton'] = ""
        self.model_strat['scale'] = 0.0
        self.model_strat['indiv_range'] = 0
        self.model_strat['comment'] = 0
        self.model_strat['dir'] = ""
        self.model_strat['texture_prefix'] = ""
        self.model_strat['texture_format'] = ""
        self.model_strat['model_flexi_m'] = ""
        self.model_strat['shadow_model_flexi'] = ""

    def __repr__(self):
        return "{}: {}".format(self.model_strat['type'], self.model_strat['role'])
