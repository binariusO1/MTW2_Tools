FILE_NAME = "descr_regions.txt"
FILE_NAME_EXPORT = "export_descr_regions_to_excel_paste_P1_OUTPUT.txt"

def run():
    file = open(FILE_NAME, "r", encoding="utf8")
    exportFile = open(FILE_NAME_EXPORT, "w", encoding="utf8")
    multiple = 0
    counter = 0
    word = ""
    for i, line in enumerate(file):
        all_words = line.split()
        if i == 92+(multiple+1):
            word = all_words[0] + '\t'
        elif i == 93+(multiple+1):
            word = word + all_words[0] + '\t'
        elif i == 94+(multiple+1):
            word = word + all_words[0] + '\t'
        elif i == 95 + (multiple + 1):
            word = word + all_words[0] + '\t'
        elif i == 96 + (multiple + 1):
            print(line)
            word = word + all_words[0] + '\t'
            word = word + all_words[1] + '\t'
            word = word + all_words[2] + '\t'
        elif i == 97 + (multiple + 1):
            continue
        elif i == 98 + (multiple + 1):
            continue
        elif i == 99 + (multiple + 1):
            word = word + all_words[0] + '\t'
        elif i == 100 + (multiple + 1):
            word = word + all_words[3] + '\t'
            word = word + all_words[5] + '\t'
            word = word + all_words[7] + '\t'
            word = word + all_words[9] + '\t'
            word = word + all_words[11]
            word = word + '\n'
            multiple = multiple + 9
            exportFile.write(word)
            word = ""
    file.close()
    exportFile.close()

run()
