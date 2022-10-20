# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
import LC116_populating_next_right_pointers_in_each_node
from leetcodepractice.data_structure_elements import Node
from leetcodepractice.test.LCTestUtils import build_binary_tree


class Solution:

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # The BFS approach can also solve this problem
        return LC116_populating_next_right_pointers_in_each_node.Solution().connect(root)

    def connect_2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node: 'Optional[Node]', next: 'Optional[Node]'):
            if not node:
                return
            node.next = next

            first_next = None
            while next:
                if next.left:
                    first_next = next.left
                    break
                if next.right:
                    first_next = next.right
                    break
                next = next.next

            if node.left and node.right:
                dfs(node.right, first_next)
                dfs(node.left, node.right)
            elif node.left and not node.right:
                dfs(node.left, first_next)
            elif not node.left and node.right:
                dfs(node.right, first_next)

        dfs(root, None)
        return root


if __name__ == '__main__':
    root = build_binary_tree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8], Node())
    print(root)
    result = Solution().connect_2(root)
    print(root)
