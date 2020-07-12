# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_max_depth(root, current_level):
            if root:
                current_level += 1
                return max(find_max_depth(root.left, current_level), find_max_depth(root.right, current_level))
            else:
                return current_level
        return find_max_depth(root, 0)