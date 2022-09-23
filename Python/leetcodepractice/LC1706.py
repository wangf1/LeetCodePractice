# https://leetcode.com/problems/where-will-the-ball-fall/
from typing import List


class Solution:
    _up = "up"
    _left = "left"
    _right = "right"

    def findBall(self, grid: List[List[int]]) -> List[int]:
        result0 = []
        m = len(grid)
        n = len(grid[0])

        for i in range(n):
            nxt_cel = (self._up, 0, i)
            loop = 0
            while True:
                loop += 1
                if not nxt_cel:
                    result0.append(-1)
                    break
                if nxt_cel[1] >= m:
                    result0.append(nxt_cel[2])
                    break
                if nxt_cel[2] < 0 or nxt_cel[2] >= n:
                    result0.append(-1)
                    break
                nxt_cel = self.next_cell(nxt_cel, grid)
            # For pass through case, loop = 2 * m + 1, which is bad than findBall2, which is m
            print(f"findBall: loop times for {i}:  {loop}")

        return result0

    # Return next cell, or None for stuck
    def next_cell(self, current_cell: tuple[str, int, int], grid: List[List[int]]) -> tuple[str, int, int] | None:
        entry_direction, row, col = current_cell[0], current_cell[1], current_cell[2]
        if entry_direction == self._up:
            if grid[row][col] == 1:
                # if col + 1 >= n:
                #     print(f"Stuck between {row, col} and right edge")
                return self._left, row, col + 1
            if grid[row][col] == -1:
                # if col - 1 < 0:
                #     print(f"Stuck between {row, col} and left edge")
                return self._right, row, col - 1
        if entry_direction == self._left:
            if grid[row][col] == 1:
                # if row + 1 >= m:
                #     print(f"Pass through from {row, col}")
                return self._up, row + 1, col
            if grid[row][col] == -1:
                # print(f"Stuck between {row, col} and {row, col + 1}")
                return None
        if entry_direction == self._right:
            if grid[row][col] == 1:
                # print(f"Stuck between {row, col} and {row, col + 1}")
                return None
            if grid[row][col] == -1:
                # if row + 1 >= m:
                #     print(f"Pass through from {row, col}")
                return self._up, row + 1, col

    def findBall2(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        result0: list[int] = list(range(n))
        loop = 0
        for r in range(m):
            for i in range(n):
                loop += 1
                c = result0[i]
                if c == -1:
                    continue
                c_next = c + grid[r][c]
                stuck_at_left_edge = c_next < 0
                if stuck_at_left_edge:
                    result0[i] = -1
                    # print(f"findBall2: Stuck between {r, c} and left edge.")
                    continue
                stuck_at_right_edge = c_next >= n
                if stuck_at_right_edge:
                    result0[i] = -1
                    # print(f"findBall2: Stuck between {r, c} and right edge.")
                    continue
                stuck_between_cells = grid[r][c_next] == -grid[r][c]
                if stuck_between_cells:
                    result0[i] = -1
                    # print(f"findBall2: Stuck between {r, c} and {r, c_next}.")
                    continue
                result0[i] = c_next
        print(f"findBall2: loop times {loop}")
        return result0


if __name__ == '__main__':
    result = Solution().findBall(
        [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]])
    expected = [0, 1, 2, 3, 4, -1]
    assert result == expected, f"Value should be {expected}, but {result}"

    result = Solution().findBall2(
        [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]])
    expected = [0, 1, 2, 3, 4, -1]
    assert result == expected, f"Value should be {expected}, but {result}"

    long_grid = [[1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1,
                  1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1],
                 [-1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1,
                  -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1],
                 [1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1,
                  1,
                  -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1]]
    result = Solution().findBall(long_grid)
    expected = [-1, -1, 1, -1, -1, -1, -1, 10, 11, -1, -1, 12, 13, -1, -1, -1, -1, -1, 17, -1, -1, 20, -1, -1, -1, -1,
                -1, -1, -1, -1, 27, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert result == expected, f"Value should be {expected}, but {result}"

    result = Solution().findBall2(long_grid)
    assert result == expected, f"Value should be {expected}, but {result}"
