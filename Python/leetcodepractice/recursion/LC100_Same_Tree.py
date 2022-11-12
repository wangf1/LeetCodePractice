# https://leetcode.com/problems/same-tree/

import collections
from typing import Optional

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def isSameTree_1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = collections.deque()
        que.append((p, q))
        while que:
            p, q = que.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            que.append((p.left, q.left))
            que.append((p.right, q.right))
        return True
