import collections
from typing import Optional, List

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def post_order(root: Optional[TreeNode]):
            if not root:
                return
            post_order(root.left)
            post_order(root.right)
            result.append(root.val)

        post_order(root)
        return result

    def postorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        stack = collections.deque()
        stack.append(root)
        while stack:
            node: TreeNode = stack.pop()
            result.insert(0, node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result
