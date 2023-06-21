#!/usr/bin/python3
def copy_list(a_list):
    """return a_list[:]"""
    if a_list is None:
        return None
    else:
        new_list = []
        for i in a_list:
            new_list.append(i)
        return new_list
