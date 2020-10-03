# -*- coding: utf-8 -*-
"""
Q3 Digits of The pi Number

@author: mertd
"""
a = 2
numerator = 4
pi = 3

for i in range(15):
    denominator = a * (a + 1) * (a + 2)
    if i%2 == 0:
        pi = pi + (numerator / denominator)
    else:
        pi = pi - (numerator / denominator)
    a += 2
    i += 1
    print(pi)    
    