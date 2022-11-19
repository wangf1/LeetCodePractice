# https://leetcode.com/problems/invert-binary-tree

import collections
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    # Approach 1: Recursive
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    # Approach 2: Iterative by using queue
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        q = collections.deque()
        q.append(root)
        while q:
            r = q.pop()
            if r:
                r.left, r.right = r.right, r.left
                q.append(r.left)
                q.append(r.right)
        return root
