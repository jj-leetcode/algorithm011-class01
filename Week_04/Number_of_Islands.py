# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        number_of_islands = 0
        if grid == []:
            return number_of_islands
        derections = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])

        def check(pos):
            x, y = pos
            if 0 <= x <= rows-1 and 0 <= y <= cols-1:
                return True
            else:
                return False

        for i in range(rows):
            for j in range(cols):
                cell = grid[i][j]
                if cell == '1':
                    grid[i][j] = '0'
                    number_of_islands += 1
                    Q = deque()
                    Q.append((i, j))
                    while Q:
                        (x, y) = Q.popleft()
                        for around in derections:
                            ax = around[0] + x
                            ay = around[1] + y
                            if check((ax, ay)) and grid[ax][ay] == '1':
                                Q.append((ax, ay))
                                grid[ax][ay] = '0'
        return number_of_islands
