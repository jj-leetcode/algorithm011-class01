# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:return[nums]
        ans = []
        def func(n, prefix):
        	if len(n) == 1:
        		ans.append(prefix + n)
        		return
        	for i in range(len(n)):
        		key=n[i]
        		l = n[:i] + n[i+1:]
        		func(l, prefix+[key])
        
        func(nums, [])
        return ans
