# -*- coding: utf-8 -*-
"""
Q6 TR Identity Number Validator

@author: mertd
"""

def is_valid_tcn(tcn):
    tcn = [int(x) for x in str(tcn)]
    all_number_check = [int(x) for x in str(tcn) if x.isdigit()]
    tenth_digit_check = ((sum(tcn[0:9:2])*7) - sum(tcn[1:9:2])) % 10
    eleventh_number_check = sum(tcn[0:10]) % 10
    if len(tcn) != 11 or tcn[0] == 0 or all_number_check != tcn:
        return False
    elif tenth_digit_check != tcn[9]:
        return False
    elif eleventh_number_check != tcn[10]:
        return False
    else:
        return True

x = is_valid_tcn(79851289650)
y = is_valid_tcn(36203837373)
z = is_valid_tcn(95339019908)

