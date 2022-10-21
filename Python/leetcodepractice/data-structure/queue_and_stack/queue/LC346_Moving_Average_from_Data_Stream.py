# https://leetcode.com/problems/moving-average-from-data-stream/
import collections


class MovingAverage:
    def __init__(self, size):
        self.que = collections.deque()
        self.size = size

    def next(self, val) -> int:
        if len(self.que) >= self.size:
            self.que.popleft()
        self.que.append(val)
        avg = sum(self.que) / len(self.que)
        return avg
