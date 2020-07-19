# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Solution(object):
    def minMutation(self, start, end, bank):
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }
        queue = [(start, 0)]

        while queue:
            node, step = queue.pop(0)

            if node == end:
                return step

            for i, s in enumerate(node):
                for c in change_map[s]:
                    node = node[:i] + c + node[i+1:]
                    # new = node[:i] + c + node[i+1:] way II
                    if node in bank:
                        queue.append((node, step+1))
                        # bank.remove(new) way II
                    node = node[:i] + s + node[i+1:]
        return -1
