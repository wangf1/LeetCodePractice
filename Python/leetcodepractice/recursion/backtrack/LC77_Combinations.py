# https://leetcode.com/problems/combinations/
from typing import List


class Solution:

    # Approach 1: Dynamic programming (recursion + memo)
    def combine(self, n: int, k: int) -> List[List[int]]:

        memo = {}

        def combinations(nums: List[int], k: int) -> List[List[int]]:
            key = (str(nums), k)
            if key in memo:
                print(f"memo{key}: {memo[key]}")
                return memo[key]

            if k == 1:
                results = [[i] for i in nums]
                memo[key] = results
                return results

            results = []
            used_nums = set()

            for i in nums:
                used_nums.add(i)
                new_nums = [e for e in nums if e not in used_nums]
                if not new_nums:
                    break
                pre_results = combinations(new_nums, k - 1)
                for pre in pre_results:
                    result = [i]
                    result.extend(pre)
                    results.append(result)
            memo[key] = results
            return results

        return combinations([n for n in range(1, n + 1)], k)

    # Approach 2: backtracking
    def combine_2(self, n: int, k: int) -> List[List[int]]:
        sol = []

        def backtrack(remain, comb, nex):
            if remain == 0:
                sol.append(comb.copy())
            else:
                for i in range(nex, n + 1):
                    comb.append(i)
                    backtrack(remain - 1, comb, i + 1)
                    comb.pop()

        backtrack(k, [], 1)
        return sol


if __name__ == '__main__':
    results1 = Solution().combine(4, 3)
    print(results1)
