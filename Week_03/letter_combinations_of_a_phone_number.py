# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '': return []
        number_dict={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'         
        }
        res = []
        n = len(digits)
        def dfs(i, path):
            if i == n:
                res.append(path)
                return
            for k in number_dict[digits[i]]:
                dfs(i+1, path+k)
        dfs(0, '')
        return res