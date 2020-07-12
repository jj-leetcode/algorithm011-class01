# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder != []:
            root = TreeNode(preorder.pop(0))
            i = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i+1:])
        return root