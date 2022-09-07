# https://leetcode.com/problems/two-sum/

#O(N)
def twoSum(nums, target):
    nums_dict = {}
    for i in range(len(nums)): #O(N)
        if nums_dict.get(nums[i],'Not Found') == 'Not Found': #O(1)
            nums_dict[nums[i]] = i
        else:
            value = nums_dict.get(nums[i]) #O(1)
            if not isinstance(value,list):
                nums_dict[nums[i]] = [value, i]

    for j in range(len(nums)): #O(N)
        frst = nums[j]
        scnd = target - frst
        if frst == scnd:
            value = nums_dict.get(frst)
            if isinstance(value,list):
                return [value[0], value[1]]
        else:
            if nums_dict.get(scnd, 'Not Found') != 'Not Found': #O(1)
                value = nums_dict.get(scnd)
                if isinstance(value, list):
                    return [j, value[0]]
                else:
                    return [j, value]

    return []


if __name__ == '__main__':
    print(twoSum([2,7,11,15],9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3,3], 6))
    print(twoSum([2,4,11,3], 6))
