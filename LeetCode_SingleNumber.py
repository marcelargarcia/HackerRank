# https://leetcode.com/problems/single-number/description/

def singleNumber(nums):
    nums.sort()
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        if i > 0 and i < len(nums) -1:
            left = nums[i-1]
            right = nums[i+1]
            if nums[i] != left and nums[i] != right:
                return nums[i]
        elif i == 0 and i < len(nums) -1:
            right = nums[i+1]
            if nums[i] != right:
                return nums[i]
        elif i == len(nums) -1:
            left = nums[i-1]
            if nums[i] != left:
                return nums[i]


print(singleNumber([2,2,1]))