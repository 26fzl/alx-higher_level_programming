#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    reslt = 0
    for i in new:
        reslt += i
    return reslt
