# https://leetcode.com/problems/maximum-depth-of-binary-tree/
import collections
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    # top down approach
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs_top_down(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return depth
            depth += 1
            depth_l = dfs_top_down(node.left, depth)
            depth_r = dfs_top_down(node.right, depth)
            return max(depth_l, depth_r)

        return dfs_top_down(root, 0)

    # top down approach 2
    def maxDepth_2(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs_top_down(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return depth
            depth += 1
            if not node.left and not node.right:
                result[0] = max(depth, result[0])
            dfs_top_down(node.left, depth)
            dfs_top_down(node.right, depth)

        dfs_top_down(root, 0)
        return result[0]

    # bottom up approach
    def maxDepth_3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth_l = self.maxDepth_3(root.left)
        depth_r = self.maxDepth_3(root.right)
        return max(depth_l, depth_r) + 1

    # Level order approach
    def maxDepth_4(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        que = collections.deque()
        que.append(root)
        while que:
            result += 1
            next_que = collections.deque()
            while que:
                node = que.popleft()
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)
            que = next_que
        return result

