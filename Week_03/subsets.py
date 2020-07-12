# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution:

    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res