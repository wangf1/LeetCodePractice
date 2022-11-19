# https://leetcode.com/problems/backspace-string-compare/
import itertools


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_reminder(string: str):
            raminder = []
            for i in range(len(string)):
                if string[i] != '#':
                    raminder.append(string[i])
                else:
                    raminder.pop() if raminder else None
            return raminder

        reminder_s = get_reminder(s)
        reminder_t = get_reminder(t)
        return reminder_s == reminder_t

    # Space complexity O(1)
    def backspaceCompare2(self, s: str, t: str) -> bool:
        def get_from_tail(s_: str):
            skip = 0
            for c in reversed(s_):
                if c == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield c

        return all(x == y for x, y in itertools.zip_longest(get_from_tail(s), get_from_tail(t)))
