# This is a demo task.
#
# Write a function:
#
#     def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].
#

def solution(A): #O(N)
    A.sort() #O(logN)
    i = 0

    while i < len(A): #O(N)
        if i < len(A) - 1 and A[i] > 0 and A[i] < A[i+1] - 1:
            return A[i] + 1
        elif i < len(A) - 1 and A[i] <= 0 and A[i+1] > 1:
            return 1
        i = i + 1
    if A[i-1] < 1 or A[0] > 1:
        return 1
    else:
        return A[len(A)-1] + 1


def solution_2(A):#O(N2)
    A.sort() #O(logN)
    count = 1
    i = 0
    retorno = 0
    found = False

    while not found and retorno != count: #O(N2)
        while i < len(A):
            if A[i] > 0 and A[i] == count:
                count = count + 1
                found = True
                i = 0
            else:
                found = False
                i = i + 1
        if not found:
            retorno = count
    return retorno



if __name__ == '__main__':
    # print(solution([1, 2, 3]))
    # print(solution([-3, -4]))
    # print(solution([1, 2, 3, 5, 6]))

    print(solution([1, 2, 3]) == 4)
    print(solution([-3, -4, 0, 2, 3, 4]) == 1)
    print(solution([-3, -4, 2, 3 ,4]) == 1)
    print(solution([-3, -4, 1, 2, 3, 4]) == 5)
    print(solution([1, 2, 3, 4, 5]) == 6)
    print(solution([0]) == 1)
    print(solution([-2, -3, 1, 2, 3, 3, 5, 3, 3, 6]) == 4)
    print(solution([2,2,2,2,2]) == 1)
    print(solution([2, 2, 3]) == 1)
    print(solution([1, 3, 6, 4, 1, 2]) == 5)
    print(solution([1]) == 2)
    print(solution([1,1,1,1,1]) == 2)
    print(solution([1, 1, 1, 1, 1]) == 2)
    print(solution([0, -1]) == 1)
    print(solution([0, 2]) == 1)
    print(solution([0, 2, 0]) == 1)
    print(solution([1, 5]) == 2)
    print(solution([-5, 0]) ==1)
    print(solution([0, 5]) == 1)