#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    sw = 0
    i = 0
    while i < len(arr):
        if arr[i] -1 != i:
            temp = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = temp
            sw+=1
        else:
            i+=1
    return sw

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
