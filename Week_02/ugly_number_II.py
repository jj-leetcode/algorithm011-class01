# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from heapq import heappop, heappush

class Solution(object):
    def __init__(self):
        self.res = self.get_n()

    def nthUglyNumber(self, n):
        return self.res[n-1]

    def get_n(self, max_n=1690):
        seen = set([])
        heap = []
        heappush(heap, 1)
        res = []
        for x in range(max_n):
            number = heappop(heap)
            res.append(number)
            for k in (2, 3, 5):
                new_number = number * k
                if new_number not in seen:
                    seen.add(new_number)
                    heappush(heap, new_number)
        return res


class Solution(object):
    def __init__(self):
        self.res = self.get_n()

    def nthUglyNumber(self, n):
        return self.res[n-1]

    def get_n(self, max_n=1690):
        dp = [1 for _ in range(max_n)]
        i, j, k = 0, 0, 0
        for e in range(1, max_n):
            m2, m3, m5 = dp[i]*2, dp[j]*3, dp[k]*5
            ugly = min(m2, m3, m5)
            if m2 == ugly: i+=1
            if m3 == ugly: j+=1
            if m5 == ugly: k+=1
            dp[e] = ugly
        return dp
        