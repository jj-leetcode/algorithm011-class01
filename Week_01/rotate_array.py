# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]