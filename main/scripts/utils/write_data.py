from scripts.utils.Constants import *
from scripts.utils.filestamp import *


def write_filestamp(file):
    for line in get_filestamp():
        file.write(line + '\n')


def write_info(file, info_file_name):
    info_file = open(DIR_TEMPLATES + info_file_name, "r", encoding="utf8")
    file.write('\n')
    for line in info_file:
        file.write(line)
    file.write('\n')
    info_file.close()


def get_empty_template(p_template_name):
    templates = []
    file = open(DIR_TEMPLATES + p_template_name, "r", encoding="utf8")
    for line in file:
        templates.append(line)
    file.close()
    return templates


def get_tabs(p_word, p_numberOfTabs):
    NUMBER_OF_CHARS_PER_WORD = 8
    firstNumberOfChars = 2
    wordLen = len(p_word)
    for num in range(p_numberOfTabs):
        if (firstNumberOfChars + num * NUMBER_OF_CHARS_PER_WORD + 1) > wordLen:
            return '\t' * (p_numberOfTabs - num + 1)
    return '\t'*p_numberOfTabs