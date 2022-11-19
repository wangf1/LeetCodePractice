# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/

from typing import List

from leetcodepractice.VerifyError import VerifyError


# Hash Table + Sliding Window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(s) < len(p):
            return result
        dict_p = {}
        dict_sub_s = {}
        for i in range(len(p)):
            c_p, c_s = p[i], s[i]
            dict_p[c_p] = 1 + dict_p.get(c_p, 0)
            dict_sub_s[c_s] = 1 + dict_sub_s.get(c_s, 0)

        if dict_p == dict_sub_s:
            result.append(0)

        for i in range(1, len(s) - len(p) + 1):
            c_remove = s[i - 1]
            dict_sub_s[c_remove] -= 1
            if dict_sub_s[c_remove] == 0:
                del dict_sub_s[c_remove]

            c_add = s[len(p) + i - 1]
            dict_sub_s[c_add] = 1 + dict_sub_s.get(c_add, 0)

            if dict_p == dict_sub_s:
                result.append(i)

        return result


if __name__ == '__main__':
    result1 = Solution().findAnagrams(s="abab", p="ab")
    expected = [0, 1, 2]
    if result1 != expected:
        raise VerifyError(f'Result should be {expected}, but get {result1}')
