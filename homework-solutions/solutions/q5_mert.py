# -*- coding: utf-8 -*-
"""
Q5 Random Plate Number Generator

@author: mertd
"""
import random
import string


def random_plate_generator():
    banned_letters = ["Q", "W", "X"]
    ascii_letter_list = list(string.ascii_uppercase)
    letter_list = list(set(ascii_letter_list).difference(set(banned_letters)))
    plate_city = str(random.randrange(1, 82)).zfill(2)
    plate_numbers = str(random.randrange(1, 999)).zfill(2)
    plate_letters = ''.join(random.choice(letter_list) for i in range(2))
    return (plate_city + " " + plate_letters + " " + plate_numbers)


x = random_plate_generator()
print(x)
