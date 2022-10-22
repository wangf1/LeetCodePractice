# https://leetcode.com/problems/number-of-islands/

import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)
        directions = (up, down, left, right)

        for row in range(m):
            for col in range(n):
                if visited[row][col] or grid[row][col] == '0':
                    continue
                que = collections.deque([(row, col)])
                visited[row][col] = True
                while que:
                    for _ in range(len(que)):
                        cell = que.popleft()
                        for direct in directions:
                            x = cell[0] + direct[0]
                            y = cell[1] + direct[1]
                            if x in range(m) and y in range(n) and not visited[x][y]:
                                visited[x][y] = True
                                if grid[x][y] == '1':
                                    que.append((x, y))
                result += 1

        return result
