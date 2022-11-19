# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []
        lo, hi = 0, len(matrix)
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] > target:
                hi = mid
            elif matrix[mid][-1] < target:
                lo = mid + 1
            else:
                row = matrix[mid]
                break
        if not row:
            return False

        lo, hi = 0, len(matrix[0])
        while lo < hi:
            mid = (lo + hi) // 2
            if row[mid] > target:
                hi = mid
            elif row[mid] < target:
                lo = mid + 1
            else:
                return True

        return False

    # Simplified version: consider the matrix as single list
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo, hi = 0, m * n

        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid // n][mid % n] > target:
                hi = mid
            elif matrix[mid // n][mid % n] < target:
                lo = mid + 1
            else:
                return True

        return False
