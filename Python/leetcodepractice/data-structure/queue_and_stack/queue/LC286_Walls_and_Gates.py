# https://leetcode.com/problems/walls-and-gates/

import collections
from typing import List


class Solution:
    # Use queue BFS approach.
    def wallsAndGates(self, rooms: List[List[int]]):
        m = len(rooms)
        n = len(rooms[0])
        inf = 2147483647
        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)
        directions = (up, down, left, right)

        for row in range(m):
            for col in range(n):
                que = collections.deque()
                visited = set()
                curr_val = rooms[row][col]
                if curr_val != inf:
                    continue
                curr_cell = (row, col)
                que.append(curr_cell)
                visited.add(curr_cell)
                step = 0
                while que:
                    for _ in range(len(que)):
                        cell = que.popleft()
                        val = rooms[cell[0]][cell[1]]
                        if val == -1:
                            continue
                        elif val == 0:
                            rooms[curr_cell[0]][curr_cell[1]] = step
                            que.clear()  # Clear the queue to terminate the outer while loop
                            break
                        else:
                            for direct in directions:
                                x = cell[0] + direct[0]
                                y = cell[1] + direct[1]
                                next_level_cell = (x, y)
                                if x in range(m) and y in range(n) and next_level_cell not in visited:
                                    que.append(next_level_cell)
                                    visited.add(next_level_cell)
                    step += 1
