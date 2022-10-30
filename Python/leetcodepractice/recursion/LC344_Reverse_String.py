# https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    def reverseString_1(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseString(self, s: List[str]) -> None:

        def recur(s: List[str], start: int, end: int):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            recur(s, start + 1, end - 1)

        recur(s, 0, len(s) - 1)
