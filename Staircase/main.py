#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    c = "#"
    for i in range(n):
        line = (n-i-1)*" "
        line += c*(i+1)
        print(line)
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
