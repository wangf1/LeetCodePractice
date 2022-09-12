# https://leetcode.com/problems/validate-binary-search-tree/
import math
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid_bst(root, -math.inf, math.inf)

    def _is_valid_bst(self, root: Optional[TreeNode], min_: float, max_: float) -> bool:
        if not root:
            return True
        if root.val <= min_:
            return False
        if root.val >= max_:
            return False
        return self._is_valid_bst(root.left, min_, root.val) and self._is_valid_bst(root.right, root.val, max_)


if __name__ == '__main__':
    root = TreeNode(5, TreeNode(4), TreeNode(7, TreeNode(3), TreeNode(9)))
    if Solution().isValidBST(root):
        raise ValueError("The Tree should NOT be BST")

    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    if not Solution().isValidBST(root2):
        raise ValueError("The tree should be BST")
