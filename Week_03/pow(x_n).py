# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Solution(object):
    def myPow_mine(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow(x, -n)
        else:
            y = self.myPow(x, n//2)  # do not repeat this line.
            if n % 2 == 0:
                return y * y
            else:
                return y * y * x


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1/self.myPow(x, -n)
        ans = 1
        while n:
            if n%2 != 0:
                ans *= x
            x *= x

            n = n / 2
        return ans
