#https://leetcode.com/problems/valid-sudoku

def isValidSudoku(board):
    mapPositions = {}

    for r in range(len(board)):
        r_key = "r" + str(r)
        for c in range(len(board)):
            c_key = "c" + str(c)
            s_key = calculateSqr(r, c)
            num = board[r][c]
            if num != ".":
                if not mapPosition(mapPositions, c_key, num) or not mapPosition(mapPositions, r_key,
                                                                                num) or not mapPosition(mapPositions,
                                                                                                        s_key, num):
                    return False
    return True

def mapPosition(hashMap, key, value):
    if hashMap.get(key, 'Not Found') == 'Not Found':
        hashMap[key] = set(value)
    else:
        if value in hashMap[key]:
            return False
        hashMap[key].add(value)
    return True


def calculateSqr(r, c):
    if r <= 2 and c <= 2:
        return "s_0"
    elif 3 <= r <= 5 and c <= 2:
        return "s_1"
    elif 6 <= r <= 8 and c <= 2:
        return "s_2"
    elif r <= 2 and 3 <= c <= 5:
        return "s_3"
    elif 3 <= r <= 5 and 3 <= c <= 5:
        return "s_4"
    elif 6 <= r <= 8 and 3 <= c <= 5:
        return "s_5"
    elif r <= 2 and 6 <= c <= 8:
        return "s_6"
    elif 3 <= r <= 5 and 6 <= c <= 8:
        return "s_7"
    else:
        return "s_8"


board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(isValidSudoku(board1))

board2 =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board2))

###############################################################
# Input: matrix
# Output: True/False
# Strategy:
# Build a hash map with 27 keys
# 9-rows -> set(1,2,3,9)
# 9-columns
# 9-squares
# While we're adding numbers in the hash map
# If we already have this number in this set