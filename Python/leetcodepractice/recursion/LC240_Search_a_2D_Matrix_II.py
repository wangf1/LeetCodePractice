# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix) and len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else:
                return True
        return False

    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:

        memo = {}

        def b_search(row: List[int], target: int, start, end) -> bool:
            if (start, end) in memo:
                return memo[(start, end)]

            if start >= end:
                memo[(start, end)] = False
                return memo[(start, end)]
            mid = (start + end) // 2
            if row[mid] == target:
                memo[(start, end)] = True
                return memo[(start, end)]
            if row[mid] < target:
                return b_search(row, target, mid + 1, end)
            else:
                return b_search(row, target, start, mid)

        for row in matrix:
            if b_search(row, target, 0, len(row)):
                return True
        return False
