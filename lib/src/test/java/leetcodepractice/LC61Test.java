package leetcodepractice;

import leetcodepractice.datastructure.ListNode;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

class LC61Test {

    @Test
    public void test() {
        LC61 testee = new LC61();

        ListNode head = LCListTestUtils.buildNodeList(Arrays.asList(1, 2, 3, 4, 5));
        ListNode newHead = testee.rotateRight(head, 2);
        LCListTestUtils.verifyNodeList(List.of(4, 5, 1, 2, 3), newHead);


        head = LCListTestUtils.buildNodeList(Arrays.asList(0, 1, 2));
        newHead = testee.rotateRight(head, 4);
        LCListTestUtils.verifyNodeList(List.of(2, 0, 1), newHead);

        head = LCListTestUtils.buildNodeList(Arrays.asList(0, 1, 2));
        newHead = testee.rotateRight(head, -4);
        LCListTestUtils.verifyNodeList(List.of(1, 2, 0), newHead);
    }

}
