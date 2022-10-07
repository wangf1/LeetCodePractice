# https://leetcode.com/problems/path-sum-iii/

from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:

    def __init__(self):
        self.path_sum = None
        self.cache = {}
        self.target_sum = None

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path_sum = 0
        self._dfs_traverse(root, targetSum)
        return self.path_sum

    def _dfs_traverse(self, root, targetSum):
        if not root:
            return self.path_sum
        self._find_path(root, targetSum)
        self._dfs_traverse(root.left, targetSum)
        self._dfs_traverse(root.right, targetSum)

    def _find_path(self, node, targetSum) -> None:
        if not node:
            return
        if node.val == targetSum:
            self.path_sum += 1
        self._find_path(node.left, targetSum - node.val)
        self._find_path(node.right, targetSum - node.val)

    # Solution 2: Use cache to improve performance. Cache the old sums of previous nodes.
    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path_sum = 0
        self.cache = {0: 1}
        self.target_sum = targetSum
        self._dfs_traverse2(root, 0)
        return self.path_sum

    def _dfs_traverse2(self, node, current_sum):
        if not node:
            return
        current_sum += node.val
        old_sum = current_sum - self.target_sum
        self.path_sum += self.cache.get(old_sum, 0)
        self.cache[current_sum] = 1 + self.cache.get(current_sum, 0)
        self._dfs_traverse2(node.left, current_sum)
        self._dfs_traverse2(node.right, current_sum)
        self.cache[current_sum] -= 1
