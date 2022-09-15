# https://leetcode.com/problems/fibonacci-number/submissions/
from leetcodepractice.VerifyError import VerifyError


class Solution:
    _memory = {0: 0, 1: 1};

    def fib(self, n: int) -> int:
        if n in self._memory:
            return self._memory[n]
        else:
            self._memory[n] = self.fib(n - 1) + self.fib(n - 2)
            return self._memory[n]


class Solution2:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        previous = 0
        current = 1
        for i in range(2, n + 1):
            old_current = current
            current = previous + current
            previous = old_current
        return current


if __name__ == '__main__':
    r1 = Solution().fib(10)
    r2 = Solution2().fib(10)

    if not (r1 == r2 == 55):
        raise VerifyError(f"fib(10) should be 55, but {0} and {1}", r1, r2)
