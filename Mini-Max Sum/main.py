#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_num = min(arr)
    max_num = max(arr)
    sum_arr = sum(arr)
    min_sum = sum_arr - max_num
    max_sum = sum_arr - min_num
    print(min_sum, max_sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
