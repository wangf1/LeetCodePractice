import collections
from typing import List

from leetcodepractice.VerifyError import VerifyError


# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))
            while q:
                r_curr, c_curr = q.popleft()
                # r, c = q.pop() if use pop method, then it is DFS instead of BFS
                directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
                for dr, dc in directions:
                    r_new, c_new = r_curr + dr, c_curr + dc
                    if r_new in range(rows) and c_new in range(cols) and grid[r_new][c_new] == '1' and (
                            r_new, c_new) not in visited:
                        q.append((r_new, c_new))
                        visited.add((r_new, c_new))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    islands = Solution().numIslands(grid)
    if islands != 3:
        raise VerifyError(f"Should have 3 islands but has {0}", islands)
