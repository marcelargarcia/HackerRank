#https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        return len(nums) != len(nums_set)
