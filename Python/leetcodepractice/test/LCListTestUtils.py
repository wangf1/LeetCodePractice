import collections
from typing import TypeVar
from unittest import TestCase

from leetcodepractice.data_structure_elements import ListNode

T = TypeVar('T')


def build_node_list(ints: list[int]) -> ListNode:
    head = None
    ints.reverse()
    for i in ints:
        head = ListNode(i, head)
    return head


def verify_node_list(expected_values: list[int], head: ListNode):
    assertions = TestCase()
    if head is None:
        assertions.assertIsNone(expected_values)
    actual_values = []
    while head is not None:
        actual_values.append(head.val)
        head = head.next
    print(actual_values)
    assertions.assertEquals(expected_values, actual_values)


def build_binary_tree(ints: list[int], root: T) -> T:
    root.val = ints[0]

    def bfs():
        length = len(ints)
        que = collections.deque([root])
        i = 1
        while que:
            if i >= length:
                break
            for _ in range(len(que)):
                node = que.popleft()
                if i < length and ints[i]:
                    node.left = type(root)(ints[i])
                    que.append(node.left)
                i += 1
                if i < length and ints[i]:
                    node.right = type(root)(ints[i])
                    que.append(node.right)
                i += 1

    bfs()
    return root
