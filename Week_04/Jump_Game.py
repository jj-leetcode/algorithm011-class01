# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        max_reach = 0
        for i in range(len(nums)):
            max_reach = max(max_reach, nums[i] + i)
            if i >= max_reach: # 到达了就算
                return False
            if max_reach >= len(nums) -1: # 到达了就算
                return True
