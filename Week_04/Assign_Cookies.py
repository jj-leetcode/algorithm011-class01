# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        l_g = len(g)
        l_s = len(s)
        i = j = 0
        res = 0
        while i < l_g and j < l_s:
            while j < l_s and s[j] < g[i]:
                j += 1
            if i < l_g and j < l_s:
                if g[i] <= s[j]:
                    res += 1
            i += 1
            j += 1
        return res
        