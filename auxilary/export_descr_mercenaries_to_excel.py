FILE_INPUT = "descr_mercenaries.txt"
FILE_OUTPUT_REGIONS = "descr_mercenaries_output_regions regions are alphabetically).txt"
FILE_OUTPUT_UNITS = "descr_mercenaries_output_units.txt"


def export_file(p_input, p_output_regions, p_output_units):
    pools = []
    units = []
    with open(p_input, "r") as file:
        lines = file.readlines()
        regions = []
        actual_pool = ""
        actual_type = ""
        for line in lines:

            unit = {"pool": "", "unit": "", "type": "", "exp": 0, "cost": 0, "replenish_min": 0.0, "replenish_max": 0.0,
                    "max": 0, "initial": 0,
                    "start_year": 0, "end_year": 0, "catholic": "", "orthodox": "", "islam": "", "crusading": "",
                    "event_1": "", "event_2": ""}

            if "pool" in line and not ';' in line:
                actual_pool = line.split()[-1].strip()
                regions.append({'pool': actual_pool})
            elif "_Province" in line:
                all_words = line.split()
                for elem in all_words[1:]:
                    regions.append({'region': elem})
                pools.append(regions)
                regions = []
            elif "MISSILES" in line:
                actual_type = "missiles"
            elif "INFANTRY" in line:
                actual_type = "infantry"
            elif "CRUSADERS" in line:
                actual_type = "crusaders"
            elif "CAVALRY" in line:
                actual_type = "cavalry"
            elif "SPEARMEN" in line:
                actual_type = "spearmen"
            elif "ARTILLERY" in line:
                actual_type = "artillery"
            elif "SHIPS" in line:
                actual_type = "ships"
            elif "HEAVY INFANTRY" in line:
                actual_type = "heavy infantry"
            elif "unit" in line and not ';' in line:
                all_words = line.split()
                unit['pool'] = actual_pool
                unit['unit'] = all_words[1:all_words.index("exp")]
                unit['type'] = actual_type
                unit['exp'] = all_words[all_words.index("exp") + 1]
                unit['cost'] = all_words[all_words.index("cost") + 1]
                unit['replenish_min'] = all_words[all_words.index("replenish") + 1]
                unit['replenish_max'] = all_words[all_words.index("replenish") + 3]
                unit['max'] = all_words[all_words.index("max") + 1]
                unit['initial'] = all_words[all_words.index("initial") + 1]
                if "start_year" in line:
                    unit['start_year'] = all_words[all_words.index("start_year") + 1]
                if "end_year" in line:
                    unit['end_year'] = all_words[all_words.index("end_year") + 1]
                if "catholic" in line:
                    unit['catholic'] = "yes"
                if "orthodox" in line:
                    unit['orthodox'] = "yes"
                if "islam" in line:
                    unit['islam'] = "yes"
                if "crusading" in line:
                    unit['islam'] = "yes"
                if "events" in line:
                    unit['event_1'] = all_words[all_words.index("events") + 2]
                    if not all_words[all_words.index("events") + 3] == "" and not all_words[all_words.index("events") + 3] == "}":
                        unit['event_2'] = all_words[all_words.index("events") + 3]
                units.append(unit)
                # print(unit)

        # units

        with open(p_output_units, "w") as output:
            for un in units:
                for value in un.values():
                    if type(value) == list:
                        for element in value:
                            if element == value[-1]:
                                output.write(f"{element}\t")
                            else:
                                output.write(f"{element} ")
                    else:
                        output.write(f"{value}\t")
                output.write(f"\n")
                # print(unit)

        # regions

        aRegions = []
        aPools = []
        for pool in pools:
            # print(pool)
            poolValue = ""
            for i, elem in enumerate(pool):
                # print(elem)
                if i == 0:
                    poolValue = elem['pool']
                else:
                    aRegions.append(elem['region'])
                    aPools.append(poolValue)
                    # output.write(f"{elem['region']}\t{poolValue}\n")
        aRegions, aPools = sort_lists(aRegions, aPools)
        with open(p_output_regions, "w") as output:
            for i, elem in enumerate(aRegions):
                output.write(f"{aPools[i]}\n")
                # output.write(f"{elem['pool']}")

                # output.write(f"\t{elem['region']}")
            # output.write("\n")


def sort_lists(list1, list2):
    # sort list1 alphabetically
    sorted_list1 = sorted(list1)
    # create a list of tuples containing the index and the value of each element in list1
    indexed_list1 = list(enumerate(list1))
    # sort the indexed list based on the value of each element (which is the second element of each tuple)
    sorted_indexed_list1 = sorted(indexed_list1, key=lambda x: x[1])
    # extract the sorted indices from the sorted indexed list
    sorted_indices = [index for index, value in sorted_indexed_list1]
    # use the sorted indices to sort list2 in the same order as list1
    sorted_list2 = [list2[index] for index in sorted_indices]
    # return the sorted lists
    return sorted_list1, sorted_list2

export_file(FILE_INPUT, FILE_OUTPUT_REGIONS, FILE_OUTPUT_UNITS)
