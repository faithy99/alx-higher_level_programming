#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    if len(a_dictionary.values()) == 0:
        return None

    max_value = max(a_dictionary.values())

    for key, value in a_dictionary.items():
        if value == max_value:
            return 
