package leetcodepractice;

import leetcodepractice.datastructure.ListNode;

public class LC206 {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode previous, current = head, next = current.next;
        while (next != null) {
            previous = current;
            current = next;
            next = next.next;
            current.next = previous;
        }
        head.next = null;
        return current;
    }

    public ListNode reverseList1(ListNode head) {
        return recursive(null, head);

    }

    ListNode recursive(ListNode previous, ListNode current) {
        if (current == null) {
            return previous;
        }
        var oldPrevious = previous;
        previous = current;
        current = current.next;
        previous.next = oldPrevious;
        return recursive(previous, current);
    }
}
