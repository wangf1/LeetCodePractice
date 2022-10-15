# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import List, Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root_val = postorder.pop()
        root_index = inorder.index(root_val)

        lefts = inorder[: root_index]
        rights = inorder[root_index + 1:]

        root = TreeNode(root_val)
        root.right = self.buildTree(rights, postorder)
        root.left = self.buildTree(lefts, postorder)

        return root
