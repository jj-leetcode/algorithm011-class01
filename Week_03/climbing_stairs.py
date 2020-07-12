# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        dp = [0] * n
        # n == 1
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1]  + dp[i-2]
        return dp[-1]


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        if n == 2:
            return 2
        ans = 2
        step1, step2 = 1, 2
        for i in range(3, n):
            ans = step1 + step2
            step1 = step2
            step2 = ans
        ans = step1 + step2
        return ans