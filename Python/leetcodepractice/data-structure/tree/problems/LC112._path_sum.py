# https://leetcode.com/problems/path-sum/
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: Optional[TreeNode], parent_sum):
            if not node:
                return False
            parent_sum += node.val
            if (not node.left and not node.right) and parent_sum == targetSum:
                return True
            return dfs(node.left, parent_sum) or dfs(node.right, parent_sum)

        return dfs(root, 0)

    def hasPathSum_iterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, 0)]
        while stack:
            node, parent_sum = stack.pop()
            parent_sum += node.val
            if (not node.left and not node.right) and parent_sum == targetSum:
                return True
            if node.left:
                stack.append((node.left, parent_sum))
            if node.right:
                stack.append((node.right, parent_sum))
        return False
