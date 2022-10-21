# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

import collections

from leetcodepractice.data_structure_elements import TreeNode
from leetcodepractice.test import LCTestUtils


class Codec:

    # BFS approach
    def serialize_1(self, root):
        if not root:
            return '#'
        result = []
        que = collections.deque([root])
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node:
                    result.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
                else:
                    result.append('#')
        return ",".join(str(i) for i in result)

    def deserialize_1(self, data):
        if data == '#':
            return None
        strs = collections.deque(data.split(','))
        root = TreeNode(strs.popleft())
        que = collections.deque([root])
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                val = strs.popleft()
                if val != '#':
                    node.left = TreeNode(val)
                    que.append(node.left)
                val = strs.popleft()
                if val != '#':
                    node.right = TreeNode(val)
                    que.append(node.right)
        return root

    # DFS approach
    def serialize(self, root):
        def dfs_preorder(node):
            if node:
                vals.append(str(node.val))
                dfs_preorder(node.left)
                dfs_preorder(node.right)
            else:
                vals.append('#')

        vals = []
        dfs_preorder(root)
        string = ' '.join(vals)
        return string

    def deserialize(self, data):
        def dfs_preorder():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs_preorder()
            node.right = dfs_preorder()
            return node

        vals = iter(data.split())
        root = dfs_preorder()
        return root


if __name__ == '__main__':
    root = LCTestUtils.build_binary_tree(
        [1, 2, 3, None, None, 4, 5], TreeNode())

    ser = Codec()
    deser = Codec()
    ans = deser.deserialize_1(ser.serialize_1(root))

    print(ans)
