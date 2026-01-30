#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
     arr.sort()
     n = len(arr)

     def median(a):
        m = len(a)
        if m % 2 == 0:
            return (a[m//2 - 1] + a[m//2]) // 2
        else:
            return a[m//2]

     q2 = median(arr)

     if n % 2 == 0:
         lower = arr[:n//2]
         upper = arr[n//2:]
     else:
         lower = arr[:n//2]
         upper = arr[n//2 + 1:]

     q1 = median(lower)
     q3 = median(upper)

     return [q1, q2, q3]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
