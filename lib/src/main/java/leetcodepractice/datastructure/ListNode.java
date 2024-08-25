package leetcodepractice.datastructure;

import javax.annotation.Nullable;

public class ListNode {
    public int val;
    @Nullable
    public ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
