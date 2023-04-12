from scripts.utils.logger import *

ASCII_A = 65


def column_char_to_int(char):
    if len(char) == 1:
        return ord(char) - ASCII_A
    elif len(char) == 2:
        return 26*(ord(char[0]) - ASCII_A+1) + (ord(char[1]) - ASCII_A)
    raise Exception("Excel column id is too big")


def collect_data_from_row(worksheet_name, col_start, col_end, row):
    # logger.INFO("collect_data_from_row()")
    value = []
    for j in range(column_char_to_int(col_start), column_char_to_int(col_end) + 1):
        value.append(worksheet_name.cell_value(row, j))
        # print(value)
    return value


class Cell:
    col = "A"
    row = 1

    def __init__(self, col, row):
        self.col = col
        self.row = row
