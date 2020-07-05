# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        d = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k not in d:
                d[k] = []
            d[k].append(s)
        for k in d:
            ans.append(d[k])
        return ans