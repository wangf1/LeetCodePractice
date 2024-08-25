package leetcodepractice;

import leetcodepractice.datastructure.ListNode;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LC142Test {


    private LC142 testee;

    @BeforeEach
    void setUp() {
        testee = new LC142();
    }

    @Test
    void detectCycle() {
        ListNode n1 = new ListNode(3, null);
        ListNode n2 = new ListNode(2, null);
        ListNode n3 = new ListNode(0, null);
        ListNode n4 = new ListNode(-4, null);

        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n2;

        Assertions.assertSame(n2, testee.detectCycle(n1));
        Assertions.assertSame(n2, testee.detectCycle2PointerApproach(n1));


        n1.next = n2;
        n2.next = n1;
        Assertions.assertSame(n1, testee.detectCycle(n1));
        Assertions.assertSame(n1, testee.detectCycle2PointerApproach(n1));

        n1.next = null;
        Assertions.assertNull(testee.detectCycle(n1));
        Assertions.assertNull(testee.detectCycle2PointerApproach(n1));
    }

}
