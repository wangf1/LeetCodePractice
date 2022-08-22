package leetcodepractice;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static leetcodepractice.LCTestUtils.buildNodeList;
import static leetcodepractice.LCTestUtils.verifyNodeList;

class LC206Test {

    private LC206 testee;

    @BeforeEach
    void setUp() {
        testee = new LC206();
    }

    @Test
    void reverseList() {
        // Input: head = [1,2,3,4,5]
        // Output: [5,4,3,2,1]
        ListNode head = buildNodeList(new int[]{1, 2, 3, 4, 5});
        verifyReverse(head, Arrays.asList(5, 4, 3, 2, 1));
        // Input: head = [1,2]
        // Output: [2,1]
        verifyReverse(buildNodeList(new int[]{1, 2}), Arrays.asList(2, 1));
        // Input: head = []
        // Output: []
        verifyReverse(null, null);
    }

    private void verifyReverse(ListNode head, List<Integer> expectedResult) {
        ListNode reverted = testee.reverseList(head);
        verifyNodeList(expectedResult, reverted);

        ListNode origin = testee.reverseList1(reverted);
        reverted = testee.reverseList1(origin);
        verifyNodeList(expectedResult, reverted);
    }
}
