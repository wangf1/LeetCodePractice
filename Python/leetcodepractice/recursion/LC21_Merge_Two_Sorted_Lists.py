# https://leetcode.com/problems/merge-two-sorted-lists/
import math
from typing import Optional

from leetcodepractice.data_structure_elements import ListNode


class Solution:
    def mergeTwoLists_1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = ListNode(-math.inf, list2)
        pre = dummy
        pos = list2
        node = list1
        while node and pos:
            if node.val < pos.val:
                next_node = node.next
                node.next = pos
                pre.next = node
                pre = node
                node = next_node
            if node and node.val >= pos.val:
                pre = pos
                pos = pos.next
        if node:
            pre.next = node
        return dummy.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def recur(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val < list2.val:
                list1.next = recur(list1.next, list2)
                return list1
            else:
                list2.next = recur(list1, list2.next)
                return list2

        return recur(list1, list2)
