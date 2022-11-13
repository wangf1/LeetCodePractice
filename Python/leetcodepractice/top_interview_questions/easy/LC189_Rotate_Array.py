# https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        left = nums[:length - k]
        right = nums[-k:]

        for i in range(len(right)):
            nums[i] = right[i]
        for i in range(len(left)):
            nums[i + k] = left[i]

    def rotate_2(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        count = 0
        start = 0
        while count < length:
            curr_index = start
            curr_val = nums[curr_index]
            while True:
                next_index = (curr_index + k) % length
                tmp = nums[next_index]
                nums[next_index] = curr_val
                curr_val = tmp
                curr_index = next_index
                count += 1
                if curr_index == start:
                    break
            start += 1
