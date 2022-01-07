#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # Write your code here
    max_hourglass = -sys.maxsize - 1

    # 4 pra baixo
    for i in range(len(arr) - 2):

        # 4 pra direita
        for j in range(len(arr) - 2):
            soma_linha_1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            soma_linha_2 = arr[i + 1][j + 1]
            soma_linha_3 = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

            if (soma_linha_1 + soma_linha_2 + soma_linha_3) >= max_hourglass:
                max_hourglass = soma_linha_1 + soma_linha_2 + soma_linha_3

            #print(i)
            #print(j)
            #print(soma_linha_1 + soma_linha_2 + soma_linha_3)
            #print(max_hourglass)
            #print('\n')



    # ret = len(arr) + len(arr[1])

    return max_hourglass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
