# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']
        if n < 0: return []
        res = []
        
        def dfs(l, r, path):
            if l == 0 and r == 0:
                res.append(path)
            elif l > r or l < 0:
                return
            else:
                dfs(l-1, r, path+'(')
                dfs(l, r-1, path+')')

        dfs(n, n, '')
        return res

