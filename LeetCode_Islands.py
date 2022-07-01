# https://leetcode.com/problems/number-of-islands/
from collections import deque

# DFS
def numIslands_DFS(grid):
    to_check_stack = []
    islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                to_check_stack.append([r, c])
                islands = islands + 1
                while to_check_stack:
                    next = to_check_stack.pop()
                    grid[next[0]][next[1]] = 0
                    neig = getNeighbors(grid, next[0], next[1])
                    for k in range(len(neig)):
                        elem = neig[k]
                        if grid[elem[0]][elem[1]] == '1':
                            to_check_stack.append(elem)

    return islands


# BFS
def numIslands_BFS(grid):
    to_check = deque([])
    visited = []
    islands = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if [r,c] not in visited and grid[r][c] == '1':
                to_check.append([r, c])
                islands = islands + 1
            while to_check:
                next = to_check.popleft()
                to_check = addAdjacents(grid, visited, to_check, next[0], next[1])
                visited.append([next[0], next[1]])


    return islands

def addAdjacents(grid, visited, to_check, i, j):
    neig = getNeighbors(grid, i, j)
    for k in range(len(neig)):
        elem = neig[k]
        if elem not in visited and elem not in to_check and grid[elem[0]][elem[1]] == '1':
            to_check.append(elem)
    return to_check


def getNeighbors(grid, i, j):
    neig = []
    if j - 1 != -1:
        left = [i, j - 1]
        neig.append(left)
    if j + 1 != len(grid[0]):
        right = [i, j + 1]
        neig.append(right)
    if i - 1 != -1:
        up = [i - 1, j]
        neig.append(up)
    if i+1 != len(grid):
        down = [i + 1, j]
        neig.append(down)
    return neig





if __name__ == '__main__':
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(numIslands_BFS(grid1))
    print(numIslands_DFS(grid1))

    grid2 = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "0", "0", "0"],
        ["1", "0", "1", "0", "0"],
        ["1", "0", "0", "1", "1"]
    ]
    print(numIslands_BFS(grid2))
    print(numIslands_DFS(grid2))

    grid3 = [["1"]]
    print(numIslands_BFS(grid3))
    print(numIslands_DFS(grid3))