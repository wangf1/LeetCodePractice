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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __repr__(self) -> str:
        result = []

        def bfs():
            if not self:
                return ""
            que = collections.deque([self])
            while que:
                for _ in range(len(que)):
                    node: TreeNode = que.popleft()
                    result.append(node.val)
                    if not node.left and not node.right:
                        continue
                    if node.left:
                        que.append(node.left)
                    else:
                        result.append(None)
                    if node.right:
                        que.append(node.right)
                    else:
                        result.append(None)

        bfs()
        string = ','.join(str(x) for x in result)
        return '[' + string + ']'
