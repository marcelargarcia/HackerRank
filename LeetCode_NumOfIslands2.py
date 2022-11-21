# https://leetcode.com/problems/number-of-islands/

from collections import deque

#BFS - FIFO - Queue/Deque

def numIslands(grid):
    islands = 0
    onePos = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                onePos.add(tuple([i,j]))

    while onePos:
        queue = deque([onePos.pop()])
        islands += 1

        while queue:
            i,j = queue.popleft()
            for item in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if item in onePos:
                    onePos.remove(item)
                    queue.append(item)
    return islands



def numIslands_2(grid):
    to_check = deque()
    checked = []
    islands = 0
    onePos = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                onePos.add(tuple([i, j]))

    while onePos:
        pos = onePos.pop()
        to_check.append(pos)
        islands += 1

        while to_check:
            elem = to_check.popleft()
            if elem in onePos: onePos.remove(tuple(elem))
            neighbors = defineNeighbors(elem, grid, onePos, to_check)
            to_check.extend(neighbors)
            onePos = onePos - neighbors

    return islands

def defineNeighbors(elem, grid, onePos, queue):
    m = elem[0]
    n = elem[1]
    neig = set()
    if m > 0 and grid[m-1][n] == '1'  and [m-1,n] not in queue and (m-1,n) in onePos: neig.add(tuple([m-1,n]))
    if m < len(grid) -1 and grid[m+1][n] == '1' and [m+1,n] not in queue and (m+1,n) in onePos: neig.add(tuple([m+1,n]))
    if n > 0 and grid[m][n-1] == '1' and [m,n-1] not in queue and (m,n-1) in onePos: neig.add(tuple([m, n-1]))
    if n < len(grid[0]) -1 and grid[m][n+1] == '1' and [m,n+1] not in queue and (m,n+1) in onePos: neig.add(tuple([m,n+1]))

    return neig



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid2))
