#!/usr/bin/env python3
"""Min Operations to get n H characters"""
from math import sqrt


def minOperations(n: int) -> int:
    increment = 1
    k = 1
    count = 1
    
    if n <= 0:
        return 0
    for i in range(n):
        if (n % k == 0 and (k != 1 and k != n)):
            increment = k
            count = count + 2
            k = k + increment
        else:
            if (k == n):
                return count
            k = k + increment
            count = count + 1
        if (k == n):
                return count