# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from data_stucture import TreeNode

class Solution:

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.mystack = []
        node = root
        while node or self.mystack:
            while node:
                self.ans.append(node.val)             
                self.mystack.append(node)
                node = node.left
            node = self.mystack.pop()            
            node = node.right
        return self.ans