# https://leetcode.com/problems/count-univalue-subtrees/
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode
from leetcodepractice.test.LCListTestUtils import build_binary_tree


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        result = [0]

        if not root:
            return result[0]

        def dfs(node: TreeNode) -> bool:
            if not node:
                return True
            if not node.left and not node.right:
                result[0] += 1
                return True
            result_left = dfs(node.left)
            result_right = dfs(node.right)
            if result_left and result_right and (not node.left or node.left.val == node.val) and (
                    not node.right or node.right.val == node.val):
                result[0] += 1
                return True
            return False

        dfs(root)
        return result[0]


if __name__ == '__main__':
    root = build_binary_tree([5, 1, 5, 5, 5, None, 5])
    result = Solution().countUnivalSubtrees(root)
    assert result == 4, f"Wrong result {result}!"
