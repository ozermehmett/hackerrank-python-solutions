#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    l = len(arr)
    p = 0
    s = 0
    e = 0
    for i in range(l):
        if arr[i] < 0:
            e+=1
        elif arr[i] == 0:
            s+=1
        else:
            p+=1
    print(f"{p/n:.6f}")
    print(f"{e/n:.6f}")
    print(f"{s/n:.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
