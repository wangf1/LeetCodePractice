# https://leetcode.com/problems/target-sum/
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, sum) -> int:
            cached = memo.get((i, sum))
            if cached:
                return cached

            ans: int
            if i == len(nums):
                if sum == target:
                    ans = 1
                else:
                    ans = 0
            else:
                ans = dfs(i + 1, sum + nums[i]) + dfs(i + 1, sum - nums[i])
            memo[(i, sum)] = ans
            return ans

        return dfs(0, 0)


if __name__ == '__main__':
    result = Solution().findTargetSumWays([5, 40, 23, 47, 43, 19, 36, 10, 28, 46, 14, 11, 5, 0, 5, 22, 39, 30, 50, 41],
                                          48)
    assert result == 5726
