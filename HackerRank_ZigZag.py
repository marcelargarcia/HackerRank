# https://leetcode.com/problems/zigzag-conversion/
from collections import deque
def convert(s, numRows):
    letters = len(s)
    numCols = 0
    matrix = []
    on = True
    while letters > 0:
        if on:
            letters = letters - numRows
            numCols = numCols +1
        else:
            letters = letters - (numRows - 2)
            numCols = numCols + 1
        on = not on
    s_deq = deque(s)
    i = j = 0
    while j < numCols:
        i = i - 1
        while i < numRows:
            matrix[i][j] = s_deq.popLeft()
            i = i + 1
