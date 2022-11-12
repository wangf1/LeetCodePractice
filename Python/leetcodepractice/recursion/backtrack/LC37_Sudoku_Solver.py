# https://leetcode.com/problems/sudoku-solver/
from typing import List


class Solution:

    # Follow the back tracking template
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        complete = [False]

        def backtrack(r: int, c: int):
            if complete[0]:
                return
            if r == 8 and c == 8:
                complete[0] = True

            if c == 8:
                new_r = (r + 1) % 9
            else:
                new_r = r
            new_c = (c + 1) % 9

            if board[r][c] != '.':
                # For pre-set cell, should not do backtracking
                backtrack(new_r, new_c)
            else:
                for i in range(1, 10):
                    val = str(i)
                    if not is_valid_number_for_cell(val, r, c):
                        continue
                    board[r][c] = val
                    backtrack(new_r, new_c)
                    # When completed, no more backtracking
                    if complete[0]:
                        return
                    board[r][c] = '.'

        def is_valid_number_for_cell(val, r, c) -> bool:
            # check row
            if val in board[r]:
                return False
            # check column
            for r_index in range(9):
                if board[r_index][c] == val:
                    return False
            # check block
            r_start = r // 3 * 3
            c_start = c // 3 * 3
            for r_curr in range(r_start, r_start + 3):
                for c_curr in range(c_start, c_start + 3):
                    if board[r_curr][c_curr] == val:
                        return False
            return True

        backtrack(0, 0)


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    expected = [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

    Solution().solveSudoku(board)

    print(board)
    assert board == expected
