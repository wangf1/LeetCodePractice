# https://leetcode.com/problems/maximum-subarray/
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
            max_sum = max(max_sum, dp[i])
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        sum = 0
        for i in nums:
            sum += i
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
        return max_sum
