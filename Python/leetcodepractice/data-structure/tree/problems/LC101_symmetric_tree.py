# https://leetcode.com/problems/symmetric-tree/
import collections
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs_mirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not (left and right):
                return False

            if left.val != right.val:
                return False

            if not dfs_mirror(left.left, right.right):
                return False

            return dfs_mirror(left.right, right.left)

        return dfs_mirror(root.left, root.right)

    def isSymmetric_iterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = collections.deque()
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            left = stack.popleft()
            right = stack.pop()
            if not left and not right:
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            stack.appendleft(left.right)
            stack.appendleft(left.left)
            stack.append(right.left)
            stack.append(right.right)
        return True
