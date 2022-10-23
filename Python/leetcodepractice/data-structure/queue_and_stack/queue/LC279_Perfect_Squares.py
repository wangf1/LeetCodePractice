# https://leetcode.com/problems/perfect-squares/submissions/

import collections


class Solution:
    # find the "virtual tree", and use BFS to solve the issue
    def numSquares(self, n: int) -> int:
        que = collections.deque([n])
        level = 0
        while que:
            for _ in range(len(que)):
                curr = que.popleft()
                i = 1
                while True:
                    remain = curr - i * i
                    if remain == 0:
                        level += 1
                        return level
                    if remain < 0:
                        break
                    que.append(remain)
                    i += 1
            level += 1
        return level
