import collections
from typing import Optional, List

from leetcodepractice.data_structure_elements import TreeNode


# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Ad-hoc recurring approach
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        self._level_order_recur(root, result, 0)
        return result

    def _level_order_recur(self, root: Optional[TreeNode], result: List[List[int]], height: int):
        if not root:
            return
        height += 1
        if len(result) < height:
            result.append([])
        result[height - 1].append(root.val)
        if root.left or root.right:
            self._level_order_recur(root.left, result, height)
            self._level_order_recur(root.right, result, height)


# Formal BFS queue approach
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            current_level_values = []
            q_len = len(queue)
            for _ in range(q_len):
                node: TreeNode = queue.popleft()
                current_level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_level_values:
                result.append(current_level_values)
        return result
