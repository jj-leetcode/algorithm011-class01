# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) / 2
            #print(mid, l, r)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid] < nums[r] and target <= nums[r] or nums[l] < nums[mid] and nums[l]  < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > nums[l] and target >= nums[l] or nums[r] > nums[mid] and nums[r] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1



t = 3
nums = [5,1,3]
print(Solution().search(nums, t))