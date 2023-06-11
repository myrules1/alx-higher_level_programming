#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list)!=0:
        maxint = 0
        ln = len(my_list)
        for i in my_list:
            if i > maxint:
                maxint = i
    else:
        return None
    return maxint
