# https://leetcode.com/problems/powx-n/
class Solution:
    # Recursive approach is good.  Iterative approach performance is not acceptable
    def myPow(self, x: float, n: int) -> float:

        def recur(x: float, n: int):
            if n == 0:
                return 1
            if n % 2 == 0:
                half = recur(x, n // 2)
                return half * half
            else:
                half = recur(x, n // 2)
                return half * half * x

        if n >= 0:
            return recur(x, n)
        else:
            return 1 / recur(x, -n)
