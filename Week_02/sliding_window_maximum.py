# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return []
        if k == 1:
            return nums
        windows = deque()
        res = []

        def update_queue(index):
            if windows and windows[0] == index - k:
                windows.popleft()
            val = nums[index]
            while len(windows) != 0:
                if val > nums[windows[-1]]:
                    windows.pop()
                else:
                    break
            windows.append(index)

        for i in range(k):
            update_queue(i)
        res.append(nums[windows[0]])
        for i in range(k, len(nums)):
            update_queue(i)
            res.append(nums[windows[0]])
        return res
