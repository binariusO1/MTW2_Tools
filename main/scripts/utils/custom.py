def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


def compare_lists(p_list_1, p_list_2):
    unique_elements = []
    unique_elements_1 = []
    unique_elements_2 = []
    for element in p_list_1:
        if element not in p_list_2 and element not in unique_elements:
            unique_elements.append(element)
            unique_elements_1.append(element)
    for element in p_list_2:
        if element not in p_list_1 and element not in unique_elements:
            unique_elements_2.append(element)
    unique_elements_1 = [x for x in unique_elements_1 if x != '']
    unique_elements_2 = [x for x in unique_elements_2 if x != '']
    return unique_elements_1, unique_elements_2