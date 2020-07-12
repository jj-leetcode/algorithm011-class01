# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np

class Solution(object):
    def isValidBST_recursive(self, root):
        self.checker = -np.inf

        def trace(node):
            if node:
                l = trace(node.left)
                if self.checker >= node.val:
                    return False
                else:
                    self.checker = node.val
                r = trace(node.right)
            else:
                return True
            return l and r
        if not root:
            return True
        return trace(root)


class Solution(object):
    def isValidBST_iterative(self, root):

        my_stack = []
        node = root
        pre = None
        ans = True
        while node or my_stack:
            while node:
                my_stack.append(node)
                node = node.left
            node = my_stack.pop()
            if pre is None:
                pre = node.val
            else:
                if node.val <= pre:
                    ans = False
                    break
                else:
                    pre = node.val
            node = node.right
        return ans

