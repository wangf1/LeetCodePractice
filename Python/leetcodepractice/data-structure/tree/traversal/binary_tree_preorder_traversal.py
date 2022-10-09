from collections import deque
from typing import Optional, List

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._preorder_traverse(root, result)
        return result

    def _preorder_traverse(self, root: Optional[TreeNode], result: List[int]) -> None:
        if not root:
            return
        result.append(root.val)
        self._preorder_traverse(root.left, result)
        self._preorder_traverse(root.right, result)

    def preorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        stack = deque()
        stack.append(root)
        while stack:
            node: TreeNode = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
