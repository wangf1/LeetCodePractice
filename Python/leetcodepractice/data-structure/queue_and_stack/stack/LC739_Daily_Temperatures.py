# https://leetcode.com/problems/daily-temperatures/
# https://www.youtube.com/watch?v=cTBiBSnjO3c
from typing import List


# Monotonic Stack: Keep the stack Monotonically increasing/decreasing

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result
