# https://www.udemy.com/course/11-essential-coding-interview-questions
# O(N3)

# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    matrix = []
    clm_lst = []

    # Matrix with 0s
    matrix = [[0 for i in range(num_cols)] for j in range(num_rows)]

    # Add bombs and sum
    for x in range(len(bombs)): #qtt of bombs
        rw = bombs[x][0]
        clm = bombs[x][1]
        matrix[rw][clm] = -1
        for i in range(rw-1, rw+2):
            if i < 0 or i >= num_rows:
                continue
            for j in range(clm-1, clm+2):
                if j < 0 or j >= num_cols:
                    continue
                if matrix[i][j] != -1:
                    matrix[i][j] += 1


    return to_string(matrix)


def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    print('[' + ',\n '.join(list_rows) + ']')


# NOTE: The following input values will be used for testing your solution.
mine_sweeper([[0, 2], [2, 0]], 3, 3)
# should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)
# should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)
# should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]