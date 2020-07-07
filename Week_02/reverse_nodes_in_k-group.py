# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while p.next != tail.next:
            #p.next, prev, p = prev, p, p.next
            p, p.next, prev = p.next, prev, p
        p.next = prev
        return p, head

    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return dummy.next
        return hair.next