# https://leetcode.com/problems/flood-fill
from collections import deque


def floodFill(image, sr, sc, color):
    to_check = deque()
    visited = set()
    to_check.append([sr, sc])
    iniColor = image[sr][sc]
    while to_check:
        elem = to_check.popleft()
        r = elem[0]
        c = elem[1]
        image[r][c] = color
        to_check.extend(adjacents(image, elem, iniColor, to_check, visited))
        visited.add(tuple(elem))
    return image

def adjacents(image, elem, iniColor, to_check, visited):
    # up
    r = elem[0]
    c = elem[1]
    adj = []
    if r - 1 >= 0 and image[r - 1][c] == iniColor and [r - 1, c] not in to_check and tuple([r - 1, c]) not in visited:
        adj.append([r - 1, c])
    if c - 1 >= 0 and image[r][c - 1] == iniColor and [r, c - 1] not in to_check and tuple([r, c - 1]) not in visited:
        adj.append([r, c - 1])
    if r + 1 < len(image) and image[r + 1][c] == iniColor and [r + 1, c] not in to_check and tuple([r + 1, c]) not in visited:
        adj.append([r + 1, c])
    if c + 1 < len(image[0]) and image[r][c + 1] == iniColor and [r, c + 1] not in to_check and tuple([r, c + 1]) not in visited:
        adj.append([r, c + 1])
    return adj

#print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
print(floodFill([[0,0,0],[0,0,0]],1,0,2))