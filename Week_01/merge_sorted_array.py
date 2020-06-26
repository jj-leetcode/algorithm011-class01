# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l1, l2, r = m-1, n-1, m+n-1        
        #print(l1, l2, r)
        while l1 >= 0 and l2 >=0 :
            #print(l1, l2, r)
            if nums1[l1] >= nums2[l2]:
                nums1[r] = nums1[l1]
                l1 -= 1
            else:
                nums1[r] = nums2[l2]
                l2 -= 1
            r -= 1      
        if l2 >= 0:
            print(l2)
            nums1[:r+1] = nums2[:l2+1]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m] + nums2
        nums1.sort()