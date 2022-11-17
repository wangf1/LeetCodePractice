# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transpose matrix
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # reflect matrix
        for r in range(n):
            for c in range(n // 2):
                matrix[r][c], matrix[r][-c - 1] = matrix[r][-c - 1], matrix[r][c]
