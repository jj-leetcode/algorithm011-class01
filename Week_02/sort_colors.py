# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for k in range(len(nums)):
            val = nums[k]
            nums[k] = 2
            if val < 2:
                nums[j] = 1
                j +=  1
            if val < 1:
                nums[i] = 0
                i += 1
