# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans_set = {}
        for i in range(len(nums)):
            if nums[i] not in ans_set:
                ans_set[target - nums[i]] = i
            else:
                return [i, ans_set[nums[i]]]