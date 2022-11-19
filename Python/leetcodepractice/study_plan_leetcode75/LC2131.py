# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = 0
        dict_ = {}
        for word in words:
            # print(f"word: {word}")
            key = word[::-1]
            # print(f"key: {key}")
            if key in dict_:
                # print(f"has key: {key}")
                count += 2
                dict_[key] -= 1
                if dict_[key] == 0:
                    del dict_[key]
            else:
                # print(f"put word: {word}")
                dict_[word] = 1 + dict_.get(word, 0)
        for key, _ in dict_.items():
            if key[0] == key[1]:
                count += 1
                break
        print(count * 2)
        return count * 2
