#!/usr/bin/python3
"""
utf-8 validator script
checks if the list of integers represent the correct encoding
of the utf-8
"""
from typing import List


def check(num):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    mask = 1 <<(8-1)
    i = 0
    while num & mask:
        mask >>= 1
        i += 1
    return i


def validUTF8(data: List) -> bool:
    """ validates if the data in list is
    a valid utf-8 encodeing"""
    i = 0
    while i < len(data):
        """ loops tru the datas in the list and
        performs a check operation on it"""
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1: return False
            i += 1
    return True
