#!/usr/bin/python3
def search_replace(my_list, search, replace):
    myn_list = my_list.copy()
    for i in range(len(my_list)):
        if myn_list[i] is search:
            myn_list.pop(i)
            myn_list.insert(i, replace)
    return myn_list
