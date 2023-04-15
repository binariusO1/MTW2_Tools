FILE_NAME = "descr_regions.txt"
FILE_NAME_EXPORT = "export_descr_regions_to_excel_paste_P2_OUTPUT.txt"


def concatenate_strings(arr):
    return ''.join(arr)


def run():
    file = open(FILE_NAME, "r", encoding="utf8")
    exportFile = open(FILE_NAME_EXPORT, "w", encoding="utf8")
    multiple = 0
    counter = 0
    word = ""
    titles = ["faction_1",
              "faction_2",
              "faction_3",
              "capital",
              "no_pirates",
              "knights_of_santiago_chapter_house",
              "templars_chapter_house",
              "teutonic_knights_chapter_house",
              "st_johns_chapter_house",
              "crusade",
              "jihad",
              "horde_target",
              "river",
              "desert",
              "silk_road",
              "hanse",
              "caravan",
              "slavemarket",
              "africa",
              "andalusia",
              "armenia",
              "berber",
              "crusader",
              "flanders",
              "prussia",
              "slavic",
              "tartars",
              "unique1",
              "unique2",
              "Constantinople",
              "santiago"]
    newWord = ['\t' for x in range(len(titles) + 3)]
    for i, line in enumerate(file):
        if i == 97 + (multiple + 1):
            print(line)
            all_words = line.split(", ")
            is_set_yes = False
            for i, word in enumerate(all_words):
                for j, title in enumerate(titles):
                    if word.endswith('\n'):
                        word = word[:-1]
                    if word[0] == '\t':
                        word = word[1:]
                    if word == title:
                        print(word, '==', title, '(', j, ')')
                        newWord[j] = '\t' + "yes"
                        is_set_yes = True
                        break
                if newWord[0] == '\t' and not is_set_yes:
                    print(word, '-[0]')
                    newWord[0] = word
                    is_set_yes = True
                elif newWord[1] == '\t' and not is_set_yes:
                    print(word, '-[1]')
                    newWord[1] = '\t' + word
                    is_set_yes = True
                elif newWord[2] == '\t' and not is_set_yes:
                    print(word, '-[2]')
                    newWord[2] = '\t' + word
                    is_set_yes = True
                if not is_set_yes :
                    print(word)
                    raise ValueError("Empty record!")
                is_set_yes = False

            multiple = multiple + 9
            concatenated = concatenate_strings(newWord)
            exportFile.write(concatenated+'\n')
            newWord = ['\t' for x in range(len(titles) + 2)]
    file.close()
    exportFile.close()


run()
