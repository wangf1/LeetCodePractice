# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(start: int, end: int) -> Optional[TreeNode]:
            if start >= end:
                return None
            if start + 1 == end:
                return TreeNode(nums[start])
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(start, mid)
            root.right = dfs(mid + 1, end)
            return root

        return dfs(0, len(nums))
