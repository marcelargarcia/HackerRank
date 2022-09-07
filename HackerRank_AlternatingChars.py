# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#O(n)
def alternatingCharacters(s):
    queue_s = deque(s)
    new_s = []
    new_s.append(queue_s[0])
    q = 1
    while q < len(queue_s):
        if queue_s[q] != queue_s[q-1]:
            new_s.append(queue_s[q])
        q = q + 1

    return len(queue_s) - len(new_s)


#O(n2) - Time limit:
def alternatingCharacters_2(s):
    queue_s = deque(s)
    deletions = 0
    q = 1
    while q < len(queue_s):
        if queue_s[q] == queue_s[q-1]:
            del queue_s[q] #O(n)
            deletions = deletions + 1
        else:
            q = q + 1
    return deletions

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
