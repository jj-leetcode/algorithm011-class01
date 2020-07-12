# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(node):
            if node:
                ans.append(node.val)
                dfs(node.left)
                dfs(node.right)
            else:
                ans.append('#')
        dfs(root)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == []:
            return None
        data = deque(data)
        def dfs():
            if data:
                val = data.popleft()
                if val == '#':
                    return None
                head = TreeNode(int(val))
                head.left = dfs()
                head.right = dfs()
                return head
        return dfs()
