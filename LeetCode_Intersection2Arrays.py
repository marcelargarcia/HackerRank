#https://leetcode.com/problems/intersection-of-two-arrays/

class Solution(object):
    def intersection(self, nums1, nums2):
        return set(nums1).intersection(set(nums2))
