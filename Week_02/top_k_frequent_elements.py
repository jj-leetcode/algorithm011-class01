# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import groupby
from operator import itemgetter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for (j, v) in groupby(nums):
            res.append((j, len(list(v))))
        res.sort(key=itemgetter(1), reverse=True)
        return([x[0] for x in res[:k]])
l = [1,1,1,2,2,3]
k = 2
res = Solution().topKFrequent(l, k)