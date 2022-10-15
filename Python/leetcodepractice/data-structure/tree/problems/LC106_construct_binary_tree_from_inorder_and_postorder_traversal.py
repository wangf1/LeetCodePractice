# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import List, Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        length = len(inorder)
        if length == 0:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)
        inorder_left = inorder[0: root_index]
        inorder_right = inorder[root_index + 1: length]
        postorder_right = postorder[-len(inorder_right) - 1: -1]
        postorder_left = postorder[-len(inorder_left) - len(inorder_right) - 1: -len(inorder_right) - 1]

        left = self.buildTree(inorder_left, postorder_left)
        right = self.buildTree(inorder_right, postorder_right)

        root.left = left
        root.right = right

        return root
