import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}--next-->{self.next.val if self.next else None}"


class Node:
    """
    A node structure that can be used for several LeetCode problems.
    """

    def __init__(self, val=None, children=None, *, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        self.children = children

    def __repr__(self) -> str:
        return build_bfs_string(self)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __repr__(self) -> str:
        return build_bfs_string(self)


def build_bfs_string(root) -> str:
    result = []

    def bfs():
        que = collections.deque([root])
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node:
                    result.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
                else:
                    result.append(None)
        while not result[-1]:
            result.pop()
        return ",".join(str(i) for i in result)

    bfs()
    string = ','.join(str(x) for x in result)
    return '[' + string + ']'
