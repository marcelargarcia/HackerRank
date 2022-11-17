#https://leetcode.com/problems/4sum/
from itertools import combinations

def fourSum(nums, target):
    result = []
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
            res = list(combinations(value,2))
    return result


def fourSum_2(nums, target): #O(N2 LogN)
    result = []
    comb = list(combinations(nums, 4)) #O(r * (n choose r))
    for i in range(len(comb)): #O(N)
        listComb = sorted(list(comb[i])) #O(N logN) quick sort
        if sum(listComb) == target and listComb not in result:
            result.append(listComb)
    return result

#print(fourSum([1,0,-1,0,-2,2],0))
print(fourSum([2,1,2,1,3,0,3,0],6))
print(fourSum([2,2,2,2,2],8))
print(fourSum([],2))
print(fourSum([1],2))
print(fourSum([-5,5,4,-3,0,0,4,-2],4))