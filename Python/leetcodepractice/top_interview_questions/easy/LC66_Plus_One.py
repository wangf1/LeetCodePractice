# https://leetcode.com/problems/plus-one/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = (digits[i] + 1) // 10
        digits[i] = (digits[i] + 1) % 10
        i -= 1

        while i >= 0 and carry > 0:
            carry = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            i -= 1

        if carry > 0:
            digits.insert(0, carry)

        return digits
