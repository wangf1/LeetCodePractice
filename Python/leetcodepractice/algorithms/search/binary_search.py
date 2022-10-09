from typing import List


class Solution:
    def binary_search_1(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        return -1

    def binary_search_2(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if (lo < len(nums) and nums[lo] == target) else -1

    def binary_search_3(self, nums: List[int], target: int):

        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        # Post-processing:
        # End Condition: left + 1 == right
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


if __name__ == '__main__':
    result = Solution().binary_search_2([-1, 0, 3, 5, 9, 12], 9)
    assert result == 4

    result = Solution().binary_search_2([5], 5)
    assert result == 0
