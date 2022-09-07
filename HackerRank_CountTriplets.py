# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# !/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
from math import factorial
from collections import Counter

# O(n2)
def countTriplets(arr, r):
    elemn = {}
    count = 0
    non_rep = list(set(arr))

    elemn = Counter(arr)

    for i in range(len(non_rep)):
        next1 = non_rep[i] * r
        next2 = non_rep[i] * r * r

        if next1 in elemn and next2 in elemn:
            if r == 1:
                totalComb = elemn.get(non_rep[i])
                count = count + ((factorial(totalComb) / (factorial(totalComb - 3) * factorial(3))))
            else:
                totalComb = elemn.get(non_rep[i]) + elemn.get(next1) + elemn.get(next2)
                count = count + ((factorial(totalComb) / (factorial(totalComb - 3) * factorial(3))) - (
                        elemn.get(non_rep[i]) * elemn.get(next1) * elemn.get(next2)))

    return int(count)


# O(n2) - Wrong results
def countTriplets_2(arr, r):
    divisores = []
    for i in range(len(arr)):
        if arr[i] % r == 0 or arr[i] == 1:
            divisores.append(arr[i])

    comb = list(combinations(divisores, 3))  # O(n2)
    j = 0
    while j < len(comb):
        if j < len(comb) and (comb[j][2] / comb[j][1] != r or comb[j][1] / comb[j][0] != r):
            comb.pop(j)  # O(n)
        else:
            j += 1
    return len(comb)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
