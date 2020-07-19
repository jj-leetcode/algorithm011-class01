# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None or []: 
            return []
        ans = []

        def bfs(root):
            my_q = deque([root])
            tmp = []
            ans.append([root.val])
            while my_q:
                node = my_q.popleft()
                tmp = []
                if node.left:
                    my_q.append(node.left)
                    tmp.append(node.left.val)
                if node.right:
                    my_q.append(node.right)
                    tmp.append(node.right.val)
                if tmp != []:
                    ans.append(tmp)
        bfs(root)
        return ans
