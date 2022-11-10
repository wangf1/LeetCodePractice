# https://leetcode.com/problems/sort-an-array/
import math
from typing import List


class Solution:
    # merge sort implementation cost more space than merge_sort.py
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(nums):
            length = len(nums)
            if length <= 1:
                return nums
            l = nums[:length // 2]
            r = nums[length // 2:]
            l_sorted = merge_sort(l)
            r_sorted = merge_sort(r)
            return merge(l_sorted, r_sorted)

        def merge(l, r):
            res = []
            i = j = 0
            length = len(l) + len(r)
            l.append(math.inf)
            r.append(math.inf)
            for k in range(length):
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1
            return res

        return merge_sort(nums)
