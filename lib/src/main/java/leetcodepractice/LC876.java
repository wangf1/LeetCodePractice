package leetcodepractice;

// https://leetcode.com/problems/middle-of-the-linked-list/
public class LC876 {
    public ListNode middleNode(ListNode head) {
        if (head == null) {
            return head;
        }
        int length = 0, middleIndex = 0;
        ListNode tail = head, middle = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
            int currentMiddleIndex = (length / 2) + (length % 2 == 0 ? 0 : 1);
            if (currentMiddleIndex > middleIndex) {
                middleIndex = currentMiddleIndex;
                assert middle != null;
                middle = middle.next;
            }
        }
        return middle;
    }
}
