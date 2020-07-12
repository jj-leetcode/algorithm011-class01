# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None

        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root


class Solution(object):
    def invertTree(self, root):

        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root