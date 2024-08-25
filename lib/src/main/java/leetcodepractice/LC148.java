package leetcodepractice;


import leetcodepractice.datastructure.ListNode;

public class LC148 {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode head2 = split(head);
        head = sortList(head);
        head2 = sortList(head2);
        head = merge(head, head2);
        return head;
    }

    @SuppressWarnings("ConstantConditions")
    private ListNode split(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        ListNode slow = head;
        ListNode preSlow = slow;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            preSlow = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        preSlow.next = null;
        return slow;
    }

    private ListNode merge(ListNode head, ListNode head2) {
        if (head == null) {
            return head2;
        } else if (head2 == null) {
            return head;
        }

        ListNode dummy = new ListNode(0, null);
        ListNode curr = dummy;
        while (head != null && head2 != null) {
            if (head.val < head2.val) {
                curr.next = head;
                head = head.next;
            } else {
                curr.next = head2;
                head2 = head2.next;
            }
            curr = curr.next;
        }
        if (head != null) {
            curr.next = head;
        }
        if (head2 != null) {
            curr.next = head2;
        }

        return dummy.next;
    }


}