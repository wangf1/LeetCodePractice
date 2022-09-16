# https://leetcode.com/problems/unique-paths/
from leetcodepractice.VerifyError import VerifyError


# sub-problem: cell = cell_right + cell_down ===> grid[i][j] = grid[i][j+1] + grid[i+1][j]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[m - 1][n - 1] = 1

        range_row = range(m - 1, -1, -1)
        range_col = range(n - 1, -1, -1)
        for row in range_row:
            for col in range_col:
                down = row + 1
                right = col + 1
                if down in range_row:
                    grid[row][col] += grid[down][col]
                if right in range_col:
                    grid[row][col] += grid[row][right]
        return grid[0][0]


if __name__ == '__main__':
    result = Solution().uniquePaths(3, 2)
    expected = 3
    if result != expected:
        raise VerifyError(f'Result should be {expected}, but get {result}')

    result = Solution().uniquePaths(3, 7)
    expected = 28
    if result != expected:
        raise VerifyError(f'Result should be {expected}, but get {result}')
