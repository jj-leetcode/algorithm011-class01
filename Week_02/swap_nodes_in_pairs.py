# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current_front = dummy
        while current_front:
            if current_front.next:
                if current_front.next.next:
                    p1 = current_front.next
                    p2 = current_front.next.next
                    current_front.next, p2.next, p1.next = p2, p1, p2.next
                    current_front = current_front.next.next
                    #print(current_front.val)
                else:
                    current_front = current_front.next
            else:
                current_front = current_front.next
        return dummy.next


