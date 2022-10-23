# https://leetcode.com/problems/min-stack/

import math


class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if self.data:
            curr_min = self.getMin()
        else:
            curr_min = math.inf
        self.data.append((val, min(curr_min, val)))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
