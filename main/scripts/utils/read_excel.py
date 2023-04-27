import xlrd
from scripts.utils.logger import *

ASCII_A = 65


class Cell:
    col = "A"
    row = 1

    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __repr__(self):
        return "({}, {})".format(self.col, self.row)


def address_to_cell(address):
    col = ''
    row = ''
    for char in address:
        if char.isalpha():
            col += char
        else:
            row += char
    return Cell(col, int(row))


def increment_column(column):
    if len(column) == 1:
        if column == 'Z':
            return 'AA'
        else:
            return chr(ord(column) + 1)
    else:
        last_char = column[-1]
        second_last_char = column[-2]
        if last_char == 'Z':
            if second_last_char == 'Z':
                return 'AAA'
            else:
                new_second_last_char = chr(ord(second_last_char) + 1)
                return column[:-2] + new_second_last_char + 'A'
        else:
            new_last_char = chr(ord(last_char) + 1)
            return column[:-1] + new_last_char


def decrement_column(column):
    if len(column) == 1:
        if column == 'A':
            return 'Z'
        else:
            return chr(ord(column) - 1)
    else:
        last_char = column[-1]
        second_last_char = column[-2]
        if last_char == 'A':
            if second_last_char == 'A':
                raise ValueError("Can't decrement column below 'A'")
            else:
                new_second_last_char = chr(ord(second_last_char) - 1)
                return column[:-2] + new_second_last_char + 'Z'
        else:
            new_last_char = chr(ord(last_char) - 1)
            return column[:-1] + new_last_char


def increment_cell_address(cell):
    newCol = increment_column(cell.col)
    newRow = cell.row + 1
    return Cell(newCol, newRow)


def decrement_cell_address(cell):
    newCol = decrement_column(cell.col)
    newRow = cell.row - 1
    return Cell(newCol, newRow)


def column_char_to_int(char):
    if len(char) == 1:
        return ord(char) - ASCII_A
    elif len(char) == 2:
        return 26 * (ord(char[0]) - ASCII_A + 1) + (ord(char[1]) - ASCII_A)
    raise Exception("Excel column id is too big")


def collect_data_from_row(worksheet_name, col_start, col_end, row):
    # logger.INFO("collect_data_from_row()")
    value = []
    for j in range(column_char_to_int(col_start), column_char_to_int(col_end) + 1):
        value.append(worksheet_name.cell_value(row, j))
        # print(value)
    return value


def get_rows(p_workbook_name, p_worksheet_index, p_table_index=0):
    workbook = xlrd.open_workbook(p_workbook_name)
    worksheet_name = workbook.sheet_by_index(p_worksheet_index)
    range_start = get_tables_size(worksheet_name)[p_table_index*2]
    range_end = get_tables_size(worksheet_name)[p_table_index*2 + 1]
    rows = []
    value = []
    for row in range(range_start.row, range_end.row):
        for col in range(column_char_to_int(range_start.col), column_char_to_int(range_end.col) + 1):
            value.append(worksheet_name.cell_value(row, col))
        rows.append(value)
        value = []
    return rows


def collect_first_row_as_titles(worksheet_name, range_start, range_end):
    titlesList = []
    for row in range(range_start.row - 1, range_start.row):
        titlesList = collect_data_from_row(worksheet_name, range_start.col, range_end.col, row)
    # print(titlesList)
    return titlesList


def get_titles_from_first_row(p_workbook_name, p_worksheet_index, p_table_index=0):
    workbook = xlrd.open_workbook(p_workbook_name)
    worksheet_name = workbook.sheet_by_index(p_worksheet_index)
    range_start = get_tables_size(worksheet_name)[p_table_index*2]
    range_end = get_tables_size(worksheet_name)[p_table_index*2 + 1]
    return collect_first_row_as_titles(worksheet_name, range_start, range_end)


def get_tables_size(worksheet_name):
    addresses = []
    i = 0
    while True:
        if worksheet_name.cell_value(0, i) == "" or worksheet_name.cell_value(1, i) == "":
            break
        cell1 = increment_cell_address(address_to_cell(worksheet_name.cell_value(0, i)))
        cell2 = decrement_cell_address(address_to_cell(worksheet_name.cell_value(1, i)))
        addresses.append(cell1)
        addresses.append(cell2)
        i += 1
    # print(addresses)
    return addresses
