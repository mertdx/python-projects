# -*- coding: utf-8 -*-
"""
Q8 Sorted Insert

@author: mertd
"""

def sorted_insert(data_list, num):
    data_list.append(num)
    data_list.sort()    
    return data_list

x = sorted_insert([1, 2, 4, 5 ,8 ,7 ,6], 3)
y = sorted_insert([1, 2, 4, 5 ,8 ,7 ,6], 22)
z = sorted_insert([1, 2, 4, 5 ,8 ,7 ,6], -3)
