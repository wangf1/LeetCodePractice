# https://leetcode.com/problems/swap-nodes-in-pairs/
from typing import Optional

from leetcodepractice.data_structure_elements import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head
