# https://leetcode.com/problems/decode-string/
from collections import deque


class Solution:
    # Recursive approach is more complex than stack approach
    def decodeString2(self, s: str) -> str:
        return self._decode_recurr(s, 0, len(s))

    def _decode_recurr(self, s: str, begin: int, end: int) -> str:
        result = []
        i = begin
        while i < end:
            if not s[i].isdigit():
                result.append(s[i])
                i += 1
            else:
                bracket_index = s.find('[', i, end)
                repeat = int(s[i:bracket_index])
                matching_bracket_index = self.find_matching_bracket(s, bracket_index + 1, end)
                sub_str_decoded = self._decode_recurr(s, bracket_index + 1, matching_bracket_index)
                result.append(sub_str_decoded * repeat)
                i = matching_bracket_index + 1
        return "".join(result)

    def find_matching_bracket(self, s: str, start: int, end: int) -> int:
        left_bracket_count = 0
        for i in range(start, end):
            if s[i] == '[':
                left_bracket_count += 1
            elif s[i] == ']':
                if left_bracket_count == 0:
                    return i
                left_bracket_count -= 1
        return -1

    # Stack approach is more clear
    def decodeString(self, s: str) -> str:

        stack = deque()
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                sub_str = self.pop_until_bracket(stack)
                repeat = self.pop_all_digits(stack)
                decoded_str = sub_str * repeat
                stack.append(decoded_str)
        result0 = ''.join(stack)
        return result0

    def pop_until_bracket(self, q: deque) -> str:
        chars = deque()
        while q[-1] != '[':
            c0 = q.pop()
            chars.appendleft(c0)
        q.pop()
        res = "".join(chars)
        return res

    def pop_all_digits(self, q: deque) -> int:
        digits = deque()
        while q and q[-1].isdigit():
            d = q.pop()
            digits.appendleft(d)
        i = "".join(digits)
        return int(i)


if __name__ == '__main__':
    result = Solution().decodeString("3[a]2[bc]")
    expected = 'aaabcbc'
    assert result == expected, f"Value should be {expected}, but {result}"

    result = Solution().decodeString("3[a2[c]]")
    expected = 'accaccacc'
    assert result == expected, f"Value should be {expected}, but {result}"

    result = Solution().decodeString("2[abc]3[cd]ef")
    expected = "abcabccdcdcdef"
    assert result == expected, f"Value should be {expected}, but {result}"

    result = Solution().decodeString("100[leetcode]")
    expected = "leetcode" * 100
    assert result == expected, f"Value should be {expected}, but {result}"
