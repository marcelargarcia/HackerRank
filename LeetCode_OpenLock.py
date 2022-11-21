import sys
from collections import deque

def openLock(deadends, target):
    deadends = set(tuple(deadends))
    root = '0000'
    turn = 0
    if target in deadends or root in deadends:
        return -1
    if target == root:
        return 0
    path = deque([root])
    while path:
        turn += 1
        q = len(path)
        for _ in range(q):
            p = path.popleft()
            for item in findMyPath(p, deadends):
                if item == target:
                    return turn
                else:
                    if item not in deadends and item not in path:
                        path.append(item)
            deadends.add(p)
    return -1

def findMyPath(code, deadends):
    code = tuple(map(int,code))
    pos = list(range(0,10))
    myPath = []

    for p in range(0,4):
        for i in (-1, 1):
            temp = []
            temp.extend(code)
            if i == 1:
                elem = pos[(code[p] + i) % len(pos)]
            else:
                elem = pos[(code[p] + i) % -len(pos)]
            temp[p] = elem
            temp = tuple(temp)
            temp_str = ''.join(map(str, temp))
            if temp_str not in deadends:
                myPath.append(temp_str)
    return myPath


print(openLock(["0201", "0101", "0102", "1212", "2002", "9202"], "0202"))
print(openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
print(openLock(["8887"], "0009"))