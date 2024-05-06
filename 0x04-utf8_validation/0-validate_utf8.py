#!/usr/bin/python3
"""
script for task 0
"""


def validUTF8(data):
    """
    schecks if the data list is utf 8 compliant
    """
    skip = 0
    dat = len(data)
    for a in range(dat):
        if skip > 0:
            skip -= 1
            continue
        if type(data[a]) != int or data[a] < 0 or data[a] > 0x10ffff:
            return False
        elif data[a] <= 0x7f:
            skip = 0
        elif data[a] & 0b11111000 == 0b11110000:
            span = 4
            if dat - a >= span:
                next_b = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[a + 1: a + span],
                ))
                if not all(nxt_b):
                    return False
                skip = span - 1
            else:
                return False
        elif data[a] & 0b11110000 == 0b11100000:
            span = 3
            if dat - a >= span:
                next_b = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[a + 1: a + span],
                ))
                if not all(next_b):
                    return False
                skip = span - 1
            else:
                return False
        elif data[a] & 0b1110000 == 0b11000000:
            span = 2
            if dat - a > span:
                next_b = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[a + 1: a + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
