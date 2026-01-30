#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    n = len(arr)
    mean = sum(arr) / n

    variance = sum((x - mean) ** 2 for x in arr) / n
    std_deviation = math.sqrt(variance)

    print(f"{std_deviation:.1f}")
    # Print your answers to 1 decimal place within this function

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
