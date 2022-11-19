# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            # Special boundary condition: target is the last element
            if target == nums[-1]:
                return len(nums) - 1

            mid = (lo + hi) // 2
            # mid and target are at same side of the pivot
            if (target > nums[-1] and nums[mid] > nums[-1]) or (target < nums[-1] and nums[mid] < nums[-1]):
                if target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            # target is at the left side of pivot, mid is at the right side of pivot
            elif target > nums[-1]:
                hi = mid
            # target is at the right side of pivot, mid is at the left side of pivot
            elif target < nums[-1]:
                lo = mid + 1
            else:
                assert False, "Program should never run into here!"

        return lo if nums[lo] == target else -1

    def search2(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1
        pivot = lo

        lo, hi = 0, len(nums) - 1
        n = len(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            real_mid = (mid + pivot) % n
            if nums[real_mid] == target:
                return real_mid
            if nums[real_mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


if __name__ == '__main__':
    # result = Solution().search([1, 2], 1)
    # assert result == 0, f"Wrong result: {result}"
    #
    result = Solution().search2([1, 2], 2)
    assert result == 1, f"Wrong result: {result}"
    #
    # result = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
    # assert result == 4, f"Wrong result: {result}"

    result = Solution().search2([4, 5, 6, 7, 0, 1, 2], 0)
    print(result)

    result = Solution().search2([0, 1, 2, 4, 5, 6, 7], 0)
    print(result)

    result = Solution().search2([4, 5, 6, 7, 0, 1, 2], 3)
    print(result)
