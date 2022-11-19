# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional

from leetcodepractice.data_structure_elements import ListNode


class Solution:
    class Solution:
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            if (n == 0) or (not head):
                return head

            last = head
            last_nth = head
            last_nplus1th = None

            i = 0
            while last.next:
                last = last.next
                i += 1
                if i >= n:
                    last_nplus1th = last_nth
                    last_nth = last_nth.next

            if not last_nplus1th:
                if last_nth == last:
                    # Edge case 1: List only has one node
                    return None
                if last_nth != last:
                    # Edge case 2: Remove the first node
                    result = last_nth.next
                    last_nth.next = None
                    return result
            # Normal case
            last_nplus1th.next = last_nth.next
            last_nth.next = None
            return head

        # Insert dummy node before head can eliminate the two special cases that pre_left node is None
        def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            if (n == 0) or (not head):
                return head
            dummy = ListNode(0, head)
            left = dummy
            right = head

            while n > 0 and right:
                right = right.next
                n -= 1

            while right:
                right = right.next
                left = left.next
            left.next = left.next.next
            return dummy.next
