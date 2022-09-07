# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'sherlockAndAnagrams' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# O(n3)
def sherlockAndAnagrams(s):
    anam = 0
    list_comb = getCombinations(s) #O(n)???
    for i in range(len(list_comb)): #O(n)
        for j in range(i+1,len(list_comb)): #O(n)
            if len(list_comb[i]) == len(list_comb[j]) and isAnagram(list_comb[i], list_comb[j]): #O(n)
                anam = anam + 1
                #print(list_comb[i], list_comb[j])

    return anam

def sherlockAndAnagrams_2(s):
    anam = 0
    for i in range(len(s)): #O(n)
        for j in range(len(s)): #O(n)
            first = s[i:j]
            #second = s[]

def getCombinations(s):
    res = [s[x:y] for x, y in combinations(range(len(s) + 1), 2)]
    return res


def isAnagram(a, b):
    for i in range(len(a)):
        if a.count(a[i]) != b.count(a[i]):
            return False
    return True

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
