# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        root_val = preorder.pop(0)
        root_index = inorder.index(root_val)

        lefts = inorder[: root_index]
        rights = inorder[root_index + 1:]

        root = TreeNode(root_val)
        root.left = self.buildTree(preorder, lefts)
        root.right = self.buildTree(preorder, rights)

        return root
