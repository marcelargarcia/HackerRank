#https://leetcode.com/problems/perfect-squares

import math
from collections import deque
def numSquares(n):
    rest = n
    to_check = deque([rest])
    path = -1
    allPosSquares = list(range(1, (int(math.sqrt(n)))+1))
    checked = set()
    perfSq = isPerfectSquare(n)

    if perfSq != 0:
        return 1

    while to_check:
        q = len(to_check)
        path += 1
        while q > 0:
            elem = to_check.popleft()
            if elem == 0:
                return path
            perfSq = isPerfectSquare(elem)
            if perfSq != 0:
                new = int(elem - (math.pow(int(perfSq), 2)))
                to_check.append(new)
                if new == 0 and len(to_check) > 1:
                    to_check = deque(list(to_check)[int(len(to_check)-1):int(len(to_check))])
                    q=0
            else:
                for a in range(len(allPosSquares)):
                    new = int(elem - (math.pow(allPosSquares[a],2)))
                    if new < 0:
                        break
                    to_check.append(new)
            q -=1
            checked.add(elem)

    return path
def isPerfectSquare(n):
    sq = math.sqrt(n)
    if sq.is_integer():
        return sq
    else:
        return 0

print(numSquares(4))
print(numSquares(12))
print(numSquares(17))
print(numSquares(13))
print(numSquares(16))
print(numSquares(7168))