# https://leetcode.com/problems/populating-next-right-pointers-in-each-node
import collections
from typing import Optional

from leetcodepractice.data_structure_elements import Node


class Solution:
    # BFS approach with queue
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        que = collections.deque()
        que.append(root)
        while que:
            pre: Node = Node(-1)  # A dummy pre node can eliminate null check of pre
            for _ in range(len(que)):
                curr: Node = que.popleft()
                pre.next = curr
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                pre = curr
        return root

    # DFS approach with recursion
    def connect_2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(curr: 'Optional[Node]', next: 'Optional[Node]'):
            if not curr:
                return
            curr.next = next
            dfs(curr.left, curr.right)
            dfs(curr.right, curr.next.left if curr.next else None)

        dfs(root, None)
        return root
