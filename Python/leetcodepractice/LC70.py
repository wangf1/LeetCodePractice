# https://leetcode.com/problems/climbing-stairs/
from leetcodepractice.VerifyError import VerifyError


# c(1) -> 1
# c(2) -> 2 (1, 2)
# c(3) -> 3 (111, 12, 21)
# c(4) -> 5 (1111, 211, 121, 112, 22)
# c(5) -> 8 (11111, 2111, 1211, 1121, 1112, 221, 212, 122)
# I can guess that c(n) = c(n-2) + c(n-1), it is very similar to Fibonacci Number.
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
        raise VerifyError(f'ways of 7 steps should be 21, but {0}', result)
