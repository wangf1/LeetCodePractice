# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_index = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index
