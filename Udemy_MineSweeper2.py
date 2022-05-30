# https://www.udemy.com/course/11-essential-coding-interview-questions/learn/quiz/380026#questions
# O(N*M)
from collections import deque


# Implement your function below.
# DFS - backtracking
def click_DFS(field, num_rows, num_cols, given_i, given_j):
    if field[given_i][given_j] == -1 or field[given_i][given_j] >= 1:
        return field

    field[given_i][given_j] = -2

    for i in range(given_i - 1, given_i + 2):
        if i < 0 or i >= num_rows:
            continue
        for j in range(given_j - 1, given_j + 2):
            if j < 0 or j >= num_cols:
                continue
            if field[i][j] == 0:
                field[i][j] = -2
                click(field, num_rows, num_cols, i, j)

    return field

# BFS -
def click(field, num_rows, num_cols, given_i, given_j):
    if field[given_i][given_j] == -1 or field[given_i][given_j] >= 1:
        return field

    queue = deque()
    field[given_i][given_j] = -2

    i = given_i - 1
    j = given_j - 1

    while i in range(given_i - 1, given_i + 2):
        if i < 0:
            i += 1
            continue
        for j in range(given_j - 1, given_j + 2):
            if j < 0:
                j = 0
                continue
            if j >= num_cols:
                break
            if field[i][j] == 0:
                queue.append([i, j])
                field[i][j] = -2
        i += 1
        j = given_j - 1

        if (i == given_i + 2 or i == num_rows) and len(queue) > 0:
            next = queue.popleft()
            given_i = next[0]
            given_j = next[1]
            i = given_i - 1
            j = given_j - 1
        elif (i == given_i + 2 or i == num_rows) and len(queue) == 0:
            return field

    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

print(to_string(click(field1, 3, 5, 2, 2)))
# should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

print(to_string(click(field1, 3, 5, 1, 4)))
# should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

print(to_string(click(field2, 4, 4, 0, 1)))
# should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

print(to_string(click(field2, 4, 4, 1, 3)))
# should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
