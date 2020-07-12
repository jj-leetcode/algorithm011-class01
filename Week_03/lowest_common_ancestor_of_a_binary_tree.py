# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None: return None
        if root == p: return p
        if root == q: return q

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        elif l:
            return l
        elif r:
            return r