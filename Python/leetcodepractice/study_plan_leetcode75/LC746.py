# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List

from leetcodepractice.VerifyError import VerifyError


# minCost(n-1) = cost[n-1]
# minCost(n-1)= cost[n-2]
# minCost(n-2) = cost[n-3] + min(minCost(n-1), minCost(n-2))
# I find out sub-problem of dynamic programming

# See https://www.youtube.com/watch?v=ktmzAZWkEZ0 for detail explanation for how to find sub-problems of dynamic
# programming

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])


if __name__ == '__main__':
    result = Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    expected = 6
    if result != expected:
        raise VerifyError(f'Result should be {expected}, but get {result}')
