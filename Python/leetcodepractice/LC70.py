# https://leetcode.com/problems/climbing-stairs/
from leetcodepractice.VerifyError import VerifyError


# c(1) -> 1

# c(2) -> 2 (11, 2)

# c(3) -> 3 (111, 12, 21). Explanation: if take 1 step, has 2 ways: (111, 12); if take 2 steps, has 1 way: (21)


# c(4) -> 5 (1111, 112, 121, 211, 22). Explanation: if take 1 step, has 3 ways: (1111, 112, 121); if take 2 steps,
# has 1 way: (211, 22)


# I can see that c(n) = c(n-2) + c(n-1), I find out the sub-problem of dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1, 2]:
            return n
        previous = 1
        current = 2
        for _ in range(3, n + 1):
            old_current = current
            current = current + previous
            previous = old_current
        return current


if __name__ == '__main__':
    result = Solution().climbStairs(7)
    if result != 21:
        raise VerifyError(f'ways of 7 steps should be 21, but {result}')
