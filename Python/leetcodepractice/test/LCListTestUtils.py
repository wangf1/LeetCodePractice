from unittest import TestCase

from leetcodepractice.data_structure_elements import ListNode


def build_node_list(ints: list) -> ListNode:
    head = None
    ints.reverse()
    for i in ints:
        head = ListNode(i, head)
    return head


def verify_node_list(expected_values: list, head: ListNode):
    assertions = TestCase()
    if head is None:
        assertions.assertIsNone(expected_values)
    actual_values = []
    while head is not None:
        actual_values.append(head.val)
        head = head.next
    assertions.assertEquals(expected_values, actual_values)
