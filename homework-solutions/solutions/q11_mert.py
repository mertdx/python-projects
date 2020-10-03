# -*- coding: utf-8 -*-
"""
Q11 Only Words

@author: mertd
"""


def only_words(text):
    words = text.split()
    curr_index = 0
    for word in words:
        if word[-1].isalpha() is False:
            word = word[:-1]
            words[curr_index] = word
        elif word[0].isalpha() is False:
            word = word[1:]
            words[curr_index] = word
        curr_index += 1
    return words


x = only_words(
    "Examples of contractions 'include': don’t, isn’t, and wouldn’t.")
print(x)
