# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        target = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                target = nums[i]
            if target == nums[i]:
                count += 1
            else:
                count -= 1
        return target 