# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

from leetcodepractice.data_structure_elements import ListNode


class Solution:
    def reverseList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = [None]

        def recur(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None
            if not node.next:
                new_head[0] = node
                return node
            next_node = node.next.next
            pre = node.next
            pre.next = node
            node.next = None
            new_head[0] = pre
            tail = recur(next_node)
            if tail:
                tail.next = pre
            return node

        recur(head)
        return new_head[0]

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recur(node, pre):
            if not node:
                return pre
            next = node.next
            node.next = pre
            return recur(next, node)

        return recur(head, None)
