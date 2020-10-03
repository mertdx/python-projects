# -*- coding: utf-8 -*-
"""
Q2 Finding Real Roots of a Quadratic Function

@author: mertd
"""
import math

def find_real_roots(a,b,c): 
    disc = (b**2) - (4*a*c)
    
    if disc == 0:
        result = (-b + math.sqrt(disc)) / (2*a)
        print(f"Your equation has 1 real root and it's: {result}")
    elif disc > 0:
        result = (-b + math.sqrt(disc)) / (2*a)
        result = abs(result)
        print(f"Your equation has 2 real roots and they are: {result} and -{result}")   
    else:
        print("Your equation has no real roots.")
        
find_real_roots(1, 0, -4)
find_real_roots(1, 2, 1)
find_real_roots(1, 0, 1)

