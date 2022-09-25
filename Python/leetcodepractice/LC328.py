# https://leetcode.com/problems/odd-even-linked-list/
from typing import Optional

from leetcodepractice.data_structure_elements import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        last_odd = head
        first_even = head.next
        even = first_even

        while True:
            has_odd = True
            has_even = True

            if odd and odd.next and odd.next.next:
                next_odd = odd.next.next
                odd.next = next_odd
                odd = next_odd
                last_odd = odd
            else:
                has_odd = False

            if even and even.next and even.next.next:
                next_even = even.next.next
                even.next = next_even
                even = next_even
            else:
                has_even = False
                even.next = None

            if (not has_odd) and (not has_even):
                break

        last_odd.next = first_even
        return head

    # Same idea but simplified
    def oddEvenList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        first_even = head.next
        even = first_even

        while even and even.next:
            next_odd = even.next

            odd.next = next_odd
            odd = next_odd

            next_even = next_odd.next
            even.next = next_even
            even = next_even

        odd.next = first_even
        return head
