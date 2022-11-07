# https://leetcode.com/problems/unique-binary-search-trees-ii/
from typing import List, Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        memo = {}

        def helper(start: int, end: int):
            if (start, end) in memo:
                return memo[(start, end)]

            if start > end:
                result = [None]  # Must return [None] rather than empty list
                memo[(start, end)] = result
                return result

            all_trees = []
            for root_val in range(start, end + 1):
                all_left_subtree = helper(start, root_val - 1)
                all_right_subtree = helper(root_val + 1, end)
                for left_root in all_left_subtree:
                    for right_root in all_right_subtree:
                        all_trees.append(TreeNode(root_val, left_root, right_root))
            memo[(start, end)] = all_trees
            return all_trees

        return helper(1, n)
