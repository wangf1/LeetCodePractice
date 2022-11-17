# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
