# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        left_brackets = ["(", "{", "["]
        right_to_left = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in left_brackets:
                stack.append(c)
            elif stack and stack.pop() == right_to_left[c]:
                continue
            else:
                return False
        if stack:
            return False
        return True
