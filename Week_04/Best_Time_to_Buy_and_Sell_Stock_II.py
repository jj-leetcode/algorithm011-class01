# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        n = len(prices)
        buy = 0
        for i in range(1, n):
            d = max(prices[i] - prices[i-1], 0)
            buy += d
        return buy
