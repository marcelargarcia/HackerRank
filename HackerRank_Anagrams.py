# c
#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

#O(n2)
def makeAnagram(a, b):
    delete = 0
    visited = []
    if isAnagram(a,b):
        return 0
    else:
        maxlen = max(len(a), len(b))
        for i in range(0, maxlen):
            if i < len(a) and a[i] not in visited and a.count(a[i]) != b.count(a[i]):
                visited.append(a[i])
                delete = abs(a.count(a[i]) - b.count(a[i])) + delete
            if i < len(b) and b[i] not in visited and a.count(b[i]) != b.count(b[i]):
                visited.append(b[i])
                delete = abs(a.count(b[i]) - b.count(b[i])) + delete
    return delete

def isAnagram(a, b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a.count(a[i]) != b.count(a[i]):
                return False
    return True

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
