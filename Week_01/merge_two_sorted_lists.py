# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None
        else:
            head = ListNode(0)
            p = head
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next            
            if l1:
                p.next = l1
            if l2:
                p.next = l2
        return head.next                    