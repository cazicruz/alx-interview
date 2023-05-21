#!/usr/bin/python3
""" utf-8 validator script
checks if the list of integers represent the correct encoding
of the utf-8"""
from typing import List


def check(num):
    """checks how many continuation bit the number has"""
        mask = 1 <<(8-1)
        i = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i


def validUTF8(data: List) -> bool:
    """ validates if the data in list id a valid utf-8 data"""
    i = 0
    while i < len(data):
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
