package leetcodepractice;

import leetcodepractice.datastructure.ListNode;

// https://leetcode.com/problems/merge-two-sorted-lists/
public class LC21 {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head;
        if (list1 == null) {
            return list2;
        } else if (list2 == null) {
            return list1;
        } else {
            head = list1.val < list2.val ? list1 : list2;
        }

        ListNode currentNode1 = list1;
        ListNode previousNode1;

        ListNode currentNode2 = list2;
        ListNode previousNode2 = null;

        while (currentNode1 != null && currentNode2 != null) {
            if (currentNode1.val >= currentNode2.val) {
                previousNode2 = currentNode2;
                currentNode2 = currentNode2.next;
            } else {
                previousNode1 = currentNode1;
                currentNode1 = currentNode1.next;
                previousNode1.next = currentNode2;
                if (previousNode2 != null) {
                    previousNode2.next = previousNode1;
                }
                currentNode2 = previousNode1;
            }
        }
        if (currentNode2 == null) {
            previousNode2.next = currentNode1;
        }
        return head;
    }

}
