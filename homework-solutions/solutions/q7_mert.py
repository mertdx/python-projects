# -*- coding: utf-8 -*-
"""
Q7 Sorted List Check

@author: mertd
"""

def is_sorted(data_list):
    sorted_list = data_list.copy()
    sorted_list.sort()
    if data_list == sorted_list:
        return True
    else:
        return False
    
x = is_sorted([1, 2, 3, 4, 5])
y = is_sorted([2, 4, 3, 5, 1])    

