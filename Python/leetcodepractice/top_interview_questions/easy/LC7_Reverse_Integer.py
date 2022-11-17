# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        positive = True if x >= 0 else False
        if not positive:
            x = -x
        digits = []
        while x != 0:
            digits.append(x % 10)
            x = x // 10
        result = 0
        highest_bit = len(digits) - 1
        for i in range(len(digits)):
            result += digits[i] * 10 ** (highest_bit - i)
        if not positive:
            result = -result
        if not -2147483648 < result < 2147483647:
            result = 0
        return result
