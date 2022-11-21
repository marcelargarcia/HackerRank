#https://leetcode.com/problems/4sum/
import itertools

def twoSum(nums, target):
    res = []
    lo, hi = 0, len(nums) - 1

    while (lo < hi):
        curr_sum = nums[lo] + nums[hi]
        if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
            lo += 1
        elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
            hi -= 1
        else:
            res.append([nums[lo], nums[hi]])
            lo += 1
            hi -= 1

    return res

def kSum(nums, target, k):
    res = []

    if not nums:
        return res

    # There are k remaining values to add to the sum. The
    # average of these values is at least target // k.
    average_value = target // k

    # We cannot obtain a sum of target if the smallest value
    # in nums is greater than target // k or if the largest
    # value in nums is smaller than target // k.
    if average_value < nums[0] or nums[-1] < average_value:
        return res

    if k == 2:
        return twoSum(nums, target)

    for i in range(len(nums)):
        if i == 0 or nums[i - 1] != nums[i]:
            for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                res.append([nums[i]] + subset)

    return res

def fourSum(nums, target):
    nums.sort()
    return kSum(nums, target, 4)



##Outros
def fourSum_1(nums, target): #O(N2 LogN) Run time
    result = set()
    comb = list(itertools.combinations(nums, 4)) #O(r * (n choose r))
    for i in range(len(comb)): #O(N)
        listComb = sorted(list(comb[i])) #O(N logN) quick sort
        if sum(listComb) == target:
            result.add(tuple(listComb))
    return result


def fourSum_2(nums, target): #O(N2) Wrong results
    result = []
    temp = []
    hashSums={}
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum = nums[i] + nums[j]
            value = hashSums.get(sum,'Not Found')
            if value == 'Not Found':
                hashSums[sum] = [[nums[i],nums[j]]]
            else:
                if [nums[i],nums[j]] not in value:
                    value.append([nums[i],nums[j]])

    for k,v in hashSums.items():
        targ = target - k
        value = hashSums.get(targ,'Not Found')
        if value != 'Not Found' and targ == k and len(value) >= 2:
            temp.extend(list(itertools.combinations(value,2)))
        elif value != 'Not Found' and targ != k:
            temp.extend(list(itertools.product(value,v)))

    for r in range(len(temp)):
        res = sorted(temp[r][0]+temp[r][1])
        if res not in result:
            result.append(res)


    return result

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3,3], 6))
print(twoSum([2,4,11,3], 6))
#
# print(fourSum([1,0,-1,0,-2,2],0))
# print(fourSum([2,1,2,1,3,0,3,0],6))
# print(fourSum([2,2,2,2,2],8))
# print(fourSum([],2))
# print(fourSum([1],2))
# print(fourSum([-5,5,4,-3,0,0,4,-2],4))