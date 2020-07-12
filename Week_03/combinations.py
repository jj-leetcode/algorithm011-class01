# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k > n or k < 0:
            return []
        if k == 0:
            return [[]]
        nums = list(range(1, n+1))
        res = []
        def dfs(level, index, path):
            if level == k:
                res.append(path)
            else:
                for i in range(index, n):
                    dfs(level+1, i+1, path+[nums[i]])

        dfs(0, 0, [])
        return res

