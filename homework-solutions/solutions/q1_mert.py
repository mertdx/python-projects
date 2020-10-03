# -*- coding: utf-8 -*-
# %%
"""
Q1 Black or White

@author: mertd
"""


def black_or_white(place):
    black_letters = ["a", "c", "e", "g"]
    black_numbers = ["1", "3", "5", "7"]
    white_letters = ["b", "d", "f", "h"]
    white_numbers = ["2", "4", "6", "8"]
    if place[0] in black_letters and place[1] in white_numbers:
        return "white"
    elif place[0] in white_letters and place[1] in black_numbers:
        return "white"
    else:
        return "black"


x = black_or_white("d3")
print(x)

# %%
