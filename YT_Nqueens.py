# https://www.youtube.com/watch?v=jJPtLzq1E-Y&t=24s
# https://www.youtube.com/watch?v=wGbuCyNpxIg

def isValidPos(queensList, rw, clmn):
    if len(queensList) == 1:
        return True
    for i in range(len(queensList) - 1):
        rwList = queensList[i][0]
        clmnList = queensList[i][1]
        if rw == rwList or clmn == clmnList or abs(rw - rwList) / abs(clmn - clmnList) == 1:
            return False
    return True


def solveNQueens(n, clmnj):
    if clmnj == n:
        return True

    for rwi in range(0, n):
        #Our choice:
        queensList.append([rwi, clmnj])

        #Our Constraints
        if isValidPos(queensList, rwi, clmnj) and solveNQueens(n, clmnj+1):
            return True

        #Undo our choice:
        queensList.pop()

    return False

if __name__ == '__main__':
    global queensList
    queensList = []
    solveNQueens(4, 0)
    print(queensList)
