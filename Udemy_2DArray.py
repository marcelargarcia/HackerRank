# https://www.udemy.com/course/11-essential-coding-interview-questions
# O(N2)

import copy
import math

# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)

    for i in range(n):
        for j in range(n):
            value = given_array[i][j]
            rw = j
            clmn = n - 1 - i
            rotated[rw][clmn] = value
    return rotated

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    print('[' + ',\n '.join(list_rows) + ']')


# NOTE: The following input values will be used for testing your solution.
rotated = {}
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# to_string(rotate(a1, 3))
# to_string(rotate_2(a1, 3))
# should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
# to_string(rotate(a2, 4))
# to_string(rotate_2(a2, 4))
# should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]

a3 = [[1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25]]
# to_string(rotate(a3, 5))
# to_string(rotate_2(a3, 5))

