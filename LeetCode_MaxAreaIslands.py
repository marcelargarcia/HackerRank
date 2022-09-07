# https://leetcode.com/problems/max-area-of-island/

# O(N2)
def maxAreaOfIsland(grid):
    area = 0
    maxArea = 0
    visited = []
    toCheck = []
    neig = []
    toCheck.append([0, 0])
    while toCheck:
        i, j = toCheck.pop()
        if [i, j] not in visited:
            neig = mapNeighbors(toCheck, visited, grid, i, j)  # O(1)
            if grid[i][j] == 1:
                area = calcArea(neig, grid, visited, i, j)  # O(N)
                if area > maxArea:
                    maxArea = area
        visited.append([i, j])
    return maxArea


def calcArea(neig, grid, visited, i, j):
    area = 1
    toCheck2 = []
    visited2 = []
    visited2.append([i, j])
    toCheck2.extend(neig)
    while toCheck2:
        m, n = toCheck2.pop()
        visited2.append([m, n])
        visited.append([m, n])
        if grid[m][n] == 1:
            area = area + 1
            mapNeighbors(toCheck2, visited2, grid, m, n)

    return area


def mapNeighbors(toCheck, visited, grid, i, j):
    neig = []
    # i - 1
    if isValid(grid, i - 1, j) and isNotInLists(i - 1, j, toCheck, visited):
        toCheck.append([i - 1, j])
    if isValid(grid, i - 1, j):
        neig.append([i - 1, j])

    # i
    if isValid(grid, i, j - 1) and isNotInLists(i, j - 1, toCheck, visited):
        toCheck.append([i, j - 1])
    if isValid(grid, i, j - 1):
        neig.append([i, j - 1])

    if isValid(grid, i, j + 1) and isNotInLists(i, j + 1, toCheck, visited):
        toCheck.append([i, j + 1])
    if isValid(grid, i, j + 1):
        neig.append([i, j + 1])

    # i + 1
    if isValid(grid, i + 1, j) and isNotInLists(i + 1, j, toCheck, visited):
        toCheck.append([i + 1, j])
    if isValid(grid, i + 1, j):
        neig.append([i + 1, j])

    return neig


def isValid(grid, i, j):
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
        return True
    else:
        return False


def isNotInLists(i, j, toCheck, visited):
    if [i, j] not in toCheck and [i, j] not in visited:
        return True
    else:
        return False


if __name__ == '__main__':
    grid1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(maxAreaOfIsland(grid1))

    grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
    print(maxAreaOfIsland(grid2))

    grid3 = [[1]]
    print(maxAreaOfIsland(grid3))
