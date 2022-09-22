# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        current_int = n
        while current_int not in seen:
            seen.add(current_int)
            next_int = 0
            for c in str(current_int):
                next_int += int(c) ** 2
            current_int = next_int
        happy = 1 in seen
        return happy
