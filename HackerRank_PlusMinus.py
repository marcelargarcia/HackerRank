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
    count_neg = sum(map(lambda x: x < 0, arr))
    count_zer = sum(map(lambda x: x == 0, arr))
    count_pos = len(arr) - count_neg - count_zer

    print("{:.6f}".format(float(count_pos/len(arr))))
    print("{:.6f}".format(float(count_neg / len(arr))))
    print("{:.6f}".format(float(count_zer / len(arr))))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
