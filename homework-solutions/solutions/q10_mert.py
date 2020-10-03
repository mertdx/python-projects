# -*- coding: utf-8 -*-
"""
Q10 Perfect Number

@author: mertd
"""

def is_perfect(num):
    sum1 = 0
    i = 1
    while i < num:
        if num % i == 0:
            sum1 += i
        i += 1
    if sum1 == num:
        return True
    else:
        return False
    
x = is_perfect(28)
y = is_perfect(30)
