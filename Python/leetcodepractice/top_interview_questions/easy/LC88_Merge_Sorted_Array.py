# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_m = nums1[:m]
        i = j = k = 0
        while k < m + n and i < m and j < n:
            if nums1_m[i] < nums2[j]:
                nums1[k] = nums1_m[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            nums1[n + i] = nums1_m[i]
            i += 1
        while j < n:
            nums1[m + j] = nums2[j]
            j += 1

    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
