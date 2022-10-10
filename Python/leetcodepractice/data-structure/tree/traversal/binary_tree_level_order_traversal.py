# https://leetcode.com/problems/binary-tree-level-order-traversal/
import collections
from typing import Optional, List

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        curr_que = collections.deque()
        curr_que.append(root)
        while curr_que:
            curr_result = []
            next_que = collections.deque()
            while curr_que:
                node: TreeNode = curr_que.popleft()
                curr_result.append(node.val)
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)
            result.append(curr_result)
            curr_que = next_que
        return result

    def levelOrder_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def bfs_recursive(node: Optional[TreeNode], level: int):
            if not node:
                return
            if len(result) < level + 1:
                result.append([])
            current_level_result: List[int] = result[level]
            current_level_result.append(node.val)
            bfs_recursive(node.left, level + 1)
            bfs_recursive(node.right, level + 1)

        bfs_recursive(root, 0)
        return result
