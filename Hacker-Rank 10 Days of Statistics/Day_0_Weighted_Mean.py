#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    weighted_sum = 0
    total_weight = 0

    for i in range(len(X)):
        weighted_sum += X[i] * W[i]
        total_weight += W[i]

    result = weighted_sum / total_weight
    print(f"{result:.1f}")
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
