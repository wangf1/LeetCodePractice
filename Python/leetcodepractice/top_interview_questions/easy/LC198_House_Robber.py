# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob_1(self, nums: List[int]) -> int:
        memo = [(0, nums[0])]

        # result[0] is the ammount exclude nums[end], result[1] is the ammount include nums[end]
        def dp(end: int) -> (int, int):
            if end < len(memo):
                return memo[end]
            pre = dp(end - 1)
            amount_without_end = max(pre[0], pre[1])
            amount_with_end = pre[0] + nums[end]
            result = (amount_without_end, amount_with_end)
            memo.append(result)
            # print(result)
            return result

        return max(dp(len(nums) - 1))

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        memo = [nums[0], max(nums[0], nums[1])]

        def dp(end: int) -> int:
            if end < len(memo):
                return memo[end]
            result = max(dp(end - 1), dp(end - 2) + nums[end])
            memo.append(result)
            return result

        return dp(len(nums) - 1)
