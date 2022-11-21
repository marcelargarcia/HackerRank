# https://leetcode.com/problems/two-sum/

def twoSum(nums, target): #O(N)
    nums_dict = {}
    for i in range(len(nums)): #O(N)
        num = nums[i]
        if nums_dict.get(num,'Not Found') == 'Not Found': #O(1)
            nums_dict[num] = i
        else:
            value = nums_dict.get(num) #O(1)
            if not isinstance(value,list):
                nums_dict[num] = [value, i]

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

#Necessita ajuste:
def allTwoSum(nums, target):
    res = []
    s = set()

    for i in range(len(nums)):
        if len(res) == 0 or res[-1][1] != nums[i]:
            k = target - nums[i]
            if k in s:
                kIndex = nums.index(k)
                res.append([kIndex, i])
        s.add(nums[i])

    return res

if __name__ == '__main__':
    # print(twoSum([2,7,11,15],9))
    # print(twoSum([3,2,4], 6))
    # print(twoSum([3,3,3], 6))
    # print(twoSum([2,4,11,3], 6))
    #
    # print(allTwoSum([2,7,11,15],9))
    # print(allTwoSum([3,2,4], 6))
    print(allTwoSum([3,3,3], 6))
    print(allTwoSum([2,4,11,3], 6))
