# https://leetcode.com/problems/4sum-ii/description/
#from itertools import combinations

import math
def fourSumCount(nums1, nums2, nums3, nums4):
    hmap1 = {}
    hmap2 = {}
    result = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            sum = nums1[i] + nums2[j]
            if hmap1.get(sum,'Not Found') == 'Not Found':
                hmap1[sum] = [[nums1[i], nums2[j]]]
            else:
                hmap1[sum].append([nums1[i], nums2[j]])

    for m in range(len(nums1)):
        for l in range(len(nums2)):
            sum = nums3[m] + nums4[l]
            if hmap2.get(sum,'Not Found') == 'Not Found':
                hmap2[sum] = [[nums3[m], nums4[l]]]
            else:
                hmap2[sum].append([nums3[m], nums4[l]])

    for k1,v1 in hmap1.items():
        for k2, v2 in hmap2.items():
            if 0 <= k1 + k2 < len(nums1):
                result += math.comb(len(v1),len(v2))

    return result

print(fourSumCount([1,2], [-2, -1], [-1,2], [0,2]))
print(fourSumCount([0], [0], [0], [0]))



