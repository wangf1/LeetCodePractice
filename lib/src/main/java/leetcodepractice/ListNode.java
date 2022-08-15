package leetcodepractice;

import javax.annotation.Nullable;

class ListNode {
    final int val;
    @Nullable
    ListNode next;

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
