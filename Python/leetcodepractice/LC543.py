# https://leetcode.com/problems/diameter-of-binary-tree/
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    # Same approach as LC110: DFS return multiple values
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #  Return (diameter, height)
        def dfs_d_h(node: Optional[TreeNode]) -> (int, int):
            if not node:
                return 0, -1
            left = dfs_d_h(node.left)
            right = dfs_d_h(node.right)
            # current node diameter is left_child_height + 1 + right_child_height + 1.
            diameter = max(left[1] + right[1] + 2, left[0], right[0])
            height = 1 + max(left[1], right[1])
            return diameter, height

        return dfs_d_h(root)[0]
