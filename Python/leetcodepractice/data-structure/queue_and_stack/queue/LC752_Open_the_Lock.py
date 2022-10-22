# https://leetcode.com/problems/open-the-lock/
import collections
from typing import List


class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        """
        How to try unlock the lock:
        1. Switch 1st wheel back and forth.
        2. Switch 2nd wheel back and forth (Must put 1st wheel back to original value).
        3. Do same thing for 3rd wheel.
        4. Do the same thing for 4th wheel.

        5. If during step 1-4, the lock happen to unlock, then we are done.
            And during step 1-4, we must skip the dead ends conditions.

        6. During step 1-4, we have tried 8 conditions. Based on the 8 condition, we try next round.

        7. If all round done without early return, that means there is no solution.
        """
        que = collections.deque()
        visited = set()
        dead_ends = set(deadends)

        init_val = '0000'
        que.append(init_val)
        visited.add(init_val)
        level = 0
        while que:
            for _ in range(len(que)):
                s: str = que.popleft()
                if s == target:
                    return level
                if s in dead_ends:
                    continue
                for i, c in enumerate(s):
                    num = int(c)
                    s1 = s[:i] + str((num - 1) % 10) + s[i + 1:]
                    s2 = s[:i] + str((num + 1) % 10) + s[i + 1:]
                    if s1 not in visited:
                        que.append(s1)
                        visited.add(s1)
                    if s2 not in visited:
                        que.append(s2)
                        visited.add(s2)
            level += 1
        return -1
