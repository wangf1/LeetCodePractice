# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode
from leetcodepractice.test import LCTestUtils


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional[TreeNode]:
        if not root:
            return None
        # Find p or q in tree
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # If p and q are in left and right child tree, the root is the lowest parent node
        if left and right:
            return root
        # Else the lowest parent node exist in left or right child tree
        else:
            return left or right


if __name__ == '__main__':
    root = LCTestUtils.build_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], TreeNode())
    parent = Solution().lowestCommonAncestor(root, root.left, root.left.right.right)
    assert parent == root.left, f"Result should be node '5'"
