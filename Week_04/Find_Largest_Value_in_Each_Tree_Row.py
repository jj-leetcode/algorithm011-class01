# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root, depth):
            if not root: return 
            if len(res) <= depth:
                res.append(float("-inf"))
            res[depth] = max(res[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return res


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, cur = [], [root]
        while cur:
            nxt = []
            res.append(float("-inf"))
            for node in cur:
                res[-1] = max(res[-1], node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
        return res 
