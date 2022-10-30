# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = [[1]]

        def recur(row_index) -> List[int]:
            if row_index < 0:
                return None
            if row_index < len(memo):
                return memo[row_index]

            pre_row = recur(row_index - 1)

            row = [1] * (row_index + 1)
            for i in range(1, row_index):
                row[i] = pre_row[i - 1] + pre_row[i]
            memo.append(row)
            return row

        return recur(rowIndex)
