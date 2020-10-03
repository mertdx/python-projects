# -*- coding: utf-8 -*-
"""
Q4 nextPrime() Function

@author: mertd
"""

def nextPrime(num):
    next_prime = num + 1
    prime = True
    while True:
        for i in range(2, next_prime):
            if next_prime % i == 0:
                prime = False
                break
        if prime:
            return next_prime
        else:
            next_prime += 1
            if next_prime % 2 == 0:
                next_prime += 1
            prime = True 
            
x = nextPrime(15)
