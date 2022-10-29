"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional

from leetcodepractice.data_structure_elements import Node


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        val_to_node = {}

        def dfs(cur: 'Node') -> Optional['Node']:
            if not cur:
                return None
            cloned = val_to_node.get(cur.val)
            if cloned:
                return cloned
            cloned = Node(cur.val)
            val_to_node[cur.val] = cloned
            for neighbor in cur.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned.neighbors.append(cloned_neighbor)
            return cloned

        return dfs(node)
