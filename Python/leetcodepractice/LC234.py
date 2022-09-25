# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional

from leetcodepractice.data_structure_elements import ListNode


# Put values into list is straightforward solution, but memory complexity is O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        fast = head
        slow = head

        # Find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the right half
        pre = None
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp

        # compare the left half with the right half
        left, right = head, pre
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1, None)))))
    result = Solution().isPalindrome(head)
    expected = True
    assert result == expected, f"Result should be {expected} but {result}"

    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
    result = Solution().isPalindrome(head)
    expected = True
    assert result == expected, f"Result should be {expected} but {result}"
