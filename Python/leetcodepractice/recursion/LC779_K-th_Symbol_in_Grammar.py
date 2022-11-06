# https://leetcode.com/problems/k-th-symbol-in-grammar/
import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        memo = {}
        memo[(1, 1)] = 0

        def get_cell(n: int, k: int) -> int:
            if memo.get((n, k), None) != None:
                return memo[(n, k)]
            pre = get_cell(n - 1, int(math.ceil(k / 2)))
            if pre == 0:
                curr = [0, 1]
            else:
                curr = [1, 0]
            if k % 2 == 1:
                result = curr[0]
            else:
                result = curr[1]

            memo[(n, k)] = result
            return result

        return get_cell(n, k)
