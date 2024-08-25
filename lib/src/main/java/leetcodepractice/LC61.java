package leetcodepractice;

import leetcodepractice.datastructure.ListNode;

// https://leetcode.com/problems/rotate-list/
// Advance version: https://www.algoexpert.io/questions/shift-linked-list
public class LC61 {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) {
            return head;
        }
        int length = makeCycleAndReturnLength(head);
        int step = (length - (k % length)) % length;
        ListNode newTail = null;
        for (int i = 0; i < step; i++) {
            newTail = head;
            head = head.next;
        }
        newTail.next = null;
        return head;
    }

    private int makeCycleAndReturnLength(ListNode head) {
        int length = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }
        tail.next = head;
        return length;
    }
}
