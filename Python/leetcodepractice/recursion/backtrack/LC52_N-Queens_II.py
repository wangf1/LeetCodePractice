# https://leetcode.com/problems/n-queens-ii/


class Solution:
    def totalNQueens(self, n: int) -> int:
        result = [0]
        used_columns = set()
        asc_diagonals = set()
        desc_diagonals = set()

        def backtrack(r):
            if r == n:
                result[0] += 1
            for c in range(n):
                if c in used_columns or (r + c) in asc_diagonals or (r - c) in desc_diagonals:
                    continue

                used_columns.add(c)
                asc_diagonals.add(r + c)
                desc_diagonals.add(r - c)

                backtrack(r + 1)

                used_columns.remove(c)
                asc_diagonals.remove(r + c)
                desc_diagonals.remove(r - c)

        backtrack(0)
        return result[0]
