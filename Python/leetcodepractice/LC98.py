# https://leetcode.com/problems/validate-binary-search-tree/
import math
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


# Preorder Traversal + find proper min and max boundaries
class Solution:
    def isValidBST_1(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid_bst(root, -math.inf, math.inf)

    def _is_valid_bst(self, root: Optional[TreeNode], min_: float, max_: float) -> bool:
        if not root:
            return True
        if root.val <= min_:
            return False
        if root.val >= max_:
            return False
        return self._is_valid_bst(root.left, min_, root.val) and self._is_valid_bst(root.right, root.val, max_)

    # More complex version than solution one. The idea is similar. Memo can boost performance for 50%
    def isValidBST_2(self, root: Optional[TreeNode]) -> bool:

        memo = {}

        def dfs(node: Optional[TreeNode]) -> (bool, int, int):

            if node in memo:
                return memo[node]

            if not node.left and not node.right:
                result = (True, node.val, node.val)
                memo[node] = result
                return result

            l_result = None
            r_result = None

            if node.left:
                l_result = dfs(node.left)
                if not l_result[0] or l_result[2] >= node.val:
                    result = (False, min(l_result[1], l_result[2], node.val), max(l_result[1], l_result[2], node.val))
                    memo[node] = result
                    return result
            if node.right:
                r_result = dfs(node.right)
                if not r_result[0] or r_result[1] <= node.val:
                    result = (False, min(r_result[1], r_result[2], node.val), max(r_result[1], r_result[2], node.val))
                    memo[node] = result
                    return result
            if l_result:
                min_val = l_result[1]
            else:
                min_val = node.val
            if r_result:
                max_val = r_result[2]
            else:
                max_val = node.val
            result = (True, min_val, max_val)
            memo[node] = result
            return result

        return dfs(root)[0]


if __name__ == '__main__':
    root = TreeNode(5, TreeNode(4), TreeNode(7, TreeNode(3), TreeNode(9)))
    if Solution().isValidBST(root):
        raise ValueError("The Tree should NOT be BST")

    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    if not Solution().isValidBST(root2):
        raise ValueError("The tree should be BST")
