# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i, j = click
        row, col = len(board), len(board[0])
        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        candidates = ((-1, -1),
                      (0, -1),
                      (1, -1),
                      (-1, 0),
                      (1, 0),
                      (-1, 1),
                      (-0, 1),
                      (1, 1))

        def cal_bombs(i, j):
            res = 0
            for x, y in candidates:
                cx, cy = x+i, y+j
                if 0 <= cx < row and 0 <= cy < col:
                    if board[cx][cy] == 'M':
                        res += 1
            return res

        def dfs(i, j):
            count = cal_bombs(i, j)
            #print(count)
            if count > 0:
                board[i][j] = str(count)
            else:
                board[i][j] = 'B'
                for x, y in candidates:
                    nx, ny = x+i, y+j
                    if 0 <= nx < row and 0 <= ny < col:
                        if board[nx][ny] == 'E':
                            dfs(nx, ny)
        dfs(i, j)
        return board