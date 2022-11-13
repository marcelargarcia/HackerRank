#https://leetcode.com/problems/intersection-of-two-arrays-ii

from itertools import repeat

#O(N)
def intersect_2(nums1, nums2):
    freqNumsSmal = {}
    freqNumsLarg = {}
    resultList = []

    if len(nums1) < len(nums2):
        smallNum = nums1
        largNum = nums2
    else:
        smallNum = nums2
        largNum = nums1

    for i in range(len(smallNum)):
        num = smallNum[i]
        value = freqNumsSmal.get(num,0)
        freqNumsSmal[num] = value + 1
    for j in range(len(largNum)):
        num = largNum[j]
        value = freqNumsLarg.get(num, 0)
        freqNumsLarg[num] = value + 1

    for k in range(len(smallNum)):
        num = smallNum[k]
        if num in freqNumsLarg:
            freqLarg = freqNumsLarg.get(num)
            freqSmall = freqNumsSmal.get(num)
            minFreq = min(freqLarg, freqSmall)
            resultList.extend(repeat(num, minFreq))
            freqNumsLarg.pop(num)
            freqNumsSmal.pop(num)

    return resultList

#O(N2)
def intersect_1(nums1, nums2):
    occuSet = set()
    resultList = []
    if len(nums1) < len(nums2):
        smallNum = nums1
        largNum = nums2
    else:
        smallNum = nums2
        largNum = nums1

    for i in range(len(smallNum)): #O(N2)
        num = smallNum[i]
        if num in largNum and num not in occuSet:
            minFreq = min(smallNum.count(num), largNum.count(num)) #O(N)
            resultList.extend(repeat(num,minFreq))
        occuSet.add(num)

    return resultList

print(intersect([1,2,2,1],[2,2]))
print(intersect([4,9,5],[9,4,9,8,4]))


####################################################################
# Input: 2 array [integers]
# Output: 1 array [integers] intersection

# What I want to know: if this number is in the other array
# If so, return the lower frequency. (freq1, freq2 -> lowest)

# 1, 2, 2, 1,1,1,1,1
# 2, 2, 2 ,2 ,2 ,2

# 1- Strategy
    # Loop i in the smallest array (list2)
    # For each integer, I will check:
        # set.add()
        # If is integer in list1 and is not in the set:
            # minfreq = min(count freq1, count freq2)
            # List_result.extend(repeat(integer,minfreq))

    # Cons:
        # Space Complexity - new set O(N) - worst case
        # Space Complexity - new list
    # Pros:
        # Time Complexity - O(N2)

# 2- Strategy
    #Space Complexity - O(N) - new hash map, result list
    #Time Complexity O(N)