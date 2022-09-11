# https://leetcode.com/problems/rotate-list/

from typing import Optional

from leetcodepractice.data_structure_elements import ListNode


class LC61:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        length = self._make_cycle_and_return_length(head)
        step = length - k % length
        new_tail = None
        for i in range(step):
            new_tail = head
            head = head.next
        new_tail.next = None
        return head

    @staticmethod
    def _make_cycle_and_return_length(head: Optional[ListNode]) -> int:
        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1
        tail.next = head
        return length
