# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []: return False
        m = len(matrix)
        n = len(matrix[0])
        length = m*n - 1
        l, r = 0, length
        def cal_ij(mid):
            return mid//n, mid%n
        while l <= r:
            mid_point = (l + r) // 2
            i, j = cal_ij(mid_point)
            #print(mid_point, i, j, matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid_point-1
            else:
                l = mid_point+1
        return False