# https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            for y in range(9):
                curr_val = board[x][y]
                if curr_val == '.':
                    continue
                board[x][y] = '.'
                # validate row
                if curr_val in board[x]:
                    return False
                # validate column
                for r in range(9):
                    if curr_val == board[r][y]:
                        return False
                # validate block
                start_row = x // 3 * 3
                start_col = y // 3 * 3
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        if curr_val == board[r][c]:
                            return False
                board[x][y] = curr_val
        return True
