# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
from typing import List

from leetcodepractice.data_structure_elements import Node


class LC589:

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        values = []
        self._preorder_recurring(root, values)
        return values

    def _preorder_recurring(self, root: 'Node', values: List):
        values.append(root.val)
        if not root.children:
            return
        for child in root.children:
            self._preorder_recurring(child, values)


if __name__ == '__main__':
    child3 = Node(3, [Node(5), Node(6)])
    root = Node(1, [child3, Node(2), Node(4)])

    result = LC589().preorder(root)
    if result != [1, 3, 5, 6, 2, 4]:
        raise ValueError("result should be [1,3,5,6,2,4]")
