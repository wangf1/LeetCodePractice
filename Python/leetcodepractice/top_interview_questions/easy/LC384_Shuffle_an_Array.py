# https://leetcode.com/problems/shuffle-an-array/
from random import randint
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self._origin = nums.copy()

    def reset(self) -> List[int]:
        return self._origin.copy()

    def shuffle(self) -> List[int]:
        result = []
        nums = self._origin.copy()
        for _ in range(len(nums)):
            i = randint(0, len(nums) - 1)
            result.append(nums.pop(i))
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
