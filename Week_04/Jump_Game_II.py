# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        max_reach, last_reach = 0, 0
        count = 0
        for i in range(len(nums)):
            max_reach = max(max_reach, nums[i] + i)
            if i == last_reach:
                last_reach = max_reach
                count += 1
                print(i)
                if max_reach >= len(nums) -1:
                    return count