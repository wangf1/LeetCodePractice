# https://leetcode.com/problems/move-zeroes/


from typing import List


class Solution:
    def moveZeroes_1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                nums[i - count_zero] = nums[i]

        for i in range(1, count_zero + 1):
            nums[-i] = 0

    # Two pointer approach
    def moveZeroes(self, nums: List[int]) -> None:
        insert_point = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_point] = nums[i]
                insert_point += 1
        for i in range(insert_point, len(nums)):
            nums[i] = 0
