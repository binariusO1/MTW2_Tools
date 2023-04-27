class FaultExcelData(Exception):
    print("fault")


class IData:
    main_path = ""

    def __init__(self, p_main_path):
        self.main_path = p_main_path

    def load_all_data(self):
        pass

    def create_all(self):
        pass
