# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import deque

class Solution(object):

    def numIslands(self, grid):
        count = 0
        visited = set([])
        h, w = len(grid), len(grid[0])

        def check_border(x, y):
            if 0<=x<=h-1 and 0<=y<=w-1:
                return True
            else:
                return False

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    count += 1
                    Q = deque()
                    Q.append((i, j))
                    visited.add((i, j))
                    grid[i][j] = '0'
                    while Q:
                        x, y = Q.popleft()
                        left, right, up, down = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
                        for m, n in [left, right, up, down]:
                            if check_border(m, n):
                                if grid[m][n] == '1' and (m, n) not in visited:
                                    Q.append((m,n))
                                    grid[m][n] = '0'
                                visited.add((m,n))
        return count