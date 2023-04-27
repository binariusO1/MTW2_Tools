FILE_INPUT = "descr_rebel_factions.txt"
FILE_OUTPUT = "descr_rebel_factions_OUTPUT.txt"


def export_descr_rebel_factions(input_, output_):
    with open(input_, "r") as file:
        lines = file.readlines()
        rebel_types = []

        for line in lines:
            if "rebel_type" in line:
                rebel = {"rebel_type": "", "category": "", "chance": "", "description": "", "unit": []}
                rebel_types.append(rebel)
                rebel["rebel_type"] = line.split("\t")[-1].strip()
            elif "category" in line:
                rebel["category"] = line.split("\t")[-1].strip()
            elif "chance" in line:
                rebel["chance"] = line.split("\t")[-1].strip()
            elif "description" in line:
                rebel["description"] = line.split("\t")[-1].strip()
            elif "unit" in line:
                un = line.split("\t")[-1].strip()
                rebel["unit"].append(un)

    with open(output_, "w") as output:
        for rebel in rebel_types:
            output.write(f"{rebel['rebel_type']}\t{rebel['category']}\t{rebel['chance']}\t{rebel['description']}\t")
            if rebel["unit"]:
                output.write("\t".join(rebel["unit"]))
            output.write("\n")


export_descr_rebel_factions(FILE_INPUT, FILE_OUTPUT)
