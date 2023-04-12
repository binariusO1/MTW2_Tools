VERSION = 0.1


def get_separator():
    rowSeparator = ""
    for i in range(100):
        rowSeparator = rowSeparator + ";"
    return rowSeparator


def get_filestamp():
    filestamp = [get_separator(), ";", ";", ";", get_separator()]
    scriptStamp = " Generated for SSHIP by python multi tool. Version: " + str(VERSION) + " Author: binarius0110@gmail.com"
    filestamp[2] = filestamp[2] + scriptStamp
    # print(filestamp)
    return filestamp