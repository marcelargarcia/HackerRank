#https://leetcode.com/problems/3sum/

from collections import Counter
import itertools


#Terminar:
def threeSum(nums): #(N3 LogN)
    resp = set()
    temp = []
    allIndexes = {}
    twoSum = {}
    for n in range(len(nums)):
        num = nums[n]
        indexNum = allIndexes.get(num,'None')
        if indexNum == 'None':
            allIndexes[num] = n
        else:
            allIndexes[num] = [indexNum]
            allIndexes[num].append(n)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            value = twoSum.get(sum, 'None')
            if value == 'None':
                twoSum[sum] = [[i,j]]
            else:
                twoSum[sum].append([i,j])

    for sum,indexes in twoSum.items():
        targ = 0-sum
        indTarg = allIndexes.get(targ,'None')
        if indTarg != 'None':
            #\
                #and isinstance(indTarg, list):
            temp.extend(indexes)
            temp.append([indTarg])
            temp = list(itertools.product(*temp))
            temp.extend(list(itertools.product(indexes, indTarg)))
        else:
            temp.extend(list(itertools.product(indexes, [indTarg])))

    for t in range(len(temp)):
        print(itertools.chain(*temp[t]))
        print(''.join(str(s) for s in temp[t]))

    return resp

            # for x in range(len(indexes)):
            #     ind = indexes[x]
            #     ind1 = ind[0]
            #     ind2 = ind[1]
            #
            #     ind_set = set(tuple(ind + indTarg))
            #     if len(ind_set) == 3:
            #         three = sorted([nums[ind1], nums[ind2], nums[indTarg]])
            #         resp.add(tuple(three))

def threeSum_2(nums): #(N3 LogN)
    resp = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            target = 0 - sum
            if target in nums: #O(N)
                ind = nums.index(target) #O(N)
                if ind != i and ind != j:
                    three = sorted([nums[i], nums[j], target]) #O(N LogN)
                    resp.add(tuple(three))
    return resp

print(threeSum([-1,0,1,2,-1,-4]))
