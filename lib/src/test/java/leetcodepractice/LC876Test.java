package leetcodepractice;

import leetcodepractice.datastructure.ListNode;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static leetcodepractice.LCListTestUtils.buildNodeList;

class LC876Test {

    private LC876 testee;

    @BeforeEach
    void setUp() {
        testee = new LC876();
    }

    @Test
    void middleNode() {
        // Input: head = [1,2,3,4,5]
        // Output: [3,4,5]
        ListNode middle = testee.middleNode(buildNodeList(new int[]{1, 2, 3, 4, 5}));
        Assertions.assertEquals(3, middle.val);

        // Input: head = [1,2,3,4,5,6]
        // Output: [4,5,6]
        middle = testee.middleNode(buildNodeList(new int[]{1, 2, 3, 4, 5, 6}));
        Assertions.assertEquals(4, middle.val);
    }


}
