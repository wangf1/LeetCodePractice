# https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = (end + start) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return max(start, end)


def isBadVersion(v: int) -> bool:
    if v <= 5:
        return True
    else:
        return False
