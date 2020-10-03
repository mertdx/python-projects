# -*- coding: utf-8 -*-
"""
Q9 Remove Outliers

@author: mertd
"""

def remove_outliers(data_list, allowed_range):
    result = [x for x in data_list if allowed_range[0] <= x <= allowed_range[1]]
    return result

x = remove_outliers([4, 7, 2, 9, 3, 8, 2, 6, 5, 12, -3], [3, 6])