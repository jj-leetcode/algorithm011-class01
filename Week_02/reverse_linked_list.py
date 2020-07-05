# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution(object):
    def reverseList(self, head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


class Solution(object):
    def reverseList_iter(self, head):
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        p = head
        pre = None
        while p and p.next:
            p.next, pre, p = pre, p, p.next
        p.next = pre
        return p

    def reverseList_recur(self, head):
        def _recursive(node, prev=None):
            if not node:
                return prev
            n = node.next
            node.next = prev
            return _recursive(n, node)
        return _recursive(head)
