# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        right = n - 1
        bottom = m - 1
        left = 0
        while True:
            if right < left:
                break
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            if bottom < top:
                break
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            if right < left:
                break
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
            if bottom < top:
                break
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
        return res

    # Use length to check break condition is also OK
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        total = m * n

        top = 0
        right = n - 1
        bottom = m - 1
        left = 0
        while True:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            if len(res) == total:
                break
            top += 1
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            if len(res) == total:
                break
            right -= 1
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            if len(res) == total:
                break
            bottom -= 1
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            if len(res) == total:
                break
            left += 1
        return res


if __name__ == '__main__':
    result = Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    result2 = Solution().spiralOrder2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert result == result2 == expected, f"Expect {expected} but {result} and {result2}"
