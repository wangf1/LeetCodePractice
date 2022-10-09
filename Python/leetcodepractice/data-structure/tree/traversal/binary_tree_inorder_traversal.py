# https://leetcode.com/problems/binary-tree-inorder-traversal/
from collections import deque
from typing import Optional, List

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs_in_order(node: Optional[TreeNode]):
            if not node:
                return
            dfs_in_order(node.left)
            result.append(node.val)
            dfs_in_order(node.right)

        dfs_in_order(root)
        return result

    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        stack = deque()
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result
