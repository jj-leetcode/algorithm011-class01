# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def permuteUnique(self, nums):
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
        	nums.sort()
        	i=0
        	while i < len(n):
        		if i != 0:
        			print(i, 'flg', n)
        			while i < len(n) and n[i] == n[i-1]:
        				i += 1
        		if i < len(n):
        			key=n[i]
        			l = n[:i] + n[i+1:]
        			func(l, prefix+[key])
        			i += 1
        
        func(nums, [])
        return ans
