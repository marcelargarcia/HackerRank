# https://leetcode.com/problems/target-sum
#continuar depois

def findTargetSumWays(nums, target):
    posToCheck = ['+0']
    posToCheck.append('-0')
    sum = 0
    res = 0
    while posToCheck:
        posTo = posToCheck.pop()
        operation = posTo[:1]
        pos = int(str(posTo[1:]))
        if operation == '+':
            sum += nums[pos]
        else:
            sum -= nums[pos]

        rtn = adjacents(nums, pos)
        if rtn[0] == None:  # No more adjacents, check SUM
            if sum == target:
                res += 1
            if operation == '+':
                sum -= nums[pos]
            else:
                sum += nums[pos]
        else:
            posToCheck.extend(rtn)

    return sum


def adjacents(nums, pos):
    if pos + 1 == len(nums):
        return [None]
    else:
        return ['+' + str(pos + 1), '-' + str(pos + 1)]

print(findTargetSumWays([2,2,3],6))


#[2,2,3], 6 = 1

# DFS:
#                     0
#         -2                     +2
#   -2          +2          -2         +2
# -3   +3      -3  +3      -3   +3     -3  +3
# -7    -1    -2    4      -4    0     0     6
#[+0,+1,]