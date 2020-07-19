# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.mystack = []
        node = root
        while node or self.mystack:
            while node:             
                self.mystack.append(node)
                node = node.left
            node = self.mystack.pop()
            self.ans.append(node.val)
            node = node.right
        return self.ans

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