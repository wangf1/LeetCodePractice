# https://leetcode.com/problems/number-of-islands/

import collections
from typing import List

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)
directions = (up, down, left, right)


class Solution:
    # BFS approach using queue
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

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

    # DFS approach
    def numIslands_DFS(self, grid: List[List[str]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int):
            if r not in range(m) or c not in range(n) or visited[r][c]:
                return
            visited[r][c] = True
            if grid[r][c] == '0':
                return
            for direct in directions:
                dfs(r + direct[0], c + direct[1])

        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c] == '1':
                    dfs(r, c)
                    result += 1

        return result
