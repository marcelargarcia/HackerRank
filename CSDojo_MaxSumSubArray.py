# Source: CS Dojo = https://www.youtube.com/watch?v=86CQq3pKSUw&t=576s

# Problem: "Find the maximum sum of a sub array"
# Example:
#  [1,-3,2,1,-1] -> [2,1]

import sys

# Brute-force solution:
# Generate all possible subarrays (O(Nˆ2))
def maxSumSubArray_1(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr

    maxSum = - sys.maxsize - 1
    arr_result = []
    for i in range(len(arr)):
        sum_total = arr[i]
        sum_j = 0
        for j in range(i + 1, len(arr)):
            sum_j = sum_j + arr[j]
            sum_total = sum_total + arr[j]

            if sum_total > maxSum:
                maxSum = sum_total
                arr_result.clear()
                arr_result.append(arr[i])
                for k in range(i + 1, j + 1):
                    arr_result.append(arr[k])
    return arr_result


# Optimal Soluction:
# Keep track of local and global optimals.
# O(N) time
# O(N) space (could improve it if I stored indices instead of the array)
def maxSumSubArray_2(arr):
    if len(arr) ==0:
        return None
    if len(arr) == 1:
        return arr

    global_sum = local_sum = arr[0]
    arr_result = []
    arr_result.append(arr[0])
    contin = True
    for i in range(1, len(arr)):
        prev_local_sum = local_sum

        if contin:
            local_sum = max(arr[i], prev_local_sum, prev_local_sum + arr[i])
        else:
            local_sum = max(arr[i], prev_local_sum)

        if local_sum > global_sum:
            global_sum = local_sum

        if global_sum == arr[i]: #New Global Sum
            arr_result.clear()
            arr_result.append(arr[i])
            contin = True
        elif global_sum == prev_local_sum + arr[i]: #Summing the Global Sum
            arr_result.append(arr[i])
            contin = True
        else: #Previous Global Sum
            contin = False

    return arr_result

if __name__ == '__main__':
    arr1 = [1, -3, 2, 1, -1]

    print("Array 1: [1, -3, 2, 1, -1]")
    print("Result: [", end='') # should return 2, 1
    arr1_res = maxSumSubArray_2(arr1)
    for ar in arr1_res:
        print(str(ar) + ", ", end='')
    print("]")

    arr2 = [1, 2, 3, 4, 5]
    print("Array 2: [1, 2, 3, 4, 5]")
    print("Result: [", end='') # should return 1, 2, 3, 4, 5
    arr1_res = maxSumSubArray_2(arr2)
    for ar in arr1_res:
        print(str(ar) + ", ", end='')
    print("]")

    arr3 = [-1, -2, -3, -4, -5]
    print("Array 2: [-1, -2, -3, -4, -5]")
    print("Result: [", end='') # should return 1, 2, 3, 4, 5
    arr1_res = maxSumSubArray_2(arr3)
    for ar in arr1_res:
        print(str(ar) + ", ", end='')
    print("]")

    arr4 = []
    print("Array 2: []")
    print("Result: [", end='')  # should return 1, 2, 3, 4, 5
    arr1_res = maxSumSubArray_2(arr4)
    for ar in arr1_res:
        print(str(ar) + ", ", end='')
    print("]")