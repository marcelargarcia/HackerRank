# https://www.hackerrank.com/challenges/save-the-prisoner/problem

import math
import os
import random
import re
import sys

# n number of prisioners
# m number of candy
# s position that will start


#Time limit:
def saveThePrisoner(n, m, s):
    pos = s
    for i in range(1, m):
        if pos == n and i != m:
            pos = 1
        else:
            pos = pos + 1
    return pos


#Wrong results:
def saveThePrisoner_2(n, m, s):
    if ((m % n) + s - 1) == n:
        return n
    else:
        return ((m % n) + s - 1) % n

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()