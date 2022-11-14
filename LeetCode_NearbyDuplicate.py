# https://leetcode.com/problems/contains-duplicate-ii/description/

import math
def containsNearbyDuplicate(nums, k):
    indexesMap = {}

    for i in range(len(nums)):
        num = nums[i]
        value = indexesMap.get(num,'Not Found')
        if value == 'Not Found':
            indexesMap[num] = i
        else:
            if not isinstance(value, list):
                indexesMap[num] = [value,i]
            else:
                indexesMap[num].append(i)

            value = indexesMap.get(num)
            numIndexes = len(value)

            if numIndexes > 1:
                for j in range(0,numIndexes-1):
                    if abs(i-j) <= k:
                        return True

    return False

print(containsNearbyDuplicate([1,2,3,1],3))
print(containsNearbyDuplicate([1,0,1,1],1))
print(containsNearbyDuplicate([1,2,3,1,2,3],2))

############################################################
# Input: 1 array, 1k
# Output: False/True

# [M,N] in this array [X,M,Y,N,Z]; M = N and abs(the position of M - position of N) <= K

# Strategy
    #1
    # Build a hash map nums -> [index1, index2, index3]
        # [1,1,1,1,1,1,1,1]
        # 1 -> [0,1,2,3,4,5,6,7]

        #If len(value(num)) in hash map > 1
            #For i in len(values(num))):
                #
        #Add Hash Map