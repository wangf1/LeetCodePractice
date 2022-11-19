# https://leetcode.com/problems/balanced-binary-tree

import collections
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        BalanceAndHeight = collections.namedtuple('BalanceAndHeight', ['is_balanced', 'height'])

        def dfs_check_balance(node: Optional[TreeNode]) -> BalanceAndHeight:
            if not node:
                return BalanceAndHeight(is_balanced=True, height=-1)

            left = dfs_check_balance(node.left)
            right = dfs_check_balance(node.right)

            b = left.is_balanced and right.is_balanced and abs(left.height - right.height) <= 1
            h = 1 + max(left.height, right.height)
            return BalanceAndHeight(is_balanced=b, height=h)

        return dfs_check_balance(root).is_balanced

    # Not as good as above 1. Time: O(nlgn)
    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_h = self.get_height(root.left)
        right_h = self.get_height(root.right)
        if abs(left_h - right_h) >= 2:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
