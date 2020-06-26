# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        current = nums[0]
        tail = 1
        for ele in nums[1:]:
            if current != ele:
                current = nums[tail] = ele
                tail += 1
        #print(nums[:tail])
        return tail