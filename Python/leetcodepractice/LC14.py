# https://leetcode.com/problems/longest-common-prefix/solution/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for i in range(len(s0)):
            for j in range(1, len(strs)):
                curr = strs[j]
                if len(curr) <= i or curr[i] != s0[i]:
                    return s0[0:i]
        return s0
