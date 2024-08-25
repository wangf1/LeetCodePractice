package leetcodepractice;

import leetcodepractice.datastructure.ListNode;

import java.util.HashMap;
import java.util.Map;

/**
 * <a href="https://leetcode.com/problems/linked-list-cycle-ii/">142. Linked List Cycle II</a>
 */
public class LC142 {
    /**
     * Hash table approach
     *
     * @param head list head
     * @return start point of loop
     */
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return head;
        }
        Map<ListNode, Integer> nodeIndexMap = new HashMap<>();
        int pos = 0;
        while (head.next != null) {
            if (nodeIndexMap.containsKey(head)) {
                return head;
            }
            nodeIndexMap.put(head, pos);
            pos++;
            head = head.next;
        }
        return null;
    }

    /**
     * See <a href="https://www.tutorialcup.com/leetcode-solutions/linked-list-cycle-ii-leetcode-solution.htm">Explanation</a>
     * 2(x+y) - (x+y) = Nc <br>
     * ===> x+y=Nc  <br>
     * ===> meetPoint + y steps = the start point of cycle
     */

    public ListNode detectCycle2PointerApproach(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }

        ListNode meetPoint = meetPoint(head);
        if (meetPoint == null) {
            return null;
        }

        while (head != meetPoint) {
            head = head.next;
            meetPoint = meetPoint.next;
        }
        return head;

    }

    private ListNode meetPoint(ListNode head) {
        ListNode fast = head, slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                return slow;
            }
        }
        return null;
    }

}
