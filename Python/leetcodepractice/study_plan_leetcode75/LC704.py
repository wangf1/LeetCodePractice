# https://leetcode.com/problems/binary-search/
from typing import List


# Recursive approach
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self._binary_search(nums, target, 0, len(nums) - 1)

    def _binary_search(self, nums: List[int], target: int, start: int, end: int):
        if start > end:
            return -1
        mid = (start + end) // 2
        current = nums[mid]
        if current == target:
            return mid
        elif current < target:
            return self._binary_search(nums, target, mid + 1, end)
        else:
            return self._binary_search(nums, target, start, mid - 1)


# Loop approach
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (end + start) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        return -1
