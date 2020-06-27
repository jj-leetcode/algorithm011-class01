# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def trap_naive(self, height):
        from_left = [0 for x in height]
        from_right = [0 for x in height]
        left_bar = 0
        for i in range(0, len(height), 1):
            if height[i] < left_bar:
                from_left[i] = left_bar - height[i]
            else:
                left_bar = height[i]
        right_bar = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] < right_bar:
                from_right[i] = right_bar - height[i]
            else:
                right_bar = height[i]
        ans = 0
        for i in range(len(height)):
            ans += min(from_left[i], from_right[i])
        return ans

    def trap_two_pointers(self, height):
        left, right = 0, len(height) - 1
        left_bar, right_bar = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_bar:
                    ans += left_bar - height[left]
                else:
                    left_bar = height[left]
                left += 1
            else:
                if height[right] < right_bar:
                    ans += right_bar - height[right]
                else:
                    right_bar = height[right]
                right -= 1
        return ans

    def trap_stack(self, height):
        stack = []
        ans = 0
        for i in range(len(height)):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                water_bottom = height[stack.pop()]
                if len(stack) == 0:
                    break
                left_bar_index = stack[-1]
                lefr_bar = height[left_bar_index]
                water_top = min(lefr_bar, height[i])
                water_height = water_top - water_bottom
                ans += water_height * (i - left_bar_index - 1)
            stack.append(i)
        return ans