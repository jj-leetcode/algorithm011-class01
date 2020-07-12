# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        
        def could_place(row, col):
            return (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col]) == 0
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
            
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtracing(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row == n - 1: 
                        add_solution()
                    else:
                        backtracing(row+1)
                    remove_queen(row, col)
        backtracing()
        return output

