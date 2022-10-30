# https://leetcode.com/problems/search-in-a-binary-search-tree/
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val < val:
                return dfs(node.right)
            else:
                return dfs(node.left)

        return dfs(root)
